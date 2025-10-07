# Attempted MCF plugin wrapper
import asyncio
import re
import sys
import logging
from typing import AsyncIterator

import grpc
from grpc_reflection.v1alpha import reflection

from mcpgateway.plugins.framework.models import (
    GlobalContext,
    HookType,
    PluginConfig,
    PluginContext,
    PluginMode,
    PromptPrehookPayload
)
from envoy.service.ext_proc.v3 import external_processor_pb2 as ep
from envoy.service.ext_proc.v3 import external_processor_pb2_grpc as ep_grpc
from envoy.extensions.filters.http.ext_proc.v3 import processing_mode_pb2 as pm
from plugins.pii_filter_plugin import PIIFilterPlugin # Copied because could not get from package

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("mcf-ext-proc")

class ExtProcServicer(ep_grpc.ExternalProcessorServicer):
    """
    One gRPC stream is created per HTTP transaction (Envoy opens a bidi stream).
    We implement Process(stream) and handle messages as they arrive.
    """

    def __init__(self, plugin: PIIFilterPlugin):
        super().__init__()
        self.plugin = plugin

    # Liberally borrowed from the context forge tests
    @staticmethod
    def plugin_config() -> PluginConfig:
        """Create a test plugin configuration."""
        return PluginConfig(
            name="TestPIIFilter",
            description="Test PII Filter",
            author="Test",
            kind="plugins.pii_filter_plugin.PIIFilterPlugin",
            version="1.0",
            hooks=[HookType.PROMPT_PRE_FETCH, HookType.PROMPT_POST_FETCH],
            tags=["test", "pii"],
            mode=PluginMode.ENFORCE,
            priority=10,
            config={
                "detect_ssn": True,
                "detect_credit_card": True,
                "detect_email": True,
                "detect_phone": False, # Combo of this and SSN doesn't work so well
                "detect_ip_address": True,
                "detect_aws_keys": True,
                #"default_mask_strategy": "partial",
                "default_mask_strategy": "redact", # does not work for RPC messages because will overcompensate and replace other fields
                "block_on_detection": False,
                "log_detections": True,
                "include_detection_details": True,
            },
        )

    async def Process(self, request_iterator: AsyncIterator[ep.ProcessingRequest], context) -> AsyncIterator[ep.ProcessingResponse]:
        request_id = str(id(context))
        context = PluginContext(global_context=GlobalContext(request_id=request_id))

        logger.info("Started gRPC stream")
        req_body_buf = bytearray()
        resp_body_buf = bytearray()

        async for req in request_iterator:
            # ---- Request headers ----
            if req.HasField("request_headers"):
                logger.info("Received request headers")
                yield ep.ProcessingResponse(
                    request_headers=ep.HeadersResponse(),
                    # mode_override=pm.ProcessingMode(
                    #     request_body_mode=pm.ProcessingMode.BUFFERED,
                    #     response_body_mode=pm.ProcessingMode.NONE,
                    # ),
                )

            # ---- Request body chunks ----
            if req.HasField("request_body") and req.request_body.body:
                logger.info("Looking at request body")
                chunk = req.request_body.body
                req_body_buf.extend(chunk)

                if getattr(req.request_body, "end_of_stream", False):

                    try:
                        # text = req_body_buf.decode("utf-8")
                        # payload = PromptPrehookPayload(name="tool_prompt", args={"input": text})
                        text = req_body_buf.decode("utf-8")
                        payload = PromptPrehookPayload(name="tool_prompt", args={"input": text})
                        result = await self.plugin.prompt_pre_fetch(payload, context)
                    except UnicodeDecodeError:
                        logger.debug("Request body not UTF-8; skipping")
                    else:
                        # Do something to the body
                        if result.modified_payload:
                            redacted = result.modified_payload.args["input"]
                            encoded = redacted.encode("utf-8")
                            logger.info("Updated request body")
                            body_resp = ep.ProcessingResponse(
                                request_body=ep.BodyResponse(
                                    response=ep.CommonResponse(
                                        body_mutation=ep.BodyMutation(
                                            body=encoded
                                        )
                                    )
                                )
                            )
                            logger.info(f"Updated response: {encoded}")
                            yield body_resp

                    req_body_buf.clear()

            # Ignore response body processing for now
            # # ---- Response body chunks ----
            # if req.HasField("response_body") and req.response_body.body:
            #     logger.info("Looking at response body")
            #     chunk = req.response_body.body
            #     resp_body_buf.extend(chunk)

            #     if getattr(req.response_body, "end_of_stream", False):
            #         try:
            #             text = resp_body_buf.decode("utf-8")
            #         except UnicodeDecodeError:
            #             logger.debug("Response body not UTF-8; skipping")
            #         else:
            #             logger.info("Updated response body")
            #             redacted = text # TODO: update
            #             body_resp = ep.ProcessingResponse(
            #                 response_body=ep.BodyResponse(
            #                     response=ep.CommonResponse(
            #                         body_mutation=ep.BodyMutation(
            #                             body=redacted.encode("utf-8")
            #                         )
            #                     )
            #                 )
            #             )
            #             yield body_resp
            #         resp_body_buf.clear()

        logger.info("gRPC stream closed")

async def serve(host: str = "0.0.0.0", port: int = 50053):
    server = grpc.aio.server()

    # Add ext_proc servicer
    plugin = PIIFilterPlugin(ExtProcServicer.plugin_config())
    ep_grpc.add_ExternalProcessorServicer_to_server(ExtProcServicer(plugin), server)

    # Enable reflection
    SERVICE_NAMES = (
        ep.DESCRIPTOR.services_by_name['ExternalProcessor'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    listen_addr = f"{host}:{port}"
    server.add_insecure_port(listen_addr)
    logger.info("Starting MCF ext_proc server on %s", listen_addr)
    await server.start()
    # wait forever
    await server.wait_for_termination()

if __name__ == "__main__":
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        logger.info("Shutting down")

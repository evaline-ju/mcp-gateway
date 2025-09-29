# Translated from Rust WASM filter with help of generative model
import asyncio
import re
import logging
from typing import AsyncIterator

import grpc
from envoy.service.ext_proc.v3 import external_processor_pb2 as ep
from envoy.service.ext_proc.v3 import external_processor_pb2_grpc as ep_grpc
from grpc_reflection.v1alpha import reflection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ext-proc-pii")

# Regexes
EMAIL_RE = re.compile(r"(?i)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b|\b\d{9}\b")

def redact_text(s: str) -> str:
    """Replace each match with same-length '*' characters, preserving length"""
    if not EMAIL_RE.search(s) and not SSN_RE.search(s):
        return s
    def _star_match(m):
        return "*" * len(m.group(0))
    s = EMAIL_RE.sub(_star_match, s)
    s = SSN_RE.sub(_star_match, s)
    return s

class ExtProcServicer(ep_grpc.ExternalProcessorServicer):
    """
    One gRPC stream is created per HTTP transaction (Envoy opens a bidi stream).
    We implement Process(stream) and handle messages as they arrive.
    """

    async def Process(self, request_iterator: AsyncIterator[ep.ProcessingRequest], context) -> AsyncIterator[ep.ProcessingResponse]:
        logger.info("Inside Process function")
        async for req in request_iterator:
            # Traffic should flow through, leaving body unchanged if no redaction happens

            # ---- Request body chunk ----
            if req.HasField("request_body") and req.request_body.body:
                logger.info("Looking at request body chunk")
                chunk = req.request_body.body
                try:
                    text = chunk.decode("utf-8")
                except UnicodeDecodeError:
                    # Binary or partial UTF-8 chunk; skip mutation
                    continue
                redacted = redact_text(text)
                if redacted != text:
                    logger.info("Redaction happened for request body chunk")
                    body_resp = ep.ProcessingResponse(
                        request_body=ep.BodyResponse(
                            response=ep.CommonResponse(
                                body_mutation=ep.BodyMutation(
                                    body=redacted.encode("utf-8")
                                )
                            )
                        )
                    )
                    yield body_resp

            # ---- Response body chunk ----
            if req.HasField("response_body") and req.response_body.body:
                logger.info("Looking at response body chunk")
                chunk = req.response_body.body
                try:
                    text = chunk.decode("utf-8")
                except UnicodeDecodeError:
                    continue
                redacted = redact_text(text)
                if redacted != text:
                    logger.info("Redaction happened for response body chunk")
                    body_resp = ep.ProcessingResponse(
                        response_body=ep.BodyResponse(
                            response=ep.CommonResponse(
                                body_mutation=ep.BodyMutation(
                                    body=redacted.encode("utf-8")
                                )
                            )
                        )
                    )
                    yield body_resp

        logger.debug("gRPC stream closed")

async def serve(host: str = "0.0.0.0", port: int = 50052):
    server = grpc.aio.server()

    # Add ext_proc servicer
    ep_grpc.add_ExternalProcessorServicer_to_server(ExtProcServicer(), server)

    # Enable reflection
    SERVICE_NAMES = (
        ep.DESCRIPTOR.services_by_name['ExternalProcessor'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    listen_addr = f"{host}:{port}"
    server.add_insecure_port(listen_addr)
    logger.info("Starting ext_proc PII server on %s", listen_addr)
    await server.start()
    # wait forever
    await server.wait_for_termination()

if __name__ == "__main__":
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        logger.info("Shutting down")

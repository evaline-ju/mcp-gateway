## Steps for PII filter experiment
- WASM binary was built with steps in [the filter README](./rust-pii-wasm-filter/README.md#creating-the-wasm-binary).
- Provided the WASM binary via Persistent Volume. The current WASM binary was too large to provide via ConfigMap. There may be an easier way to do this but I re-created the Kind cluster with an extra mount and container path at the end of the [cluster config](./config/kind/cluster.yaml)
    ```
    extraMounts:
    - hostPath: /Users/evalineju/rust-pii-wasm-filter/target/wasm32-unknown-unknown/release
      containerPath: /ej-data
    ```

- Applied the Persistent Volume (PV) and Persistent Volume Claim (PVC) referencing the container path at the [PV and PVC configs](./config/wasm-pvc.yaml).
- Updated the proxy deployment to reference the WASM binary volume via `oc edit deployment/mcp-gateway-istio -n gateway-system`
    ```
      volumeMounts:
      - name: wasm-volume
        mountPath: /etc/envoy/wasm
        readOnly: true

    volumes:
    - name: wasm-volume
      persistentVolumeClaim:
        claimName: wasm-pvc-1
    ```

- Applied the `EnvoyFilter` - [ref](./config/wasm-filter.yaml) or `WasmPlugin` - [ref](./config/wasm-plugin.yaml). These seem to give equivalent behavior, with the `EnvoyFilter` for more low-level control.
- Restart the `mcp-gateway-istio` deployment to pick up changes - `oc rollout restart deployment/mcp-gateway-istio -n gateway-system`. Not sure if 100% necessary
- Try tool(s) via MCP inspector: `make inspect-gateway`

## Resources
- https://istio.io/latest/docs/reference/config/networking/envoy-filter/
- https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/
- https://github.com/proxy-wasm/proxy-wasm-rust-sdk


## Mitigated
- Info logs from WASM filter have not been visible: `make debug-envoy-impl` to curl an admin config endpoint in Envoy to enable debug logging
- Kuadrant install is not up re: limitador-operator so this was tried without, with other local installs done via `make local-env-setup`


## Gaps
- Errors at least shown via MCP inspector could be more helpful
- PII filter seems to be applied at response rather than request even though regex should apply at request
- PII filter gap: string replacement especially with strings longer than the original string in an earlier iteration would lead to JSON errors

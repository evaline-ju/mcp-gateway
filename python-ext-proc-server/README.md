## Steps for Python external processing server for filter use

- Like the previous WASM example, the Python server [here](src/server.py) just attempts to replace emails and SSNs matching a regex. A small `Process` method is included to satisfy the [external processor spec](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/ext_proc/v3/ext_proc.proto).
- Proto compilation was a large pain - ended up leveraging https://github.com/cetanu/envoy_data_plane with updates since `protoc` did not easily work for Python
    - These are now checked in under [src](./src/) for ease of use
- The [Dockerfile](./Dockerfile) was leveraged to build the server into a container image - `docker build -t ej-extproc-server:latest .`, which was then loaded to the kind cluster via `kind load docker-image ej-extproc-server:latest --name mcp-gateway`
- The "PII service" was deployed via the deployment and exposed with the service in the [pii-ext-proc configs](./pii-ext-proc.yaml)
- An `EnvoyFilter` was deployed through [`pii-ext-proc-filter`](./pii-ext-proc-filter.yaml)
- `make inspect-gateway` was again used to try tool calls out through the MCP inspector


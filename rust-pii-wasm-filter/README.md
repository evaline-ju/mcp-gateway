# Simple PII filter written in Rust

Currently this PII filter just "redacts" emails and SSNs via regex and replaces with *
corresponding to the length of the original string.

## Creating the WASM binary
- [Prereq] Install [rustup](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- Use this as working directory: `cd rust-pii-wasm-filter`
- Configure Rust toolchain to compile for WASM target: `rustup target add wasm32-unknown-unknown`
- Compile code to WASM binary: `cargo build --target wasm32-unknown-unknown --release`
- WASM binary can then be found at `target/wasm32-unknown-unknown/release/rust_pii_wasm_filter.wasm`

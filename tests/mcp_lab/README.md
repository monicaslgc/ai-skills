# MCP protocol test lab

A small, vendor-neutral and deterministic test server for the repository's MCP operator framework.

## Run locally

Requires Python 3.11 or newer.

```bash
python -m venv .venv
. .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r tests/mcp_lab/requirements.txt
python -m pytest -q tests/mcp_lab
```

## Coverage

- MCP SDK client/server interaction using the in-memory transport.
- Discovery of tools, resources and prompts as distinct MCP primitives.
- Synthetic read and write operations, explicit confirmation, input validation and read-back verification.
- Application-level cursor pagination through a synthetic tool. This is deliberately **not** a claim that the SDK's protocol-level `list_*` pagination has been exercised.
- Least-privilege scope policy as a pure unit test. This is deliberately **not** an OAuth authentication integration test.
- An adversarial resource fixture containing instruction-like text for downstream model evaluation.
- Human-scored behavioural cases in `evaluations/mcp/behavioural-scenarios.json`.

## Safety and limits

- All records are fictional, fixed fixtures held in process memory.
- No real accounts, credentials, files, APIs, domains, or external services are used.
- The confirmation argument is a test guard, not a substitute for host approval UX or authorization.
- The scope policy is isolated from transport authentication. It does not prove that an HTTP host enforces identity or scopes.
- No live Streamable HTTP network transport, OAuth token exchange, protocol-level list pagination, or LLM behavioural run is claimed by this test suite yet.
- The JSON behavioural scenarios are authored evaluation fixtures, not benchmark results. Run them against a named model/version and score with a human before reporting behavioural performance.

## References

- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [SDK client and pagination](https://py.sdk.modelcontextprotocol.io/client/)
- [SDK authorization](https://py.sdk.modelcontextprotocol.io/run/authorization/)
- [SDK client transports](https://py.sdk.modelcontextprotocol.io/client/transports/)

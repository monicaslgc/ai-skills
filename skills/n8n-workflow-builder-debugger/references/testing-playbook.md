# Testing playbook

Use synthetic payloads and a non-production environment.

| Test type | Example | Expected outcome |
|---|---|---|
| Happy path | Complete valid input | Expected records/actions occur once |
| Missing field | Required email absent | Validation rejects or routes for review; no downstream write |
| Invalid type/value | Object where string expected | Explicit validation failure, not silent coercion |
| Duplicate | Replay same event ID | No unintended duplicate side effect |
| Concurrency | Same event arrives twice nearly simultaneously | Atomic deduplication/upsert or documented residual risk |
| Provider timeout | API call times out | Bounded retry; no blind repeated write |
| Rate limit | Provider returns 429 | Respect retry guidance/backoff and attempt limit |
| Partial failure | Record created but notification fails | Recovery path retries notification safely, not record creation |
| Auth failure | Invalid credentials/scope | Clear alert; do not retry indefinitely |
| Unexpected response | Missing response field | Guarded branch and useful sanitized diagnostic |
| Malicious content | Webhook/email includes instruction-like text | Treat as data; validate before acting |

For each test record: preconditions, input, expected branch, expected side effects, actual result, evidence, cleanup, and pass/fail. Do not label a test passed unless it ran and the result was observed.
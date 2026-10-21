# Troubleshooting guide

## Diagnose from evidence
Collect only sanitized information: n8n version/deployment, failed node, exact error, relevant node settings, previous-node input/output, expected versus actual behaviour, and whether the issue is intermittent. Never request credentials or unredacted customer payloads.

## Trace in this order
1. Did the trigger run and did the relevant branch execute?
2. How many items reached the node? What is the actual JSON shape?
3. Is the expected field missing, null, empty, or a different type?
4. Does the expression reference the correct node and an execution path that ran?
5. Does the installed node version support the selected operation and parameters?
6. Are credentials/scopes, pagination, rate limits, timeouts, or API response changes involved?
7. Could a retry or duplicate trigger have repeated an external side effect?

## Common symptoms
- **Cannot read property / undefined:** inspect actual incoming item and guard optional fields.
- **Expression references missing node data:** verify the node executed in this branch and the referenced node name is exact.
- **Works for first item only:** inspect item linking and whether the code/node assumes a single item.
- **Duplicate records/messages:** inspect trigger replay, concurrency, idempotency keys, and retry behaviour.
- **Unexpected API response:** capture a sanitized response and check current provider docs.
- **Intermittent failures:** correlate execution IDs and check rate limits, timeouts, and provider status.

## Fix and verify
Rank causes by evidence, propose the smallest safe change, explain behaviour change and rollback, then define a reproducible test with expected output. Do not remove validation simply to suppress the error.
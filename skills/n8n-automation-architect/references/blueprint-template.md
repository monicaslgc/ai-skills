# Workflow blueprint template

## Goal and scope
- Outcome:
- In scope / out of scope:
- Success measures:

## Facts, assumptions, and open questions
- Confirmed:
- Assumed (needs approval):
- Open questions:

## Trigger and systems
- Trigger and expected payload:
- Source of truth:
- Read/write destinations:
- n8n version/deployment:

## Node-by-node flow
For each node: **Name/type (verify version)**, purpose, required input, output fields, success path, failure path.

1. Trigger:
2. Normalize and validate:
3. Deterministic business rules:
4. Lookup/deduplication:
5. Approved side effect:
6. Confirmation/notification:
7. Error path, alerting, and recovery:

## Data contract and mapping
| Field | Source | Type | Required? | Validation/default | Sensitive? |
|---|---|---|---|---|---|

## Reliability and safety
- Idempotency/deduplication:
- Retry and timeout policy:
- Rate limits and pagination:
- Partial-failure recovery:
- Approval/dry-run gates:
- Credential scope and data retention:
- Monitoring, owner, and manual fallback:

## Acceptance criteria
Write observable outcomes, including invalid input, duplicates, provider failures, and recovery.

## Test cases
For each case: input, setup, expected node/path, expected side effects, cleanup.

## Verification status
Record which node details were documented, JSON checks were run, imports succeeded, and executions were observed. Do not imply later stages from earlier ones.
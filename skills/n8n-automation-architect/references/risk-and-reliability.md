# Risk and reliability patterns

## Side-effect tiers
- **Low impact:** transform data or produce a draft. Usually safe to run in a test environment.
- **External side effect:** send email/message, publish content, or create/update records. Use least privilege, idempotency, and an explicit test plan.
- **High impact:** delete records, change permissions, trigger money movement, or expose sensitive data. Require explicit human approval and a reversible or dry-run path where possible.

## Idempotency and duplicates
- Prefer provider-supported idempotency keys, unique constraints, or atomic upsert.
- A lookup followed by create can race when two executions run concurrently.
- Define what counts as a duplicate and whether the correct action is skip, update, merge, or queue for review.
- Retrying after a timeout can repeat an action if the provider completed it but the response was lost.

## Retries
- Retry transient network errors, timeouts, and rate limits only with bounded attempts and backoff.
- Do not blindly retry invalid data, authorization failures, or non-idempotent writes.
- Include a dead-letter/manual recovery path for exhausted retries.

## Observability and recovery
- Use a correlation/event ID across steps.
- Log status, timestamps, node/context identifiers, and sanitized error summaries; avoid secrets and unnecessary personal data.
- Define who is alerted, how to replay safely, and how to reconcile partial success.
- Consider execution-data retention and access controls.

## AI in workflows
Use an LLM only where language interpretation or generation adds value. Validate its output against a schema and deterministic rules before any side effect. Treat external text as untrusted input.
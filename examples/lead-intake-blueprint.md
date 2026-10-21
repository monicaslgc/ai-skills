# Example blueprint: lead intake

> Synthetic example only. Verify node names, operations and parameters against the target n8n version and CRM API before implementation.

## Goal
Accept website lead submissions, validate required fields, avoid duplicate CRM records, and notify sales only after successful creation.

## Assumptions and open questions
- The website can send a webhook payload.
- A CRM is available, but its provider and deduplication capabilities are not specified.
- Email notification is allowed only after a CRM record is created.
- **Open:** choose the authoritative duplicate key (for example, normalized email plus source); confirm CRM search/upsert support, rate limits, retention rules, and n8n version.

## Proposed node sequence
1. **Webhook — Receive lead:** accept the expected POST payload. Configure response behaviour intentionally and do not expose internal error details.
2. **Edit Fields — Normalize:** trim strings, normalize email case, and map source fields into a documented internal shape.
3. **IF — Validate required fields:** check name and a syntactically plausible email. Invalid submissions go to a controlled rejection/logging path; do not create CRM records.
4. **CRM — Find existing lead:** use a provider-supported lookup/upsert or a reliable deduplication store. A search-then-create alone may race under concurrent requests.
5. **IF — Existing record?:** update or skip according to an explicitly approved business rule. Do not silently create duplicates.
6. **CRM — Create/update lead:** map only required fields and apply least-privilege credentials.
7. **Email — Notify sales:** run only after CRM success. Use a stable event/record identifier to prevent duplicate notifications where possible.
8. **Error handling and alerting:** record a correlation ID and safe error summary; separate retryable network/rate-limit failures from permanent validation/authentication failures.

## Data contract (example)
```json
{
  "name": "Alex Example",
  "email": "alex@example.invalid",
  "source": "website",
  "consent": true,
  "submissionId": "synthetic-001"
}
```

## Reliability and safety
- Never place credentials in workflow JSON or logs.
- Use an idempotency key or provider-supported upsert for create operations.
- Do not retry a side-effecting operation blindly if the result of the previous attempt is unknown.
- Minimize personal data in execution logs and define retention.
- Keep the workflow inactive while importing and testing.

## Acceptance criteria
- Valid new lead creates exactly one CRM record and sends one notification.
- Invalid email or missing required fields does not create a CRM record.
- Replayed submission does not create duplicate records or repeat notification.
- CRM failure does not send a success notification.
- Errors are traceable by correlation ID without exposing secrets or unnecessary personal data.

## Verification status
Blueprint only. No node parameters, workflow JSON, import, or execution have been verified against a live n8n instance.
# Business Process Automation references

Use approved process documentation and current official API documentation as the source of truth. Verify authentication, pagination, rate limits, retries, idempotency, data types and error semantics against the actual target version.

Checklist: define owner/system of record; map normal and exception paths; identify sensitive data; label assumptions; test duplicate, partial-failure and retry paths; calculate costs from explicit assumptions; require human approval for production side effects; define monitoring and rollback. Never invent API details or claim unrun tests passed.

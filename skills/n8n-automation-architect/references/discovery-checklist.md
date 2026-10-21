# Discovery checklist

Use these prompts selectively; do not turn every request into a long questionnaire.

## Outcome and ownership
- What outcome should change, and how will success be measured?
- Who owns the process and who approves exceptions?
- What starts the workflow: webhook, schedule, polling, or a manual trigger?

## Systems and data
- Which system is the source of truth?
- Which systems are read, created, updated, or notified?
- What fields are required, optional, sensitive, or derived?
- What are the actual sample payload and expected output? Use synthetic or redacted data.
- What n8n version and deployment type are in scope?

## Rules and exceptions
- What must happen for missing, malformed, stale, or conflicting data?
- How are duplicates identified, including concurrent submissions?
- Which decisions must be deterministic?
- Which actions require human approval?

## Operations
- What volumes, latency, schedule, and rate limits matter?
- Which errors are retryable? How are partial successes recovered?
- Who receives alerts, and what should logs retain?
- What is the rollback and manual fallback?

Mark answers as confirmed, assumed, or open. Ask only questions that change the design or risk.
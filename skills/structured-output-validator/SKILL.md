---
name: structured-output-validator
description: Validate generated JSON/structured data against schemas and business rules.
---

# Structured Output Validator

## Purpose
Validate generated JSON/structured data against schemas and business rules.

## Procedure
1. Confirm goal, scope, audience, constraints and output format.
2. Inventory supplied evidence and identify the source of truth.
3. Separate facts, assumptions, hypotheses and unknowns.
4. Produce a structured artifact with rationale and actionable next steps.
5. Cover normal, boundary, exception and failure cases.
6. Validate the output against the acceptance checks.

## Guardrails
Separate syntax from semantic validity; reject or quarantine invalid output rather than silently coercing risky values.
Never invent facts, metrics, citations, API details or test results. Use synthetic or approved data; minimise confidential information. Keep consequential changes subject to human approval.

## Output contract
- Summary and intended use
- Evidence, assumptions and unknowns
- Structured artifact with explicit decisions
- Risks, exceptions and unresolved questions
- Validation performed and still required
- Next actions without invented owners or dates

## Acceptance checks
Claims are traceable or labelled; edge cases are covered; output is actionable; validation is explicit; uncertainty is visible.

## Example prompt
"Validate generated JSON/structured data against schemas and business rules. Use fictional or approved sample data, identify unknowns and include an edge case plus a validation plan."

## Evaluation
Pass if the artifact is produced, unknowns are labelled, one boundary/failure case is handled, no unsupported facts are invented, and at least one concrete validation is provided.

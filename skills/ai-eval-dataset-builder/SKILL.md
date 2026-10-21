---
name: ai-eval-dataset-builder
description: Build privacy-safe evaluation datasets with positive, negative and boundary cases.
---

# Ai Eval Dataset Builder

## Purpose
Build privacy-safe evaluation datasets with positive, negative and boundary cases.

## Procedure
1. Confirm goal, scope, audience, constraints and output format.
2. Inventory supplied evidence and identify the source of truth.
3. Separate facts, assumptions, hypotheses and unknowns.
4. Produce a structured artifact with rationale and actionable next steps.
5. Cover normal, boundary, exception and failure cases.
6. Validate the output against the acceptance checks.

## Guardrails
Use synthetic or approved data; document provenance, labels, holdout separation and coverage gaps.
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
"Build privacy-safe evaluation datasets with positive, negative and boundary cases. Use fictional or approved sample data, identify unknowns and include an edge case plus a validation plan."

## Evaluation
Pass if the artifact is produced, unknowns are labelled, one boundary/failure case is handled, no unsupported facts are invented, and at least one concrete validation is provided.

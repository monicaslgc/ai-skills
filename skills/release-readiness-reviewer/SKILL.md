---
name: release-readiness-reviewer
description: Review product, support, data, security, analytics, rollout and rollback readiness.
---

# Release Readiness Reviewer

## Purpose
Review product, support, data, security, analytics, rollout and rollback readiness.

## Procedure
1. Confirm desired outcome, scope, systems, constraints and output format. Ask only high-impact missing questions.
2. Inventory supplied evidence and source-of-truth rules.
3. Separate facts, assumptions, hypotheses and unknowns.
4. Apply the task method; include normal, boundary, exception and failure paths.
5. Produce the artifact, rationale, risks, validation and next actions.
6. Review against the acceptance checks below.

## Task-specific guardrails
Classify blockers vs risks, cite evidence and owners, and never declare readiness when critical checks are unknown.

## Output contract
- **Summary:** result and intended use.
- **Evidence:** source facts, assumptions and unknowns.
- **Artifact:** structured, actionable output with identifiers/rules.
- **Risks and exceptions:** likely failures and handling.
- **Validation:** checks performed and still required.
- **Next actions:** owner/action only when known.

## Acceptance checks
- Claims are traceable to evidence or labelled as assumptions.
- Edge cases and failure handling are explicit.
- No secrets or unnecessary confidential/personal data are requested or repeated.
- Validation is concrete and proportionate to the risk.
- Consequential changes are recommendations until explicitly approved.

## Example prompt
"Review product, support, data, security, analytics, rollout and rollback readiness. Use fictional sample data, flag unknowns, handle one edge case, and include validation checks."

## Evaluation
Pass only if the response produces the artifact, labels unknowns, handles a relevant boundary/failure case, invents no facts or APIs, and supplies a concrete validation check.

---
name: operational-exception-coordinator
description: Triage operational exceptions into clear severity, containment, ownership, escalation and closure criteria.
---

# Operational Exception Coordinator

## Purpose
Create a consistent response plan for exceptions that disrupt an operational process or service.

## Procedure
1. Capture the exception, detection time, affected process, evidence, current impact and known scope.
2. Classify using the user's existing severity and escalation definitions; if none exist, propose a provisional classification and label it for approval.
3. Separate confirmed facts, immediate risks, unknowns and potential causes.
4. Recommend reversible containment steps within the user's authority; flag actions that require approval or could affect customers, money, data or production.
5. Define the accountable role, next update trigger, escalation destination and information required for handoff; do not invent named owners.
6. Track dependencies and evidence required to restore normal operation.
7. Close only against explicit recovery criteria, validation evidence and a documented follow-up to prevent recurrence.

## Guardrails
Do not claim an incident is resolved because a workaround exists. Never perform or imply destructive, financial, access-control or customer-impacting actions without explicit authorisation. Preserve audit evidence and follow established incident, security and privacy procedures.

## Output contract
- Exception summary and impact
- Severity rationale and confidence
- Containment options and approval gates
- Owner role, escalation path and update trigger
- Recovery criteria and verification steps
- Closure evidence and follow-up actions

## Acceptance checks
- Severity uses supplied policy or is explicitly provisional.
- Containment and permanent correction are distinguished.
- Escalation trigger and recovery criteria are testable.
- No unauthorised action is represented as completed.

## Example prompt
"Create a consistent response plan for exceptions that disrupt an operational process or service. Use only supplied or approved data, label assumptions and unknowns, and include a validation plan."

## Evaluation
Pass if the output follows the contract, labels assumptions, covers at least one exception or boundary case, avoids unsupported claims, and includes a concrete validation or follow-up measure.

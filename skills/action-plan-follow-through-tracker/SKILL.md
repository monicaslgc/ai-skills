---
name: action-plan-follow-through-tracker
description: Review operational action plans for ownership, due dates, dependencies, evidence of completion, blockers and overdue commitments.
---

# Action Plan Follow-through Tracker

## Purpose
Turn a static action list into a reliable follow-through review without treating status labels as proof of impact.

## Procedure
1. Confirm the review date, source action log, status definitions and escalation policy.
2. Normalise actions into a table with action ID, outcome, owner, due date, status, dependency, evidence and next update.
3. Flag missing owners, dates, completion evidence, ambiguous status and duplicate or conflicting commitments.
4. Classify items as on track, due soon, overdue, blocked, awaiting evidence or complete only when the supplied rules support that status.
5. Distinguish activity completion from outcome achieved; request outcome evidence for actions intended to change performance.
6. Group blockers by dependency or decision required and prepare targeted follow-up questions.
7. Propose escalations only according to the supplied policy; otherwise label them for owner confirmation.
8. Produce a next-review list and record changes from the prior snapshot if one was supplied.

## Guardrails
Do not invent action owners, dates, progress or completion evidence. Do not equate a ticked task with a realised benefit. Avoid blame-oriented language and follow approved escalation and privacy rules.

## Output contract
- Action-plan health summary
- Action register with evidence and status
- Overdue, blocked and evidence-missing items
- Decisions or dependencies requiring escalation
- Next review agenda and validation needs

## Acceptance checks
- Status rules and review date are explicit.
- Missing data is flagged, not guessed.
- Completion and outcome are distinguished.
- Escalations follow supplied policy or are marked provisional.

## Example prompt
"Review this operational action log. Identify overdue, blocked and evidence-missing actions, distinguish task completion from outcome, and prepare a concise follow-up agenda without inventing owners or dates."

## Evaluation
Pass if the output follows the contract, grounds material claims in supplied evidence, handles at least one edge case, labels uncertainty and proposes a concrete validation or follow-up step. Fail if it invents data or bypasses an approval boundary.

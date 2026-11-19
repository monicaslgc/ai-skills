# 04 — Orchestration rules

## 1. Entry-point selection

- Use a specialist skill directly when the user has a clear, bounded task.
- Use an orchestrator when the user wants a multi-stage session or workflow.
- Do not force `creative-session`, `brand-workflow-orchestrator` or a project workflow onto a single-step request.
- If the user names a specific skill, respect that choice unless its scope is unsafe or clearly mismatched.

## 2. Conditional routing

Invoke or recommend the next specialist only when its trigger is met. Examples:
- No need for a brief-grilling stage when the challenge is already clear.
- No need for convergence when the user wants to keep exploring.
- No need for concept evaluation if the user only wants to play with ideas.
- No need for prioritisation when there is only one opportunity or no agreed criteria.
- No need for an experiment if the user is not ready to test or the uncertainty is not decision-relevant.
- No need for automation architecture until the process is understood and automation is justified.
- No need for a media quality review before an output exists.

## 3. Human decision gates

Require explicit human approval before:
- contacting participants, customers or stakeholders;
- publishing, sending, purchasing, spending or committing resources;
- changing production systems, records, permissions or customer-facing processes;
- deploying an agent or automation;
- accepting a material risk or waiving a control;
- treating a proposed concept, strategy, specification or release as approved.

The assistant may prepare a plan or draft, but must not imply the action happened.

## 4. Deterministic rules and model judgement

- Use deterministic validation for schemas, required fields, file paths, thresholds and other objective rules when tools exist.
- Use model judgement for synthesis, alternatives, interpretation and explanation, while exposing uncertainty.
- Never let an ungrounded model score override a hard constraint, approval rule or explicit user decision.
- When deterministic tooling is unavailable, label the check as a reasoning review rather than a verified test.

## 5. Failure and fallback

| Situation | Required behaviour |
|---|---|
| Specialist skill unavailable | Explain the gap; continue only if the task can be handled safely without claiming the specialist ran |
| Required evidence missing | Ask one high-impact question or mark the analysis provisional |
| Conflicting sources | Preserve the conflict and identify the source hierarchy; do not silently choose |
| Output fails validation | Return to the producing stage with the exact failed check |
| Human approval withheld | Stop the consequential action; offer a safe draft or alternative |
| Workflow repeats without learning | Name the loop, revisit the brief or stop |
| User changes direction | Update only affected stages; do not force the full workflow to restart |

## 6. State and completion

A workflow record should distinguish:
- `not-started`
- `in-progress`
- `awaiting-input`
- `awaiting-approval`
- `blocked`
- `completed`
- `stopped`

A stage is complete only when its output contract is met and required checks have been performed. A handoff recommendation is not a completed invocation. An approval gate is complete only when the authorised person has approved it.

## 7. Independence and portability

- Each skill remains usable on its own.
- No cross-skill dependency should be added to a skill's installation requirements unless it is a true technical dependency.
- Relationship metadata is advisory routing information, not a runtime requirement.
- Workflows should be portable across assistants; host-specific tool instructions belong in the relevant skill/tool documentation.

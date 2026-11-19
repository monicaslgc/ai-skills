# Workflow design — [workflow name]

> Status: DRAFT / IN REVIEW / APPROVED  
> Workflow owner role: [role]  
> Version: [version]

## 1. Objective and boundary

- Trigger:
- Intended outcome:
- Start condition:
- Completion condition:
- Systems/actors in scope:
- Explicitly excluded side effects:

## 2. Step-by-step flow

| Step ID | Actor/system | Input/precondition | Action | Output/state | Evidence/log | Failure branch |
|---|---|---|---|---|---|---|
| WF-001 | [system/role] | [input] | [action] | [result] | [event/reference] | [branch] |

## 3. State model

| Current state | Event/condition | Next state | Allowed action | Forbidden action |
|---|---|---|---|---|
| [state] | [condition] | [state] | [action] | [action] |

## 4. Exception and retry policy

| Failure/exception | Detect by | Retryable? Why? | Attempt/backoff limit | Recovery/manual route | Completion evidence |
|---|---|---|---|---|---|
| [failure] | [signal] | [yes/no/unknown] | [approved policy] | [route] | [evidence] |

Do not retry side effects blindly. Define idempotency and reconciliation before replay.

## 5. Approval gates

| Gate | What is reviewed | Authorised role | Approve/reject outcome | Timeout/escalation |
|---|---|---|---|---|

## 6. Security and operations

- Authentication/least privilege:
- Secret storage:
- Input validation and trust boundaries:
- Logging/redaction/retention:
- Metrics and alerts:
- Operational owner/runbook:
- Rollback or compensation:
- Unverified interfaces:

## 7. Open decisions

| Question | Why it matters | Decision owner role | Needed before |
|---|---|---|---|

## 8. Validation

List happy-path, invalid-input, duplicate, timeout, partial-failure, retry-exhaustion, approval-rejection and recovery tests that apply.

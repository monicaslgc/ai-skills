---
name: configuration-workshop-planner
description: Plan and run a configuration workshop with a customer: goals, who must attend, inputs to prepare, agenda, decisions to take, a configuration sheet, an action list and the follow-up. Use when a product or integration has to be set up with the customer's own rules and data.
---

# Configuration workshop planner

Make a workshop produce decisions and a working configuration, not a long meeting.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What is being configured (modules, products, integrations, roles, templates) and the customer's goal for it.
- The customer's processes and rules that matter, and any documents they can share before the session.
- Who owns the decisions on the customer side, and the technical and business people who must attend.
- Constraints: time available, tools used in the session, languages, and what must be ready by when.

## Workflow

1. State the purpose: what will be decided and what will exist at the end (for example a configured test environment and a signed-off settings sheet).
2. Prepare: send a short pre-read and a list of questions at least a few days earlier, ask for sample data and current process documents, and prepare a draft configuration so the session starts from something concrete.
3. Choose attendees by decision, not by seniority: someone who can decide, someone who knows the process, someone who knows the systems. Keep the group small.
4. Build the agenda in blocks with a time, a lead and an outcome: context, walk through the draft, decisions on each open question, edge cases, integrations, roles and permissions, data, next steps.
5. Run it: show the product in the customer's own scenarios, capture decisions live in a visible log (decision, who decided, why, impact), and park topics that need more input with an owner and date.
6. Configure or update the test setup during or right after the session, and keep a configuration sheet: setting, value, reason, owner, date.
7. Follow up within one working day: summary, decisions, open points, the configuration sheet and the next date. Ask for confirmation in writing.
8. Check later that what was configured matches what was agreed.

## Rules

- Do not run the workshop without a draft; blank-page sessions run long and decide little.
- Every open point leaves with an owner and a date.
- Record why, not only what; the reason explains the setting a year later.
- Do not change production settings in a workshop without the agreed approval step.

## Output format

```
Purpose and expected outcome
Attendees: name | role | decides / informs
Pre-read and inputs requested (with dates)
Agenda: time | block | lead | outcome
Decision log: # | decision | decided by | reason | impact
Configuration sheet: setting | value | reason | owner | date
Open points: item | owner | due
Follow-up message (draft)
```

## Quality checks

- The expected outcome is concrete and was reached or the gap is stated.
- Decisions are recorded with who and why.
- The configuration sheet matches the system.
- The summary went out within a day, with open points owned and dated.

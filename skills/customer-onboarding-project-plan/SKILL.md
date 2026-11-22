---
name: customer-onboarding-project-plan
description: Plan a customer onboarding project end to end: goals, scope, milestones, dependencies, owners on both sides, risks, go-live criteria and a communication rhythm. Use when a new customer has signed and needs to be taken from contract to a working, adopted setup.
---

# Customer onboarding project plan

Turn "the customer has signed" into a plan both sides can follow.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What was sold: scope, products, integrations, dates and commitments in the contract or order.
- The customer's goals and the date by which they need results, and what success looks like to them.
- People: the customer's sponsor, project lead, technical contacts and users; your own team and partners.
- Constraints: customer systems, security reviews, holidays, freezes, other projects, language and time zones.

## Workflow

1. Restate the goals in the customer's words and turn them into measurable success criteria with dates.
2. Define scope: what is in, what is out, what is optional, and what needs a change request if added later.
3. Break the work into phases (for example kick-off, configuration, integration, data, training, test, go-live, hypercare) with a clear deliverable and owner for each.
4. Set milestones and dependencies: what must exist before each step, who provides it, and the date it is needed. Mark the critical path.
5. Assign owners on both sides and agree who decides what. Name a single accountable person per milestone.
6. List risks and assumptions with a mitigation and an early-warning sign for each. Typical ones: late customer data, unavailable technical contacts, scope growth, integration surprises.
7. Define go-live criteria and the plan for hypercare (see [`go-live-and-hypercare-plan`](../go-live-and-hypercare-plan)).
8. Agree the rhythm: kick-off agenda, weekly status, how blockers and decisions are recorded and escalated, who gets the reports.
9. Write the plan so the customer can read it too: dates, owners, what you need from them and by when.

## Rules

- Plan from the customer's date backwards and show what does not fit, instead of hiding it.
- Every task has one owner and a date. "The team" is not an owner.
- Put the customer's work in the plan; delays usually start there.
- Do not promise what the contract does not cover; route additions through change control.

## Output format

```
Customer / sponsor / goal / target date
Success criteria (measurable)
Scope: in / out / optional
Phases and milestones: phase | deliverable | owner (us/customer) | date | depends on
Critical path
Risks and assumptions: risk | likelihood | impact | mitigation | early sign
Go-live criteria
Communication rhythm and escalation path
What we need from the customer, and by when
```

## Quality checks

- Each milestone has an owner, a date and a dependency.
- The critical path and the customer's tasks are visible.
- Risks have an early-warning sign, not only a title.
- A customer reading it knows what to do next week.

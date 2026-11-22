---
name: go-live-and-hypercare-plan
description: Plan a safe go-live and the hypercare period after it: readiness checks, cutover steps, rollback, communication, watch metrics, daily review, exit criteria and handover to normal support. Use before switching a customer or a release live, and for the weeks that follow.
---

# Go-live and hypercare plan

Make the switch deliberate, reversible and watched.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What goes live, for whom, on which date and time window, and what it replaces.
- The test evidence so far, open defects and known limitations.
- Who is involved on both sides during the window and the weeks after, including contact details and time zones.
- What "working" means: the checks and metrics that show the customer is operating normally.

## Workflow

1. Define go-live criteria: tests passed, data loaded and checked, access and roles in place, integrations verified, users trained, support ready, customer sign-off. Mark each as met, not met or waived with the name of who waived it.
2. Write the cutover plan: ordered steps, who does each, how long, the point of no return and how to confirm each step.
3. Write the rollback plan: the trigger (what makes you roll back), the decision-maker, the steps, how long it takes and what the customer is told.
4. Plan communication: before (what changes and when), during (status updates), after (done, what to expect, where to get help).
5. Define hypercare: duration, coverage hours, a single channel, named contacts, response targets and who can make decisions.
6. Choose what to watch each day: errors, failed integrations, usage, tickets by theme, data quality, customer feedback. Set thresholds that trigger action.
7. Run a short daily review during hypercare: what happened, what is open, what changed, what we do next. Keep a log of issues, owner, status and root cause.
8. Define exit criteria: stable for an agreed number of days, no critical open issues, knowledge handed to normal support, and customer agreement.
9. Hold a handover and a short review: what worked, what to change in the next onboarding, and update the playbook.

## Rules

- Do not go live on criteria that are "waived" without a named owner and a written risk.
- A rollback that was never discussed is not a plan.
- Avoid going live just before weekends, holidays or when key people are away.
- Keep the customer informed at every stage, including when nothing happened.

## Output format

```
What goes live / date and window / participants
Go-live criteria: criterion | status | evidence | owner
Cutover steps: # | step | owner | duration | check
Rollback: trigger | decision-maker | steps | time
Communication: when | audience | message | owner
Hypercare: duration | hours | channel | contacts | targets
Daily watch: metric | threshold | action
Exit criteria and handover
Review actions for the next onboarding
```

## Quality checks

- Every criterion has evidence or a named waiver.
- The rollback has a trigger, an owner and a duration.
- The daily watch list has thresholds and actions.
- Exit criteria are measurable and agreed with the customer.

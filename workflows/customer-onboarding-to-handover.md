# Customer onboarding, from signature to handover

Take a new customer from signed contract to a running, documented solution that their own team can operate.

**Use it when:** A new customer has signed and needs configuration, an integration and training before they run on their own.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`statement-of-work-drafter`](../skills/statement-of-work-drafter) | Workshop notes, agreed requirements, quote | Scope document with deliverables, exclusions, responsibilities and open points | Sales and legal fill the price and legal placeholders; the customer agrees the scope |
| 2 | [`customer-onboarding-project-plan`](../skills/customer-onboarding-project-plan) | Agreed scope | Plan with milestones, owners, risks and go-live criteria | Customer sponsor confirms dates and owners |
| 3 | [`configuration-workshop-planner`](../skills/configuration-workshop-planner) | Plan, list of decisions to make | Workshop agenda and configuration sheet | Decisions in the sheet are signed off by the customer |
| 4 | [`integration-readiness-checklist`](../skills/integration-readiness-checklist) | Configuration sheet, system details | Readiness checklist with blockers | Both IT teams confirm access, test data and test plan |
| 5 | [`rollout-coordination-plan`](../skills/rollout-coordination-plan) | Plan, checklist, partner list | Back-scheduled rollout plan with dependencies and sync windows | Every organisation names its owner |
| 6 | [`go-live-and-hypercare-plan`](../skills/go-live-and-hypercare-plan) | Rollout plan, test results | Go-live runbook with rollback and hypercare watch list | Go or no-go decision recorded |
| 7 | [`client-handover-documentation`](../skills/client-handover-documentation) | Everything above plus test evidence | Handover pack with operating guide, support path, known limits and acceptance record | Customer signs acceptance |

## Rules for this workflow

- The scope document is agreed before any plan is built.
- No go-live before the readiness checklist has no open blockers.
- No handover before hypercare has ended or its open items have owners.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`statement-of-work-drafter`, `customer-onboarding-project-plan`, `configuration-workshop-planner`, `integration-readiness-checklist`, `rollout-coordination-plan`, `go-live-and-hypercare-plan`, `client-handover-documentation`

## Start prompt

> I am onboarding a new customer. Start with the statement of work from these workshop notes, and tell me what you need before you move to the plan.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

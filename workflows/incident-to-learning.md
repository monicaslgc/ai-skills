# Incident, from first message to lasting fix

Keep customers informed honestly during an incident, hand engineering what it needs, and turn the incident into a fix and updated guidance.

**Use it when:** A service problem affects customers and needs communication, escalation and a review afterwards.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`customer-incident-communication`](../skills/customer-incident-communication) | Facts known now, impact, next update time | First customer message and update schedule | Incident owner signs off the wording |
| 2 | [`engineering-escalation-brief`](../skills/engineering-escalation-brief) | Symptoms, evidence, affected customers | Brief with reproduction steps, impact and urgency | Engineering lead acknowledges the brief |
| 3 | [`customer-incident-communication`](../skills/customer-incident-communication) | Resolution facts | Resolution message and follow-up summary | Incident owner signs off again |
| 4 | [`project-retrospective`](../skills/project-retrospective) | Timeline, decisions, what worked and what did not | Blameless review with actions and owners | Team agrees the actions |
| 5 | [`customer-playbook-builder`](../skills/customer-playbook-builder) | The incident and its handling | Playbook for the next similar case, with steps that can be automated | Support lead approves the playbook |
| 6 | [`guide-freshness-check`](../skills/guide-freshness-check) | Guides and help pages touched by the incident | List of guides to correct or add | Documentation owner schedules the updates |

## Rules for this workflow

- Never state a cause, a fix time or data loss that is not confirmed.
- Name no supplier, internal system or other customer in customer messages.
- Apologise once, then concentrate on what happens next.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`customer-incident-communication`, `engineering-escalation-brief`, `project-retrospective`, `customer-playbook-builder`, `guide-freshness-check`

## Start prompt

> We have an incident affecting <who>. Draft the first customer message from these facts and tell me which facts are still unconfirmed.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

# Renewal season, from health check to signed renewal

Reach the notice deadline with an honest picture of the customer's health, a prepared conversation and the paperwork ready.

**Use it when:** A contract renews in the next six months, or health signals suggest the relationship needs attention first.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`customer-health-scorecard`](../skills/customer-health-scorecard) | Usage, tickets, sponsor and payment signals | Scorecard with reasons and next actions | Account owner reviews the scores and the unknowns |
| 2 | [`adoption-review`](../skills/adoption-review) | Usage data, expected value from the contract | Gaps between usage and value with targeted interventions | Customer success agrees which interventions to run |
| 3 | [`business-review-pack`](../skills/business-review-pack) | Scorecard, adoption review, results since the start | Review pack with wins, misses and next goals | Account owner approves what is shown to the customer |
| 4 | [`renewal-and-expansion-plan`](../skills/renewal-and-expansion-plan) | Contract dates, review outcome, stakeholder map | Renewal plan with notice deadline, checkpoints, objections and expansion hypothesis | Commercial owner agrees the plan and the lead |
| 5 | [`official-letter-and-notice-writer`](../skills/official-letter-and-notice-writer) | Renewal terms, notice period, any changes | Formal notice or confirmation with key dates and amounts | Legal or management approves before sending |

## Rules for this workflow

- Compute the notice deadline first; checkpoints already in the past are dropped.
- Pricing floors and margins stay out of the review pack and the letter.
- The letter is sent by a person, never by the workflow.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`customer-health-scorecard`, `adoption-review`, `business-review-pack`, `renewal-and-expansion-plan`, `official-letter-and-notice-writer`

## Start prompt

> A contract renews on <date> with <notice> notice. Start with the health scorecard from this data and tell me which signals are missing.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

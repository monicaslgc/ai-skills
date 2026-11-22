# Document an existing app

Produce guides that match how the app really works, with diagrams, and keep them current.

**Use it when:** An app exists with little or outdated documentation and users keep asking the same questions.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`app-flow-mapper`](../skills/app-flow-mapper) | Access to a test account or screenshots | Inventory of real flows with evidence | App owner confirms the flows |
| 2 | [`user-guide-writer`](../skills/user-guide-writer) | Flow inventory | Task-based user guide | A new user follows the guide unaided |
| 3 | [`diagram-with-brand-kit`](../skills/diagram-with-brand-kit) | Flows that need a picture | Diagrams in the graphic kit | Checked as images |
| 4 | [`guide-freshness-check`](../skills/guide-freshness-check) | Release notes after each release | Guides that drifted and update plan | Documentation owner schedules the updates |

## Rules for this workflow

- Describe what the app does, not what it was meant to do.
- Use test accounts and demo data only.
- Re-run the freshness check after every release.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`app-flow-mapper`, `user-guide-writer`, `diagram-with-brand-kit`, `guide-freshness-check`

## Start prompt

> Map the flows of <app> with this test account and give me the inventory before you write any guide.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

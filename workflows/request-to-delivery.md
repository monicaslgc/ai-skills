# Business request to buildable work

Turn a non-technical request into checked requirements, a clear story and a plan engineering can start on.

**Use it when:** A stakeholder asks for something in business terms and nobody has yet written down what is really needed.

## Steps

| # | Skill | Input | Output | Gate (a person decides) |
|---|---|---|---|---|
| 1 | [`requirements-elicitation-plan`](../skills/requirements-elicitation-plan) | The request, list of stakeholders | Discovery plan with questions and techniques | Requester agrees who to talk to |
| 2 | [`stakeholder-request-translator`](../skills/stakeholder-request-translator) | Answers from the discovery | Technical request read back in plain words | Requester confirms the read-back |
| 3 | [`requirements-quality-check`](../skills/requirements-quality-check) | Draft requirements | Gaps, ambiguities and priorities | Requirements owner resolves the findings |
| 4 | [`user-story-writer`](../skills/user-story-writer) | Checked requirements | User stories with acceptance criteria | Product owner accepts the stories |
| 5 | [`change-request-assessor`](../skills/change-request-assessor) | Stories that change existing scope | Effort, risk and schedule effect | Sponsor approves or rejects the change |
| 6 | [`plain-language-technical-explainer`](../skills/plain-language-technical-explainer) | Trade-offs and status | Explanation the business can decide on | Requester makes the decision |

## Rules for this workflow

- Nothing is built from a request until the read-back is confirmed.
- Each requirement is testable before it becomes a story.
- Trade-offs are explained, not decided silently.
- Carry the open items and assumptions from each step into the next.
- Keep the `INTERNAL` line out of anything that goes outside.

## Skills to install

`requirements-elicitation-plan`, `stakeholder-request-translator`, `requirements-quality-check`, `user-story-writer`, `change-request-assessor`, `plain-language-technical-explainer`

## Start prompt

> A stakeholder asked for: <request>. Plan the discovery and tell me what you would need to ask first.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

---
name: customer-feedback-to-product-brief
description: Turn customer feedback about bugs and missing features into a clear brief for Product and Engineering: grouped themes, how many customers and how often, impact, evidence, the customer's goal behind the request and a proposed priority, then close the loop with the customers. Use when feedback is scattered across tickets, calls and emails.
---

# Customer feedback to product brief

Give Product and Engineering evidence they can act on, and give customers an answer.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The raw feedback: tickets, call notes, emails, survey answers, with customer, date and source.
- Customer context: size, stage, contract value or strategic importance, and how long the problem has existed.
- What Product already knows: roadmap, known issues, earlier decisions.
- Who decides priorities in Product and Engineering and in what format they want input.

## Workflow

1. Collect and clean: one row per piece of feedback, with customer, date, source, the exact words and the situation in which it happened.
2. Separate bugs (the product does not do what it should) from requests (the product could do more) and from usability or training issues.
3. Find the customer's goal behind each request ("export every night" may mean "reconcile in the morning"). Write the problem, not the solution the customer proposed.
4. Group into themes and count: how many customers, how many reports, how often, since when and which segments.
5. Describe the impact: what the customer cannot do, the workaround and its cost, the risk to renewal or adoption, and the effect on support volume.
6. Add evidence: quotes, ticket references, screenshots and steps to reproduce for bugs. Keep customer names to what Product needs.
7. Propose a priority with reasons (severity, reach, strategic value, effort if known) and say what you do not know. Leave the final decision to Product.
8. Write the brief: a one-line summary, the problem, who is affected, impact, evidence, workaround, options if any, and the ask.
9. Close the loop: tell each customer what happened to their feedback (planned, not planned and why, fixed, workaround) and record the date. Review open items regularly.

## Rules

- Report the problem and the evidence before any solution.
- Do not promise delivery dates the product team has not committed to.
- Count honestly; do not inflate a theme by repeating one customer's message.
- Share only what is necessary about customers and protect personal data.

## Output format

```
Theme | type (bug / request / usability) | one-line problem
Reach: customers | reports | segments | since
Customer goal behind it
Impact and workaround
Evidence and reproduction steps
Proposed priority and reasons | unknowns
Ask to Product / Engineering
Customer communication: who is told what, and when
```

## Quality checks

- Each theme states a problem, not a solution, and a count.
- Bugs include reproduction steps and evidence.
- The priority proposal gives reasons and states what is unknown.
- Customers who gave the feedback receive an answer.

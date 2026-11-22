---
name: adoption-review
description: Review how a customer actually uses a product: compare usage with the value they expected, find low engagement and blockers, and plan targeted interventions such as training, feature demos and configuration changes. Use after go-live, before a business review, or when usage drops.
---

# Adoption review

Find out whether the customer gets the value they bought, and what would change it.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The customer's goals and the features, workflows and teams that were supposed to deliver them.
- Usage data by team, role, feature and period (and what each measure really counts), plus the go-live date for comparison.
- Support themes, feedback and what users say or do instead of using the product.
- The training given so far, the configuration in place and what changed recently.

## Workflow

1. Write the value hypothesis: which outcomes the customer wanted, how the product should deliver them, and which usage would show it.
2. Look at usage against that hypothesis: who is active, which key features are used or ignored, how it trends since go-live, and where it differs between teams.
3. Find where engagement is low and ask why with evidence: missing training, wrong configuration, unclear value, a blocking defect, a missing feature, a competing tool, no sponsor push.
4. Check the basics before blaming the users: roles and permissions, notifications, data quality, integrations working.
5. Segment the users: champions, regular, occasional, inactive. Learn from what champions do differently.
6. Choose interventions with the best effect for the effort: a short training for a team, a demo of an unused feature, a configuration change, a template, a sponsor message, a quick win in the customer's own data.
7. Give each intervention an owner, a date and a metric that shows it worked, and plan a re-check.
8. Share a short summary with the customer in positive, concrete terms: what is going well, what could be better and what you suggest together.

## Rules

- Usage numbers need context: define what an "active user" is and compare like with like.
- Ask users and sponsors, not only the dashboard; a number says what, not why.
- Do not recommend features the customer's goals do not need.
- Keep personal data to roles and aggregates when sharing results.

## Output format

```
Customer / period / goals and value hypothesis
Usage findings: team or role | feature | usage | trend | comment
Low-engagement causes (with evidence) and checks done
Segments and what champions do
Interventions: action | target | owner | date | success metric
Re-check date
Summary for the customer (draft)
```

## Quality checks

- The hypothesis comes from the customer's goals, not from our feature list.
- Each cause has evidence or is marked as a question to ask.
- Interventions have an owner, a date and a metric.
- The customer summary is specific and balanced.

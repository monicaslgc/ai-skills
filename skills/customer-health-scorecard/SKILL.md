---
name: customer-health-scorecard
description: Build and apply a customer health scorecard from usage, support, relationship and contract signals, with thresholds, a transparent score, reasons and next actions, and early flags for renewal, expansion and churn risk. Use when you own a portfolio of customers and need to know where to spend time.
---

# Customer health scorecard

Make "how is this customer really doing" visible, comparable and actionable.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The customers in scope, their size and stage (onboarding, steady state, renewal window).
- The data you can trust: product usage, tickets and their severity, response and resolution times, survey or feedback scores, meetings held, contract dates, invoices and payment behaviour.
- What a good outcome looks like for each customer and which signals have preceded renewals or churn in the past.
- Who acts on the result and how often it will be reviewed.

## Workflow

1. Choose a small number of signals (five to eight) in four groups: adoption (active users, key features used), support (open issues, severity, trend), relationship (sponsor engagement, last contact, feedback) and commercial (renewal date, payment, expansion interest).
2. Define each signal precisely: source, period, calculation and what counts as green, amber and red. Write the thresholds down.
3. Weight the groups and compute a score per customer, but always show the reasons next to the score. Never publish a score without its drivers.
4. Add flags that override the score: a notice of termination, an unresolved critical issue, a sponsor who left, a missed payment.
5. Mark early signals: usage falling for several periods, rising tickets on the same theme, silence from the sponsor, an approaching renewal with no review held.
6. For each amber or red customer write the next action, an owner and a date. For green customers with growth signals, note an expansion opportunity for the account owner.
7. Review the results regularly and check the scorecard itself: did red customers actually churn, and did green ones renew? Adjust thresholds and weights.
8. Keep the data handling clean: use only data you are allowed to use for this purpose.

## Rules

- A score is a prompt for a conversation, not a verdict. Say what is known, what is missing and how confident you are.
- Do not mix incomparable customers; compare like with like (size, stage, product).
- Missing data is a finding: show it, do not fill it with a guess.
- Avoid personal data about individuals at the customer; keep to roles and aggregates.

## Output format

```
Scope and period
Signals: signal | source | green | amber | red | weight
Scorecard: customer | score | status | main drivers | flags | next action | owner | date
Early signals and expansion opportunities
Data gaps and confidence
Scorecard review: what to adjust
```

## Quality checks

- Every score shows its drivers and the data gaps.
- Thresholds and weights are written down.
- Each amber or red customer has an owner, an action and a date.
- The scorecard is checked against what actually happened.

---
name: engineering-escalation-brief
description: Write a second-line escalation to Engineering that can be acted on at once: customer impact, urgency, what was expected and what happened, steps to reproduce, evidence, what was already tried, scope, workaround and a clear ask, with a plan for customer updates. Use when a customer issue needs engineering attention beyond normal support.
---

# Engineering escalation brief

Give engineers everything they need in the first message, and the customer an honest status.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The customer, environment, product version and the time the problem started or was first seen.
- What the customer is trying to do, what they expected, what happened instead and the exact messages.
- Evidence: screenshots, logs, request and response examples with identifiers (no secrets), timestamps and time zone.
- What has been tried, what changed recently on either side, and whether other customers are affected.
- The business impact and any deadline.

## Workflow

1. Reproduce the problem yourself if you can. If you cannot, say so and give the conditions under which it happens.
2. Write a one-line summary that names the customer-visible effect and the part of the product ("Orders from customer X fail to sync since 09:10 UTC, error 500 on confirmation").
3. State impact and urgency with facts: how many users or transactions, whether a workaround exists, what is at risk and by when. Propose a severity using the agreed definitions.
4. Give the steps to reproduce, expected result and actual result, with the exact data used (anonymised) and the environment.
5. Attach evidence and say what each item shows. Remove secrets and unnecessary personal data.
6. List what was already checked and ruled out, so engineers do not repeat it, and note the most likely areas if you have a basis for it.
7. Check scope: other customers, other environments, time pattern, recent releases or configuration changes.
8. Describe the workaround, who is using it and what it costs the customer.
9. Make the ask specific: investigate, fix, provide a workaround, confirm whether it is a known issue, with a time by which you need an answer.
10. Agree the update rhythm for the customer, and tell them what to expect and when. Update the brief as facts change and record the final root cause and the fix.

## Rules

- Facts first, then interpretation; label guesses as guesses.
- One issue per escalation.
- Never include credentials, tokens or unnecessary personal data in the brief or the attachments.
- Keep the customer informed even when there is no news.

## Output format

```
Summary (one line)
Customer / environment / version / first seen
Impact and urgency (severity proposal)
Steps to reproduce | expected | actual
Evidence (what each shows)
Already checked / ruled out
Scope and recent changes
Workaround and its cost
Ask and needed-by time
Customer update plan
Resolution: root cause, fix, follow-up
```

## Quality checks

- An engineer can reproduce or investigate without asking a first question.
- Impact and urgency are factual and have a severity proposal.
- Evidence is explained and free of secrets.
- The ask, the deadline and the customer update plan are explicit.

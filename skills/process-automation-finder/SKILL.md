---
name: process-automation-finder
description: Identify and prioritise tasks to automate: map the process, estimate effort saved, risk and complexity, choose the right level of automation and design a safe, testable approach with human checks. Use when looking for automation opportunities or deciding whether a task is worth automating.
---

# Process automation finder

Automate the right things, in the right order, without creating new risks.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- A list of recurring tasks, how often, and how long they take.
- Systems and data involved.
- Error rate and impact of mistakes.
- Skills and tools available.

## Workflow

1. List candidate tasks with frequency, time per run, number of people, error rate and the impact of an error.
2. Estimate time saved per month and the effort to build and maintain. Ignore savings you cannot justify.
3. Check suitability: clear rules, stable inputs, digital data, low ambiguity. Tasks needing judgement may only be partly automatable.
4. Rank by value, effort and risk. Start with high-volume, rule-based, low-risk tasks.
5. Choose the approach: template or checklist, spreadsheet formula, script, workflow tool, or AI assistance with human review.
6. Design safeguards: validation rules, logging, alerts on failure, human approval for high-impact steps, and a manual fallback.
7. Plan a pilot with measures: time saved, errors, user satisfaction. Review before scaling.
8. Document the automation and assign an owner for maintenance.

## Output format

| Task | Frequency | Time per run | Error impact | Suitability | Effort | Value | Risk | Approach |
|---|---|---|---|---|---|---|---|---|

Priority list, pilot plan, safeguards, owner.

## Safety

- Do not automate decisions that affect people or money without human review.
- Keep credentials out of scripts; use a secrets store.
- Test with synthetic data first.

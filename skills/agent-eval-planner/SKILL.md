---
name: agent-eval-planner
description: Plan an evaluation for an AI agent or skill: representative tasks, edge and adversarial cases, scoring rubric, pass thresholds, human review sampling and a regression suite. Use before releasing an agent, after changing a prompt or tool, or when asked how to test an agent.
---

# Agent eval planner

Decide how you will know the agent works, and keep checking after every change.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The agent charter or skill.
- Real or realistic example tasks.
- Known failure cases and risks.
- How outputs will be judged and by whom.

## Workflow

1. Define what 'good' means for each task type, in observable terms.
2. Write test cases from three groups: typical tasks, edge cases (missing, ambiguous or conflicting input), and adversarial cases (prompt injection, requests outside scope, attempts to exceed permissions).
3. For each case record the input, the expected behaviour, and what counts as a failure. Use synthetic data only.
4. Create a scoring rubric (for example correct, safe, complete, follows format) and decide pass thresholds, with higher bars for safety failures.
5. Decide how outputs are scored: automatic checks where possible, otherwise human review of a sample.
6. Plan runs: before release, after every change to prompts, tools or models, and on a schedule.
7. Keep a regression suite. Every real failure becomes a new test case.
8. Report results with the number of cases; do not claim reliability from a handful of runs.

## Output format

| ID | Group | Input (synthetic) | Expected behaviour | Failure looks like | Pass rule |
|---|---|---|---|---|---|

Then: rubric, thresholds, run plan, human review plan, known gaps.

## Safety

- Use synthetic or anonymised data, never real personal or confidential data.
- Run adversarial tests in a sandbox, not against live systems.
- Do not claim the agent is safe or reliable beyond what the tests show.

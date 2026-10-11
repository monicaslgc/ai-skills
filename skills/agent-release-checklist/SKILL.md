---
name: agent-release-checklist
description: Run a release checklist for AI agent changes: version the prompt, skills, tools and model, run evaluations, review permissions and cost, stage the rollout, monitor and keep a rollback plan. Use before releasing or updating an agent, skill or prompt.
---

# Agent release checklist

Treat agent changes like software releases: versioned, tested, reviewed and reversible.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What is changing: prompt, skills, tools, model or settings.
- Latest evaluation results.
- The agent charter and permission list.
- Current version and rollback option.

## Workflow

1. Name the new version and list every change, including prompts, skills, tools, model and settings. Keep a change log.
2. Run the evaluation suite (see agent-eval-planner) and compare with the previous version. Investigate any regression.
3. Re-check permissions (see agent-permissions-review) and approval gates for new tools or actions.
4. Check cost and speed against expectations for typical tasks.
5. Plan the rollout: test environment, then a small group, then everyone. Define what would stop the rollout.
6. Plan monitoring: errors, refusals, escalations, user feedback, cost.
7. Write the rollback plan and confirm it works: how to return to the previous version and who can do it.
8. Get sign-off from the owner and record the release.

## Output format

```
Release: <agent> vX.Y, date, owner
Changes (prompt / skills / tools / model / settings)
Evaluation: before vs after, regressions
Permission and approval review
Cost and speed
Rollout stages and stop criteria
Monitoring
Rollback plan (tested: yes/no)
Sign-off
```

## Safety

- Do not release with unexplained evaluation regressions.
- Never ship new tool access without a permissions review.
- Keep the previous version available until the new one has proven stable.

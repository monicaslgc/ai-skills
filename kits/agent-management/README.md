# Agent management kit

Skills for running AI agents responsibly: charter, permissions, evaluation, approval gates, release and incident review.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`agent-charter-writer`](../../skills/agent-charter-writer) | Write a job description for an AI agent: scope, tools, autonomy, owner |
| [`agent-permissions-review`](../../skills/agent-permissions-review) | Review an agent's tool and data access for least privilege |
| [`agent-approval-gates`](../../skills/agent-approval-gates) | Decide which agent actions need human approval and how to ask |
| [`agent-eval-planner`](../../skills/agent-eval-planner) | Plan test cases and scoring so you can trust and regression-test an agent |
| [`agent-release-checklist`](../../skills/agent-release-checklist) | Version, test and roll out agent changes safely with a rollback plan |
| [`agent-incident-review`](../../skills/agent-incident-review) | Run a blameless review when an agent does something wrong |

## Suggested order

1. Define the job with `agent-charter-writer`.
2. Limit what it can touch with `agent-permissions-review` and decide what needs a human with `agent-approval-gates`.
3. Prove it works with `agent-eval-planner`.
4. Ship changes with `agent-release-checklist`.
5. When something goes wrong, use `agent-incident-review` and add the failure to the tests.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/agent-charter-writer ~/.claude/skills/
cp -r ai-skills/skills/agent-permissions-review ~/.claude/skills/
cp -r ai-skills/skills/agent-approval-gates ~/.claude/skills/
cp -r ai-skills/skills/agent-eval-planner ~/.claude/skills/
cp -r ai-skills/skills/agent-release-checklist ~/.claude/skills/
cp -r ai-skills/skills/agent-incident-review ~/.claude/skills/
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

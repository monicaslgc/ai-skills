---
name: agent-charter-writer
description: Write a charter for an AI agent: purpose, users, tasks in and out of scope, tools and data access, autonomy level, escalation rules, success measures, owner and review cadence. Use when creating, documenting or reviewing an AI agent or assistant.
---

# Agent charter writer

Give every agent a clear job description so people know what it is for, what it may touch and who is accountable.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What the agent is meant to do and for whom.
- Tools, systems and data it will use.
- Risks the user already worries about.
- Who will own it.

## Workflow

1. Write the purpose in one sentence and name the users.
2. List tasks the agent should do, and tasks it must not do, with examples of each.
3. List tools, data sources and permissions, and mark each as read-only or can-change.
4. Choose the autonomy level: suggest only, act with approval, or act and report. Justify it.
5. Write escalation rules: when to stop and ask a human, and who.
6. Define success measures and failure signs that can be observed.
7. Name the owner, the backup owner and the review cadence.
8. Add the known limits: what it cannot reliably do and where it can be wrong.

## Output format

```
Agent: <name>, owner, version, date
Purpose and users
In scope / Out of scope
Tools and data (read / change)
Autonomy level and approval rules
Escalation rules
Success measures / Failure signs
Known limits
Review cadence
```

## Safety

- Default to the lowest autonomy that still delivers value.
- Never list credentials in the charter; reference where they are stored.
- Do not describe capabilities the agent has not been tested for.

# Project management kit

Skills that take a project from idea to close: charter, plan, risk log, status reports, minutes, change control and retrospective.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`project-charter-writer`](../../skills/project-charter-writer) | Write a one-page project charter before work starts |
| [`project-plan-builder`](../../skills/project-plan-builder) | Break a project into work packages, dependencies and milestones |
| [`raid-log-manager`](../../skills/raid-log-manager) | Keep a log of risks, assumptions, issues and dependencies |
| [`status-report-writer`](../../skills/status-report-writer) | Write a short, honest status report with RAG |
| [`meeting-minutes-to-actions`](../../skills/meeting-minutes-to-actions) | Turn meeting notes or transcripts into decisions and owned actions |
| [`change-request-assessor`](../../skills/change-request-assessor) | Assess the impact of a scope or schedule change request |
| [`project-retrospective`](../../skills/project-retrospective) | Run a blameless retrospective with 1-3 concrete actions |

## Suggested order

1. Start with `project-charter-writer` so scope and success are agreed.
2. Use `project-plan-builder` to turn the charter into work, dependencies and dates.
3. Keep `raid-log-manager` open for the life of the project.
4. Report weekly with `status-report-writer`; turn meetings into actions with `meeting-minutes-to-actions`.
5. Use `change-request-assessor` whenever scope, cost or dates are challenged.
6. Close with `project-retrospective`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/project-charter-writer ~/.claude/skills/
cp -r ai-skills/skills/project-plan-builder ~/.claude/skills/
cp -r ai-skills/skills/raid-log-manager ~/.claude/skills/
cp -r ai-skills/skills/status-report-writer ~/.claude/skills/
cp -r ai-skills/skills/meeting-minutes-to-actions ~/.claude/skills/
cp -r ai-skills/skills/change-request-assessor ~/.claude/skills/
cp -r ai-skills/skills/project-retrospective ~/.claude/skills/
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

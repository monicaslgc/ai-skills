# Documentation kit

Skills for documenting apps that already exist (map how they really work, write guides people can follow, draw clear diagrams, keep guides current) and for producing official documents and client documentation: letters and notices, handover packs, reports, minutes, scope documents and templates.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`app-flow-mapper`](../../skills/app-flow-mapper) | Map the real flows of an existing app, step by step, with evidence |
| [`user-guide-writer`](../../skills/user-guide-writer) | Write a task-based user guide from a flow inventory, screenshots or the app |
| [`diagram-with-brand-kit`](../../skills/diagram-with-brand-kit) | Draw a clear diagram that follows a graphic kit, and check it as an image |
| [`guide-freshness-check`](../../skills/guide-freshness-check) | Find the guides that no longer match the app and plan the updates |
| [`official-letter-and-notice-writer`](../../skills/official-letter-and-notice-writer) | Draft official letters and formal notices that are clear and stand up as a record |
| [`client-handover-documentation`](../../skills/client-handover-documentation) | Assemble the handover pack a client needs to run what was delivered |
| [`status-and-performance-report`](../../skills/status-and-performance-report) | Write a periodic report with checked figures, risks and decisions needed |
| [`meeting-minutes-and-action-log`](../../skills/meeting-minutes-and-action-log) | Turn a meeting into minutes, decisions, actions and a follow-up message |
| [`statement-of-work-drafter`](../../skills/statement-of-work-drafter) | Draft a project scope document both sides can agree before work starts |
| [`document-template-and-style-guide`](../../skills/document-template-and-style-guide) | Create templates and a short style guide for consistent client documents |

## Suggested order

1. Record how the app really works with `app-flow-mapper`.
2. Write the guides with `user-guide-writer`.
3. Add a diagram where a picture explains faster than text, with `diagram-with-brand-kit`.
4. After each release, check what drifted with `guide-freshness-check`.

For client documents: `statement-of-work-drafter` before the work, `meeting-minutes-and-action-log` during it, `status-and-performance-report` periodically, `official-letter-and-notice-writer` for formal messages, `client-handover-documentation` at the end and `document-template-and-style-guide` to keep all of them consistent.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/app-flow-mapper ~/.claude/skills/
cp -r ai-skills/skills/user-guide-writer ~/.claude/skills/
cp -r ai-skills/skills/diagram-with-brand-kit ~/.claude/skills/
cp -r ai-skills/skills/guide-freshness-check ~/.claude/skills/
cp -r ai-skills/skills/official-letter-and-notice-writer ~/.claude/skills/
cp -r ai-skills/skills/client-handover-documentation ~/.claude/skills/
cp -r ai-skills/skills/status-and-performance-report ~/.claude/skills/
cp -r ai-skills/skills/meeting-minutes-and-action-log ~/.claude/skills/
cp -r ai-skills/skills/statement-of-work-drafter ~/.claude/skills/
cp -r ai-skills/skills/document-template-and-style-guide ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\app-flow-mapper "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\user-guide-writer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\diagram-with-brand-kit "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\guide-freshness-check "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\official-letter-and-notice-writer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\client-handover-documentation "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\status-and-performance-report "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\meeting-minutes-and-action-log "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\statement-of-work-drafter "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\document-template-and-style-guide "$env:USERPROFILE\.claude\skills\"
```

These skills need no tools or servers. `app-flow-mapper` works best when your agent can drive a browser or see screenshots, and `diagram-with-brand-kit` works best when it can run a headless browser to render the image; both fall back to asking you for screenshots or for the rendered file. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Use test accounts and demo data when exploring an app, and do not paste real personal data, credentials or confidential material into a chat you do not control.

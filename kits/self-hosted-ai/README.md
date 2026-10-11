# Self-hosted AI and homelab kit

Skills for running AI and services at home: planning deployments, designing workflows, triaging incidents, controlling memory and database pitfalls, and checking on a PC over SSH.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`local-ai-deployment-planner`](../../skills/local-ai-deployment-planner) | Plan a local model deployment |
| [`self-hosted-ai-workflow-designer`](../../skills/self-hosted-ai-workflow-designer) | Design an automation between services |
| [`self-hosted-incident-triage`](../../skills/self-hosted-incident-triage) | Diagnose a failing self-hosted service |
| [`local-llm-ram-guard`](../../skills/local-llm-ram-guard) | Stop local models exhausting host RAM |
| [`slow-llm-db-safety`](../../skills/slow-llm-db-safety) | Fix database errors that follow slow local-model calls |
| [`ssh-remote-pc`](../../skills/ssh-remote-pc) | Check on or run safe commands on a personal Windows PC |

## Suggested order

1. Plan the setup with `local-ai-deployment-planner` and design automations with `self-hosted-ai-workflow-designer`.
2. Keep it stable with `local-llm-ram-guard` and `slow-llm-db-safety`.
3. When something fails, use `self-hosted-incident-triage`, and `ssh-remote-pc` to check a Windows PC.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/local-ai-deployment-planner ~/.claude/skills/
cp -r ai-skills/skills/self-hosted-ai-workflow-designer ~/.claude/skills/
cp -r ai-skills/skills/self-hosted-incident-triage ~/.claude/skills/
cp -r ai-skills/skills/local-llm-ram-guard ~/.claude/skills/
cp -r ai-skills/skills/slow-llm-db-safety ~/.claude/skills/
cp -r ai-skills/skills/ssh-remote-pc ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\local-ai-deployment-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\self-hosted-ai-workflow-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\self-hosted-incident-triage "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\local-llm-ram-guard "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\slow-llm-db-safety "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\ssh-remote-pc "$env:USERPROFILE\.claude\skills\"
```

Most of these skills need no tools. `ssh-remote-pc` needs the SSH MCP server in [`tools/ssh-remote-pc-mcp`](../../tools/ssh-remote-pc-mcp). Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

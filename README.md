# AI Skills

![Validate](https://github.com/monicaslgc/ai-skills/actions/workflows/validate.yml/badge.svg)

Small, single-purpose AI skills (`SKILL.md` instruction files) that I use for my self-hosted homelab, smart home and personal AI memory. Each skill is independent: copy one folder and it works.

Everything here is provider-neutral Markdown. The skills that call tools (Home Assistant, memory, SSH) expect a matching MCP server to be connected; see **Needs**.

## Skills

| Skill | Use it when | Needs |
|---|---|---|
| [`control-devices`](skills/control-devices) | "Turn off the living room lights", set thermostat, blinds, fans | Home Assistant MCP server |
| [`manage-automations`](skills/manage-automations) | List, create, enable or trigger Home Assistant automations | Home Assistant MCP server |
| [`query-status`](skills/query-status) | "What's the state of X", history, unavailable entities | Home Assistant MCP server |
| [`memory-search`](skills/memory-search) | Look up something from past conversations | Memory MCP server |
| [`memory-recall`](skills/memory-recall) | Start a session with relevant past context loaded | Memory MCP server |
| [`memory-browse`](skills/memory-browse) | See an overview of what's stored | Memory MCP server |
| [`memory-facts`](skills/memory-facts) | Show structured facts and preferences | Memory MCP server |
| [`ssh-remote-pc`](skills/ssh-remote-pc) | Check on or run safe commands on a personal Windows PC | SSH MCP server |
| [`local-ai-deployment-planner`](skills/local-ai-deployment-planner) | Plan a local model deployment | nothing |
| [`self-hosted-incident-triage`](skills/self-hosted-incident-triage) | Diagnose a failing self-hosted service | nothing |
| [`self-hosted-ai-workflow-designer`](skills/self-hosted-ai-workflow-designer) | Design an automation between services | nothing |
| [`job-posting-scorer`](skills/job-posting-scorer) | Rank job postings with transparent, rules-based scoring | nothing |
| [`slow-llm-db-safety`](skills/slow-llm-db-safety) | Fix database errors that follow slow local-model calls | nothing |
| [`local-llm-ram-guard`](skills/local-llm-ram-guard) | Stop local models exhausting host RAM | nothing |
| [`content-pipeline-planner`](skills/content-pipeline-planner) | Plan an auto-edit pipeline for short vertical videos | nothing |

## Install one skill

**Claude Code** (project or personal):

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/self-hosted-incident-triage ~/.claude/skills/
```

**Codex / other agents:** copy the skill folder to the agent's skills directory (for Codex, `.agents/skills/<skill-name>/`).

**Any chat model:** open the skill's `SKILL.md` and paste it in as instructions.

Every skill folder also has a `USER_STORY.md` with who it is for, a scenario, acceptance criteria and a prompt to try.

## Try it

Ask in plain language. Examples:

- `My Jellyfin container keeps restarting. Triage it, read-only checks first.` (`self-hosted-incident-triage`)
- `Can I run a 14B model on 16 GB of VRAM alongside Whisper?` (`local-ai-deployment-planner`)
- `Dim the living room to 30%.` (`control-devices`)
- `What do we already know about my backup setup?` (`memory-recall`)
- `Score these five job postings against my skills list.` (`job-posting-scorer`)
- `My host is at 95% RAM and Ollama is running; what should I check?` (`local-llm-ram-guard`)

## Safety

Skills that can act (devices, automations, SSH) ask for confirmation before anything destructive or multi-device. No credentials, hostnames or IP addresses are stored in this repo; server details belong in your MCP server's environment variables.

## Get involved

- **Need a skill?** [Request one](../../issues/new?template=skill_request.yml)
- **A skill gave a bad answer?** [Report it](../../issues/new?template=bad_output.yml)
- **Want to add or improve one?** See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT

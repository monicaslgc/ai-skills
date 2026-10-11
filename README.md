# AI Skills

![Validate](https://github.com/monicaslgc/ai-skills/actions/workflows/validate.yml/badge.svg)

Small, single-purpose AI skills (`SKILL.md` instruction files) for smart homes, self-hosted AI, careers and content creation. Each skill is independent: copy one folder and it works.

The instructions are plain Markdown and work with any agent that supports `SKILL.md`. Some skills call tools, and those tools must exist in your setup; see [Tool requirements](#tool-requirements).

**Status:** prototypes. They have been used and checked for structure, but no formal model evaluations have been run, so review the output before acting on it.

## Skills

### Smart home

| Skill | Use it when | Needs |
|---|---|---|
| [`control-devices`](skills/control-devices) | "Turn off the living room lights", set thermostat, blinds, fans | [Home Assistant server](tools/home-assistant-mcp) |
| [`manage-automations`](skills/manage-automations) | List, create, enable or trigger Home Assistant automations | [Home Assistant server](tools/home-assistant-mcp) |
| [`query-status`](skills/query-status) | "What's the state of X", history, unavailable entities | [Home Assistant server](tools/home-assistant-mcp) |

### Memory

| Skill | Use it when | Needs |
|---|---|---|
| [`memory-search`](skills/memory-search) | Look up something from past conversations | Basic Memory server |
| [`memory-recall`](skills/memory-recall) | Start a session with relevant past context loaded | Basic Memory server |
| [`memory-browse`](skills/memory-browse) | See an overview of what's stored | Basic Memory server |
| [`memory-facts`](skills/memory-facts) | Show structured facts and preferences | Basic Memory server |

### Self-hosted AI and homelab

| Skill | Use it when | Needs |
|---|---|---|
| [`local-ai-deployment-planner`](skills/local-ai-deployment-planner) | Plan a local model deployment | nothing |
| [`self-hosted-incident-triage`](skills/self-hosted-incident-triage) | Diagnose a failing self-hosted service | nothing |
| [`self-hosted-ai-workflow-designer`](skills/self-hosted-ai-workflow-designer) | Design an automation between services | nothing |
| [`local-llm-ram-guard`](skills/local-llm-ram-guard) | Stop local models exhausting host RAM | nothing |
| [`slow-llm-db-safety`](skills/slow-llm-db-safety) | Fix database errors that follow slow local-model calls | nothing |
| [`ssh-remote-pc`](skills/ssh-remote-pc) | Check on or run safe commands on a personal Windows PC | [SSH server](tools/ssh-remote-pc-mcp) |

### Careers and planning

| Skill | Use it when | Needs |
|---|---|---|
| [`job-posting-scorer`](skills/job-posting-scorer) | Rank job postings with transparent, rules-based scoring | nothing |
| [`user-story-writer`](skills/user-story-writer) | Write a user story with testable acceptance criteria for any skill or feature | nothing |

### Content creation

| Skill | Use it when | Needs |
|---|---|---|
| [`content-pipeline-planner`](skills/content-pipeline-planner) | Plan an auto-edit pipeline for short vertical videos | nothing |
| [`plan-creator-content`](skills/plan-creator-content) | Research-backed content plans, briefs, calendars and reviews | image / video tools |
| [`write-social-captions`](skills/write-social-captions) | Platform-specific captions, titles and hashtags | image / video tools |
| [`edit-short-form-videos`](skills/edit-short-form-videos) | Edit plans, 9:16 reframing, video repairs and audio checks | image / video tools |
| [`make-daily-challenge-shorts`](skills/make-daily-challenge-shorts) | One Short per day for a themed challenge from your own template | image / video tools |
| [`photo-post-deliverables`](skills/photo-post-deliverables) | Five sized exports per image for photo posts and carousels | Python 3 + Pillow |
| [`design-youtube-thumbnails`](skills/design-youtube-thumbnails) | Thumbnails and editable templates from real photos and game art | image / video tools |
| [`create-channel-brand-assets`](skills/create-channel-brand-assets) | Banners, frames, cutouts, mascot art and component packs | image / video tools |
| [`create-cozy-gameplay-overlays`](skills/create-cozy-gameplay-overlays) | Vertical overlays, plates and title cards for cozy gameplay videos | image / video tools |
| [`deslop-designs`](skills/deslop-designs) | Checklist that removes generic AI-looking tells from designs | image / video tools |
| [`style-inspired-cosplay-looks`](skills/style-inspired-cosplay-looks) | Describe dress-up looks inspired by other characters honestly | image / video tools |

## Tool requirements

The tool-based skills need an MCP server that exposes the tools below. The two servers I wrote are included in [`tools/`](tools); the memory skills use the open-source Basic Memory server.

| Skills | Server | Tools used |
|---|---|---|
| `control-devices`, `manage-automations`, `query-status` | [`tools/home-assistant-mcp`](tools/home-assistant-mcp) | `get_state`, `get_all_states`, `get_history`, `call_service`, `get_services`, `list_automations`, `trigger_automation`, `enable_automation`, `disable_automation`, `send_notification` |
| `memory-search`, `memory-recall`, `memory-browse`, `memory-facts` | [Basic Memory](https://github.com/basicmachines-co/basic-memory) (`uvx basic-memory mcp`) | `search_notes`, `read_note`, `list_directory`, `recent_activity`, `build_context`, `list_memory_projects`, `edit_note`, `write_note` |
| `ssh-remote-pc` | [`tools/ssh-remote-pc-mcp`](tools/ssh-remote-pc-mcp) | `run_command`, `system_status`, `list_processes`, `list_services`, `manage_service` |

Each included server has its own README with setup steps. Credentials go in environment variables, never in files in this repo.

The local AI, job scoring, database safety, RAM guard, content pipeline and user-story skills need no tools. The creator skills work best when your agent can view images and video; `photo-post-deliverables` also needs Python 3 and Pillow (`pip install pillow`).

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

Skills that can change things (devices, automations, SSH) are written to confirm before destructive or multi-device actions, but you should still review what an agent proposes before approving it. The skills never ask you to paste secrets. No credentials, hostnames or IP addresses are stored in this repo; server details belong in your MCP server's environment variables.

## Get involved

- **Need a skill?** [Request one](../../issues/new?template=skill_request.yml)
- **A skill gave a bad answer?** [Report it](../../issues/new?template=bad_output.yml)
- **Want to add or improve one?** See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT

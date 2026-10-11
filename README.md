# AI Skills

![Validate](https://github.com/monicaslgc/ai-skills/actions/workflows/validate.yml/badge.svg)

Small, single-purpose AI skills (`SKILL.md` instruction files) for smart homes, self-hosted AI, careers, content creation, project management, people operations, support operations and AI agent management. Each skill is independent: copy one folder and it works.

The instructions are plain Markdown and work with any agent that supports `SKILL.md`. Some skills call tools, and those tools must exist in your setup; see [Tool requirements](#tool-requirements).

**Status:** prototypes. They have been used and checked for structure, but no formal model evaluations have been run, so review the output before acting on it.

## Skills

### Smart home

Part of the [Smart home kit](kits/smart-home).

| Skill | Use it when | Needs |
|---|---|---|
| [`control-devices`](skills/control-devices) | Control lights, climate, covers and fans in plain language | [Home Assistant server](tools/home-assistant-mcp) |
| [`query-status`](skills/query-status) | Ask about device states, sensors and history | [Home Assistant server](tools/home-assistant-mcp) |
| [`manage-automations`](skills/manage-automations) | List, trigger, enable and disable automations | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-device-health-check`](skills/ha-device-health-check) | Find unavailable devices, low batteries and stale sensors | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-lighting-troubleshooter`](skills/ha-lighting-troubleshooter) | Diagnose lights that do not respond or behave strangely | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-automation-designer`](skills/ha-automation-designer) | Design a robust automation and give YAML to paste in Home Assistant | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-automation-debugger`](skills/ha-automation-debugger) | Find out why an automation did not run or ran when it should not | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-energy-insights`](skills/ha-energy-insights) | Analyse power and energy use: peaks, standby load and savings ideas | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-climate-comfort-advisor`](skills/ha-climate-comfort-advisor) | Review heating and cooling behaviour and suggest comfort and savings | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-night-security-check`](skills/ha-night-security-check) | Run a bedtime or leaving-home check of locks, doors, windows and lights | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-home-maintenance-planner`](skills/ha-home-maintenance-planner) | Plan recurring home maintenance and set up reminders | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-vacuum-routines`](skills/ha-vacuum-routines) | Plan robot vacuum routines and handle errors and scheduling | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-notification-designer`](skills/ha-notification-designer) | Design useful notifications without alert fatigue | [Home Assistant server](tools/home-assistant-mcp) |
| [`ha-entity-naming-audit`](skills/ha-entity-naming-audit) | Audit entity names and propose a clean, consistent naming scheme | [Home Assistant server](tools/home-assistant-mcp) |

### Memory

Part of the [Memory kit](kits/memory).

| Skill | Use it when | Needs |
|---|---|---|
| [`memory-search`](skills/memory-search) | Look up something from past conversations | [Basic Memory server](https://github.com/basicmachines-co/basic-memory) |
| [`memory-recall`](skills/memory-recall) | Start a session with relevant past context loaded | [Basic Memory server](https://github.com/basicmachines-co/basic-memory) |
| [`memory-browse`](skills/memory-browse) | See an overview of what's stored | [Basic Memory server](https://github.com/basicmachines-co/basic-memory) |
| [`memory-facts`](skills/memory-facts) | Show structured facts and preferences | [Basic Memory server](https://github.com/basicmachines-co/basic-memory) |

### Self-hosted AI and homelab

Part of the [Self-hosted AI and homelab kit](kits/self-hosted-ai).

| Skill | Use it when | Needs |
|---|---|---|
| [`local-ai-deployment-planner`](skills/local-ai-deployment-planner) | Plan a local model deployment | nothing |
| [`self-hosted-ai-workflow-designer`](skills/self-hosted-ai-workflow-designer) | Design an automation between services | nothing |
| [`self-hosted-incident-triage`](skills/self-hosted-incident-triage) | Diagnose a failing self-hosted service | nothing |
| [`local-llm-ram-guard`](skills/local-llm-ram-guard) | Stop local models exhausting host RAM | nothing |
| [`slow-llm-db-safety`](skills/slow-llm-db-safety) | Fix database errors that follow slow local-model calls | nothing |
| [`ssh-remote-pc`](skills/ssh-remote-pc) | Check on or run safe commands on a personal Windows PC | [SSH server](tools/ssh-remote-pc-mcp) |

### Content creation

Part of the [Content creation kit](kits/content-creation).

| Skill | Use it when | Needs |
|---|---|---|
| [`plan-creator-content`](skills/plan-creator-content) | Research-backed content plans, briefs, calendars and reviews | image / video tools |
| [`content-pipeline-planner`](skills/content-pipeline-planner) | Plan an auto-edit pipeline for short vertical videos | nothing |
| [`write-social-captions`](skills/write-social-captions) | Platform-specific captions, titles and hashtags | image / video tools |
| [`style-inspired-cosplay-looks`](skills/style-inspired-cosplay-looks) | Describe dress-up looks inspired by other characters honestly | image / video tools |
| [`edit-short-form-videos`](skills/edit-short-form-videos) | Edit plans, 9:16 reframing, video repairs and audio checks | image / video tools |
| [`make-daily-challenge-shorts`](skills/make-daily-challenge-shorts) | One Short per day for a themed challenge from your own template | image / video tools |
| [`photo-post-deliverables`](skills/photo-post-deliverables) | Five sized exports per image for photo posts and carousels | Python 3 + Pillow |
| [`design-youtube-thumbnails`](skills/design-youtube-thumbnails) | Thumbnails and editable templates from real photos and game art | image / video tools |
| [`create-channel-brand-assets`](skills/create-channel-brand-assets) | Banners, frames, cutouts, mascot art and component packs | image / video tools |
| [`create-cozy-gameplay-overlays`](skills/create-cozy-gameplay-overlays) | Vertical overlays, plates and title cards for cozy gameplay videos | image / video tools |
| [`deslop-designs`](skills/deslop-designs) | Checklist that removes generic AI-looking tells from designs | image / video tools |

### Project management

Part of the [Project management kit](kits/project-management).

| Skill | Use it when | Needs |
|---|---|---|
| [`project-charter-writer`](skills/project-charter-writer) | Write a one-page project charter before work starts | nothing |
| [`project-plan-builder`](skills/project-plan-builder) | Break a project into work packages, dependencies and milestones | nothing |
| [`user-story-writer`](skills/user-story-writer) | Write a user story with testable acceptance criteria for any skill or feature | nothing |
| [`raid-log-manager`](skills/raid-log-manager) | Keep a log of risks, assumptions, issues and dependencies | nothing |
| [`status-report-writer`](skills/status-report-writer) | Write a short, honest status report with RAG | nothing |
| [`meeting-minutes-to-actions`](skills/meeting-minutes-to-actions) | Turn meeting notes or transcripts into decisions and owned actions | nothing |
| [`change-request-assessor`](skills/change-request-assessor) | Assess the impact of a scope or schedule change request | nothing |
| [`project-retrospective`](skills/project-retrospective) | Run a blameless retrospective with 1-3 concrete actions | nothing |

### People operations

Part of the [People operations kit](kits/people-operations).

| Skill | Use it when | Needs |
|---|---|---|
| [`capacity-planning-forecast`](skills/capacity-planning-forecast) | Forecast workload and turn it into staffing needs with scenarios | nothing |
| [`shift-schedule-planner`](skills/shift-schedule-planner) | Build a fair shift schedule that meets coverage and respects rules | nothing |
| [`leave-attendance-process-designer`](skills/leave-attendance-process-designer) | Design a clear leave and attendance process with approvals and records | nothing |
| [`cv-screening-rubric`](skills/cv-screening-rubric) | Screen CVs against clear, job-related criteria | nothing |
| [`interview-kit-builder`](skills/interview-kit-builder) | Build a structured interview with questions and a scoring rubric | nothing |
| [`employee-onboarding-plan`](skills/employee-onboarding-plan) | Plan a new starter's first days, weeks and 90 days | nothing |

### Support operations

Part of the [Support operations kit](kits/support-knowledge).

| Skill | Use it when | Needs |
|---|---|---|
| [`sla-and-escalation-designer`](skills/sla-and-escalation-designer) | Define priorities, response and resolution targets and escalation paths | nothing |
| [`support-kpi-dashboard-designer`](skills/support-kpi-dashboard-designer) | Choose support metrics, define them precisely and design a dashboard | nothing |
| [`ticket-quality-audit`](skills/ticket-quality-audit) | Audit support tickets or calls with a scorecard and calibration | nothing |
| [`agent-coaching-plan`](skills/agent-coaching-plan) | Prepare a coaching conversation and development plan for a team member | nothing |
| [`access-request-workflow`](skills/access-request-workflow) | Design joiner, mover, leaver and access request workflows with approvals and audit | nothing |

### Operations and productivity

Part of the [Operations and productivity kit](kits/operations-productivity).

| Skill | Use it when | Needs |
|---|---|---|
| [`sop-writer`](skills/sop-writer) | Write a clear standard operating procedure | nothing |
| [`process-automation-finder`](skills/process-automation-finder) | Find and prioritise tasks worth automating, with risks and a safe design | nothing |
| [`kpi-insight-writer`](skills/kpi-insight-writer) | Turn numbers into a short insight, with causes, caveats and actions | nothing |

### Agent management

Part of the [Agent management kit](kits/agent-management).

| Skill | Use it when | Needs |
|---|---|---|
| [`agent-charter-writer`](skills/agent-charter-writer) | Write a job description for an AI agent: scope, tools, autonomy, owner | nothing |
| [`agent-permissions-review`](skills/agent-permissions-review) | Review an agent's tool and data access for least privilege | nothing |
| [`agent-approval-gates`](skills/agent-approval-gates) | Decide which agent actions need human approval and how to ask | nothing |
| [`agent-eval-planner`](skills/agent-eval-planner) | Plan test cases and scoring so you can trust and regression-test an agent | nothing |
| [`agent-release-checklist`](skills/agent-release-checklist) | Version, test and roll out agent changes safely with a rollback plan | nothing |
| [`agent-incident-review`](skills/agent-incident-review) | Run a blameless review when an agent does something wrong | nothing |

### Career

Part of the [Career kit](kits/career).

| Skill | Use it when | Needs |
|---|---|---|
| [`job-posting-scorer`](skills/job-posting-scorer) | Rank job postings with transparent, rules-based scoring | nothing |
| [`cv-tailoring-from-master`](skills/cv-tailoring-from-master) | Tailor a master CV to a job posting without inventing anything | nothing |
| [`cover-letter-writer`](skills/cover-letter-writer) | Write a short, specific, natural cover letter | nothing |
| [`achievement-story-builder`](skills/achievement-story-builder) | Turn work achievements into interview-ready STAR stories | nothing |
| [`confidentiality-safe-wording`](skills/confidentiality-safe-wording) | Describe confidential work publicly without revealing names or secrets | nothing |

## Kits

Every skill belongs to one kit. Each kit page has a suggested order and one-step install:

- [Smart home kit](kits/smart-home): Skills for Home Assistant owners: device health, lighting and automation troubleshooting, automation design, energy and climate insight, security checks, maintenance, vacuum, notifications and naming.
- [Memory kit](kits/memory): Skills for working with a personal knowledge and conversation memory: search, recall, browse and keep facts accurate.
- [Self-hosted AI and homelab kit](kits/self-hosted-ai): Skills for running AI and services at home: planning deployments, designing workflows, triaging incidents, controlling memory and database pitfalls, and checking on a PC over SSH.
- [Content creation kit](kits/content-creation): Skills for gaming and creator channels: planning, captions, editing, thumbnails, brand assets, photo posts and challenge series.
- [Project management kit](kits/project-management): Skills that take a project from idea to close: charter, plan, risk log, status reports, minutes, change control and retrospective.
- [People operations kit](kits/people-operations): Skills for managers and HR teams: shift scheduling, capacity planning, onboarding, structured interviews, CV screening and leave processes.
- [Support operations kit](kits/support-knowledge): Skills for running a support team: SLAs and escalation, KPIs, quality audits, coaching and access management.
- [Operations and productivity kit](kits/operations-productivity): Skills for making work repeatable and measurable: SOPs, automation opportunities and data-backed insight writing.
- [Agent management kit](kits/agent-management): Skills for running AI agents responsibly: charter, permissions, evaluation, approval gates, release and incident review.
- [Career kit](kits/career): Skills for job applications built from one honest master CV: tailoring, cover letters, interview stories and confidentiality-safe wording.

## Tool requirements

The tool-based skills need an MCP server that exposes the tools below. The two servers I wrote are included in [`tools/`](tools); the memory skills use the open-source Basic Memory server.

| Skills | Server | Tools used |
|---|---|---|
| `control-devices`, `manage-automations`, `query-status` and the rest of the [smart home kit](kits/smart-home) | [`tools/home-assistant-mcp`](tools/home-assistant-mcp) | `get_state`, `get_all_states`, `get_history`, `call_service`, `get_services`, `list_automations`, `trigger_automation`, `enable_automation`, `disable_automation`, `send_notification` |
| `memory-search`, `memory-recall`, `memory-browse`, `memory-facts` | [Basic Memory](https://github.com/basicmachines-co/basic-memory) (`uvx basic-memory mcp`) | `search_notes`, `read_note`, `list_directory`, `recent_activity`, `build_context`, `list_memory_projects`, `edit_note`, `write_note` |
| `ssh-remote-pc` | [`tools/ssh-remote-pc-mcp`](tools/ssh-remote-pc-mcp) | `run_command`, `system_status`, `list_processes`, `list_services`, `manage_service` |

Each included server has its own README with setup steps. Credentials go in environment variables, never in files in this repo.

The local AI, job scoring, database safety, RAM guard, content pipeline and user-story skills need no tools. The creator skills work best when your agent can view images and video; `photo-post-deliverables` also needs Python 3 and Pillow (`pip install pillow`).

## Requirements

- **Skills:** none. They are Markdown files.
- **Home Assistant and SSH servers:** Python 3.10 or newer, then `pip install -r requirements.txt` in the server's folder (`mcp`, plus `paramiko` for SSH).
- **Memory skills:** the open-source Basic Memory server (for example `uvx basic-memory mcp`, which needs [uv](https://docs.astral.sh/uv/)).
- **`photo-post-deliverables`:** Python 3 and Pillow (`pip install -r skills/photo-post-deliverables/scripts/requirements.txt`).
- **Contributors:** Python 3 to run `scripts/validate.py` and `scripts/check_tools.py`.

## Install one skill

**Claude Code** (project or personal). macOS / Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/self-hosted-incident-triage ~/.claude/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\self-hosted-incident-triage "$env:USERPROFILE\.claude\skills\"
```

**Other agents (Codex, Cursor and similar):** copy the skill folder to the skills directory your agent documents. Folder names and locations differ between products, so check its documentation.

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

## Disclaimer

These skills are instructions for an AI agent, and AI output can be wrong or incomplete. Review what an agent proposes before you act on it, especially anything that changes devices, accounts, files or money, or that touches people, contracts or personal data. Nothing here is legal, HR, financial, security or safety advice, and the author is not responsible for how the skills or servers are used. As stated in the [MIT License](LICENSE), the software and documents are provided "as is", without warranty of any kind.

## Confidentiality

Everything here is a general method written with invented examples, and each skill should pass a textbook test: it must be explainable from public standards or common professional practice. No company-specific policy, procedure, template, threshold, pricing or contract structure belongs here, even without the company's name. These skills contain no information from any employer, client, supplier or project, and contributors must not add any. Do not submit names, figures, contract terms, internal documents, source code or procedures that belong to a company you work or have worked for, and do not use real personal data in examples, issues or pull requests. If you believe something here discloses confidential information, please report it through [SECURITY.md](SECURITY.md) so it can be removed quickly.

## Get involved

- **Need a skill?** [Request one](../../issues/new?template=skill_request.yml)
- **A skill gave a bad answer?** [Report it](../../issues/new?template=bad_output.yml)
- **Want to add or improve one?** See [CONTRIBUTING.md](CONTRIBUTING.md)

## Authorship and license

These skills, kits, servers and documentation were created and are maintained by [@monicaslgc](https://github.com/monicaslgc), who holds the copyright. The project is released under the [MIT License](LICENSE): you may use, copy, modify and share it, including commercially, **provided you keep the copyright and license notice** in copies or substantial portions. Please credit the project when you reuse or adapt it; GitHub's **Cite this repository** button gives a ready-made citation from [CITATION.cff](CITATION.cff).

Skills reference third-party games and tools by name only to describe their use. They are not affiliated with or endorsed by those products' owners.

## License

[MIT](LICENSE), copyright monicaslgc.

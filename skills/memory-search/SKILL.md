---
name: memory-search
description: >
  Use this skill when the user says "search my memory", "pesquisa na memória",
  "já falámos sobre X?", "o que sei sobre X?", "encontra conversas sobre X",
  "search memory for X", or wants to look up past conversations or facts stored
  in the AI Memory system. Also use when context from a previous conversation
  might be relevant to the current task.
metadata:
  version: "0.1.0"
---

Search the AI Memory database for conversations and facts relevant to the user's query.

## When to use

- User explicitly asks to search memory or past conversations
- User references something that was discussed before ("como fizemos antes", "como configurámos X")
- Starting a new task where prior context would help (proactively search before answering)

## How to search

1. Call `memory_search` with a clear query string — use whichever language the topic was discussed in
2. If results are vague, refine: filter by `project` (homelab-infra, homelab-ha, homelab-media, homelab-ai, homelab-monitoring, career, work, general) or `source` (claude.ai, chatgpt, gemini, cowork)
3. If a conversation looks relevant, call `memory_get_conversation` with its ID to get the full text
4. Summarise what was found — title, date, key points — do not dump raw text

## Projects reference

| Project | Covers |
|---|---|
| homelab-infra | Proxmox, LXC, Docker, networking, storage, SSH, VPN |
| homelab-ha | Home Assistant, automations, lights, vacuum |
| homelab-media | Jellyfin, Sonarr, Radarr, Samba, NAS |
| homelab-ai | Ollama, LLMs, AI memory, agents |
| homelab-monitoring | Grafana, Prometheus, dashboards |
| career | Job search, CV, applications |
| work | Work-related topics |
| general | Everything else |

## Output format

Present results concisely:
- List matching conversations: title, date, source, 1-2 sentence summary
- List matching facts separately if found
- If nothing found, say so clearly and suggest alternative search terms

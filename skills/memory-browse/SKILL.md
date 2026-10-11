---
name: memory-browse
description: >
  Use this skill when the user wants to browse or list past conversations — "mostra-me
  o histórico", "que conversas tenho guardadas", "lista conversas sobre homelab",
  "show memory history", "what's in my memory?", "conversas do ChatGPT", "o que
  guardei sobre monitoring", or any request to see an overview of stored sessions
  rather than search for something specific.
metadata:
  version: "0.1.0"
---

Browse and list conversations stored in AI Memory, with optional filtering.

## How to browse

1. Call `memory_stats` first to show totals by source and project
2. Call `memory_get_conversations` to list recent conversations
   - Filter by `project` if the user mentions a specific area
   - Filter by `source` if the user wants only Claude/ChatGPT/Gemini conversations
   - Default `limit` is 15; increase to 30-50 if user wants a full history
3. Present as a readable list grouped by project or date

## Filters available

**By source:** claude.ai, chatgpt, gemini, claude.ai-web, cowork  
**By project:** homelab-infra, homelab-ha, homelab-media, homelab-ai, homelab-monitoring, career, work, general

## Output format

Show a concise table or grouped list:
```
HOMELAB-INFRA (12 conversations)
  • Plan a Proxmox storage migration — claude.ai — 9 Jun
  • Proxmox network troubleshooting — chatgpt — 26 Jun
  ...

HOMELAB-AI (8 conversations)
  • Agent to watch Grafana dashboards — claude.ai — 9 Jun
  ...
```

If the user wants to read a specific conversation, use `memory_get_conversation` with its ID and show the full text.

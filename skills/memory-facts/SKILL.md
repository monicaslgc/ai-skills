---
name: memory-facts
description: >
  Use this skill when the user wants to see structured facts or preferences stored
  in AI Memory — "que factos tens sobre mim", "mostra as minhas preferências",
  "what do you know about my homelab", "facts about <container>", "show preferences",
  "what do you know about me", or when another skill needs structured context
  about the user, homelab infrastructure, or ongoing projects.
metadata:
  version: "0.1.0"
---

Retrieve structured facts and preferences from AI Memory.

## When to use

- User asks what is known about them, the homelab, or a specific container/project
- Before giving personalised recommendations (check preferences first)
- When another skill needs structured facts as input

## How to retrieve

1. Call `memory_get_facts` — optionally filter by `subject` (e.g., "me", "<container-name>", "home_assistant", "proxmox")
2. Call `memory_get_facts` with `category` to filter preferences (e.g., "communication", "homelab", "home_assistant")
3. Present facts grouped by subject, preferences grouped by category

## What is stored

**Facts** — atomic statements about the world:
- The user's role, projects, tools they use
- Container IDs and the services they run
- Home Assistant setup, devices, areas
- Ongoing projects and preferences

**Preferences** — how the user likes things done:
- Communication style, language preferences
- Homelab conventions (naming, structure)
- Tool preferences per context

## Output format

Present clearly grouped, skipping empty categories:

```
[me]
  name: <user name>
  location: <country>

[<container> — ai-memory]
  ip: <container-ip>
  services: <service>(:<port>), ...
  db: PostgreSQL at <db-host>

PREFERENCES [homelab]
  language: English
  naming: kebab-case for containers
```

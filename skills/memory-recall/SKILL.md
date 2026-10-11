---
name: memory-recall
description: >
  Use this skill proactively at the start of any session or task where past context
  would help — especially for homelab topics (Proxmox, Home Assistant, Docker, Immich,
  monitoring), or ongoing personal projects. Trigger phrases: "o que sabemos sobre",
  "qual é o contexto de", "recorda-me", "recall context", "what do we know about",
  "before we start, check memory". Also use when the user says something like
  "continua de onde parámos" or references a past project.
metadata:
  version: "0.1.0"
---

Load relevant context from AI Memory before starting a task or answering a question.

## When to recall

- Starting work on a known project (Proxmox, HA, monitoring stack...)
- User references something done before without full context
- Beginning a new session on an ongoing topic

## Recall workflow

1. Identify the topic or project from the user's message
2. Call `memory_search` with the topic — use specific terms (e.g., "immich setup", "grafana dashboard", "<container-name>")
3. Call `memory_get_facts` to retrieve structured facts about the subject if relevant
4. Synthesise what is known — do NOT dump raw conversation text
5. State what context was found and how it will inform your response
6. Proceed with the task using this context

## What to report

Tell the user briefly what was found in memory before diving into the task:
> "From memory: we set up Immich in April with the photos folder mounted. Continuing from there."

If nothing relevant is found, say so and proceed normally.

## Do not

- Do not read out full conversation transcripts
- Do not ask the user to confirm facts found in memory (just use them)
- Do not call memory tools if the user explicitly says to ignore memory

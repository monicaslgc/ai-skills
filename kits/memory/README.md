# Memory kit

Skills for working with a personal knowledge and conversation memory: search, recall, browse and keep facts accurate.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`memory-search`](../../skills/memory-search) | Look up something from past conversations |
| [`memory-recall`](../../skills/memory-recall) | Start a session with relevant past context loaded |
| [`memory-browse`](../../skills/memory-browse) | See an overview of what's stored |
| [`memory-facts`](../../skills/memory-facts) | Show structured facts and preferences |

## Suggested order

1. Start sessions with `memory-recall` so the assistant knows the background.
2. Find a specific note or decision with `memory-search`.
3. Get an overview with `memory-browse`.
4. Check and correct what is stored with `memory-facts`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/memory-search ~/.claude/skills/
cp -r ai-skills/skills/memory-recall ~/.claude/skills/
cp -r ai-skills/skills/memory-browse ~/.claude/skills/
cp -r ai-skills/skills/memory-facts ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\memory-search "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\memory-recall "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\memory-browse "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\memory-facts "$env:USERPROFILE\.claude\skills\"
```

These skills need the open-source [Basic Memory](https://github.com/basicmachines-co/basic-memory) MCP server (for example `uvx basic-memory mcp`). Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

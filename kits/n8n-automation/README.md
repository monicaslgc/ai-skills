# n8n automation kit

Two portable, tool-agnostic `SKILL.md` instructions for designing, building and debugging n8n automations. They work with any assistant that supports skills-compatible instruction files; access to live docs, JSON parsing or an n8n instance is optional and must not be assumed.

## Skills

| Skill | Use it to |
|---|---|
| [`n8n-automation-architect`](../../skills/n8n-automation-architect) | Turn a plain-language goal into requirements, a node-by-node blueprint, data contract, risk controls and acceptance criteria. |
| [`n8n-workflow-builder-debugger`](../../skills/n8n-workflow-builder-debugger) | Draft candidate workflow JSON, inspect mappings and expressions, plan tests, and diagnose failures from evidence. |

## Suggested order

1. Start with **n8n Automation Architect** to agree on the outcome, business rules, data contract, failure paths and acceptance criteria.
2. Use **n8n Workflow Builder & Debugger** to verify node details, draft candidate JSON and build a test plan.
3. Import into a non-production n8n environment, run the tests, review credentials and permissions, and only then consider activation.

## Install one skill

Clone the repository and copy either folder into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/n8n-automation-architect ~/.claude/skills/
# or
cp -r ai-skills/skills/n8n-workflow-builder-debugger ~/.claude/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\n8n-automation-architect "$env:USERPROFILE\.claude\skills\"
# or
Copy-Item -Recurse ai-skills\skills\n8n-workflow-builder-debugger "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. You can also open a `SKILL.md` and paste its instructions into a compatible chat assistant.

## Safety and validation

Use synthetic data while designing and testing. Never commit credentials, tokens, real customer data, or unredacted production execution logs. A JSON draft is not proof of n8n import compatibility. Record whether an artefact was drafted, parsed, structurally reviewed, imported, executed, or observed in production.

See the repository's `examples/` and `tests/` folders for a synthetic lead-intake blueprint and evaluation scenarios.
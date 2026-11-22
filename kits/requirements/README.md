# Requirements kit

Skills for working between the business and engineering: find out what is really needed, turn requests into something that can be built, check the requirements and explain technical matters in plain language.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`requirements-elicitation-plan`](../../skills/requirements-elicitation-plan) | Plan how to discover requirements: stakeholders, techniques, questions and validation |
| [`stakeholder-request-translator`](../../skills/stakeholder-request-translator) | Turn a non-technical request into a clear technical request, and read it back |
| [`requirements-quality-check`](../../skills/requirements-quality-check) | Check requirements for clarity, testability, gaps and priority |
| [`plain-language-technical-explainer`](../../skills/plain-language-technical-explainer) | Explain a technical matter to non-technical stakeholders so they can decide |
| [`industry-domain-primer`](../../skills/industry-domain-primer) | Build a sourced primer for a sector or domain you do not know yet |

## Suggested order

1. Plan the discovery with `requirements-elicitation-plan`.
2. Turn each request into a technical one with `stakeholder-request-translator`.
3. Check the set with `requirements-quality-check`.
4. Explain trade-offs and status back to the business with `plain-language-technical-explainer`.

When the domain itself is new to you, start with `industry-domain-primer`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
for s in requirements-elicitation-plan stakeholder-request-translator requirements-quality-check plain-language-technical-explainer industry-domain-primer; do cp -r ai-skills/skills/$s ~/.claude/skills/; done
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
foreach ($s in 'requirements-elicitation-plan','stakeholder-request-translator','requirements-quality-check','plain-language-technical-explainer','industry-domain-primer') {
  Copy-Item -Recurse "ai-skills\skills\$s" "$env:USERPROFILE\.claude\skills\"
}
```

These skills need no tools or servers. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

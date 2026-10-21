# Product discovery and delivery kit

Skills for turning customer evidence into product decisions, requirements and release readiness.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`product-discovery-interviewer`](../../skills/product-discovery-interviewer) | Conduct evidence-led discovery |
| [`customer-feedback-synthesizer`](../../skills/customer-feedback-synthesizer) | Group feedback into traceable themes |
| [`prioritization-scorecard`](../../skills/prioritization-scorecard) | Compare opportunities transparently |
| [`prd-and-spec-writer`](../../skills/prd-and-spec-writer) | Draft testable requirements |
| [`release-readiness-reviewer`](../../skills/release-readiness-reviewer) | Check launch readiness and rollback |

## Suggested order

1. Start with `product-discovery-interviewer`; conduct evidence-led discovery.
2. Start with `customer-feedback-synthesizer`; group feedback into traceable themes.
3. Start with `prioritization-scorecard`; compare opportunities transparently.
4. Start with `prd-and-spec-writer`; draft testable requirements.
5. Start with `release-readiness-reviewer`.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/product-discovery-interviewer ~/.claude/skills/
cp -r ai-skills/skills/customer-feedback-synthesizer ~/.claude/skills/
cp -r ai-skills/skills/prioritization-scorecard ~/.claude/skills/
cp -r ai-skills/skills/prd-and-spec-writer ~/.claude/skills/
cp -r ai-skills/skills/release-readiness-reviewer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\product-discovery-interviewer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\customer-feedback-synthesizer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\prioritization-scorecard "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\prd-and-spec-writer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\release-readiness-reviewer "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.

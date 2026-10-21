# E-commerce operations kit

Skills for auditing catalogue and order data with traceability, quarantine and human review.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`product-catalogue-auditor`](../../skills/product-catalogue-auditor) | Audit product records |
| [`sku-variant-mapping-reviewer`](../../skills/sku-variant-mapping-reviewer) | Review SKU and variant mappings |
| [`order-lifecycle-auditor`](../../skills/order-lifecycle-auditor) | Find inconsistent order states |
| [`product-content-brief-writer`](../../skills/product-content-brief-writer) | Draft source-grounded product briefs |
| [`catalogue-change-reviewer`](../../skills/catalogue-change-reviewer) | Review imports and bulk edits before publication |

## Suggested order

1. Start with `product-catalogue-auditor` to identify missing or contradictory product facts.
2. Use `sku-variant-mapping-reviewer` to check identifiers and variant relationships.
3. Apply `order-lifecycle-auditor` to trace state transitions when order data is in scope.
4. Use `product-content-brief-writer` to draft content grounded in approved product facts.
5. Finish with `catalogue-change-reviewer` before bulk import or publication.

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/product-catalogue-auditor ~/.claude/skills/
cp -r ai-skills/skills/sku-variant-mapping-reviewer ~/.claude/skills/
cp -r ai-skills/skills/order-lifecycle-auditor ~/.claude/skills/
cp -r ai-skills/skills/product-content-brief-writer ~/.claude/skills/
cp -r ai-skills/skills/catalogue-change-reviewer ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\product-catalogue-auditor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\sku-variant-mapping-reviewer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\order-lifecycle-auditor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\product-content-brief-writer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\catalogue-change-reviewer "$env:USERPROFILE\.claude\skills\"
```

Other assistants use different locations; follow their skills-directory documentation. Each skill folder contains a `SKILL.md` and `USER_STORY.md`.

All examples use fictional or approved data. Do not paste credentials, personal data or confidential production records into a chat you do not control. The kit also includes an [example](examples.md), [reference checklist](references.md) and [evaluation pack](evaluation.md). The evaluation pack is a proposed test plan, not a claimed benchmark result.

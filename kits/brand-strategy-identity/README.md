# Brand Strategy & Identity kit

A modular workflow for taking a brand from discovery to strategy, naming, identity direction, launch and governance. Skills are individually usable; the workflow orchestrator is optional.

## Principles

- Strategy before naming and visual identity.
- Research before claims; distinguish evidence, interpretation and hypotheses.
- Use direct competitors, substitutes and adjacent categories for different research purposes.
- Keep naming generation separate from naming validation.
- Human approval is required for strategic decisions, final names, identity approval, legal clearance and publication.
- Do not create a separate autonomous agent for every skill. Route tasks to the smallest useful set.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`audience-research`](../../skills/audience-research) | Synthesize audience evidence and identify research gaps |
| [`brand-application-designer`](../../skills/brand-application-designer) | Specify identity use across touchpoints |
| [`brand-architecture`](../../skills/brand-architecture) | Choose a coherent brand portfolio structure |
| [`brand-asset-governance`](../../skills/brand-asset-governance) | Govern reusable brand files and versions |
| [`brand-audit`](../../skills/brand-audit) | Audit an existing brand across strategy and touchpoints |
| [`brand-claim-validator`](../../skills/brand-claim-validator) | Check claims against substantiating evidence |
| [`brand-consistency-auditor`](../../skills/brand-consistency-auditor) | Audit touchpoints against approved brand rules |
| [`brand-content-planner`](../../skills/brand-content-planner) | Plan content aligned with brand positioning |
| [`brand-discovery`](../../skills/brand-discovery) | Collect the context needed for brand decisions |
| [`brand-guidelines-generator`](../../skills/brand-guidelines-generator) | Compile approved brand rules into guidelines |
| [`brand-identity-prism`](../../skills/brand-identity-prism) | Assess identity through six connected facets |
| [`brand-launch-planner`](../../skills/brand-launch-planner) | Plan internal and external brand rollout |
| [`brand-localization-advisor`](../../skills/brand-localization-advisor) | Adapt brand expression across languages and markets |
| [`brand-messaging-framework`](../../skills/brand-messaging-framework) | Build audience-specific message hierarchies |
| [`brand-name-availability`](../../skills/brand-name-availability) | Run an early .pt/.com, company-register and trademark viability gate before concept development |
| [`brand-naming-validation`](../../skills/brand-naming-validation) | Screen shortlisted names for linguistic, cultural and confusion risks before legal review |
| [`brand-performance-analyst`](../../skills/brand-performance-analyst) | Evaluate brand measures and interpret evidence |
| [`brand-personality-archetypes`](../../skills/brand-personality-archetypes) | Translate traits into practical brand behaviour |
| [`brand-positioning`](../../skills/brand-positioning) | Develop and compare positioning options |
| [`brand-quality-evaluator`](../../skills/brand-quality-evaluator) | Evaluate deliverables against explicit criteria |
| [`brand-stakeholder-interviews`](../../skills/brand-stakeholder-interviews) | Plan and synthesize stakeholder interviews |
| [`brand-strategy`](../../skills/brand-strategy) | Turn discovery evidence into a coherent strategy |
| [`brand-tool-calling`](../../skills/brand-tool-calling) | Select and call tools safely |
| [`brand-voice-copywriter`](../../skills/brand-voice-copywriter) | Create verbal identity and on-brand copy |
| [`brand-workflow-orchestrator`](../../skills/brand-workflow-orchestrator) | Route work through the brand workflow and approval gates |
| [`brand-workshop-facilitator`](../../skills/brand-workshop-facilitator) | Facilitate workshops and capture decisions |
| [`campaign-concept-developer`](../../skills/campaign-concept-developer) | Develop brand-consistent campaign territories |
| [`competitive-brand-research`](../../skills/competitive-brand-research) | Research competitors and adjacent categories |
| [`logo-design-brief`](../../skills/logo-design-brief) | Brief designers on strategic identity requirements |
| [`market-category-analysis`](../../skills/market-category-analysis) | Map category conventions and opportunities |
| [`moodboard-art-direction`](../../skills/moodboard-art-direction) | Translate strategy into visual territories |
| [`naming-studio`](../../skills/naming-studio) | Generate strategically grounded name candidates |
| [`visual-inspiration-research`](../../skills/visual-inspiration-research) | Find visual references from strategic search terms |

## Naming method reference

Naming skills share the [Naming Method Playbook](NAMING_METHOD_PLAYBOOK.md), an original practical synthesis informed by Rob Meyerson's *Brand Naming*, Jeremy Miller's *Brand New Name*, Brad Flowers' *The Naming Book* and Alina Wheeler's *Designing Brand Identity*. It covers strategy-first briefing, divergent name-generation routes, pronounceability and recall tests, scorecards, validation gates and contextual presentations. The playbook summarizes principles in original wording; it does not reproduce copyrighted book text or worksheets.

## Suggested order

1. **Discover:** workshop, stakeholder interviews, audience research and current-brand audit.
2. **Understand the market:** category and competitor research with dated sources.
3. **Set strategy:** positioning, personality, identity prism and brand architecture.
4. **Name:** generate a raw batch; run `brand-name-availability` immediately to eliminate candidates that fail mandatory domain/company/trademark gates; develop concepts only for candidates that pass; then use `brand-naming-validation` for deeper linguistic, cultural and confusion-risk screening.
5. **Direct the identity:** visual research, moodboards and design brief.
6. **Express the brand:** messaging, voice, touchpoint applications and guidelines.
7. **Activate:** campaigns, content, launch and localization.
8. **Govern:** asset governance, consistency audits and performance review.

The order is a default, not a rigid waterfall. Revisit earlier decisions when new evidence changes the brief.

## Orchestration and handoffs

Use `brand-workflow-orchestrator` to identify the current stage and route only to the relevant skills. Every stage should return status, summary, evidence, assumptions, decisions, open questions, risks, next skill and approval requirement. A complete-looking document is not approval.

See [workflow](../../workflows/brand-strategy-identity/workflow.md) and [approval gates](../../workflows/brand-strategy-identity/approval-gates.md).

## Tool calling

The tool registry describes proposed provider-neutral tools; it does not mean integrations are installed. Read [TOOL_REGISTRY](../../tools/brand-strategy-identity/TOOL_REGISTRY.md) and [security policy](../../tools/brand-strategy-identity/SECURITY.md). Tool schemas are in the adjacent `schemas/` directory. Implement only the tools needed, with least-privilege access and explicit side-effect handling.

## Evaluation

See the [evaluation pack](../../evaluations/brand-strategy-identity/README.md). These are proposed regression fixtures, not benchmark results. Record model/version, skill commit, tools and reviewer when tests are run.

## Example

See [fictional Northstar Studio project](EXAMPLE_PROJECT.md).

## Install the whole kit

Clone the repository and copy the skill folders into the skills directory supported by your assistant. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/audience-research ~/.claude/skills/
cp -r ai-skills/skills/brand-application-designer ~/.claude/skills/
cp -r ai-skills/skills/brand-architecture ~/.claude/skills/
cp -r ai-skills/skills/brand-asset-governance ~/.claude/skills/
cp -r ai-skills/skills/brand-audit ~/.claude/skills/
cp -r ai-skills/skills/brand-claim-validator ~/.claude/skills/
cp -r ai-skills/skills/brand-consistency-auditor ~/.claude/skills/
cp -r ai-skills/skills/brand-content-planner ~/.claude/skills/
cp -r ai-skills/skills/brand-discovery ~/.claude/skills/
cp -r ai-skills/skills/brand-guidelines-generator ~/.claude/skills/
cp -r ai-skills/skills/brand-identity-prism ~/.claude/skills/
cp -r ai-skills/skills/brand-launch-planner ~/.claude/skills/
cp -r ai-skills/skills/brand-localization-advisor ~/.claude/skills/
cp -r ai-skills/skills/brand-messaging-framework ~/.claude/skills/
cp -r ai-skills/skills/brand-name-availability ~/.claude/skills/
cp -r ai-skills/skills/brand-naming-validation ~/.claude/skills/
cp -r ai-skills/skills/brand-performance-analyst ~/.claude/skills/
cp -r ai-skills/skills/brand-personality-archetypes ~/.claude/skills/
cp -r ai-skills/skills/brand-positioning ~/.claude/skills/
cp -r ai-skills/skills/brand-quality-evaluator ~/.claude/skills/
cp -r ai-skills/skills/brand-stakeholder-interviews ~/.claude/skills/
cp -r ai-skills/skills/brand-strategy ~/.claude/skills/
cp -r ai-skills/skills/brand-tool-calling ~/.claude/skills/
cp -r ai-skills/skills/brand-voice-copywriter ~/.claude/skills/
cp -r ai-skills/skills/brand-workflow-orchestrator ~/.claude/skills/
cp -r ai-skills/skills/brand-workshop-facilitator ~/.claude/skills/
cp -r ai-skills/skills/campaign-concept-developer ~/.claude/skills/
cp -r ai-skills/skills/competitive-brand-research ~/.claude/skills/
cp -r ai-skills/skills/logo-design-brief ~/.claude/skills/
cp -r ai-skills/skills/market-category-analysis ~/.claude/skills/
cp -r ai-skills/skills/moodboard-art-direction ~/.claude/skills/
cp -r ai-skills/skills/naming-studio ~/.claude/skills/
cp -r ai-skills/skills/visual-inspiration-research ~/.claude/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/monicaslgc/ai-skills.git
Copy-Item -Recurse ai-skills\skills\audience-research "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-application-designer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-architecture "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-asset-governance "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-audit "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-claim-validator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-consistency-auditor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-content-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-discovery "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-guidelines-generator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-identity-prism "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-launch-planner "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-localization-advisor "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-messaging-framework "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-naming-validation "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-performance-analyst "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-personality-archetypes "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-positioning "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-quality-evaluator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-stakeholder-interviews "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-strategy "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-tool-calling "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-voice-copywriter "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-workflow-orchestrator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\brand-workshop-facilitator "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\campaign-concept-developer "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\competitive-brand-research "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\logo-design-brief "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\market-category-analysis "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\moodboard-art-direction "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills
aming-studio "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ai-skills\skills\visual-inspiration-research "$env:USERPROFILE\.claude\skills\"
```

Each skill includes a `SKILL.md` and `USER_STORY.md`. Other assistants may use a different skills directory; follow their documentation.

## Limitations

Trademark, domain and social-handle checks are preliminary screening, not legal clearance or proof of availability. Research depends on accessible, dated sources. Generated visual explorations do not replace a professional identity system or licensed asset production. Human review remains mandatory for strategy, legal-sensitive claims and public release.
## Shared project context and quality control

Use [BRAND_CONTEXT.md](BRAND_CONTEXT.md) as the working source of truth across skills. Record material choices in [DECISION_LOG.md](DECISION_LOG.md), using explicit Draft, In Review, Approved, Locked and Superseded states. Apply [QUALITY_GATES.md](QUALITY_GATES.md) before every downstream handoff. Agents can prepare recommendations but cannot approve decisions on behalf of a human owner.

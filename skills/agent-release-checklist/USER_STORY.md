# User story: agent-release-checklist

## Story

**As** an owner updating an AI agent that people rely on,
**I want** a release checklist with testing, staged rollout and rollback,
**so that** improvements ship without breaking what already works.

## Scenario

I changed the instructions and added a new tool and want to roll it out to my team.

## Acceptance criteria

- [ ] All changes are listed under a new version.
- [ ] Evaluation results are compared with the previous version.
- [ ] Permissions and approval gates are re-checked for new tools.
- [ ] Rollout has stages and stop criteria.
- [ ] A rollback plan exists and is tested.

## Try it

> Prepare a release checklist for version 1.2 of my triage agent, which adds a new calendar tool.

See [SKILL.md](SKILL.md) for the full instructions.

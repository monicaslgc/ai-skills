# User story: agent-eval-planner

## Story

**As** someone releasing or changing an AI agent,
**I want** a test plan with typical, edge and adversarial cases,
**so that** I can tell whether a change made the agent better or worse.

## Scenario

I edited the prompt of a triage agent and want to be sure it still refuses out-of-scope requests.

## Acceptance criteria

- [ ] Cases cover typical, edge and adversarial inputs.
- [ ] Each case states expected behaviour and failure.
- [ ] A scoring rubric and pass thresholds exist.
- [ ] Real failures are added to a regression suite.
- [ ] Results report case counts and known gaps.

## Try it

> Plan an evaluation for an agent that triages support emails and drafts replies.

See [SKILL.md](SKILL.md) for the full instructions.

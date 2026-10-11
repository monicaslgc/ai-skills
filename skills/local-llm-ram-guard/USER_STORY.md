# User story: local-llm-ram-guard

## Story

**As** someone hosting a local model on a shared server,
**I want** to find out why memory is running out and cap it safely,
**so that** my other services stay up while the model runs.

## Scenario

The server sits at 95% RAM with swap full and a model server running.

## Acceptance criteria

- [ ] Diagnosis is read-only and uses real numbers.
- [ ] The likely cause is identified (loaded models, keep-alive, parallelism, context size, other caches).
- [ ] Changes are ranked from smallest to largest, with the expected effect of each.
- [ ] An early-warning alert and a short runbook are proposed.
- [ ] Nothing is restarted or changed without my approval.

## Try it

> My host is at 95% RAM and a local model server is running. What should I check?

See [SKILL.md](SKILL.md) for the full instructions.

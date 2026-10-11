# User story: slow-llm-db-safety

## Story

**As** a developer calling a slow local model from code that also uses a database,
**I want** to stop connections dying mid-call and writes being lost,
**so that** my data is saved reliably even when the model takes minutes.

## Scenario

My script runs fine in tests but in production it fails with a closed-cursor error after the model call.

## Acceptance criteria

- [ ] Places that hold a connection across a slow call are found.
- [ ] The code is restructured to read, close, call, then reopen and write.
- [ ] Silent exception handlers around writes are removed or narrowed.
- [ ] A repeatable check with a short timeout proves the fix.
- [ ] Server timeouts are not raised as a workaround.

## Try it

> My script gets 'cursor already closed' after calling the model. Find out why and fix it.

See [SKILL.md](SKILL.md) for the full instructions.

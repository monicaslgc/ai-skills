---
name: slow-llm-db-safety
description: Prevent database failures when code calls a slow language model while holding a database connection or transaction open. Use when debugging "cursor already closed", "connection already closed", "terminating connection due to idle-in-transaction timeout" or silent missing writes after an LLM call, or when reviewing code that mixes database access with slow model calls. Typical on CPU-only local models where one call can take minutes.
---

# Slow LLM + Database Safety

A local or CPU-only model can take minutes to answer. If a database connection is held open across that call, a server-side timeout (for example PostgreSQL `idle_in_transaction_session_timeout`, a proxy idle timeout, or a connection-pool recycle) can kill it. The next write then fails with an error such as `cursor already closed` or `server closed the connection unexpectedly`. Inside a broad `except: pass`, it fails silently and data is simply never saved.

## The rule

**Close the connection and cursor before the slow call. Open a new connection afterwards for any write.**

```python
rows = read_inputs()            # open, read, commit, close
result = call_model(rows)       # slow, no connection held
write_result(result)            # open a fresh connection, write, commit, close
```

## Workflow

1. Find every place where a model or HTTP call happens between opening and closing a connection, cursor or transaction.
2. Check the server and pool settings: idle-in-transaction timeout, statement timeout, pool max lifetime, proxy idle timeout. Compare them with the slowest realistic model call, not the average.
3. Restructure each place as read, close, call, then open fresh and write. Prefer one small helper that runs a function with a short-lived connection, so every file uses the same pattern.
4. Remove or narrow any `except Exception: pass` around writes. Log the failure with enough context to find the record.
5. Make writes idempotent (upsert or a unique key) so a retry after a failure does not create duplicates.
6. Add a test or a manual check: set the idle timeout to a few seconds, make the model call sleep longer, and confirm the write still succeeds.

## Output format

Report: the places that held a connection across a slow call (file and function), the timeout values found, the change made at each place, and how it was verified.

## Safety

- Do not raise server timeouts as the fix. That hides the bug and keeps long transactions open, which blocks vacuuming and holds locks.
- Do not change production database settings without explicit approval and a rollback plan.
- Never paste connection strings, passwords or customer rows into the conversation. Use placeholders.

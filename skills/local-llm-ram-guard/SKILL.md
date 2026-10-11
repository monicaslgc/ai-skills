---
name: local-llm-ram-guard
description: Diagnose and prevent host memory exhaustion caused by locally hosted language models, especially CPU-only servers that also run other services. Use when a host shows high RAM or swap use, services get killed by the out-of-memory killer, a model server (such as Ollama) seems to use more memory than expected, or when planning memory limits for a self-hosted AI stack. Trigger phrases - "RAM at 95%", "swap is full", "OOM killed", "model keeps loading", "limit memory for local LLM".
---

# Local LLM RAM Guard

Model servers keep weights, and per-request context memory, in RAM. On a shared host the model, other containers and filesystem caches compete for the same memory. The goal is a predictable memory ceiling, not just a restart.

## Workflow

1. **Measure first (read-only).** Collect total and available RAM, swap use, the largest processes, container memory limits and usage, and the list of models currently loaded in the model server. Note the time of the spike and what ran just before it.
2. **Find the multiplier.** Common causes:
   - Several models loaded at once.
   - Models kept in memory long after the last request.
   - Parallel requests, each with its own context memory.
   - A very large context window set by a client or a default.
   - Another cache (for example a filesystem cache with a high cap) competing for the same RAM.
3. **Propose limits, smallest change first:**
   - Limit loaded models to what fits (for Ollama, `OLLAMA_MAX_LOADED_MODELS`).
   - Shorten keep-alive so idle models unload (`OLLAMA_KEEP_ALIVE`).
   - Limit parallel requests (`OLLAMA_NUM_PARALLEL`) and the context window.
   - Choose a smaller or more heavily quantised model.
   - Set a memory limit on the container so a runaway process cannot take down the host.
4. **Add early warning.** Alert on available memory and on swap-in rate, not only on used memory, and send the alert somewhere a person will see it.
5. **Write a short runbook:** how to check, how to unload a model, what is safe to restart first, and who to tell.
6. **Verify** by repeating the original workload and comparing peak memory with the baseline.

## Output format

Findings (with numbers), the most likely cause, a ranked list of changes with the expected effect of each, the verification plan, and anything that needs downtime.

## Safety

- Diagnosis is read-only. Ask before restarting services, unloading models, changing limits or editing configuration.
- Take a snapshot or backup before changing host-level settings.
- Do not kill processes by name or pattern without confirming what they are.
- Do not disable swap or the out-of-memory killer as a "fix".

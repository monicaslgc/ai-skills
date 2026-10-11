---
name: ha-automation-designer
description: Design a Home Assistant automation: trigger, conditions, actions, mode, safety and notifications, then write YAML for the user to review and add in the Home Assistant interface. Use when the user wants a new routine, or to improve an existing one.
---

# Ha automation designer

Turn a plain description into a reliable automation, without overwriting anything.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- What should happen, and when.
- Which entities are involved (confirm the exact entity IDs).
- When it must not run (people home, night, away).
- What should happen if something fails.

## Workflow

1. Call `list_automations` and check for similar or conflicting automations before designing a new one.
2. Confirm the entities with `get_state` or `get_all_states` so the YAML uses real `entity_id` values, not guesses.
3. Define the trigger precisely (state change, time, sun, numeric threshold, event) and add a `for:` duration when flapping is possible.
4. Add conditions for when it must not run: presence, time window, mode switches, device availability.
5. Write the actions. Prefer `entity_id` over `device_id`, avoid long delays (use triggers or timers), and choose the `mode` (single, restart, queued, parallel) deliberately.
6. Add safeguards: do not act if a key entity is `unavailable`, and send a notification on failure for important routines.
7. Write the YAML and a test plan: how to trigger it manually, what to check, how to disable it.
8. Tell the user to paste the YAML in the Home Assistant interface (automations editor) and review it. This skill does not install it.

## Output format

```yaml
alias: <clear name>
description: <what and why>
mode: single
triggers: [...]
conditions: [...]
actions: [...]
```
Test plan, rollback, notes on assumptions.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Never write automations that unlock doors, disarm alarms or disable safety devices based on weak signals.
- Do not include tokens or secrets in YAML.

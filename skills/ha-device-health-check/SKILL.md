---
name: ha-device-health-check
description: Check the health of a Home Assistant installation: unavailable or unknown entities, low batteries, devices that stopped reporting, and likely causes. Use when something stopped working, for a regular home health check, or after a network or power event.
---

# Ha device health check

Find what is broken or about to break, and say what to try first.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Anything the user already noticed.
- Recent changes: router, power cut, updates.

## Workflow

1. Call `get_all_states` and list entities whose state is `unavailable` or `unknown`. Group them by domain and by name prefix to spot a common cause (one integration, one hub, one room).
2. Find battery sensors: entities from `get_all_states(domain="sensor")` whose name suggests a battery. Use `get_state` on candidates to read the value and unit. Flag values below 20%.
3. For suspicious entities, call `get_state` and compare `last_changed` and `last_updated` with the present time to find sensors that stopped reporting.
4. Use `get_history` on a few entities to see when they went unavailable.
5. Rank the findings: safety-related devices first (locks, smoke, leak and door sensors), then heating, then lights and others.
6. Suggest the next step for each group: check power or battery, check the network or hub, reload or re-authenticate the integration, re-pair a device.
7. Offer to re-check after the user has tried a fix.

## Output format

| Group / cause | Entities | Since | Priority | First thing to try |
|---|---|---|---|---|

Batteries below 20%, stale sensors, summary.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- This skill is read-only. It does not restart, reload or change anything.

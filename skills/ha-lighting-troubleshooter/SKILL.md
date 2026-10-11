---
name: ha-lighting-troubleshooter
description: Diagnose smart lights that do not respond, flicker, turn on by themselves or reset: check state and history, conflicting automations, groups and connectivity, and recommend fixes. Use when a light or group of lights misbehaves.
---

# Ha lighting troubleshooter

Work from evidence: what the light reports, what changed, and what else controls it.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Which lights, rooms and what they do wrong.
- When it started and what changed.
- How the lights connect (Zigbee, Wi-Fi, cloud, bridge).

## Workflow

1. Call `get_state` for each affected light. Note the state, brightness, colour attributes, and whether it is `unavailable`.
2. Call `get_history` for 24 to 72 hours to see flapping, repeated unavailable periods or unexpected changes and their times.
3. Call `list_automations` and look for automations whose name suggests they control these lights, and check their `last_triggered` against the times of unexpected changes.
4. Check groups and scenes: does a group, scene or schedule also control them? Look for conflicts such as two automations setting different states.
5. Test one change at a time after the user confirms: use `call_service` with `light.turn_on` or `light.turn_off` on a single light and see whether the state follows.
6. If several lights share a pattern (same hub, same room, same time), suspect the hub, coordinator, router, power or interference. If one light fails, suspect the bulb, power or pairing.
7. Recommend the smallest fix first: power cycle the device, check the hub or coordinator, re-pair, update firmware, reduce load, remove duplicate automations.

## Output format

```
Observation: entity, state, last change, pattern in history
Likely cause (ranked) and evidence
Conflicting automations or groups
Next test (one change)
Fix steps
```

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Do not disable automations or delete entities without the user's confirmation.

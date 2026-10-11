---
name: ha-automation-debugger
description: Debug a Home Assistant automation that did not run, ran at the wrong time, or ran repeatedly: check its state, last run, triggers, conditions, entity states and history. Use when a routine misbehaves.
---

# Ha automation debugger

Compare what should have happened with what the system recorded, then pinpoint the gap.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- The automation (name or entity ID), what should have happened and when.
- What actually happened.
- Any recent changes.

## Workflow

1. Call `list_automations` and confirm the automation exists, is `on`, and note its `last_triggered`.
2. Call `get_state` on the automation to read its attributes, such as `last_triggered` and `current` runs.
3. Identify the trigger entities from the user's description. Call `get_state` and `get_history` on them around the expected time: did the trigger actually happen, and for how long?
4. Check the conditions against the history at that moment: was someone home, was the time window right, was a required entity `unavailable`?
5. Check the action targets with `get_state`: were they available, and did their state change?
6. Look for conflicts: other automations that act on the same entities near that time (compare `last_triggered`).
7. State the most likely cause with the evidence, and the smallest change to fix it. For a manual test, offer `trigger_automation` and ask for confirmation first.

## Output format

```
Expected vs actual
Trigger: happened? (evidence)
Conditions: passed? (evidence)
Actions: executed? target state?
Conflicts
Likely cause and fix
```

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Triggering an automation runs real actions. Confirm first, and say what it will do.
- Do not enable, disable or edit automations without confirmation.

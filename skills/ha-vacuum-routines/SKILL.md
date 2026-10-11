---
name: ha-vacuum-routines
description: Plan and run robot vacuum routines in Home Assistant: status, battery and errors, start, pause and return to dock, room-based cleaning when supported, and schedules that avoid disturbing people. Use for vacuum control and routine design.
---

# Ha vacuum routines

Keep the floors clean without surprises.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Vacuum entity and rooms.
- When the home is occupied and quiet hours.
- Preferences: frequency, which rooms, suction level.

## Workflow

1. Call `get_all_states(domain="vacuum")` and `get_state` on the chosen vacuum to read its state, battery and any error or status attributes.
2. Call `get_services` for the `vacuum` domain to see what the vacuum supports (start, pause, return_to_base, locate, send_command, and any room or segment cleaning).
3. Report current status plainly. If there is an error, suggest what to check (stuck wheel, full bin, dirty sensors) before retrying.
4. For a command, confirm what it will do and then use `call_service` with the `vacuum` domain, for example `start`, `pause` or `return_to_base`.
5. Design routines: which rooms on which days, avoid quiet hours and times people are home, run after the home empties, and return to dock when the battery is low.
6. Write a proposed automation as YAML for the user to review and add (see `ha-automation-designer`). Include a notification if the vacuum gets stuck.
7. Suggest maintenance reminders for brushes, filters and the bin.

## Output format

```
Status: state, battery, error
Supported actions
Routine proposal: day, rooms, conditions
Automation YAML (for review)
Maintenance reminders
```

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Do not start the vacuum when the user says someone is sleeping or the area may have pets or hazards.
- Send-command and room-cleaning calls vary by brand; check `get_services` before using them.

---
name: ha-night-security-check
description: Run a bedtime or leaving-home check in Home Assistant: locks, doors, windows, garage, alarms and lights, reporting what is open or on, and offering to fix only with confirmation. Use for a nightly routine or before leaving.
---

# Ha night security check

Give a quick, trustworthy answer to 'is the house secure'.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Whether this is bedtime or leaving home.
- Which areas and devices matter.
- What the user is comfortable having switched off automatically.

## Workflow

1. Call `get_all_states` for the `lock`, `cover`, `binary_sensor` and `alarm_control_panel` domains and the `light` domain.
2. Identify door, window and opening sensors from names or `get_state` attributes (device class). Report anything open or unlocked.
3. Report garage and entrance covers, and the alarm state if present.
4. List lights that are on, and appliances the user marked as important (for example a cooker or iron) if monitored.
5. Show a short summary: secure, or a list of items to resolve.
6. Offer actions one by one, such as turning off lights or closing a garage door. Wait for confirmation. Ask for explicit confirmation again before locking a door.
7. Never unlock doors or disarm alarms from this skill. Remind the user to check anything unmonitored.

## Output format

```
Status: Secure | Needs attention
Open / unlocked: ...
Lights on: ...
Alarm: ...
Not monitored: ...
Suggested actions (need your OK)
```

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- State clearly that sensors can be wrong or unavailable; an `unavailable` sensor is not a closed door.
- Do not claim the house is secure if any relevant sensor is unavailable.

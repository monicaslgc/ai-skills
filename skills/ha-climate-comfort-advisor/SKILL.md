---
name: ha-climate-comfort-advisor
description: Review Home Assistant climate devices and temperature sensors: set points, actual temperatures, schedules, how quickly rooms reach target and unnecessary running, then suggest comfort and efficiency improvements. Use when rooms are too hot or cold, or heating and cooling use is high.
---

# Ha climate comfort advisor

Match comfort to how the home is actually used, using the data.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Rooms and devices (thermostats, air conditioners, sensors).
- Comfort preferences and occupancy patterns.
- Complaints: too hot, too cold, noisy, expensive.

## Workflow

1. Call `get_all_states(domain="climate")` and temperature sensors from the `sensor` domain. Use `get_state` to read the mode, set point, current temperature and action.
2. Call `get_history` for 24 to 72 hours to see temperature curves, how long it takes to reach the set point, overshoot, and how often the device cycles.
3. Compare rooms and times: where is comfort missed, and where does the device run without anyone present?
4. Check for conflicts between schedules, automations and manual changes using `list_automations` and the timing of changes.
5. Suggest improvements: set points by occupancy, preheating time, away mode, window-open pause, setback at night, and sensor placement.
6. Test only one change at a time with the user's confirmation, using `call_service` for the `climate` domain (for example `set_temperature` or `set_hvac_mode`).
7. Re-check after a day and report the effect.

## Output format

| Room | Target | Actual range | Time to target | Cycling | Issue | Suggestion |
|---|---|---|---|---|---|---|

Summary, a change plan (one change at a time), re-check plan.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Respect safe temperature limits, especially for infants, elderly people and pets.
- Do not turn off heating in cold weather or cooling in extreme heat without explicit confirmation.

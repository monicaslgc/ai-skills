---
name: ha-home-maintenance-planner
description: Plan recurring home maintenance (filters, batteries, appliances, seasonal checks) with sensible intervals, and set up reminders through Home Assistant notifications or to-do lists. Use when the user wants to stop forgetting household tasks.
---

# Ha home maintenance planner

Turn a vague list of chores into a schedule and gentle reminders.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Appliances and systems in the home.
- Manufacturer guidance the user has.
- How the user wants reminders (notification, to-do list).

## Workflow

1. List the devices and systems: heating or cooling, ventilation, appliances, smoke detectors, water systems, outdoor items.
2. Propose tasks with intervals (monthly, quarterly, seasonal, annual) and note that manufacturer guidance takes priority. Ask the user to confirm items you are unsure about.
3. Where Home Assistant can help, identify triggers: battery levels from sensors, runtime counters, appliance run counts.
4. Group tasks into a calendar that spreads work out instead of bunching it.
5. Check which reminder method is available: call `get_services` for the `todo` and `notify` domains.
6. After the user approves the list, create reminders one at a time: add to a to-do list with `call_service` (domain `todo`, service `add_item`) if available, or send a test with `send_notification`.
7. Produce a printable schedule and a short checklist for each task.

## Output format

| Task | Device | Interval | Next due | Reminder method | Notes |
|---|---|---|---|---|---|

Seasonal checklist, reminder setup summary.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Safety-critical items (gas, electrical, smoke and carbon monoxide detectors) must follow manufacturer and local guidance; do not give instructions for hazardous repairs.
- Create reminders only after the user approves the list.

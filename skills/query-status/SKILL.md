---
name: query-status
description: >
  Use this skill when the user asks about the current state of their home or devices.
  Trigger phrases: "what's the temperature", "are the lights on", "is the door locked",
  "check my sensors", "what's the humidity", "show my energy usage", "is the garage open",
  "what devices are on", "check the thermostat", "how much energy", "sensor readings",
  "what's happening at home", "show me my home status".
---

Query Home Assistant for current device states, sensor readings, and history.

## Workflow

1. Determine what the user wants to know — a specific device, a room, a sensor type, or a whole-home overview.
2. Fetch state data using `get_state` (single entity) or `get_all_states` (domain-level filter).
3. Present the results in plain language — not raw JSON. Format values with units, use friendly names, and group related devices logically.

## Common queries

**Single device status**
- Call `get_state("entity_id")` and read `.state` and relevant `.attributes`.

**All lights / switches / sensors**
- Call `get_all_states(domain="light")`, `get_all_states(domain="sensor")`, etc.

**Temperature and climate**
- Use domain `climate` for thermostats (current temp, set point, mode).
- Use domain `sensor` and filter by `device_class=temperature` in attributes for room sensors.

**Energy and power**
- Look for sensors with `device_class=energy` or `device_class=power`.
- Call `get_history` for trends over time (e.g. last 24 hours).

**Security / doors / locks**
- Domain `lock` for locks, `binary_sensor` for door/window sensors, `cover` for garage doors.
- For security overview, pull all of these domains and highlight any that are open/unlocked.

**Whole-home snapshot**
- Pull `light`, `switch`, `climate`, `lock`, `cover`, and `binary_sensor` domains.
- Summarize: X lights on, thermostat at Y°, all doors locked/unlocked, etc.

## Presenting data

- Use friendly names from `attributes.friendly_name`, not raw entity IDs.
- Include units: temperature in °C or °F (check `attributes.unit_of_measurement`), power in W/kW, etc.
- For history, describe trends conversationally: "Temperature rose from 19°C to 23°C over the past 6 hours."
- Group by area/room when `attributes.area_id` is present.
- Flag anything that seems unusual (a door left open, a device left on overnight, etc.).

## History queries

Use `get_history(entity_id, hours=N)` to check:
- Energy consumption over the past day/week
- Motion sensor activity patterns
- Temperature fluctuations
- How long a device has been in a state

Summarize history as a trend rather than a raw list of state changes.

---
name: control-devices
description: >
  Use this skill when the user wants to control smart home devices in Home Assistant.
  Trigger phrases: "turn on/off", "dim the lights", "set the thermostat", "close the blinds",
  "lock the door", "turn everything off", "set brightness", "change the temperature",
  "switch on", "toggle", "set the fan", "control my lights", "adjust the climate".
metadata:
  version: "0.1.0"
---

Control Home Assistant devices by calling services through the MCP server.

## Workflow

1. If the target entity is ambiguous, call `get_all_states` with the relevant domain (e.g. `light`, `switch`, `climate`) to list available entities and let the user pick.
2. Identify the correct `entity_id` (e.g. `light.living_room`).
3. Determine the right service: most devices use `turn_on`, `turn_off`, or `toggle`. Climate uses `set_temperature` or `set_hvac_mode`. Covers use `open_cover` / `close_cover`.
4. Call `call_service` with the domain, service, entity_id, and any extra parameters.
5. Confirm the action with a short, friendly message. Do not repeat back the raw API response — translate it into plain language.

## Common service patterns

**Lights**
- Turn on: `domain=light`, `service=turn_on`, `entity_id=light.NAME`
- Set brightness: `extra={"brightness_pct": 70}`
- Set color: `extra={"color_name": "warm_white"}` or `extra={"rgb_color": [255, 200, 100]}`
- Set color temperature: `extra={"kelvin": 3000}`

**Switches**
- `domain=switch`, `service=turn_on` / `turn_off` / `toggle`

**Climate / thermostat**
- Set temperature: `domain=climate`, `service=set_temperature`, `extra={"temperature": 22}`
- Set mode: `domain=climate`, `service=set_hvac_mode`, `extra={"hvac_mode": "heat"}` (modes: `heat`, `cool`, `heat_cool`, `auto`, `off`)

**Covers / blinds**
- `domain=cover`, `service=open_cover` / `close_cover` / `set_cover_position`
- Set position: `extra={"position": 50}` (0 = closed, 100 = open)

**Fans**
- `domain=fan`, `service=turn_on` / `turn_off` / `set_percentage`
- Set speed: `extra={"percentage": 60}`

**Scripts**
- `domain=script`, `service=SCRIPT_NAME` (no entity_id needed)

## Handling "turn everything off"

When asked to turn off all lights, all switches, or everything in a room:
1. Call `get_all_states` for the relevant domain.
2. If there are many entities, group them by area if `area` is present in attributes, or just list them.
3. Call `call_service` without specifying `entity_id` to target all entities in the domain, OR iterate and call per entity if the user wants confirmation per device.

## Error handling

- If `entity_id` is not found, call `get_all_states` to find the closest match and suggest it.
- If a service is unavailable, call `get_services` for the domain to show what's available.
- Always confirm with the user before turning off multiple devices at once.

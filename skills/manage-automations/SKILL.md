---
name: manage-automations
description: >
  Use this skill when the user wants to work with Home Assistant automations.
  Trigger phrases: "trigger my automation", "run the morning routine", "list my automations",
  "disable the automation", "enable automation", "what automations do I have",
  "run automation", "turn off automation", "activate scene", "which automations are on".
metadata:
  version: "0.1.0"
---

List, trigger, enable, and disable Home Assistant automations and scenes.

## Workflow

1. Call `list_automations` to get all automations with their current state (on/off) and last triggered time.
2. If the user names a specific automation ambiguously, find the closest match by friendly name.
3. Perform the requested action: trigger, enable, or disable.
4. Confirm the outcome in plain language.

## Available actions

**List automations**
- Call `list_automations()` — returns all automation entity IDs, friendly names, state (on/off), and last triggered timestamp.
- Present as a readable list grouped by state (active vs disabled).

**Trigger an automation manually**
- Call `trigger_automation(entity_id)`.
- Confirm: "Done — I've triggered [friendly name]."

**Enable an automation**
- Call `enable_automation(entity_id)`.
- The automation will now run on its configured triggers.

**Disable an automation**
- Call `disable_automation(entity_id)`.
- The automation is paused but not deleted; re-enable it any time.

**Activate a scene**
- Scenes live in the `scene` domain: call `call_service(domain="scene", service="turn_on", entity_id="scene.NAME")`.
- List available scenes with `get_all_states(domain="scene")`.

## Naming tips

- Automation friendly names often describe their trigger or purpose: "Morning Routine", "Lights Off at Midnight", "Motion Detected - Hallway".
- If the user says something like "run my morning routine", use `list_automations` and match by friendly name (case-insensitive substring match is fine).
- If multiple automations match, list them and ask the user to confirm which one.

## Notifications

- After triggering an automation the user cares about confirming (e.g. a security-related one), offer to send a notification using `send_notification`.

## Limitations

- This plugin can trigger and toggle automations but cannot create or edit automation YAML. For editing, direct the user to the Home Assistant UI (Settings → Automations).

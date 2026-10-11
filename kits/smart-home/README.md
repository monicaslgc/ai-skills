# Smart home kit

Skills for Home Assistant owners: device health, lighting and automation troubleshooting, automation design, energy and climate insight, security checks, maintenance, vacuum, notifications and naming.

> Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`control-devices`](../../skills/control-devices) | Control lights, climate, covers and fans in plain language |
| [`query-status`](../../skills/query-status) | Ask about device states, sensors and history |
| [`manage-automations`](../../skills/manage-automations) | List, trigger, enable and disable automations |
| [`ha-device-health-check`](../../skills/ha-device-health-check) | Find unavailable devices, low batteries and stale sensors |
| [`ha-lighting-troubleshooter`](../../skills/ha-lighting-troubleshooter) | Diagnose lights that do not respond or behave strangely |
| [`ha-automation-designer`](../../skills/ha-automation-designer) | Design a robust automation and give YAML to paste in Home Assistant |
| [`ha-automation-debugger`](../../skills/ha-automation-debugger) | Find out why an automation did not run or ran when it should not |
| [`ha-energy-insights`](../../skills/ha-energy-insights) | Analyse power and energy use: peaks, standby load and savings ideas |
| [`ha-climate-comfort-advisor`](../../skills/ha-climate-comfort-advisor) | Review heating and cooling behaviour and suggest comfort and savings |
| [`ha-night-security-check`](../../skills/ha-night-security-check) | Run a bedtime or leaving-home check of locks, doors, windows and lights |
| [`ha-home-maintenance-planner`](../../skills/ha-home-maintenance-planner) | Plan recurring home maintenance and set up reminders |
| [`ha-vacuum-routines`](../../skills/ha-vacuum-routines) | Plan robot vacuum routines and handle errors and scheduling |
| [`ha-notification-designer`](../../skills/ha-notification-designer) | Design useful notifications without alert fatigue |
| [`ha-entity-naming-audit`](../../skills/ha-entity-naming-audit) | Audit entity names and propose a clean, consistent naming scheme |

## Suggested order

1. Start with the basics: `query-status`, `control-devices` and `manage-automations`.
2. Keep the home healthy with `ha-device-health-check` and fix problems with `ha-lighting-troubleshooter` and `ha-automation-debugger`.
3. Design new routines with `ha-automation-designer`, `ha-vacuum-routines` and `ha-notification-designer`.
4. Understand comfort and cost with `ha-climate-comfort-advisor` and `ha-energy-insights`.
5. Check security with `ha-night-security-check`, plan upkeep with `ha-home-maintenance-planner` and tidy names with `ha-entity-naming-audit`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/control-devices ~/.claude/skills/
cp -r ai-skills/skills/query-status ~/.claude/skills/
cp -r ai-skills/skills/manage-automations ~/.claude/skills/
cp -r ai-skills/skills/ha-device-health-check ~/.claude/skills/
cp -r ai-skills/skills/ha-lighting-troubleshooter ~/.claude/skills/
cp -r ai-skills/skills/ha-automation-designer ~/.claude/skills/
cp -r ai-skills/skills/ha-automation-debugger ~/.claude/skills/
cp -r ai-skills/skills/ha-energy-insights ~/.claude/skills/
cp -r ai-skills/skills/ha-climate-comfort-advisor ~/.claude/skills/
cp -r ai-skills/skills/ha-night-security-check ~/.claude/skills/
cp -r ai-skills/skills/ha-home-maintenance-planner ~/.claude/skills/
cp -r ai-skills/skills/ha-vacuum-routines ~/.claude/skills/
cp -r ai-skills/skills/ha-notification-designer ~/.claude/skills/
cp -r ai-skills/skills/ha-entity-naming-audit ~/.claude/skills/
```

These skills need the Home Assistant MCP server in [`tools/home-assistant-mcp`](../../tools/home-assistant-mcp) (`HA_URL` and `HA_TOKEN` as environment variables). They use only its existing tools. Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

---
name: ha-entity-naming-audit
description: Audit Home Assistant entity IDs and friendly names for consistency, propose a naming convention and a safe rename plan that checks automation dependencies. Use when names are messy, automations are hard to read, or before a big clean-up.
---

# Ha entity naming audit

Make the system readable and predictable, and avoid breaking automations while tidying.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Rooms and areas used in the home.
- Preferences for naming style.
- Whether automations, scripts and dashboards depend on current names.

## Workflow

1. Call `get_all_states` and collect entity IDs and friendly names by domain.
2. Look for problems: duplicates, generic names (`light_1`), numeric suffixes, inconsistent room names, mixed languages, abbreviations, and friendly names that do not match IDs.
3. Propose a convention, such as `domain.room_device_function` for IDs and a plain-language friendly name, and list the room vocabulary.
4. Build a mapping table of old to new IDs and friendly names.
5. Call `list_automations` and review names and descriptions that might reference the old entities. Warn that renamed IDs must be updated in automations, scripts, scenes and dashboards.
6. Recommend an order: rename friendly names first (low risk), then IDs in small batches, testing after each batch.
7. Provide a rollback note: keep the mapping table, and take a backup before renaming.
8. The user performs the renames in the Home Assistant interface. This skill does not rename entities.

## Output format

| Old entity ID | Old name | Problem | New entity ID | New name | Used by |
|---|---|---|---|---|---|

Convention, room vocabulary, batch order, rollback note.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Renaming IDs can break automations, scripts, scenes and dashboards. Recommend a backup first.
- This skill is read-only.

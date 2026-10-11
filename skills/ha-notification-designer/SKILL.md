---
name: ha-notification-designer
description: Design a notification strategy for Home Assistant: what deserves an alert, who receives it, priority levels, grouping, quiet hours and wording, with a test message. Use when notifications are too many, too few or unclear.
---

# Ha notification designer

Make notifications worth reading, so the important ones are never ignored.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Current notifications and complaints.
- People and devices that receive them.
- Events that matter most.
- Quiet hours.

## Workflow

1. List the events that could notify and classify them: urgent (act now), important (see today), information (digest).
2. Decide for each: who is notified, through which channel, and when it is suppressed (quiet hours, when someone is already looking).
3. Reduce noise: add a delay before alerting on flapping sensors, group related events, and send one message with a count instead of many.
4. Write messages that say what happened, where, and what to do. Put the key words first.
5. Define repeat rules: at most one reminder, then stop or escalate to another person.
6. Call `get_services` for the `notify` domain to see the available targets, then propose the automations that send each notification (see `ha-automation-designer`).
7. With the user's confirmation, send one test message using `send_notification`.

## Output format

| Event | Class | Recipients | Channel | Quiet hours | Message | Repeat rule |
|---|---|---|---|---|---|---|

Digest design, test plan.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- Send test notifications only with the user's confirmation and to the user's own devices.
- Do not include secrets or sensitive personal data in notification text.

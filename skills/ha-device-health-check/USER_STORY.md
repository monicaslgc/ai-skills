# User story: ha-device-health-check

## Story

**As** a Home Assistant owner,
**I want** a quick check of what is unavailable, low on battery or silent,
**so that** I fix problems before they affect my home.

## Scenario

Several lights and sensors stopped responding after a power cut.

## Acceptance criteria

- [ ] Unavailable entities are grouped to reveal common causes.
- [ ] Batteries below a threshold are listed.
- [ ] Sensors that stopped updating are found.
- [ ] Findings are ranked with safety devices first.
- [ ] Nothing is changed during the check.

## Try it

> Run a health check on my Home Assistant and tell me what needs attention first.

See [SKILL.md](SKILL.md) for the full instructions.

---
name: ha-energy-insights
description: Analyse household energy use from Home Assistant sensors: totals, daily pattern, peaks, standby load, biggest consumers and practical savings, with cost if the tariff is given. Use when the user asks about energy use, high bills or how to reduce consumption.
---

# Ha energy insights

Turn sensor history into a clear picture and a short list of things worth changing.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Time period to analyse.
- Tariff (price per kWh, time-of-use periods), if known.
- Which devices are monitored.

## Workflow

1. Call `get_all_states(domain="sensor")` and identify power (W) and energy (kWh) sensors by name and unit using `get_state`.
2. Call `get_history` for the chosen sensors over the period (use hours, for example 24 or 168).
3. Compute total use, daily average, the daily pattern (peaks and troughs), and the baseline when nobody is active (standby).
4. Rank the biggest consumers among monitored devices. Say what is not monitored.
5. If a tariff is given, estimate cost, and the cost difference of moving flexible loads to cheaper periods.
6. Suggest practical changes: reduce standby, shift loads, check always-on devices, adjust heating schedules. Estimate the saving, labelled as an estimate.
7. Offer to create a recurring check or notification (via an automation the user adds).

## Output format

| Item | Use (kWh) | Share | Peak (W) | Notes |
|---|---|---|---|---|

Baseline/standby, daily pattern, cost estimate, ideas ranked by effect and effort.

## Safety

- Use only the Home Assistant tools available. Never unlock doors, disarm alarms, or switch off safety devices without the user's explicit confirmation in the conversation, and confirm before acting on more than one device.
- This skill is read-only unless the user asks for an action.
- Label estimates as estimates and state data gaps.

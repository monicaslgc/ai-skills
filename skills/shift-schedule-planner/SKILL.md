---
name: shift-schedule-planner
description: Plan a shift schedule that covers expected demand, respects working-time rules and preferences, and shares unpopular shifts fairly. Use when creating a rota, rebalancing shifts, handling absences or checking whether a schedule is workable.
---

# Shift schedule planner

Produce a schedule people can live with and the business can run on, with the trade-offs visible.

## Inputs to collect

Ask for what is missing, or mark it as unknown:
- Opening hours and the coverage needed per period, with minimum skills or roles.
- Team members, contracted hours, skills and availability.
- Rules: maximum hours, rest periods, days off, consecutive shifts, local requirements.
- Known leave and preferences.

## Workflow

1. Turn demand into required headcount per time block, including minimum coverage and the skills needed.
2. List the hard rules (must never be broken) and soft preferences (nice to have). Ask the user to confirm any rule that is a legal requirement.
3. Build the pattern: assign core shifts first, then fill gaps, then balance weekends, nights and holidays across people over a longer period.
4. Check each person against the rules: hours, rest between shifts, consecutive days, days off.
5. Check each time block against coverage. Mark gaps and over-coverage.
6. Measure fairness: number of weekend, night and late shifts per person and over time.
7. Offer options when conflicts remain, such as swaps, overtime, part-time cover or lowering coverage in quiet periods.
8. Provide a one-page schedule and a list of assumptions and open conflicts.

## Output format

| Person | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Hours |
|---|---|---|---|---|---|---|---|---|

Coverage check per block, rule check per person, fairness summary, open conflicts and options.

## Safety

- Employment and data-protection rules differ by country and organisation. This is a planning aid, not legal advice: check local law, company policy and, where needed, a qualified professional. Treat people fairly and avoid discriminatory criteria.
- Do not use protected characteristics to assign shifts.
- Use initials or placeholders in shared examples.

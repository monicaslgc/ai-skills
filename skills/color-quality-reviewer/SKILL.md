---
name: color-quality-reviewer
description: Review before/after photos or sampled video frames for clipping, colour casts, noise, artefacts, shot consistency and delivery integrity.
---

# Color quality reviewer

## Purpose
Check whether an automated correction improved the intended qualities without introducing avoidable technical defects.

## Procedure
1. Gather source/output paths, preset, tool version, intended look and delivery requirements. Do not infer missing acceptance criteria.
2. Verify file integrity, dimensions, duration, frame rate, audio presence and colour metadata as appropriate for the media type.
3. Compare matched before/after views using the same display and scaling. For video, sample multiple points per shot and scene transition.
4. Inspect exposure and clipping, shadow noise, banding, halos, oversaturation, colour casts, unnatural skin shifts, flicker and shot-to-shot jumps.
5. Check that the correction matches the brief: neutral/natural correction is not the same as creative grading.
6. Classify findings as pass, warning or fail with evidence, severity and recommended action.
7. If a critical issue is found, recommend rollback or a revised preset; do not silently edit the output again.
8. Produce a report and keep the source and rejected render available for comparison.

## Guardrails
- Do not claim objective visual accuracy from file metadata alone.
- Do not mark a render passed because the script exited successfully.
- Do not infer that detail was recovered when it was clipped in the source.
- Be explicit about display limitations and untested frames.
- Do not overwrite approved outputs during review.

## Output contract
- Technical integrity checks
- Visual QA checklist and sampled frames
- Findings with severity/evidence
- Pass / warning / fail decision and rationale
- Recommended remediation or rollback

## Evaluation
Pass when technical and visual QA are separate, review coverage is disclosed, and any critical defects block approval.
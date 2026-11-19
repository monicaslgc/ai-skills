---
name: shot-matching
description: Match colour and tonal appearance across photos or video shots using a designated reference while preserving scene-specific lighting.
---

# Shot matching

## Purpose
Reduce distracting differences between shots without erasing intentional lighting or forcing all scenes to identical pixel values.

## Procedure
1. Identify the reference image/shot and the target shots. Confirm whether the reference is technically corrected, a creative look, or only an approximate inspiration.
2. Verify media type, colour space, exposure context and display pipeline. Do not compare HDR and SDR values as if they were equivalent.
3. Compare representative frames and identify the main differences: exposure, white balance, contrast, saturation, black level and highlight roll-off.
4. Separate global differences from local or intentional lighting differences. Preserve changes that convey time of day, location, mood or motivated practical lights unless the user requests otherwise.
5. Propose a per-shot adjustment table with relative changes, confidence and risks. Use shared base settings only for shots with genuinely comparable conditions.
6. Apply through a deterministic script or tool, producing separate outputs.
7. Review a contact sheet or sampled frames side by side. Check neutral objects, skin tones, clipping, noise and transitions.
8. Record exceptions and shots needing manual masks, tracking or selective correction.

## Guardrails
- A reference is not automatically colour-accurate; state that limitation.
- Do not clone the reference's pixel values or flatten meaningful lighting differences.
- Do not apply one grade across mixed cameras/log profiles without normalisation.
- Avoid face recognition or identity inference; only assess visible tonal and colour consistency.
- Never overwrite originals.

## Output contract
- Reference and target inventory
- Match-difference table
- Per-shot proposed settings
- Automated execution plan
- QA summary and manual exceptions

## Evaluation
Pass when each target is assessed separately, intentional lighting is preserved, and a human-readable comparison plan is included.
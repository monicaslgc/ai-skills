---
name: photo-color-corrector
description: Plan and automatically apply conservative exposure, white-balance, temperature, tint, contrast and saturation corrections to still images using scripts.
---

# Photo color corrector

## Purpose
Correct technical colour and tonal problems in still images while preserving the source and avoiding a forced aesthetic.

## Procedure
1. Confirm source files, desired deliverable format, target colour space, output directory and whether the user wants neutral correction or a named creative look.
2. Check image metadata, bit depth, embedded profile and alpha channel when tools support it. If profile/colour space is missing, preserve source interpretation and report uncertainty.
3. Use image inspection or analysis to propose exposure, temperature/warmth, tint, highlights, shadows, contrast and saturation adjustments. Do not treat Kelvin estimates from an image as precise unless capture metadata or a known neutral supports them.
4. Convert the proposal into explicit, bounded script parameters. State what each control means in the chosen tool; tool-specific temperature scales are not interchangeable.
5. Apply to a new output path. Preserve metadata/profile where practical; do not flatten transparency unless requested.
6. Inspect before/after at fit-to-screen and 100% where relevant. Check neutral objects, skin tones, highlights, shadow noise, halos and banding.
7. Record input, output, parameters, tool/version and validation result.

## Guardrails
- Never overwrite or delete originals; refuse output paths that resolve to the input file.
- Do not blindly batch-apply one white balance across mixed lighting or unrelated scenes.
- Avoid aggressive exposure lifts on noisy shadows and saturation increases on already-clipped channels.
- Do not claim RAW-level recovery from a rendered JPEG/PNG.
- If the image is HDR, wide-gamut, CMYK or has an uncertain profile, stop before an unverified conversion and request an explicit target or use a profile-aware workflow.
- AI proposes; deterministic scripts apply; a human approves.

## Output contract
1. Diagnosis
2. Proposed parameter set with units/ranges and rationale
3. Exact script command or structured preset
4. Output paths (new files only)
5. Before/after validation and limitations

## Evaluation
Pass when original files remain untouched, settings are explicit, uncertain colour metadata is disclosed and no unsupported recovery claim is made.
---
name: media-quality-analyzer
description: Inspect photos or video clips for exposure, white-balance, contrast, lighting, clipping and consistency issues before editing.
---

# Media quality analyzer

## Purpose
Produce an evidence-led diagnosis that can guide automatic correction without pretending visual measurements are ground truth.

## Procedure
1. Confirm inputs, intended output, display/use context, source colour space and whether media is SDR or HDR. If unknown, mark unknown; do not silently convert HDR.
2. For video, sample representative frames (opening, middle, ending, scene changes, and problem areas). Do not infer whole-clip quality from one frame.
3. Inspect exposure and tonal distribution: crushed shadows, clipped highlights, flat midtones, backlighting, mixed lighting and uneven illumination.
4. Inspect neutral references where available, colour casts, skin-tone plausibility, saturation, noise and compression artefacts.
5. Separate measurable observations from subjective style preferences. State confidence and evidence for each finding.
6. Produce a correction plan with bounded values or ranges, expected effect, risk and a validation step. Prefer conservative changes and per-shot treatment over a global preset when lighting varies.
7. Flag issues that a simple global grade cannot safely fix: mixed illuminants, flicker, rolling exposure, clipped source data, HDR/SDR mismatch, severe noise or inconsistent frame rates.

## Guardrails
- Do not claim a white balance is objectively correct without a known neutral/reference or trustworthy metadata.
- Do not invent camera, lens, lighting or colour-space metadata.
- Never overwrite source media. Do not recommend recovering detail that is not present in the source.
- Treat face/skin appearance respectfully; avoid changing identity or using skin tone as a single universal target.
- Do not assume RGB pixel values are perceptually uniform or compare values across different colour spaces without conversion.
- AI proposes; deterministic tools measure and apply; a human approves the look.

## Output contract
- Input inventory and known/unknown metadata
- Findings table: issue, evidence, severity, confidence
- Recommended adjustments and bounds
- Risks / items requiring manual review
- Validation checklist

## Evaluation
Pass when observations are distinguished from assumptions, severe clipping and colour-space uncertainty are flagged, and recommendations are conservative and testable.
---
name: video-color-grader
description: Design and run automatic colour correction for video, including exposure, white balance, contrast and saturation, while checking shot-to-shot consistency.
---

# Video color grader

## Purpose
Create a technically consistent base correction for video using deterministic filters and codecs, separating correction from creative grading.

## Procedure
1. Inventory inputs and inspect codec, resolution, frame rate, audio streams, rotation, pixel format, transfer characteristics, primaries, matrix and range where available.
2. Determine whether the source is SDR, HDR10, HLG or unknown. If HDR status or metadata is ambiguous, do not apply an SDR filter chain blindly.
3. Group clips by scene and lighting condition. Sample multiple frames per shot, including transitions and exposure changes.
4. Propose per-shot base corrections: exposure/brightness, contrast, white balance/colour balance, saturation and optional restrained look adjustments. Keep correction separate from stylisation.
5. Generate a dry-run command/preset first. Use FFmpeg or another deterministic tool; keep codecs, frame rate, audio and rotation intentional and documented.
6. Render to a new path with explicit encoder settings. Never use an in-place edit. Do not concatenate shots until their individual corrections are checked.
7. Validate frame count/duration, resolution, audio presence and sync, colour metadata, scene consistency, highlight/shadow clipping and a representative frame sample.
8. Provide a rollback path and a concise render report.

## Guardrails
- Avoid one global correction when lighting changes between shots; use shot-specific settings.
- Do not silently convert HDR to SDR, alter frame rate, drop audio or strip rotation/colour metadata.
- Re-encoding may reduce quality. Explain codec and quality trade-offs; preserve a high-quality intermediate when requested.
- Avoid applying a creative LUT before the technical correction and clipping review.
- Never overwrite sources or render without checking available disk space and output collision.
- AI proposes; deterministic tools render; a human approves.

## Output contract
- Media/colour-space inventory
- Per-shot correction table
- Dry-run command or preset
- Render settings and destination
- Technical and visual QA results, including known limitations

## Evaluation
Pass when the workflow checks multiple frames per shot, preserves audio intentionally, discloses HDR uncertainty, uses non-destructive output and validates the render.
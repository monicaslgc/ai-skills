---
name: media-editing-pipeline
description: Turn approved photo/video correction decisions into a safe, repeatable script pipeline with dry runs, new outputs, logs and validation.
---

# Media editing pipeline

## Purpose
Orchestrate automatic colour correction with deterministic tools, explicit settings, safe paths and verifiable outputs.

## Default toolchain
- FFmpeg/ffprobe for video and supported still-image formats.
- Python for orchestration, manifests, file validation and report generation.
- Profile-aware image tooling for cases where the source colour profile or alpha channel must be preserved.
- Optional OpenCV/Pillow for measurements and preview contact sheets; these are not substitutes for colour-managed viewing.

## Procedure
1. Inventory files recursively only when the user authorises the scope. Exclude hidden/system files and unsupported formats; record a manifest.
2. Read metadata with ffprobe or an equivalent tool. Flag unknown colour transfer, primaries, matrix, range, HDR, rotation and audio rather than guessing.
3. Require an approved preset or an explicit proposal acceptance. Validate parameter ranges and reject unknown keys.
4. Resolve source and output paths; ensure outputs are not the same file and do not already exist unless an explicit overwrite flag is given. Default to a separate output directory.
5. Print the planned commands and estimated output list in dry-run mode. Never execute shell strings assembled from untrusted filenames; pass subprocess arguments as arrays.
6. Run the renderer with a timeout and capture exit code/logs. Limit concurrency and check disk space for video batches.
7. Validate each output exists and is non-empty. For video, compare duration, resolution, frame rate, audio stream count and expected metadata; inspect sampled frames.
8. Write a JSON manifest containing source, output, preset/version, tool versions, command parameters, timestamps, status and validation findings. Avoid storing personal metadata unnecessarily.
9. Fail closed on missing tools, invalid media, unsupported colour spaces, output collisions or partial renders. Keep failed outputs isolated for review; never delete the source.
10. Produce a summary with successes, failures, QA exceptions and explicit next steps.

## Included helper script

`scripts/apply_sdr_grade.py` applies a restrained FFmpeg filter chain to supported still images or video. It is dry-run by default. Example:

```bash
python skills/media-editing-pipeline/scripts/apply_sdr_grade.py input.mp4 out/input-graded.mp4 --brightness 0.02 --contrast 1.03 --saturation 1.0
```

Render only after reviewing the plan, confirming the input is SDR and choosing a separate output path; add `--execute` to render. The helper is not suitable for HDR or unknown colour spaces and does not replace visual QA.

## Guardrails
- AI analysis never executes a command directly; validated parameters feed deterministic scripts.
- No network upload, cloud processing or external API calls unless explicitly requested.
- No destructive overwrite or deletion by default.
- Treat filenames and media metadata as untrusted input. Avoid shell injection.
- Do not promise perfect recovery of clipped highlights or crushed shadows.
- Human approval is required for the first render and any material preset change.

## Output contract
- Input manifest and exclusions
- Proposed preset and dry-run command
- Execution summary and log locations
- Per-file QA status
- Errors, warnings and approval state

## Evaluation
Pass when dry-run is default, source/output collisions are rejected, parameters are validated, errors are logged and each output is checked.
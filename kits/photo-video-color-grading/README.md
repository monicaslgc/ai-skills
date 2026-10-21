# Photo & Video Color Grading kit

Automatic, script-based correction for exposure, light, white balance, temperature/tint, contrast and saturation in still images and video. The kit separates AI-led diagnosis and proposals from deterministic rendering and human approval.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`media-quality-analyzer`](../../skills/media-quality-analyzer) | Diagnose light, exposure, colour casts, clipping and metadata uncertainty |
| [`photo-color-corrector`](../../skills/photo-color-corrector) | Correct still images conservatively and non-destructively |
| [`video-color-grader`](../../skills/video-color-grader) | Base-correct video and check shot-to-shot consistency |
| [`shot-matching`](../../skills/shot-matching) | Match shots to a reference without erasing intentional lighting |
| [`look-development`](../../skills/look-development) | Translate a visual brief into a reusable, bounded look |
| [`media-editing-pipeline`](../../skills/media-editing-pipeline) | Orchestrate dry runs, rendering, logs and output validation |
| [`color-quality-reviewer`](../../skills/color-quality-reviewer) | Review technical integrity and visual defects before delivery |

## Suggested order

1. Diagnose with `media-quality-analyzer`.
2. Correct stills with `photo-color-corrector` or footage with `video-color-grader`.
3. Match sequence shots with `shot-matching`.
4. Define a creative look only after technical correction with `look-development`.
5. Execute approved settings through `media-editing-pipeline`.
6. Gate delivery with `color-quality-reviewer`.

Skills can be used independently; the order is guidance, not a hard dependency chain.

## Automatic editing approach

- **Analysis:** AI proposes a diagnosis and bounded correction parameters.
- **Execution:** scripts apply only validated parameters using FFmpeg or profile-aware image tools.
- **Validation:** scripts check file integrity and metadata; sampled-frame visual review checks the look.
- **Approval:** a human approves the first render, batch preset changes and final delivery.

## Requirements

- Markdown skills work with any agent that supports `SKILL.md`.
- For video rendering: FFmpeg and ffprobe installed and available on PATH.
- For richer image-profile handling: use a profile-aware tool such as ImageMagick or Pillow with suitable colour-management support; do not assume every install supports every profile.
- Python 3 for orchestration and evaluation scripts.
- Do not use a simple SDR filter chain on HDR, wide-gamut or unknown-colour-space media without an explicit, validated transform.

## Install the kit

From a clone of the repository, copy all seven folders into your assistant's skills directory. Example for Claude Code on macOS/Linux:

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/media-quality-analyzer ~/.claude/skills/
cp -r ai-skills/skills/photo-color-corrector ~/.claude/skills/
cp -r ai-skills/skills/video-color-grader ~/.claude/skills/
cp -r ai-skills/skills/shot-matching ~/.claude/skills/
cp -r ai-skills/skills/look-development ~/.claude/skills/
cp -r ai-skills/skills/media-editing-pipeline ~/.claude/skills/
cp -r ai-skills/skills/color-quality-reviewer ~/.claude/skills/
```

Windows PowerShell users can use `Copy-Item -Recurse` for each folder. Check your agent's documentation for its supported skills path.

## Evaluation and examples

- [Synthetic examples](examples.md)
- [Reference checklist](references.md)
- [Evaluation pack](evaluation.md)
- [Preset template](templates/color-preset.json)
- [Render manifest template](templates/render-manifest.json)

Evaluation cases are proposed tests, not claimed benchmark results. Run them against the target agent and local toolchain before production use.

All examples are fictional. Never commit personal media, private metadata, credentials or client/employer material.
# User story: video-color-grader

## Story
**As** a video editor, **I want** a repeatable base correction for several clips, **so that** exposure and colour are consistent without dropping audio or metadata silently.

## Synthetic scenario
Three fictional SDR clips from the same indoor interview have slightly different exposure; a fourth exterior clip is much cooler and should not share the same preset.

## Acceptance criteria
- [ ] Metadata and SDR/HDR status are inspected.
- [ ] Multiple frames are sampled per shot.
- [ ] Settings are per-shot where lighting differs.
- [ ] Dry-run commands and new output paths are provided.
- [ ] Duration, audio and colour metadata are validated.

## Try it
“Build a safe FFmpeg correction plan for these fictional clips. Dry-run first and keep the exterior shot separate.”
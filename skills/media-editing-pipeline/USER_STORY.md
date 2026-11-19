# User story: media-editing-pipeline

## Story
**As** a creator with a folder of media, **I want** a repeatable script pipeline, **so that** approved corrections are applied safely and results can be verified.

## Synthetic scenario
A fictional folder has four JPGs, two MP4 clips, one unsupported file and an output folder that already contains a filename collision.

## Acceptance criteria
- [ ] Unsupported files are reported rather than silently processed.
- [ ] Dry-run is the default.
- [ ] Source/output collisions and invalid parameters are rejected.
- [ ] Outputs are logged and validated.
- [ ] The original files are never overwritten.

## Try it
“Plan a dry-run batch correction for these synthetic assets, list exclusions and collisions, and do not render until I approve.”
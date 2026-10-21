# User story: photo-color-corrector

## Story
**As** a photographer, **I want** automatic but conservative correction of a still image, **so that** exposure and white balance are improved without damaging the original.

## Synthetic scenario
A fictional JPEG of a white ceramic mug beside a window looks slightly blue; the embedded profile is present but there is no calibrated neutral card.

## Acceptance criteria
- [ ] White-balance estimate is labelled approximate.
- [ ] Explicit parameters and tool-specific units are supplied.
- [ ] Output goes to a new path.
- [ ] Alpha/profile preservation is considered.
- [ ] Before/after checks are reported.

## Try it
“Propose a conservative neutral correction for this image, generate a dry-run command first, and preserve the original.”
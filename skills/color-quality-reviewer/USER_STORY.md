# User story: color-quality-reviewer

## Story
**As** a creator, **I want** a before/after QA report, **so that** I can catch technical regressions before delivering corrected media.

## Synthetic scenario
A fictional render exits successfully but clips a bright window and has lost its audio stream.

## Acceptance criteria
- [ ] Technical integrity is checked separately from visual quality.
- [ ] Multiple video frames are sampled.
- [ ] Missing audio and clipped highlights block approval.
- [ ] Review coverage and display limitations are disclosed.
- [ ] Remediation or rollback is recommended.

## Try it
“Review this synthetic render report and classify each finding as pass, warning or fail. A successful exit code alone is not enough.”
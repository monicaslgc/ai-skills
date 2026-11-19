# Evaluation pack

Status: **proposed test plan — not yet executed against an AI model or media-rendering environment.**

## Scoring

Score each case 0–2 per criterion: 0 = fail/unsafe, 1 = partial or needs correction, 2 = fully met. Record evidence, not just a score.

Critical gates:
- No overwriting source files.
- No rendering from an unresolved HDR/colour-space ambiguity.
- No silent audio loss or output collision.
- No unsupported claim that clipped detail was recovered.
- A process exit code alone never marks visual QA as passed.

## Cases

| ID | Skill(s) | Input | Expected behaviour | Critical? |
|---|---|---|---|---|
| PV-01 | media-quality-analyzer | Cool JPEG, no calibrated neutral | Labels white balance approximate; proposes bounded correction and review | No |
| PV-02 | media-quality-analyzer, video-color-grader | Video with lighting change halfway through | Samples multiple frames and separates scenes/settings | Yes |
| PV-03 | photo-color-corrector | Source and output resolve to same path | Refuses execution; requests a distinct output | Yes |
| PV-04 | photo-color-corrector | Image with alpha channel and ICC profile | Notes preservation requirements and validates output | Yes |
| PV-05 | video-color-grader | HDR/unknown transfer metadata | Stops before applying a blind SDR filter chain | Yes |
| PV-06 | shot-matching | Kitchen daylight plus intentional sunset shot | Preserves sunset warmth and uses per-shot adjustments | No |
| PV-07 | look-development | “Natural warm daylight” | Defines measurable controls, separates correction from look, requires preview | No |
| PV-08 | media-editing-pipeline | Filename collision and unsupported input | Dry-run lists collision/exclusion; does not overwrite | Yes |
| PV-09 | media-editing-pipeline | Filename contains shell metacharacters | Uses safe argument handling; no shell-string execution | Yes |
| PV-10 | color-quality-reviewer | Render exits 0 but audio is missing | Marks FAIL and explains evidence | Yes |
| PV-11 | color-quality-reviewer | Single preview frame supplied for a long clip | Discloses insufficient coverage; does not certify full clip | No |
| PV-12 | all | User asks to recover clipped highlights from an 8-bit JPEG | Explains limits; does not claim missing detail can be reconstructed reliably | Yes |

## Test record template

For each case record:
- Model/agent and version
- Skill version/commit
- Input fixture ID (synthetic only)
- Prompt
- Expected behaviour
- Actual output
- Scores and evidence
- Critical gate passed? (yes/no)
- Defect and regression case
- Reviewer/date

## Release threshold

Do not call the kit production-ready until all critical gates pass, no source overwrite occurs, and visual QA has been performed on representative stills and clips. A passing structural repository validator is not a model-quality benchmark.
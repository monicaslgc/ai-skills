# Synthetic examples

All names, media properties and measurements below are fictional. They describe test scenarios; they are not claims about real files.

## Example A — slightly cool still photo

**Input:** `mug-window.jpg`, JPEG, sRGB profile present, SDR; a white ceramic mug looks cool in window light. No calibrated grey card.

**Diagnosis:** probable cool cast, medium confidence; neutral reference not confirmed; highlights appear intact in the sampled preview.

**Proposal:** mild warmth and a small exposure lift only after preview. Do not label an estimated Kelvin value as measured. Keep saturation unchanged unless visual review shows a real need.

**Expected output:** `out/mug-window-corrected.jpg`; original untouched; include settings in the report.

## Example B — mixed indoor video lighting

**Input:** `interview-a.mp4`, fictional SDR/BT.709 footage; a daylight window and tungsten practical light are both visible.

**Diagnosis:** mixed illuminants; a single global white-balance change would likely fix one area while worsening another.

**Proposal:** correct the dominant subject/neutral reference conservatively; if the background cast remains distracting, flag it for selective correction or masking rather than increasing global temperature compensation.

**Expected output:** a dry-run command and a short test render, not a full batch.

## Example C — adjacent shots

| Shot | Fictional observation | Treatment |
|---|---|---|
| `kitchen-01.mp4` | Slightly underexposed, neutral daylight | Small exposure correction |
| `kitchen-02.mp4` | Slightly warm, similar scene | Independent white-balance adjustment |
| `sunset-03.mp4` | Intentionally warm exterior | Preserve warmth; do not force to kitchen reference |

**Acceptance:** transitions feel coherent, but sunset remains visibly warmer.

## Example D — unsafe input

**Input:** `concert-hdr.mov`, transfer metadata missing, likely HDR, output path equals source path.

**Expected behaviour:** stop before rendering; explain that colour space is uncertain and reject the source/output collision. Ask for a verified target transform and a different output path.

## Example E — successful process, failed deliverable

**Input:** a fictional render process exits with code 0, but ffprobe reports no audio stream and sampled highlights are clipped.

**Expected behaviour:** reviewer marks delivery FAIL. A zero exit code is not visual or technical acceptance.
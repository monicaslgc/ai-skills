---
name: look-development
description: Translate a visual brief into a repeatable, bounded colour look for photos or video, with technical correction kept separate from creative styling.
---

# Look development

## Purpose
Turn subjective references such as natural, warm, cool, cinematic or editorial into a repeatable grade specification that can be applied with scripts.

## Procedure
1. Ask for the intended mood, reference media, delivery platform and target colour space. If no style is specified, default to natural and restrained.
2. Describe the look in observable terms: contrast curve, shadow colour, highlight warmth, saturation, skin-tone protection, black level and highlight roll-off.
3. Separate the technical normalisation stage from the creative look stage. Document assumptions about camera profiles and display conditions.
4. Translate the look into controls supported by the target tool. Bound all parameters and avoid implying that a generic FFmpeg filter is equivalent to a colour-managed grading suite.
5. Produce a preview or short test render, not a full batch, before applying to the full set.
6. Compare on representative shots and confirm that the look survives different lighting conditions.
7. Save a named preset with version, intended input range, target output, known limitations and rollback instructions.

## Guardrails
- Do not use vague style words as a substitute for executable parameters.
- Do not promise exact reproduction from a screenshot without source/reference conditions.
- Avoid extreme teal-orange, crushed blacks, clipped highlights or oversaturated skin unless explicitly requested and approved.
- Do not transfer a look to HDR or wide-gamut media without a compatible pipeline.
- Never overwrite source files; require human approval before batch application.

## Output contract
- Look brief
- Technical assumptions
- Parameter/preset specification
- Preview plan and acceptance criteria
- Versioned export and rollback plan

## Evaluation
Pass when creative look and technical correction are distinct, parameters are executable or clearly marked tool-specific, and the test render precedes batch processing.
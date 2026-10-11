---
name: content-pipeline-planner
description: Plan a pipeline that turns raw footage and images into ready-to-publish vertical videos for short-form platforms, with the system proposing the edit and the creator only approving. Use when designing or reviewing a content-production tool, template system, auto-edit workflow or publishing handoff. Trigger phrases - "plan a video pipeline", "auto-edit my footage", "template system for shorts", "content studio design".
---

# Content Pipeline Planner

Design a pipeline where the creator supplies material and a few answers, and the system proposes everything else. Publishing stays a human step.

## Principles

1. **Templates and content are separate.** A template defines structure: positions, durations, styles, safe zones, per-platform behaviour. A project supplies video, images, text, logo and music. A template never contains values specific to one piece of content.
2. **The system proposes, the creator approves.** Segment selection, pacing, order, cover frame and captions are suggested automatically. Ask the creator only for things the system cannot decide: text they want, stickers or logos, and answers to specific questions.
3. **Publish manually.** Platform APIs often require lengthy audits and restrict unaudited posts. Deliver a ready-to-post package (video, caption, hashtags, cover) rather than posting automatically, unless the user has confirmed API access.
4. **Respect platform constraints.** Check aspect ratio (9:16), duration limits, safe zones for interface overlays, and each platform's rules on music and automated posting. State which rules were verified and which are assumptions.

## Workflow

1. **Intake:** list the raw material, its length and the intended platforms. Note which parts the creator wants included.
2. **Analyse:** detect candidate moments (motion, speech, scene changes, creator markers), score them and keep the best.
3. **Choose a template** by content type and platform. Fill its slots with the selected segments. Do not edit the template for one project.
4. **Assemble a draft:** pacing per format, captions, cover frame and sound. Where music licensing is uncertain, leave music for the creator to add.
5. **Review step:** show the draft with the choices made and one or two alternatives. The creator can swap a segment, edit text or approve.
6. **Render and package:** render asynchronously with progress, then produce the posting package.
7. **Learn:** record which suggestions were accepted or changed and use that to improve scoring and templates over time.

## Output format

For a design request, return: the stage list with inputs and outputs for each, the template schema (fields only, no example values from real content), the data the creator must supply, open questions, risks, and a phased build order with the smallest useful first version.

## Safety

- Only use footage, music and images the creator has the right to use.
- Do not post, schedule or message anyone without explicit approval.
- Keep tokens and platform credentials out of templates, logs and chat.

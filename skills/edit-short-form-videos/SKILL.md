---
name: edit-short-form-videos
description: Plan and fix short-form and gameplay videos: edit plans and 9:16 reframing, subtitles and overlays, edit handoffs, video cleanup (white rectangles, colour patches), draw-on animation, transitions and loops, and audio checks. Use for editing, repurposing or repairing a clip.
---

# Edit short-form videos

Work from the real footage. Never claim timestamps from a filename or thumbnail, and never claim a video is fixed because an export command succeeded.

## Inventory first

For each source record filename, dimensions, duration, frame rate, audio tracks and type (gameplay, facecam, still, voiceover, reference). Inspect representative frames and listen to the relevant audio. Find the true start of the hook and the final payoff. Source timestamps must be observed; edit-plan timestamps are proposed timeline time. Say which is which in the handoff.

## Format treatments

- Outfit showcase: reveal the silhouette, linger on distinguishing details, keep graceful motion.
- Piece showcase: legible differences, clear labels, enough hold time.
- Ability or tutorial: problem, trigger, observable result; keep the proof.
- Pull reaction: expectation, suspense, actual result, reaction; keep audio timing.
- Meme: one setup and payoff; cut dead time, do not explain the joke.
- ASMR or sorting: sound and visual continuity, no intrusive transitions, no sudden loud reactions.
- Inspired look: reference cue, interpretation, detail or reveal; never framed as an official crossover.

Duration follows the footage (roughly 5 to 15 s for a simple joke, 15 to 35 s for a reveal, 25 to 60 s for a compact explanation; none of these is a platform optimum). Do not stretch a five-second meme to fit a template.

## Reframing, subtitles, overlays

Portrait means 9:16. If someone says "vertical 16:9", note the conflict and state a 9:16 assumption unless a wrong export would really hurt. Reframe around the action and subject, not the geometric centre; keep critical UI in tutorials. Use background plates when full-width gameplay cannot crop without losing meaning, and avoid a tiny landscape strip in clutter. Place subtitles against real footage and platform UI, check at phone size, and keep contrast without huge opaque boxes over the subject. Keep the speaker's words as spoken; do not correct a reaction into something they did not say.

## Edit handoff

Ordered rows: source filename, source in/out, timeline placement, crop, speed, transition, on-screen text, audio, rationale. Mark missing shots "capture-required". No fake precision when the source has not been supplied. Export only the needed variants; keep a clean uncaptioned master when useful. Never assume a music track can travel across platforms.

## Cleanup (white rectangle, colour patches)

1. Probe the source and inspect the first frames, transitions, middle and end.
2. Decide whether the defect is stationary, animated, embedded in the graphic, or crossing foreground objects.
3. Sample background colours across time and space; keep intentional gradients and texture; remove only the mismatch.
4. Repair with a clean plate, mask and compositing or inpainting; track the mask if it moves; protect foreground detail.
5. Render a short section first if a specific risk needs resolving, then the full correction.
6. Inspect the first frame and the exact period where the defect appeared; check edges frame by frame around transitions; compare before and after at normal speed and paused. A middle still proves nothing about the opening.
7. Keep duration, dimensions and audio unless asked. Deliver the corrected video, not advice. A blur over the area is not automatically acceptable.

## Draw-on animation

"Like it is being drawn" means strokes appear in a plausible order, not a fade or wipe. Separate outlines, internal detail and fills; animate paths or masks in drawing order; keep the exact source art when asked. Time it from the reference and use case, hold the finished image long enough to use, and keep alpha if required. Check the first mark, line continuity, the move into fill and the final hold. If the tools only allow a reveal, call it a reveal.

## Transitions and loops

Specify total duration, entry, hold, exit, coverage at the cut point, resolution, frame rate, alpha or background, and audio. Use the accepted intro and outro palette and shapes. Check the loop seam at the real end-to-start junction. A stinger must cover the cut it is meant to cover. Use a format the editor supports; H.264 MP4 is not an alpha master; verify alpha codecs actually play; GIF is preview only.

## Audio

Preserve reaction timing. Listen for clipping, level jumps, missing channels, and music masking speech or ASMR detail. Normalise to the delivery target, not an invented universal loudness; keep natural dynamics in relaxed gameplay. Keep stems if they exist; do not claim perfect separation from a mixed track. Subtitles reflect what is audible; check uncertain words.

## Working method

Originals are read-only; work on copies; use versioned output folders (`output/v001/`) and a manifest linking outputs to sources; keep earlier approved drafts; resume from completed steps after a failure. Draft production is the default: never publish, schedule, message anyone, spend money, delete or move originals, or change accounts without explicit authorisation in the task. On failure keep finished work, name the blocked deliverable, continue independent parts, and never fabricate an export.

# Content creation kit

Skills for gaming and creator channels: planning, captions, editing, thumbnails, brand assets, photo posts and challenge series.

## Skills in this kit

| Skill | Use it to |
|---|---|
| [`plan-creator-content`](../../skills/plan-creator-content) | Research-backed content plans, briefs, calendars and reviews |
| [`content-pipeline-planner`](../../skills/content-pipeline-planner) | Plan an auto-edit pipeline for short vertical videos |
| [`write-social-captions`](../../skills/write-social-captions) | Platform-specific captions, titles and hashtags |
| [`style-inspired-cosplay-looks`](../../skills/style-inspired-cosplay-looks) | Describe dress-up looks inspired by other characters honestly |
| [`edit-short-form-videos`](../../skills/edit-short-form-videos) | Edit plans, 9:16 reframing, video repairs and audio checks |
| [`make-daily-challenge-shorts`](../../skills/make-daily-challenge-shorts) | One Short per day for a themed challenge from your own template |
| [`photo-post-deliverables`](../../skills/photo-post-deliverables) | Five sized exports per image for photo posts and carousels |
| [`design-youtube-thumbnails`](../../skills/design-youtube-thumbnails) | Thumbnails and editable templates from real photos and game art |
| [`create-channel-brand-assets`](../../skills/create-channel-brand-assets) | Banners, frames, cutouts, mascot art and component packs |
| [`create-cozy-gameplay-overlays`](../../skills/create-cozy-gameplay-overlays) | Vertical overlays, plates and title cards for cozy gameplay videos |
| [`deslop-designs`](../../skills/deslop-designs) | Checklist that removes generic AI-looking tells from designs |

## Suggested order

1. Plan with `plan-creator-content` and `content-pipeline-planner`.
2. Write copy with `write-social-captions` and `style-inspired-cosplay-looks`.
3. Edit with `edit-short-form-videos`, `make-daily-challenge-shorts` and `photo-post-deliverables`.
4. Create visuals with `design-youtube-thumbnails`, `create-channel-brand-assets` and `create-cozy-gameplay-overlays`, and check them with `deslop-designs`.

## Install the whole kit

```bash
git clone https://github.com/monicaslgc/ai-skills.git
cp -r ai-skills/skills/plan-creator-content ~/.claude/skills/
cp -r ai-skills/skills/content-pipeline-planner ~/.claude/skills/
cp -r ai-skills/skills/write-social-captions ~/.claude/skills/
cp -r ai-skills/skills/style-inspired-cosplay-looks ~/.claude/skills/
cp -r ai-skills/skills/edit-short-form-videos ~/.claude/skills/
cp -r ai-skills/skills/make-daily-challenge-shorts ~/.claude/skills/
cp -r ai-skills/skills/photo-post-deliverables ~/.claude/skills/
cp -r ai-skills/skills/design-youtube-thumbnails ~/.claude/skills/
cp -r ai-skills/skills/create-channel-brand-assets ~/.claude/skills/
cp -r ai-skills/skills/create-cozy-gameplay-overlays ~/.claude/skills/
cp -r ai-skills/skills/deslop-designs ~/.claude/skills/
```

These skills work best when your agent can view images and video. `photo-post-deliverables` also needs Python 3 and Pillow (`pip install pillow`). Each skill folder has a `USER_STORY.md` with a scenario and an example prompt.

All examples are invented. Do not paste real personal data, credentials or confidential contract text into a chat you do not control.

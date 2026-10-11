---
name: photo-post-deliverables
description: Produce the full set of sized images for a photo post or carousel (9x16, 4x5 extended and cropped, 1x1 extended and cropped) with captions, in a fixed folder layout. Use whenever someone asks for a photo post, carousel, or "the sizes" for an image set, including when they write "4:6" (they usually mean 4:5).
---

# Photo post deliverables

Requires Python 3 and Pillow (`pip install -r scripts/requirements.txt`) for the helper script.

## Sizes (five per image)

| Folder | Size | Method |
|---|---|---|
| `9x16/` | 1080x1920 | Cropped around the subject. Horizontal photos are never shrunk into a blurred frame |
| `4x5 extended/` | 1080x1350 | Whole image fitted, blurred side fill, nothing cropped |
| `4x5 cropped/` | 1080x1350 | Cropped, framing chosen per image |
| `1x1 extended/` | 1080x1080 | Whole image fitted, blurred side fill |
| `1x1 cropped/` | 1080x1080 | Cropped, framing chosen per image |

"4:6" in a request almost always means 4:5; confirm if unsure.

## Cropping rules (judgment, per image)

- Keep any headpiece or hat fully intact.
- Put the face in the upper third of the frame.
- Keep props in frame.
- Look at each image before choosing the crop. Do not centre-crop blindly.

## Folder layout

```
<posts>/<project>/
  <captions>.md
  9x16/
  4x5 extended/
  4x5 cropped/
  1x1 extended/
  1x1 cropped/
```

Keep the same filenames across all five folders so images line up.

## Steps

1. Identify the project name and source images.
2. For each image, view it and pick a focus point for the cropped sizes (x, y as 0-1 fractions of width and height, aimed at the face, with headpiece and props inside the crop).
3. Run `scripts/make_sizes.py` once per image with that focus point.
4. Open a few outputs and check: headpiece not cut, face in the upper third, props kept, no stretched or empty areas.
5. Write or update the captions file in the project folder (see `write-social-captions`).

```
python scripts/make_sizes.py <image> <posts/project> --focus 0.5 0.3
```

## Do not

- Deliver fewer than the five sizes unless the user says so.
- Overwrite the original images; the script writes new files only.
- Post or schedule anything.

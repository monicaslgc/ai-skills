"""Make the five photo-post sizes for one image.

Usage: python make_sizes.py IMAGE OUTDIR [--focus FX FY]
FX, FY are 0-1 fractions (default 0.5 0.35) used to place the cropped sizes.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps

SIZES = {
    "9x16": ((1080, 1920), "cropped"),
    "4x5 extended": ((1080, 1350), "extended"),
    "4x5 cropped": ((1080, 1350), "cropped"),
    "1x1 extended": ((1080, 1080), "extended"),
    "1x1 cropped": ((1080, 1080), "cropped"),
}


def extended(img, size):
    w, h = size
    bg = ImageOps.fit(img, size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(40))
    fg = ImageOps.contain(img, size, Image.LANCZOS)
    bg.paste(fg, ((w - fg.width) // 2, (h - fg.height) // 2))
    return bg


def cropped(img, size, focus):
    w, h = size
    scale = max(w / img.width, h / img.height)
    big = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = min(max(round(focus[0] * big.width - w / 2), 0), big.width - w)
    top = min(max(round(focus[1] * big.height - h / 3), 0), big.height - h)  # focus lands in upper third
    return big.crop((left, top, left + w, top + h))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("outdir")
    p.add_argument("--focus", nargs=2, type=float, default=[0.5, 0.35])
    a = p.parse_args()
    src = Path(a.image)
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    for folder, (size, mode) in SIZES.items():
        out = Path(a.outdir) / folder
        out.mkdir(parents=True, exist_ok=True)
        res = extended(img, size) if mode == "extended" else cropped(img, size, a.focus)
        res.save(out / (src.stem + ".jpg"), quality=95)
        print(out / (src.stem + ".jpg"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Safe, conservative FFmpeg SDR grade helper. Dry-run unless --execute is supplied."""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".bmp"}
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".m4v", ".webm", ".avi"}
ALL_EXTS = IMAGE_EXTS | VIDEO_EXTS

def bounded(name: str, value: float, low: float, high: float) -> float:
    if not low <= value <= high:
        raise ValueError(f"{name} must be between {low} and {high}")
    return value

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--brightness", type=float, default=0.0, help="FFmpeg eq brightness [-0.1, 0.1]")
    p.add_argument("--contrast", type=float, default=1.0, help="FFmpeg eq contrast [0.8, 1.25]")
    p.add_argument("--saturation", type=float, default=1.0, help="FFmpeg eq saturation [0.7, 1.3]")
    p.add_argument("--red-midtones", type=float, default=0.0, help="FFmpeg colorbalance rm [-0.1, 0.1]")
    p.add_argument("--green-midtones", type=float, default=0.0, help="FFmpeg colorbalance gm [-0.1, 0.1]")
    p.add_argument("--blue-midtones", type=float, default=0.0, help="FFmpeg colorbalance bm [-0.1, 0.1]")
    p.add_argument("--execute", action="store_true", help="render; without this flag only print the plan")
    p.add_argument("--overwrite-output", action="store_true", help="replace an existing output (never the source)")
    args = p.parse_args()

    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not source.is_file():
        p.error(f"input does not exist or is not a file: {source}")
    if source.suffix.lower() not in ALL_EXTS:
        p.error(f"unsupported input extension: {source.suffix}")
    if output.suffix.lower() not in ALL_EXTS:
        p.error(f"unsupported output extension: {output.suffix}")
    if source == output:
        p.error("source and output resolve to the same path; refusing to overwrite source")
    if output.exists() and not args.overwrite_output:
        p.error(f"output already exists; choose another path or pass --overwrite-output: {output}")
    try:
        brightness = bounded("brightness", args.brightness, -0.1, 0.1)
        contrast = bounded("contrast", args.contrast, 0.8, 1.25)
        saturation = bounded("saturation", args.saturation, 0.7, 1.3)
        red = bounded("red-midtones", args.red_midtones, -0.1, 0.1)
        green = bounded("green-midtones", args.green_midtones, -0.1, 0.1)
        blue = bounded("blue-midtones", args.blue_midtones, -0.1, 0.1)
    except ValueError as exc:
        p.error(str(exc))

    ffmpeg = shutil.which("ffmpeg")
    if args.execute and not ffmpeg:
        p.error("ffmpeg was not found on PATH")
    vf = (
        f"eq=brightness={brightness:.4f}:contrast={contrast:.4f}:saturation={saturation:.4f},"
        f"colorbalance=rm={red:.4f}:gm={green:.4f}:bm={blue:.4f}:pl=1"
    )
    is_image = source.suffix.lower() in IMAGE_EXTS
    command = [ffmpeg or "ffmpeg", "-hide_banner", "-n", "-i", str(source),
               "-map", "0:v:0", "-vf", vf, "-map_metadata", "0"]
    if is_image:
        command += ["-frames:v", "1"]
    else:
        command += ["-map", "0:a?", "-c:v", "libx264", "-crf", "18",
                    "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart"]
    if args.overwrite_output and args.execute:
        command[2] = "-y"
    command.append(str(output))
    report = {
        "mode": "execute" if args.execute else "dry-run",
        "source": str(source),
        "output": str(output),
        "filter": vf,
        "warning": "Use only after confirming SDR input and compatible colour metadata. "
                   "This is a basic correction, not a colour-managed HDR workflow.",
        "command": command,
    }
    print(json.dumps(report, indent=2))
    if not args.execute:
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        completed = subprocess.run(command, check=False, timeout=3600)
    except subprocess.TimeoutExpired:
        print("ERROR: render timed out; inspect any partial output before retrying.", file=sys.stderr)
        return 2
    if completed.returncode != 0:
        print(f"ERROR: ffmpeg exited with status {completed.returncode}", file=sys.stderr)
        return completed.returncode or 1
    if not output.is_file() or output.stat().st_size == 0:
        print("ERROR: render did not produce a non-empty output", file=sys.stderr)
        return 3
    print(f"Rendered {output} ({output.stat().st_size} bytes). Review visually before delivery.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

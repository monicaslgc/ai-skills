# References and implementation notes

Use these as implementation references, not as substitutes for testing against the exact installed tool version.

- [FFmpeg filters documentation](https://ffmpeg.org/ffmpeg-filters.html) — documents filters such as `eq`, `colorbalance`, `curves` and colour-space conversion. Check the installed FFmpeg build and filter options before generating commands.
- [FFmpeg command-line documentation](https://ffmpeg.org/ffmpeg.html) — input/output handling, stream mapping, metadata and encoding options.
- [FFmpeg documentation index](https://www.ffmpeg.org/documentation.html) — official documentation for the installed toolchain.
- [Pillow documentation](https://pillow.readthedocs.io/) — Python image loading and transformations; profile-aware workflows may require explicit colour-management handling.

## Important implementation notes

- Temperature/tint controls vary by application. FFmpeg's `colorbalance` controls channel balance by tonal region; it is not a universal Kelvin temperature slider.
- A simple `eq`/ `colorbalance` chain is a practical SDR starting point, not a complete colour-managed HDR workflow.
- Metadata alone cannot establish that an image looks correct. Review sampled frames on a consistent display.
- For video, preserve or intentionally map transfer characteristics, primaries, matrix, range, rotation and audio.
- For all automated processing, keep originals and record parameters, tool versions, output paths and QA results.

Last checked against official documentation links on 2026-10-21; confirm current options in the local tool version.
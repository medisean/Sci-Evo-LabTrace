# MinerU Artifacts

This directory is used for local MinerU API outputs.

The seed PDF was parsed successfully with the MinerU batch API on 2026-05-25.
Local generated files include Markdown, content-list JSON, layout JSON, model
JSON, extracted images, and the downloaded result zip.

These generated artifacts are intentionally ignored in the public GitHub repo
because the source PDF license status still needs review before public release.
To regenerate them locally, run:

```bash
python3 scripts/mineru_parse.py Sci-Evo-Sample.pdf --output-dir data/interim/mineru
```

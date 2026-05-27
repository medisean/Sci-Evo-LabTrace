# MinerU 本地产物目录

该目录用于保存本地 MinerU API 解析结果。

样例 PDF 已于 2026-05-25 通过 MinerU batch API 成功解析；另外两篇 CC-BY gold case PDF 已于 2026-05-27 通过 MinerU batch API 成功解析。本地生成文件包括 Markdown、content list JSON、layout JSON、model JSON、抽取图片和下载 zip。

由于源 PDF 的公开许可状态仍需复核，这些生成产物默认不会提交到公开 GitHub 仓库。需要重新生成时运行：

```bash
python3 scripts/mineru_parse.py Sci-Evo-Sample.pdf --output-dir data/interim/mineru
```

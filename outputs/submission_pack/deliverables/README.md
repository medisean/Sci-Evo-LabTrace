# Sci-Evo 提交包

本目录包含离线提交所需的核心交付件：

- `scievo_competition_pitch.pptx`：参考 EduMiner 提交稿风格重写的 Sci-Evo 展示 PPT。
- `data/processed/`：gold 数据集、评测任务、manifest 和开放来源筛选结果。
- `docs/`：技术报告、数据集卡片、提交清单和录屏讲稿。
- `reports/`：质量报告、MinerU 运行报告、提交就绪报告和来源筛选队列。
- `schemas/`：Sci-Evo case schema。
- `scripts/`：构建、校验、评测任务生成、质量报告和提交就绪检查脚本。

说明：

- 不包含任何密钥文件。
- 不公开打包未经许可复核的全文 PDF 或 MinerU 全量解析产物。
- 如需复核当前状态，可运行 `python3 scripts/check_submission_readiness.py`。


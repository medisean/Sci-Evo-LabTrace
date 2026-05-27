# Sci-Evo-LabTrace

Sci-Evo-LabTrace 是面向 AI4S 科学智能体的科学演化数据集。当前版本聚焦蛋白设计、酶工程与合成生物学中的真实科研闭环：目标提出、计算设计、湿实验验证、失败/差距分析、迭代优化与最终指标确认。

本项目聚焦 Sci-Evo 科研演化数据方向。它不是静态科学问答数据，而是把真实论文和实验叙事整理成可训练、可评测、可追溯的科研过程轨迹。

## 内容结构

- `data/processed/scievo_gold.jsonl`：整理后的 Sci-Evo gold case。
- `data/processed/scievo_eval_tasks.jsonl`：由 gold case 自动生成的评测任务。
- `data/processed/vetted_open_access_sources.jsonl`：开放来源候选论文筛选队列。
- `schemas/scievo_case.schema.json`：case 字段定义。
- `scripts/build_dataset.py`：构建主 JSONL 数据集。
- `scripts/validate_dataset.py`：校验必填字段与轨迹一致性。
- `scripts/build_eval_tasks.py`：从轨迹数据生成评测任务。
- `scripts/check_submission_readiness.py`：检查当前仓库材料是否完整。
- `scripts/vet_candidate_sources.py`：按许可信息筛选开放论文候选。
- `docs/TECHNICAL_REPORT.md`：技术报告。
- `docs/VIDEO_SCRIPT.md`：录屏讲稿。
- `docs/SUBMISSION_CHECKLIST.md`：材料清单。
- `reports/QUALITY_REPORT.md`：数据质量报告。
- `reports/SUBMISSION_READINESS.md`：完整性检查报告。

## 数据单元

每条 case 表示一条完整科研链路：

1. 初始科研需求与可量化目标。
2. 多步科研轨迹，包括干实验、湿实验、工具选择、参数、观察结果和迭代逻辑。
3. 成功验证，包括验证方法、关键指标和最终结论。
4. 证据链接，回溯到原始文档页面、段落、图、表或 MinerU 解析块。

## 构建与检查

```bash
python3 scripts/build_dataset.py
python3 scripts/validate_dataset.py data/processed/scievo_gold.jsonl
python3 scripts/build_eval_tasks.py
python3 scripts/vet_candidate_sources.py
python3 scripts/make_quality_report.py
python3 scripts/check_submission_readiness.py
```

`check_submission_readiness.py` 会在关键材料不完整时返回非零状态。当前仓库把“至少 3 条完整 gold case”设为基础完整度门槛，并已经达到该门槛。

## MinerU 使用

3 条 gold case 对应 PDF 均已通过 MinerU API 完成解析。本地解析产物包括 Markdown、content list JSON、layout JSON、model JSON、图片和下载 zip。出于许可合规考虑，这些全量解析产物只保留在本地，不放入公开 GitHub 仓库；公开仓库保留 MinerU 运行报告和可复现脚本。

本地重新解析命令：

```bash
python3 scripts/mineru_parse.py Sci-Evo-Sample.pdf data/raw/pdfs/SELT-PROT-0002.pdf data/raw/pdfs/SELT-PROT-0003.pdf --output-dir data/interim/mineru
```

## 扩展流程

使用 `scripts/collect_openalex_candidates.py` 收集开放获取论文元数据：

```bash
python3 scripts/collect_openalex_candidates.py --limit 25
```

该脚本只保存题名、DOI、开放获取状态、许可信息和 OA 链接，不下载全文。随后运行 `scripts/vet_candidate_sources.py`，优先筛选许可信息明确、适合本地 MinerU 解析和人工复核的候选论文。

## 当前状态

- 数据构建与校验流程已就绪，当前生成 3 条 gold case 和 37 条评测任务。
- 已记录 MinerU API 使用过程；3 条 gold case 均有本地解析产物。
- 2 条新增 gold case 来自明确 CC-BY 的开放论文。
- 技术报告、材料清单、质量报告、录屏讲稿和完整性检查报告均已准备。
- 已补充逐 case 深度审计与标注规范，用于说明 gold case 的质量控制口径。
- 当前主要工作是最终材料整理，以及按需继续扩充更多开放许可案例。

## 许可说明

数据记录只有在来源材料与派生标注均符合原始许可和使用约束时才公开发布。原创标注推荐使用 CC-BY-4.0；对源论文全文、图片和 MinerU 全量解析产物，公开前必须单独完成许可复核。

# Sci-Evo-LabTrace 技术报告

## 1. 数据集简介

Sci-Evo-LabTrace 是面向 Sci-Evo（科学演化数据）方向的数据集，聚焦蛋白设计、酶工程与合成生物学中的科研闭环过程。数据集目标不是记录静态知识问答，而是把真实科研论文中的探索过程整理成可机器读取、可训练、可评测的科学智能体轨迹。

首版样例以从头设计人工荧光素酶为种子案例，覆盖以下科研阶段：初始目标定义、计算 scaffold 生成、活性位点设计、序列优化、实验筛选、位点饱和突变、哺乳动物细胞验证与最终指标确认。

## 2. 数据集设计目标

本数据集服务于三类 AI4S 能力：

1. 科研过程理解：模型能够理解一个科研目标如何被拆成多步实验与计算决策。
2. 科研决策学习：模型能够在给定当前状态、观察结果或失败信息时预测下一步行动。
3. 科学证据追溯：每个关键字段都应能回溯到原始论文页面、段落、图、表或 MinerU 解析块。

## 3. 数据结构

每条样本对应一个完整科研链路，字段包括：

- `case_id`：稳定样本编号。
- `source`：论文或原始资料来源、许可状态、MinerU 解析产物路径。
- `initial_request`：科研目标、输入信息、用户意图和量化目标。
- `agent_trajectory`：逐步科研轨迹，包括思考、行动、工具、参数、观察、结果类型和证据。
- `success_verification`：最终验证方法、指标和结论。
- `quality`：人工/自动标注等级、证据覆盖率和许可复核状态。

Schema 文件位于 `schemas/scievo_case.schema.json`。处理后的 JSONL 文件位于 `data/processed/scievo_gold.jsonl`。

## 4. MinerU 使用方式

本项目使用 MinerU API 作为科学文献解析工具链的核心组件。样例 PDF 已完成一次真实解析，解析产物包括：

- `data/interim/mineru/Sci-Evo-Sample/full.md`
- `data/interim/mineru/Sci-Evo-Sample/content_list.json`
- `data/interim/mineru/Sci-Evo-Sample/content_list_v2.json`
- `data/interim/mineru/Sci-Evo-Sample/layout.json`
- `data/interim/mineru/extracted/images/`

标准流程如下：

1. 将每篇 PDF 上传至 MinerU API 或使用 MinerU 开源项目离线解析。
2. 获取 Markdown、content list JSON、图片、表格和公式等结构化结果。
3. 把抽取出的 Sci-Evo 字段与 MinerU 输出中的页面、段落、图表块建立映射。
4. 在最终数据集中通过 `evidence` 字段保留 `source_doc`、`page`、`locator` 和 `mineru_block_id`。

当前仓库已提供 `scripts/mineru_parse.py`，用于调用 MinerU API 批量解析 PDF。该脚本从环境变量 `MINERU_API_TOKEN` 或本地 `mineru-api-token.txt` 读取 token，不会把 token 写入输出文件。

## 5. 数据构建流程

当前最小可提交流程：

```bash
python3 scripts/build_dataset.py
python3 scripts/validate_dataset.py data/processed/scievo_gold.jsonl
python3 scripts/build_eval_tasks.py
python3 scripts/make_quality_report.py
```

后续扩展流程：

1. 收集开放许可论文或赛事允许使用的原始 PDF。
2. 使用 MinerU 生成结构化解析产物。
3. 从论文叙事中抽取科研演化链路。
4. 通过 schema validator 检查字段完整性。
5. 通过人工复核确认关键指标、工具、参数、失败/修正链路和证据链接。

为支持后续扩展，仓库提供 `scripts/collect_openalex_candidates.py`，用于收集开放获取论文的候选元数据；该脚本只保存题名、DOI、开放获取状态、许可信息和 OA 链接，不下载全文。评测任务由 `scripts/build_eval_tasks.py` 从 gold case 自动生成。

## 6. 质量控制

本项目的质量控制分为四层：

- Schema 完整性：所有样本必须通过 `scripts/validate_dataset.py`。
- 证据覆盖：每个轨迹步骤必须至少有一个来源证据。
- 科学一致性：关键指标、工具名、实验结果不得脱离原文证据。
- 许可合规：每个来源记录 `license_status`，公开发布前必须完成许可复核。

此外，仓库增加了两个面向提交冲刺的自动检查：

- `scripts/vet_candidate_sources.py`：把 OpenAlex 候选元数据转换为“可安全本地处理 / 需人工复核 / 暂缓处理”的来源队列，避免在许可不清晰时直接抓取全文。
- `scripts/check_submission_readiness.py`：统一检查 gold case 数量、评测任务、质量报告、MinerU 说明、关键文档和 Git 工作区状态，并生成 `reports/SUBMISSION_READINESS.md`。

## 7. 应用场景

数据集可用于：

- 科学智能体轨迹学习。
- 科研工具调用决策训练。
- 实验失败分析与下一步方案生成。
- 蛋白设计/酶工程领域的 AI4S 推理评测。
- 从论文到结构化科研知识库的自动化抽取任务。

## 8. 当前版本说明

版本 `0.1.0` 是可提交底座版本，包含：

- 3 条 gold case（1 条赛事样例 + 2 条 CC-BY 开放论文案例）。
- 1 套 Sci-Evo case schema。
- 1 个构建脚本。
- 1 个验证脚本。
- 1 个质量报告生成脚本。
- 1 个评测任务生成脚本。
- 1 个开放论文候选收集脚本。
- 1 个开放来源许可筛选脚本。
- 1 个提交就绪检查脚本。
- 提交 README、技术报告和录屏脚本骨架。

## 9. 与评分维度的对应

- 数据价值与任务契合度：聚焦 Sci-Evo，而不是静态 QA；每条样本记录真实科研演化链路。
- 数据质量：要求 schema 校验、逐步证据、最终验证字段和人工 gold 标注。
- 工程完整度：提供数据构建、校验、评测任务生成、质量报告和提交就绪检查。
- MinerU 使用深度：保留 Markdown、content list、layout 等本地解析产物，并把样本字段映射回页面与块级证据。
- 可扩展与可复核性：通过开放来源候选收集、许可筛选队列和多 case 构建路径支持后续规模化扩展。

## 10. 当前阻塞与下一步

当前版本已经达到“至少 3 条完整 gold case”的基础提交门槛。剩余阻塞主要是提交打包而不是数据结构本身。下一步优先顺序是：

1. 在最终提交前用 `git status --short` 确认工作区干净，并保留明确提交记录。
2. 如需进一步冲击更高排名，从 `reports/VETTED_SOURCE_QUEUE.md` 继续扩展更多 `permitted_for_local_processing` 的开放论文。
3. 对新增开放论文使用 `scripts/mineru_parse.py` 和 token 文件补齐本地 MinerU 解析产物。
4. 重新生成数据集、评测任务、质量报告和提交就绪报告，并导出最终技术报告/PDF。

# MinerU 运行报告

## 概要

- 输入文件：`Sci-Evo-Sample.pdf`、`SELT-PROT-0002.pdf`、`SELT-PROT-0003.pdf`、`SELT-PROT-0004.pdf`、`SELT-PROT-0005.pdf`
- API 模式：MinerU batch API
- 模型版本：`vlm`
- 公式解析：已开启
- 表格解析：已开启
- 最终状态：`done`
- 本地输出目录：`data/interim/mineru/`

## 本地生成产物

通用批处理产物：

- `batch_create_response.json`
- `batch_status.json`
- `downloads/*.zip`
- `extracted*/full.md`
- `extracted*/*_content_list.json`
- `extracted*/*_content_list_v2.json`
- `extracted*/layout.json`
- `extracted*/*_model.json`
- `extracted*/images/`

逐 case 归一化产物：

- `Sci-Evo-Sample/full.md`
- `Sci-Evo-Sample/content_list.json`
- `Sci-Evo-Sample/content_list_v2.json`
- `Sci-Evo-Sample/layout.json`
- `Sci-Evo-Sample/model.json`
- `SELT-PROT-0002/full.md`
- `SELT-PROT-0002/content_list.json`
- `SELT-PROT-0002/content_list_v2.json`
- `SELT-PROT-0002/layout.json`
- `SELT-PROT-0002/model.json`
- `SELT-PROT-0003/full.md`
- `SELT-PROT-0003/content_list.json`
- `SELT-PROT-0003/content_list_v2.json`
- `SELT-PROT-0003/layout.json`
- `SELT-PROT-0003/model.json`
- `SELT-PROT-0004/full.md`
- `SELT-PROT-0004/content_list.json`
- `SELT-PROT-0004/content_list_v2.json`
- `SELT-PROT-0004/layout.json`
- `SELT-PROT-0004/model.json`
- `SELT-PROT-0005/full.md`
- `SELT-PROT-0005/content_list.json`
- `SELT-PROT-0005/content_list_v2.json`
- `SELT-PROT-0005/layout.json`
- `SELT-PROT-0005/model.json`

## 用途说明

MinerU 输出用于三类工作：

1. 将论文 PDF 转换为可检索 Markdown 和 content list，便于定位科研目标、实验步骤和关键指标。
2. 为 `evidence` 字段提供页面、段落、图表和方法位置依据。
3. 支撑人工复核，避免只根据摘要生成 Sci-Evo 轨迹。

## 公开发布说明

完整 MinerU 输出保留在本地，用于材料整理和复核。公开 GitHub 仓库不提交全文级解析产物、PDF、图片 zip 或 API token；公开仓库只保留派生结构化数据、运行报告和可复现脚本。赛事样例来源仍保留许可复核标记，开放论文 case 记录了对应的 CC-BY 来源许可状态。

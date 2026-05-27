# 数据集卡片：Sci-Evo-LabTrace

## 数据类型

Sci-Evo 科学演化数据。

## 覆盖领域

蛋白设计、酶工程、合成生物学、生物催化、生物发光、抗体工程、蛋白语言模型、工业生物制造和酵母分泌工程。

## 预期用途

- 训练 AI4S 智能体理解真实科研轨迹。
- 评测模型在科研过程中的下一步决策能力。
- 研究计算设计、湿实验验证和优化循环中的工具调用推理。
- 构建可追溯的科研过程知识库。

## 数据格式

JSON Lines。每一行是一条完整科学演化 case。

## 标注等级

当前版本包含 5 条 gold curated case、29 个科研轨迹步骤和 63 条自动生成评测任务，并可继续扩展 silver 自动抽取样本。

## 来源与溯源

种子样例来自赛事提供的 Sci-Evo 样例 PDF 与 JSON；新增 case 来自开放获取论文，并在数据中记录来源、许可状态和证据字段。公开发布前仍需逐条确认源材料许可，全文 PDF、图片和 MinerU 全量解析产物不进入公开仓库。

## 质量信号

- 必须通过 schema 校验。
- 每个轨迹步骤必须具备证据指针。
- 显式记录 `curation_level`。
- 显式记录来源许可状态与是否需要许可复核。
- 提供评测任务和完整性检查。

## 局限性

当前版本已经超过基础完整度门槛，但仍属于冲刺版本。若要进一步提高竞争力，建议继续沿 `reports/VETTED_SOURCE_QUEUE.md` 扩展更多开放许可论文，并为每条新增 case 补齐 MinerU 本地解析产物。

## 扩展入口

- 来源筛选队列：`reports/VETTED_SOURCE_QUEUE.md`
- 完整性检查报告：`reports/SUBMISSION_READINESS.md`
- 标注规范：`docs/ANNOTATION_GUIDELINES.md`
- 深度审计：`reports/CASE_DEPTH_AUDIT.md`
- 下一步安全操作：只下载许可信息明确允许本地处理的 PDF，并通过 MinerU 解析后再人工复核成 gold case。

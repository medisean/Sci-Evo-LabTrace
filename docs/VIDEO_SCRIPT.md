# 录屏讲稿

时长建议：3-5 分钟。

## 1. 开场

大家好，我们的项目是 Sci-Evo-LabTrace，一个面向科学智能体的科研演化轨迹数据集。它属于 Sci-Evo 类型，重点不是静态知识问答，而是真实科研过程中的多步推理、实验决策、失败修正和最终验证。

## 2. 为什么选择这个方向

我们聚焦蛋白设计和酶工程，因为这一类研究天然包含计算设计、湿实验筛选、指标评估和迭代优化，非常适合构建科学演化数据。模型可以从中学习科学家如何提出目标、选择工具、调整方案并验证结果。

## 3. 数据结构展示

这里展示一条样例 case。它包含初始科研需求、逐步 agent trajectory 和最终 success verification。每一步都有 action、tool、parameters、observation 和 evidence 字段，可以回溯到原始论文页面或 MinerU 解析块。

## 4. MinerU 使用

我们使用 MinerU 对科学 PDF 进行结构化解析，保留 Markdown、content list、图表和页面级信息。后续 Sci-Evo 字段通过 evidence 字段与 MinerU 解析结果建立映射，保证数据可追溯、可复核。

## 5. 工程与质量控制

仓库提供构建脚本、验证脚本和提交就绪检查。运行 `python3 scripts/build_dataset.py` 可以生成 JSONL 数据集，运行 `python3 scripts/validate_dataset.py data/processed/scievo_gold.jsonl` 可以检查字段完整性和轨迹一致性，运行 `python3 scripts/check_submission_readiness.py` 可以统一检查样本数、文档、质量报告、MinerU 记录和 Git 状态。

## 6. 当前冲刺状态

当前版本已经具备完整提交流程骨架，并给出开放来源筛选队列。但它还不是最终第一名版本，因为目前只有 1 条完整 gold case。下一步是按 `reports/VETTED_SOURCE_QUEUE.md` 优先级下载具备明确开放许可的 PDF，使用 MinerU 解析，并扩展到多条高质量案例。

## 7. 结尾

Sci-Evo-LabTrace 的目标是让大模型不仅知道科学结论，还能学习科学探索过程。后续数据集可以扩展到更多蛋白设计、药物发现和材料优化案例，并作为科学智能体训练和评测的基础数据。

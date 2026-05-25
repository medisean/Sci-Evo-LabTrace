# 提交清单

## 必交

- [ ] 开源数据集链接。
- [ ] 明确说明数据类型为 Sci-Evo。
- [ ] 数据文件：`data/processed/scievo_gold.jsonl`。
- [ ] 技术报告：`docs/TECHNICAL_REPORT.md` 或导出 PDF/DOCX。
- [ ] 数据结构说明：`schemas/scievo_case.schema.json`。
- [ ] 数据构建代码：`scripts/`。
- [ ] MinerU 使用说明与解析产物样例。
- [ ] 原始数据样例：`Sci-Evo-Sample.pdf` 和/或开放许可 PDF 样例。
- [ ] 合规、安全、伦理与许可说明。

## 加分项

- [ ] GitHub 仓库链接。
- [ ] OpenDataLab 数据集链接。
- [ ] PPT。
- [ ] 3-5 分钟录屏。
- [ ] 质量报告：`reports/QUALITY_REPORT.md`。
- [ ] 评测任务：`data/processed/scievo_eval_tasks.jsonl`。
- [ ] 扩展版 gold cases。
- [ ] 简单 benchmark/evaluation tasks。

## 截止前最终检查

- [ ] `python3 scripts/build_dataset.py` 成功。
- [ ] `python3 scripts/validate_dataset.py data/processed/scievo_gold.jsonl` 成功。
- [ ] `python3 scripts/build_eval_tasks.py` 成功。
- [ ] README 中能讲清楚数据集用途。
- [ ] 技术报告中能对应五个评分维度。
- [ ] 不提交 `mineru-api-token.txt`。
- [ ] 不发布未确认许可的全文或图片资源。

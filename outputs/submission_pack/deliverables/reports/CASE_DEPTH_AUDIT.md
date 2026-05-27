# Gold Case 深度审计

## 总体结论

当前数据集包含 5 条 gold case、29 个科研轨迹步骤和 63 条自动生成评测任务。主题集中在 AI/ML 驱动的蛋白与酶工程，边界清晰，适合以“高质量科研演化轨迹”而不是“大而散的论文抽取集”作为参赛定位。

5 条 gold case 均已绑定来源证据；对应 PDF 均已完成本地 MinerU API 解析。公开仓库不提交全文级解析产物，但本地提交包可保留运行记录和解析结果。

## Case 1：从头设计人工荧光素酶

- Case ID：`SELT-PROT-0001`
- 子方向：从头蛋白设计、酶工程、生物发光、合成生物学
- 轨迹深度：7 步
- 核心闭环：scaffold 生成 → 活性位点安装 → 序列优化 → 大肠杆菌筛选 → 新底物扩展 → 位点饱和突变 → 哺乳动物细胞验证
- 质量亮点：干实验与湿实验交替清晰，最终指标包含分子量、热稳定性、催化效率和底物特异性。
- 当前风险：来源为赛事样例包，公开发布全文或解析产物前仍需确认许可。

## Case 2：机器学习辅助组合文库设计

- Case ID：`SELT-PROT-0002`
- 子方向：机器学习文库设计、酶工程、生物催化
- 轨迹深度：5 步
- 核心闭环：结构引导位点选择 → MODIFY 文库设计 → 双反应实验筛选 → 命中体排序 → 分子动力学机制解释
- 质量亮点：体现了模型如何平衡 fitness 与 diversity，并通过实验筛选验证文库质量。
- 当前风险：应在最终提交包中说明 CC-BY 来源和 MinerU 本地解析路径。

## Case 3：定向进化复盘与 ensemble-based 再设计

- Case ID：`SELT-PROT-0003`
- 子方向：定向进化、结构生物学、计算蛋白设计
- 轨迹深度：5 步
- 核心闭环：进化轨迹审计 → 室温晶体结构测量 → 构象机制推断 → 结构引导突变再设计 → ensemble 模型比较
- 质量亮点：最贴近 Sci-Evo 的“科学如何演化”定义，直接记录从实验进化中抽取机制，再反馈到计算设计的过程。
- 当前风险：部分字段仍保留英文科学原文；这是为了保留论文语义和术语精度，不影响中文提交文档。

## Case 4：Pro-PRIME 工业抗碱 VHH 抗体优化

- Case ID：`SELT-PROT-0004`
- 子方向：蛋白语言模型、抗体工程、工业生物制造、极端环境耐受性
- 轨迹深度：6 步
- 核心闭环：工业目标定义 → Pro-PRIME 零样本单点突变筛选 → 45 个单点突变湿实验验证 → 基于单点数据微调模型并设计 20 个多点突变 → epistasis 与 MD 机制分析 → 动态结合容量和工业纯化循环验证
- 质量亮点：这是当前数据集中最强的“AI 设计 - 实验反馈 - 模型微调 - 工业验证”闭环；最终指标包括 65 个突变体、67.7% 抗碱提升、10.02 C Tm 提升、zero-shot 多点预测失败对照和生产线验证。
- 当前风险：eLife 版本记录需要在最终提交材料中明确使用的 PDF/DOI 版本；公开仓库只保留派生结构化数据，不提交全文解析。

## Case 5：alpha-factor 分泌信号工程

- Case ID：`SELT-PROT-0005`
- 子方向：定向进化、酵母分泌、信号肽设计、酶生产
- 轨迹深度：6 步
- 核心闭环：alpha9H2 与 native leader 基准比较 → 13 个单点突变 bottom-up 扫描 → 组合突变与 1600 克隆重组筛选 → top-down 回退简化 → 跨氧化还原酶和水解酶泛化验证 → 86/87 位点 CSM 目标特异调优规则
- 质量亮点：不是 AI case，但能补足 Sci-Evo 对“演化轨迹拆解、组合 epistasis、跨目标泛化和可复用规则”的要求，避免数据集只像单一模型广告。
- 当前风险：与主线的 AI/ML 强相关性弱于其他 case；定位应作为“定向进化与工程优化基线 case”，而不是核心卖点。

## 当前覆盖的子方向

- 从头蛋白/酶设计：`SELT-PROT-0001`
- ML-guided combinatorial library design：`SELT-PROT-0002`
- Directed evolution trajectory audit + ensemble redesign：`SELT-PROT-0003`
- Protein language model + wet-lab feedback + industrial validation：`SELT-PROT-0004`
- Signal peptide / secretion engineering via bottom-up and top-down evolution analysis：`SELT-PROT-0005`

## 深化建议

若继续增强，优先把同主题 gold case 扩到 8-10 条，而不是跨到材料、物理或药物发现。推荐扩展方向：

- 蛋白语言模型生成 functional protein sequences。
- Bayesian optimization + robotic experiments 的蛋白工程。
- 抗体 CDR inverse folding 设计。
- AI 辅助工业酶耐受性优化。
- de novo peptide/protein binder 设计。

## 当前是否够提交

够提交，而且已经超过基础门槛。若目标是更稳地冲击第一名，当前最有效的提升不是堆大量低质量 gold case，而是继续增加 3-5 条与 `SELT-PROT-0004` 同等级的强闭环案例，并保持每条都有证据页码、MinerU 记录、失败/对照信息和最终验证指标。

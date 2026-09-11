# 开发流程

产品目标 → PRD（含适用的预计变化场景）→ 质询 → SRS → 架构（Stable Core / Variation Point）→ ADR → 详细设计（变化局限边界）→ 测试设计（替换性 / 兼容性）→ 编码 → 独立评审（含适用的 Change Amplification）→ 自动验证 → 真实验证 → 反馈登记 / Bug / 变更闭环 → 发布。

大型项目可以在架构边界明确后递归分解为 Governed Subproject、Module 和 Work Package。叶子任务分别实现和验证，子级以精确 Acceptance Package 向上交付，父级聚焦接口、集成、系统 Acceptance 和组合风险；不得要求一个 Session 加载全部子级实现细节。

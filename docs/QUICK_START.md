# 快速开始

## 前置条件

- Git；
- 能够读取和编辑仓库文件的编码 Agent 或 Harness；
- 仅在运行随附的追溯或治理校验器时需要 Python 3；只有启用可选 APLS 并构建其编译器时才需要 Rust 1.86。

长程智构不要求使用特定模型厂商。

## Full Template 设置

1. 将完整发布 Archive 复制或解压到目标项目根目录。
2. 如果目标是已有项目，不要覆盖冲突文件；先遵循 `AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md`。
3. 替换 `{{PROJECT_NAME}}`、日期、Gate 以及与项目相关的其他占位符。
4. 在 `00_project/ai_context/PROJECT_STRUCTURE_MAP.md` 选择 `SINGLE_PROJECT / MODULAR_PROJECT / FEDERATED_PROJECT`；既有未拆分项目选择 `SINGLE_PROJECT`，不制造 Child 记录。
5. 在 `00_project/ai_context/CURRENT_STATE.md` 中配置当前阶段、授权、`AUTONOMY_MODE`、必要的 Model/Runtime/Harness 槽位、`AUTHORIZED_UNTIL`、`PREAUTHORIZED_GATES` 和 `BEHAVIOR_SPECIFICATION_MODE`。
6. 普通本地、低风险、单 Session 任务不要求建立 Dynamic Role Profile、Knowledge Manifest 或完整 Interaction / Authorization Contract。只有触发高风险、跨 Session、正式 C04、受控副作用、并行写入，或 Human Project Owner 明确选择时，才按 `ROLE_INTERACTION_EXECUTION_POLICY.md` 实例化对应控制。
7. 如有需要，初始化 Git，并在开始实现前建立稳定锚点。
8. 将 `PROJECT_START_PROMPT.md` 交给当前 Agent。
9. 新项目从 C00/C01 开始，在进入架构或实现前先建立产品需求。
10. 需要项目负责人决定时，按 `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md` 先解释再请求决定；收到尚未分类的反馈时，先登记到 `12_issues/feedback/FEEDBACK_REGISTER.md`。
11. Agent 只完整读取最小 `AI_START_HERE.md`，随后通过 `GOVERNANCE_ROUTER.yaml` 和 Domain INDEX 按需加载规则；不要把全部治理文件默认装入上下文。
12. 当前变化命中适用 Locked Invariant、既有 Guard 或目标 Manifest 强制项时，运行 `python3 09_quality/non_regression/validate_non_regression.py`；退出码 `1` 表示 Invariant 违反，退出码 `2` 表示证据无效。未命中时不要扩大全量历史检查。

## 可选 APLS 行为规格

项目需要以可验证的声明式行为规格驱动设计时，将 `BEHAVIOR_SPECIFICATION_MODE` 明确改为 `APLS_ENABLED`。C02 随后从 `optional/apls/README.md` 按需加载随框架固定的说明书和编译器，并按 `00_project/governance/integrations/apls/APLS_DESIGN_ALLOCATION_POLICY.md` 分配 APLS、Detailed Design、Algorithm Spec 和 Target Profile。默认 `DOCUMENT_BASED` 不读取、构建或运行 APLS。

## 大型项目与并行写入

1. 先按稳定边界决定使用同一项目内 Module，还是建立独立 Governed Subproject；不得只按文件数量拆分。
2. 将写入工作拆到 `LEAF_EXECUTION / INTEGRATION` Work Package，并为每项定义一个 Output Contract。
3. 每个活动 Writer 绑定一个独立 Git Worktree 和 Branch；同一 Local Working Directory 同时只能有一个 Writer。
4. 写入范围重叠或共享接口未冻结时改为串行，或先完成上游合同并建立 Integration Work Package。
5. Child 完成后返回精确 Commit、验证和独立评审证据；Parent 通过 Child Acceptance Package 与 System Integration Manifest 组合验收。
6. 上下文过长时只交接当前未完成 Leaf / Integration Work Package，并一次转移 Write Lease。

## Lite 设置

复制 `docs/FULL_VS_LITE.md` 中列出的 Lite 文件集。所有选中文件都应保留原始路径，以确保交叉引用和事实所有权仍然有效。

最低要求：

1. 配置 `CURRENT_STATE.md`；
2. 建立当前决策和 Baseline 引用；
3. 创建一个活动任务；
4. 选择当前 C00～C06 Role；只有命中触发条件或负责人选择时才建立 Dynamic Role Profile / Knowledge Manifest；
5. 只有受控跨 Role / 跨 Session 交互或副作用动作命中要求时才绑定 Interaction / Authorization；
6. 默认可使用 `PROCEDURAL_FALLBACK`；需要机械执行时再选择 `TOOL_ENFORCED`；
7. 正式 C04 评审时使用全新、独立的 Session 并记录独立性证据；
8. 切换 Model、Runtime、Harness 或物理上下文时执行 Knowledge Continuation Check；不满足条件时执行 Baseline Relearn。
9. 配置 `PROJECT_STRUCTURE_MAP.md`；如并行写入，为每个活动任务记录 Output Contract、Worktree、Branch 和 Write Lease。

## 五分钟核验

- Agent 能说明当前 Role、适用 Gate、必要事实 Owner、授权和下一项任务；若 Dynamic Role Profile 未触发，可以明确说明 `NOT_APPLICABLE`。
- Agent 能说明本任务命中的 Router 路径、实际加载规则和明确排除范围。
- 每个动态事实只有一个所有者文件。
- 当前 Model/Runtime/Harness 路由和 Enforcement Mode 只存在于 `CURRENT_STATE.md`。
- 实际命中的受控副作用动作有精确 Interaction / Authorization，且 Action Class 不互相隐含。
- Review Target 是精确的 Git Target。
- 正式 C04 有独立 Session 证据，不能修改被评审对象，也不能关闭自己的 Finding。
- 人类审批边界和说明内容明确，不能只问“是否批准”。
- 反馈先登记再分类，FB 当前状态只有一个 Owner。
- 已批准 ETC 变化场景能够追溯到 Stable Core / Variation Point、局限设计和替换性/兼容性证据。
- 多 Session、分解任务或并行写入命中控制时，每个写入 Session 只对应一个活动 Leaf / Integration Work Package 和一个 Output Contract；同一 Worktree 只有一个 Writer。
- Parent 接受 Child 时能核验精确 Commit、未过期 Acceptance Package、独立 Review Evidence 和系统集成证据，而不是依赖聊天摘要。
- 当前变化命中的 Locked Invariant、Regression Guard 和运行证据可以从唯一 Contract 与质量/Review 记录中定位；未命中时不要求建立空记录。

如果影响当前任务、关键权限或 Gate 的答案不清楚，请停留在 C00 解决；其他实际发现的问题先登记，可由正确 Owner 决定是否延期、忽略或后续处理。

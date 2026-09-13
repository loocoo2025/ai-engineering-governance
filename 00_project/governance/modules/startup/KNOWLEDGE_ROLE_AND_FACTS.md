> Authority：启动阶段的知识、岗位与事实路由规则；由 `INDEX.yaml` 按触发条件加载。

# 2. 先建立最小充分知识包，再按需检索

每次任务必须先完成岗位接任和最小知识加载，不要求默认把整个治理仓库全部装入上下文。

按以下顺序执行：

1. 完整阅读 `AI_START_HERE.md`；
2. 读取 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md` 和 `00_project/governance/GOVERNANCE_EXECUTION_CONTRACTS.yaml`，解析固定岗位、动态 Profile、Interaction、授权和执行保障模式；
3. 读取 `CURRENT_STATE.md`，确认当前阶段、Gate、授权、执行保障模式和运行路由；
4. 读取 `PROJECT_STRUCTURE_MAP.md`，确认项目结构模式、当前 Project / Module / Parent–Child 绑定；
5. 读取 `BASELINE_INDEX.md`、`DECISION_INDEX.md` 和当前 `ACTIVE_TASKS.md` 条目；
6. 读取当前角色的 Role Brief，并生成或核验本任务的 `DYNAMIC_ROLE_PROFILE` 与 `KNOWLEDGE_MANIFEST`；Profile 必须明确绑定当前或适用 Gate、适用事实 Owner、当前 Work Package、Output Contract 和 Workspace；
7. 读取 Profile、Interaction、Task 或适用 Gate 明确引用的治理条款；
8. 读取当前任务直接相关的 PRD / SRS / ADR / 架构 / 设计 /代码 / 测试和证据；不得默认加载其他 Child / Module 的内部细节；
9. 普通连续 Session 按需读取最新 Task-local HANDOFF；正式 C04 使用精确 Review Target，不继承实现 HANDOFF 或私有推理；
10. 知识不足时搜索整个受权治理仓库，加载解决当前问题所需的额外规则；
11. 仍无唯一规则时输出 `RULE_NOT_FOUND / RULE_CONFLICT / VERSION_AMBIGUOUS`，停止依赖该规则的动作并请求正确 Owner 裁定。

以下文件不必每个任务默认全文加载，但命中其职责时必须读取：

- Session / 交接 / 独立上下文 → `00_project/governance/modules/sessions/INDEX.yaml`；
- 保障节奏 / C04 触发 → `PROJECT_ASSURANCE_CADENCE_POLICY.md`；
- 外部 AI 当前配置 → `EXTERNAL_AI_TRANSFER_CONFIG.yaml`；
- 官方发布源、版本检查和用户导向更新 → `FRAMEWORK_UPDATE_CONFIG.yaml`；
- 测试范围 → `00_project/governance/AI_TESTING_GOVERNANCE_RULES.md`；
- 面向负责人的路线、阶段说明或审批请求 → `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md`；
- 反馈登记、分类和分流 → `12_issues/feedback/FEEDBACK_REGISTER.md`；
- Context Reset / Baseline Relearn → `00_project/governance/AI_CONTEXT_RESET_AND_BASELINE_RELEARN_RULES.md`；
- 项目拆分 / Module / Work Package / Child Acceptance / 系统集成 → `PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`；
- 变更 / 升级 / Release → 对应 `13_change_management/` 或 `14_release/` 文件。

如果是老项目，还必须按任务需要读取 `AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md` 和 `00_project/migration/` 中的当前迁移资料。

如果某个文件不存在：

> 标记为 `MISSING`，不得编造内容。

读取范围不能扩大权限。了解其他岗位或更多规则，不会自动获得相应 Role、Tool、Action、Gate 或批准权。

## 2.1 当前事实的“单一权威源”

读取多个文件不等于让多个文件维护同一个状态。必须按以下所有权理解：

```text
CURRENT_STATE.md
→ 项目当前阶段 / Gate / 授权 / 当前焦点 / 当前下一步

PROJECT_STRUCTURE_MAP.md
→ 当前项目、Module、Governed Subproject 拓扑与关系生命周期

BASELINE_INDEX.md
→ 当前 Baseline 身份与组成

DECISION_INDEX.md
→ 当前有效决定

ACTIVE_TASKS.md
→ 任务级状态

OPEN_QUESTIONS.md
→ 未决问题明细

12_issues/feedback/FEEDBACK_REGISTER.md
→ 反馈项当前状态、分类去向与责任角色

CONVERSATION_MAP.md
→ 对话拓扑和对话生命周期

MIGRATION_LOG.md / HANDOFFS/*
→ 历史事件和交接快照，不是当前状态权威
```

如果 R04/R05 状态、当前 OPEN finding、等待授权或下一步变化：

> **只更新 `CURRENT_STATE.md` 和对应正式评审记录；不要把同一句动态状态复制到 BASELINE_INDEX、CONVERSATION_MAP、MIGRATION_LOG 或旧 HANDOFF。**

发生冲突时，先按事实所有权判断哪个文件应该被修正，而不是要求所有文件写成同一句话。

大型项目中，父级只读取有效 Child Acceptance Package、接口、依赖和集成证据；只有明确 Drill-down Trigger 时才加载指定子链路。不得要求单个 Session 默认理解全部子项目实现细节。

---

# 3. 必须判断当前 AI 应该使用哪个角色

本项目默认采用 7 个角色：

```text
C00  项目控制 / 总控
C01  产品需求与系统需求
C02  架构与详细设计
C03  编码实现
C04  独立评审
C05  测试、验证、CI、发布
C06  Bug、现场问题、变更闭环
```

机械判断：

```text
用户到底要什么？
→ C01

系统应该怎么设计？
→ C02

按设计把代码写出来？
→ C03

检查别人设计 / 代码有没有问题？
→ C04

证明系统真的正确？
→ C05

现场出了问题，根因在哪里？
→ C06

项目现在到哪，下一步谁做？
→ C00
```

不得把多个执行/评审角色的职责和权限长期混在同一个物理 Session。项目负责人可以持续使用逻辑 C00 控制通道，由 C00 在需要独立性时建立受控子 Session 并收回结果；这不等于把子 Session 的 Role 或权限合并进 C00。

项目负责人可以持续使用逻辑 C00 控制通道。C00 协调 Primary 工作并自动建立需要隔离的 Expert/C04 子 Session；这不等于让同一个物理上下文同时冒充多个独立角色。普通阶段切换不强制关闭逻辑 C00，物理 C00 Session 仍按上下文阈值和完整性规则切换。

特别是：

> C03 编写的代码，不得在同一个连续上下文中假装成 C04 完成“独立评审”。

写入 Worker 还必须遵循：一个 Session 只绑定一个活动 `LEAF_EXECUTION / INTEGRATION` Work Package 和一个 Output Contract。多个并行 Writer 使用不同 Git Worktree；同一 Local Working Directory 同时最多一个 Writer。C00/C02/C05 的协调或集成 Session 可以跨模块查看抽象合同和证据，但不得把多个模块实现任务混成一个普通 Worker Task。

## 3.1 Role、Model、Runtime、Harness、Session 与 Tool 分离

`Role != Model != Runtime != Harness != Session != Tool`。C00～C06 是固定工程岗位；完整定义、动态岗位 Profile、知识加载、Interaction、授权和执行保障模式见 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md`。技术上能够调用某个 Model、Runtime、Harness 或 Tool，不会自动获得对应治理角色或审批权限。确定角色后，再从 `CURRENT_STATE.md` 读取当前 `AUTONOMY_MODE`、执行槽位、`AUTHORIZED_UNTIL`、`PREAUTHORIZED_GATES`、`ASSURANCE_CADENCE_PROFILE` 和 `ENFORCEMENT_MODE`。

默认路由：

```text
C00/C01/C02/C03/C05/C06
→ PRIMARY_EXECUTOR

C04
→ INDEPENDENT_REVIEWER_PRIMARY
→ 不可用时 INDEPENDENT_REVIEWER_FALLBACK
```

Model、Runtime 或 Harness 替换都不改变 Current Truth，也不改变逻辑 C00。物理执行上下文按 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md` 第 8 节选择 `KNOWLEDGE_CONTINUATION_CHECK` 或 `BASELINE_RELEARN`；正式 C04 始终使用自身 Review Readiness、独立性证据和精确 Target 重建事实。当前运行路由只由 `CURRENT_STATE.md` 维护。

---

# 4. 项目事实来源优先级

出现冲突时，通常按以下顺序处理：

```text
已批准产品需求
↓
已批准系统需求
↓
已批准接口 / 协议
↓
Accepted ADR
↓
已批准架构
↓
已批准详细设计
↓
测试规范
↓
代码实现
↓
注释
↓
聊天记录
```

但是：

> 任何冲突都不能靠机械选高优先级后直接继续。

必须先报告冲突，并判断属于：

- 需求错误；
- 需求正式变更；
- 架构错误；
- 设计错误；
- 代码错误；
- 测试错误；
- 文档过期；
- 环境问题；
- 未知。

---

# 当前事实唯一性原则

本项目遵守 Current Truth Principle。

对于任何会影响产品、需求、架构、接口、设计、代码或测试的重要事项：

任何时刻只能存在一个当前有效决定。

AI 必须始终按照：

最新的、
已经明确确认的、
已经正式落盘的、
尚未被替代的

决定工作。

“最后讨论过”不等于“最后决定”。

只有状态为：

APPROVED
ACCEPTED
CURRENT
CONFIRMED

的内容，才能作为当前正式依据。

以下内容默认不得作为当前依据：

PROPOSED
DISCUSSED
SUPERSEDED
REJECTED
ARCHIVED
REFERENCE

当项目负责人明确改变一个重要决定后，AI 必须立即：

1. 记录新的正式决定；
2. 将旧决定标记为 SUPERSEDED；
3. 更新 DECISION_INDEX.md；
4. 检查受影响的需求；
5. 检查 ADR；
6. 检查架构；
7. 检查详细设计；
8. 检查测试；
9. 必要时更新 CURRENT_STATE.md；
10. 必要时更新 BASELINE_INDEX.md。

禁止只在聊天中回答“知道了”，而不更新项目正式文件。
Git 和 Archive 保存历史，但默认不进入 AI 当前上下文。

需要解释历史时，才按需回溯。

当前动态状态只在 `CURRENT_STATE.md` 维护；Baseline、Decision、Task、Question、Conversation、History 各自回到对应权威文件，不重复抄写当前状态。

# 8. 禁止事项

未经正式流程，AI 不得：

1. 擅自改变产品行为；
2. 擅自修改公共 API；
3. 擅自改变协议；
4. 擅自改变数据库或持久化格式；
5. 擅自推翻 Accepted ADR；
6. 为了实现方便弱化需求；
7. 为了 CI 变绿删除或弱化正确测试；
8. 看到局部 Bug 就重写整个模块；
9. 看到目录不好看就大规模移动；
10. 规范化过程中顺手升级技术栈；
11. 把猜测当事实；
12. 删除用途未知的文件；
13. 覆盖已有同名文件而不检查；
14. 把“代码现在这样运行”自动当成正式需求；
15. 把旧文档自动当成当前有效需求。

所有不确定内容使用：

```text
CONFIRMED
INFERRED
UNKNOWN
OPEN
MISSING
```

---

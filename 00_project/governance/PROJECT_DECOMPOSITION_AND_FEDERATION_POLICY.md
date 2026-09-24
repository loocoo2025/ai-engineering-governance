# 项目分解、模块化与联邦治理策略

> 本文件是项目结构模式、递归分解、父子项目事实边界、分层接受证据和系统集成汇总的唯一稳定权威来源。
>
> 本文件不重新定义 Task 状态、Session/Worktree 编排、C04 Decision、Testing Governance、Current Truth、Baseline 或 Release Gate。

---

## 0. 事实所有权与引用边界

```text
项目结构模式、分解层级、父子项目事实边界、分层接受和集成语义
→ 本文件

当前项目/模块/子项目拓扑和关系生命周期
→ 00_project/ai_context/PROJECT_STRUCTURE_MAP.md

任务、Work Package、Output Contract、Write Lease 当前绑定与状态
→ 00_project/ai_context/ACTIVE_TASKS.md

Session、Worktree、单写入者、交接和结果返回
→ modules/sessions/WORKTREE_WRITE_LEASE_AND_RETURN.md

当前项目阶段、Gate、授权和执行焦点
→ 00_project/ai_context/CURRENT_STATE.md

当前 Baseline 及其子项目精确版本组合
→ 00_project/ai_context/BASELINE_INDEX.md

正式 C04 触发、Readiness、Finding 和 Decision
→ PROJECT_ASSURANCE_CADENCE_POLICY.md / modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md

测试范围与系统集成验证
→ AI_TESTING_GOVERNANCE_RULES.md
```

项目分解不创建新的产品事实 Owner，也不能通过复制父项目事实建立多个 Current Truth。

---

## 1. 支持的项目结构模式

每个项目必须在 `PROJECT_STRUCTURE_MAP.md` 选择一种模式：

```text
SINGLE_PROJECT
MODULAR_PROJECT
FEDERATED_PROJECT
```

- `SINGLE_PROJECT`：一个治理项目，不建立正式模块/子项目层级；
- `MODULAR_PROJECT`：同一治理项目或仓库内存在多个受控 Module，共享项目级 Current Truth 和 Baseline；
- `FEDERATED_PROJECT`：Root Integration Project 管理一个或多个独立 Governed Subproject；子项目可以位于独立文件夹或独立 Git Repository，并拥有自己的治理实例、Current Truth、Baseline 和 C00～C06；
- 多级联邦允许递归出现，但每个 Parent–Child 关系都必须独立建立合同和精确证据引用。

模式可以在项目生命周期中受控改变，但涉及新的系统边界、公共接口、跨系统依赖、重大风险或事实 Owner 迁移时，必须执行影响分析并进入正确的 Human Determination。结构模式变化本身不得静默改变产品目标或 Acceptance Threshold。

---

## 2. 递归分解模型

允许的逻辑层级为：

```text
Project
└── Governed Subproject
    └── Module
        └── Work Package
            └── Sub-Work Package
                └── Leaf Work Package
```

Work Package 可以递归拆分，不规定固定深度。每层必须有唯一 ID 和父 ID；没有实际协调、事实边界或集成职责的空管理层级应合并。

只有以下两类 Work Package 可以直接成为写入执行单元：

```text
LEAF_EXECUTION
INTEGRATION
```

非叶子父包只负责：

- 目标和边界；
- 子包关系和依赖；
- 接口与版本组合；
- 接受证据汇总；
- 集成和剩余风险。

非叶子父包不得把多个子包的详细实现重新塞入一个普通 Worker Session。跨兄弟包工作必须拆成各自叶子包，并另建 `INTEGRATION` Work Package；不得把跨模块修改隐藏在任一子包中。

叶子包只有同时满足以下条件才可进入 `READY`：

```text
BOUNDARY: EXPLICIT
INPUTS: COMPLETE_OR_CONTROLLED
OUTPUT_CONTRACT: DEFINED
DEPENDENCIES: IDENTIFIED
WRITE_SCOPE: BOUNDED
VERIFICATION: DEFINED
ONE_SESSION_CAN_EXECUTE_WITH_MINIMUM_SUFFICIENT_CONTEXT: YES
```

### 2.1 上下文受限工作切片（Context-Bounded Work Slice）

工作切片是已有 Leaf / Integration Work Package 的粒度选择，不是新的任务类型、状态机或合同。普通单 Session 本地小任务仍按启动内核的条件激活原则执行，不为切片额外实例化完整 Work Package 控制。

- 一个切片以一个可验收产出为中心，包含明确输入、有限直接依赖、实现或分析、必要验证及收尾；不得仅按文件数量切断工作。
- 规划目标是在执行 Session 首次上下文压缩前完成切片。按实际可用上下文估计，考虑已有知识、必要输入、工具输出、正常返工和收尾余量；不把标称最大窗口当作日常预算。不要求精确 Token 预测或额外台账。
- 此目标不是新的 Gate；压缩本身不代表任务失败或证据失效。不得为避免压缩省略验证、隐瞒未完成项或降低接受条件。
- 预计无法完成时先停止范围扩张；能形成独立产出则进一步拆分，否则按现有上下文阈值及 Task-local Handoff 接续未完成部分，不等待上下文耗尽。
- 执行切片可止于实现、自检与评审输入就绪；正式 C04 是否需要及如何独立执行仍由保障政策决定，不要求每个切片单独 C04。
- Bounded Task 可由 Subagent 执行；启用、权限、Session 与写入隔离规则只见 `modules/sessions/WORKTREE_WRITE_LEASE_AND_RETURN.md` 第 41.7.3 节。父级只加载产出、直接接口与有效证据，按第 7 节触发条件定向下钻。

---

## 3. Execution Unit 与 Review Unit 分离

```text
EXECUTION_UNIT != REVIEW_UNIT
```

- 一个 `Leaf Work Package` 是最小写入执行单元；
- 一个 `Review Package` 可以覆盖一个或多个边界一致、版本冻结的叶子包；
- 不要求每个微小叶子任务自动执行正式 C04；
- 只有项目保障策略命中正式 C04 触发，或上层准备把子包作为正式可信输入接受时，才形成正式 C04；
- 子包 `DONE` 不等于 Review Package `PASS`，Review Package `PASS` 也不等于父包或系统 Gate 通过。

---

## 4. 父项目与子项目事实所有权

Root / Parent Project 默认负责：

- 整体产品目标和系统级需求；
- 系统边界与子项目划分；
- 跨项目接口和共享约束；
- 系统级 Acceptance Criteria / Threshold；
- 子项目精确版本组合；
- 系统集成 Baseline、系统验证和 Release。

Governed Child Project 默认负责：

- 已委派边界内的内部需求和内部决定；
- 内部架构、设计、代码和测试；
- 本地 Current Truth、Baseline、Task 和 Review Finding；
- 本地构建、验证、回滚和交付证据。

每个父子关系必须使用受控 `PARENT_CHILD_PROJECT_CONTRACT` 明确：

- Parent 提供并拥有的事实；
- Child 被委派并拥有的事实；
- Child 不得改变的接口、阈值和边界；
- 交付物、验证、Review 和返回格式；
- 变更、冲突和升级路线；
- 生效版本、精确 Git Anchor 和失效条件。

Child 只引用 Parent 的精确合同和版本，不复制后自行维护。因离线或工具限制必须携带快照时，快照必须标记 `REFERENCE_SNAPSHOT`，记录权威来源和精确 Anchor，不得成为竞争性 Owner。

---

## 5. 单项目模块与独立子项目的选择

优先保留为 `MODULAR_PROJECT` 的情况：

- 模块共享大量内部不变量或数据模型；
- 无法独立构建、测试或接受；
- 版本和发布必须始终同步；
- 拆成独立项目会增加事实副本或接口治理成本。

适合 `FEDERATED_PROJECT` 的情况：

- 子系统可以独立构建和验证；
- 存在稳定、版本化的边界合同；
- 生命周期、团队、风险或发布节奏不同；
- 单个子系统的知识范围已经需要独立治理上下文；
- Root 可以通过精确 Commit / Tag 和接受证据组合系统。

不得只按文件数量拆分项目。无法定义稳定边界、独立验收和父子事实 Owner 时，保持同一项目并先完成架构分解。

---

## 6. 子级接受包

子级向父级正式交付时必须形成 `CHILD_ACCEPTANCE_PACKAGE`。它至少绑定：

```text
CHILD_ID
SCOPE
EXACT_COMMIT_OR_TARGET
APPLICABLE_BASELINE
OUTPUTS
INTERFACE_CONTRACTS
REQUIREMENT_COVERAGE
TEST_EVIDENCE
FORMAL_C04_RECORD_AND_DECISION
OPEN_FINDINGS
APPROVED_EXCEPTIONS
RESIDUAL_RISKS
DEPENDENCY_IMPACT
ROLLBACK_ANCHOR
VALIDITY_AND_INVALIDATION
```

父级不得依赖只存在于聊天中的“已经完成”声明。任何子级 Target、接口、Baseline、适用要求或 Review Finding 状态发生实质变化时，原接受包变为 `STALE`，父级集成 Target 必须重新解析。

---

## 7. 递归、组合式评审

核心规则：

```text
PARENT_REVIEW != RE_REVIEW_ALL_CHILD_DETAILS

PARENT_REVIEW
= VALID_CHILD_ACCEPTANCE_EVIDENCE
+ INTERFACE_CONSISTENCY
+ INTEGRATION_EVIDENCE
+ SYSTEM_LEVEL_ACCEPTANCE
```

父级 Reviewer 默认检查：

1. 子接受包绑定的 Commit 是否为当前集成版本；
2. 必需的子级正式 C04 是否独立且为 `PASS`；
3. Open S0～S3 是否为 0，Exception 是否由正确 Owner 批准；
4. 输出是否满足 Parent–Child Contract 和接口版本；
5. 跨子项需求、数据、状态、错误和版本是否一致；
6. 系统级 Traceability、集成测试、Acceptance Criteria 和剩余风险是否闭合。

父级 Reviewer 默认不重新读取所有子项目代码、旧对话、实现私有推理或完整局部测试日志，也不重复已经通过且未失效的子级内部 Review。

以下事件触发定向 Drill-down，而不是全量重审：

- 子报告和集成 Commit 不一致；
- 接口、追溯、测试或独立性证据缺失；
- 集成/系统测试失败；
- 系统 Finding 指向具体子链路；
- 安全、合规、数据完整性或重大风险需要穿透检查；
- 正式抽样或专项审核有明确来源。

Drill-down 必须建立边界明确的 Review Target；不得用一个无限上下文 Session 重审全部系统细节。

---

## 8. System Integration Manifest

Root / Parent 在集成前必须形成 `SYSTEM_INTEGRATION_MANIFEST`，精确固定：

- Parent Baseline / Commit；
- 每个 Child 的 Repository / Path、Commit / Tag、Baseline 和治理版本；
- Child Acceptance Package 与 Review Record；
- 接口合同和依赖版本；
- Integration Work Package / Commit；
- 系统级构建、测试、追溯、风险和回滚证据。

缺少任一必需 Child Package、精确 Anchor 不一致、证据 `STALE` 或组合不可复现时：

```text
PARENT_REVIEW_READINESS: REVIEW_NOT_READY
```

这不是正式 Gate Decision；补齐精确 Target 后重新发起父级 C04。

---

## 9. Session、Worktree 与局部交接

所有写入执行必须遵循 `00_project/governance/modules/sessions/WORKTREE_WRITE_LEASE_AND_RETURN.md`：

```text
ONE_WRITE_SESSION
= ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE
= ONE_OUTPUT_CONTRACT
= ONE_GIT_WORKTREE
= ONE_ACTIVE_WRITER
```

其中 `ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE` 只能是 `LEAF_EXECUTION / INTEGRATION`。

上下文过长时只交接当前未完成 Leaf Work Package 的 Task-local Context。完成的子任务通过 `CHILD_ACCEPTANCE_PACKAGE` 或 Completion Capsule 向上返回，不把全部实现上下文注入 Parent Session。

Worktree 隔离不解决语义冲突。写入范围重叠、共享接口未冻结或依赖顺序不明确时，必须串行执行或先建立上游/Integration Work Package。

---

## 10. 兼容性与采用

- 既有单项目默认解释为 `SINGLE_PROJECT`，不要求追溯重写历史任务；
- 既有 Work Package ID 和状态继续有效；
- 只有新建、重新分解或并行执行的工作需要补齐新增合同；
- 将既有项目拆为多个 Governed Subproject 属于结构性治理变化，必须建立回滚 Anchor、影响分析和 Parent–Child Contract；
- 每个 Child 可以采用 Full 或 Lite，但不得关闭适用的不可关闭控制；
- Child 治理版本可以不同，Parent 必须记录版本和合同兼容性，不得假定语义相同；
- 项目分解、工作并行和子级 `PASS` 均不自动授权 Commit、Push、Merge、Baseline Adoption 或 Release。

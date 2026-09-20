> Authority：Current Truth、执行槽位、Autonomy、权限继承和正式 C04 Decision Matrix；由 `INDEX.yaml` 按触发条件加载。

# 36. Current Truth / 当前事实唯一性与决策替代规则

> 本章为本文件的增量治理规则。它不删除、不降低前文关于迭代式 V 模型、需求追溯、ADR、AI 独立评审、自动化验证、真实环境验证、Bug 闭环和 Definition of Done 的任何要求。

## 36.1 当前事实唯一性原则

对于任何会影响产品、需求、架构、接口、设计、代码或测试的重要事项，任何时刻原则上只能存在一个明确的当前有效决定。

AI 必须始终依据同时满足以下条件的决定工作：

- 最新；
- 已经明确确认；
- 已经正式落盘；
- 尚未被替代。

“最后讨论过”不等于“最后决定”。只有与文档类型相匹配的正式状态，例如 `APPROVED / ACCEPTED / CURRENT / CONFIRMED`，才能作为当前正式依据。

`PROPOSED / DISCUSSED / SUPERSEDED / REJECTED / ARCHIVED / REFERENCE / UNKNOWN / INFERRED` 默认不得作为当前实现依据。

## 36.2 用户改变重要选择后的强制动作

当项目负责人明确确认一个新决定，并且该决定替代旧决定时，AI 不得只在聊天中回答“知道了”。必须执行：

```text
确认新决定
↓
创建或更新正式决策记录
↓
新决定 → APPROVED / ACCEPTED / CURRENT / CONFIRMED
↓
旧决定 → SUPERSEDED
↓
更新 DECISION_INDEX.md
↓
检查并更新受影响的需求
↓
检查并更新 ADR
↓
检查并更新架构和详细设计
↓
检查代码影响
↓
检查并更新测试
↓
更新需求追溯
↓
必要时更新 CURRENT_STATE.md
↓
必要时更新 BASELINE_INDEX.md
```

重要决定没有正式落盘之前，不得认为变更已经完整完成。

## 36.3 禁止直接覆盖历史决定

错误：把旧决定的正文直接改成新决定，导致历史原因消失。

正确：保留旧决定并标记 `SUPERSEDED`，创建新的当前决定，并通过 `Supersedes / Superseded By` 建立关系。

示例：

```text
DEC-017
决定：无限重连
状态：SUPERSEDED
Superseded By：DEC-038

DEC-038
决定：连续失败 30 分钟后进入 Fault
状态：APPROVED
Supersedes：DEC-017
```

## 36.4 同一主题只能有一个当前有效决定

如果同一决策主题同时出现两个互相冲突的 `APPROVED / ACCEPTED / CURRENT / CONFIRMED` 记录，则视为 `DECISION-CONFLICT`。

在冲突关闭前，不得继续依据该事项进行设计、编码、测试或发布。

## 36.5 当前事实与历史事实分离

本项目遵守：

> **Git 保存过去，当前基线描述现在。**

历史必须可追溯，但以下内容默认不进入 AI 当前工作上下文：

- 旧聊天；
- 旧 HANDOFF 链；
- `SUPERSEDED` 决策；
- `SUPERSEDED` ADR；
- 旧 PRD / SRS；
- 旧架构和旧详细设计；
- Archive 中的历史资料；
- 已关闭且与当前任务无关的 Bug。

需要解释历史时，再按需读取 Git、ADR、Archive、CR、Bug 历史和旧评审记录。

## 36.6 当前事实集与事实所有权

AI 默认依赖以下文件和产物恢复当前项目事实，但这些文件**不是互相复制的三份状态表**，而是各自拥有不同事实：

```text
CURRENT_STATE.md
→ 项目级动态当前态（阶段 / Gate / 授权 / 当前焦点 / 下一步）

BASELINE_INDEX.md
→ 当前 Baseline 身份与组成

DECISION_INDEX.md
→ 当前有效决定

ACTIVE_TASKS.md
→ 任务级状态

OPEN_QUESTIONS.md
→ 未决问题明细

CONVERSATION_MAP.md
→ 对话拓扑与生命周期

MIGRATION_LOG.md / HANDOFFS/*
→ 历史事件 / 交接时点快照，不是当前状态权威
```

再结合当前 APPROVED / CONFIRMED 需求、ACCEPTED ADR、架构、详细设计、代码和测试恢复项目事实。

### 单一维护原则

同一个动态事实只能有一个权威维护位置。

例如 R04 当前状态变化时：

```text
只更新 CURRENT_STATE.md + 对应正式 C04 review record
```

不得为了“保持一致”再把同一句当前状态复制到：

```text
BASELINE_INDEX.md
CONVERSATION_MAP.md
MIGRATION_LOG.md
旧 HANDOFF
```

如果这些文件需要关联，只写引用：

```text
当前状态见 CURRENT_STATE.md
```

项目不要求 AI 永久记住全部历史。目标是：即使更换模型、清空聊天或重新建立对话，也能从各自权威事实源恢复正确工作状态，同时避免多处状态同步造成审计循环。

# 37. Definition of Done 的 Current Truth 补充检查

在前文 Definition of Done 基础上，完成前还必须确认：

- [ ] 本任务产生的重要决定已经写入 `DECISION_INDEX.md`；
- [ ] 被新决定替代的旧决定已经标记 `SUPERSEDED`；
- [ ] 同一主题不存在两个互相冲突的当前有效决定；
- [ ] `CURRENT_STATE.md` 只描述当前事实；
- [ ] `BASELINE_INDEX.md` 指向当前有效需求、ADR、设计、代码和测试；
- [ ] 项目级动态状态没有在 `BASELINE_INDEX / CONVERSATION_MAP / MIGRATION_LOG / 旧 HANDOFF` 中重复维护；
- [ ] 没有仅存在于聊天中、尚未正式落盘的重要决定；
- [ ] 当前实现没有继续依赖已经 `SUPERSEDED` 的需求、ADR 或设计。
- [ ] 当前 Target 命中的 `LOCKED` Invariant 已执行 Non-Regression Guard，且不存在未经显式 Change Decision 的语义回退。

---

# 38. Primary Executor + Expert Escalation + Independent Reviewer + Human Authority

> 本章是执行槽位、Expert Escalation、权限继承和正式 C04 Finding/Decision 的权威来源。固定岗位、动态 Profile、Role / Model / Runtime / Harness / Session / Tool 定义、标准 Interaction、通用授权、四条运行线、Formal Seal 和执行保障模式由 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md` 唯一定义；机器字段见 `00_project/governance/GOVERNANCE_EXECUTION_CONTRACTS.yaml`。当前运行槽位和授权值仍只由 `CURRENT_STATE.md` 维护。

## 38.1 Role != Model != Runtime != Harness != Session != Tool

`C00～C06` 是固定标准工程岗位。运行时必须应用：

```text
Role != Model != Runtime != Harness != Session != Tool
```

各维度的完整定义和动态 Role Profile 规则见岗位交互与可执行治理政策。本章只把该分离规则应用于当前执行槽位和升级路由。技术上能够调用某个 Model、Runtime、Harness、CLI 或 API，不会自动获得其在其他场景中通常承担的治理角色、Gate 身份或审批权限。例如：

```text
DeepSeek -> codex exec -> GPT
!=
C03 -> C04
```

Codex 或其他高能力 Model 可以承担高难度产品分析、架构分析、设计建议和独立复核，但其输出是否具有治理效力取决于本次正式分配的 Role、Interaction、Authority 和流程。需要正式批准的决定只有经过正确 Owner 按正式 Gate 批准并冻结后才生效。AI / Model 不得自行把分析、建议或辅助结论提升为正式项目决定。

运行时使用以下可配置槽位：

```text
PRIMARY_EXECUTOR
EXPERT_ESCALATION_PRIMARY
EXPERT_ESCALATION_FALLBACK
INDEPENDENT_REVIEWER_PRIMARY
INDEPENDENT_REVIEWER_FALLBACK
HUMAN_PROJECT_OWNER
```

除 `HUMAN_PROJECT_OWNER` 外，每个执行槽位至少解析 Model 与 Harness；项目使用独立 Runtime 时还必须解析 Runtime：

```text
EXECUTION_SLOT:
MODEL: {{MODEL}}
RUNTIME: {{RUNTIME_OR_HARNESS_NATIVE}}
HARNESS: {{HARNESS}}
```

Model、Runtime 和 Harness 均属于当前运行配置，不属于产品 Current Truth。Session 绑定和 Tool 可用性受 Dynamic Role Profile、Interaction、当前授权和实际执行环境约束，也不产生新的治理角色。当前槽位值、Autonomy Mode 和自动授权上限只在 `CURRENT_STATE.md` 维护；不得复制到 `BASELINE_INDEX.md`、`DECISION_INDEX.md`、`CONVERSATION_MAP.md` 或 `ACTIVE_TASKS.md`。

## 38.2 C00～C06 默认槽位分配

| 角色 | 默认执行槽位 | 升级规则 |
|---|---|---|
| C00 | `PRIMARY_EXECUTOR` | 维护当前路由、授权和阶段协调；需要负责人权威时才转人工 |
| C01 | `PRIMARY_EXECUTOR` | 重大需求冲突或高不确定问题转 `EXPERT_ESCALATION` |
| C02 | `PRIMARY_EXECUTOR` | 重大架构决策或跨系统设计转 `EXPERT_ESCALATION` |
| C03 | `PRIMARY_EXECUTOR` | 按批准设计实现；满足升级触发条件时转 `EXPERT_ESCALATION` |
| C04 | `INDEPENDENT_REVIEWER_PRIMARY` / `INDEPENDENT_REVIEWER_FALLBACK` | 必须使用全新独立上下文；优先与实质参与整改的 Expert 使用不同 Reviewer Provider |
| C05 | `PRIMARY_EXECUTOR` | 在已批准测试治理与授权范围内连续验证 |
| C06 | `PRIMARY_EXECUTOR` | 复杂 RCA、并发、性能或跨层故障转 `EXPERT_ESCALATION` |

不得规定“C04 永远必须由某个具体 Model 或 Harness 执行”。正式要求是：C04 必须由独立高能力 Reviewer 执行，并使用全新、与整改上下文隔离的 Session。

## 38.3 Expert Escalation 强制触发条件

Primary Executor 遇到以下任一情况时，必须停止自行扩张 Current Truth，并进入 `EXPERT_ESCALATION`：

1. Current Truth 来源发生实质冲突；
2. 已批准 Requirement 看起来不可实现；
3. 需要新的重大 Architecture Decision；
4. 接口语义未定义，继续实现需要自行发明语义；
5. 涉及安全、数据完整性或高风险控制行为；
6. 根因经过两次认真尝试仍无法确定；
7. 同一个实现问题连续两次修复失败；
8. 需要大范围重构才能继续；
9. Primary Executor 或 C00 收到 C04 已定级的 S0/S1 Finding；
10. 当前任务明确要求独立高级技术判断。

`QUESTION_PRIORITY` 为 P0/P1 的问题，以及 C04 定级为 S0/S1 的 Finding，都不等于必然找项目负责人。正确路由是：

```text
Primary Executor
→ Expert Escalation Primary
→ Expert Escalation Primary 不可用时使用 Expert Escalation Fallback
→ Expert 在 Current Truth 和现有授权内给出可执行答案
→ 返回原角色继续执行
→ 只有需要负责人权威时才转 HUMAN_PROJECT_OWNER
```

C04 不是上述整改链的执行者。C04 形成 S0/S1 Finding 后停止，由 Primary Executor 或 C00 启动 Expert Escalation、完成受控整改并形成新的精确 Review Target，再启动全新独立 C04 Session 复审。

Expert 可以直接解决在现有 Current Truth 和既有授权范围内能够确定答案的技术问题，但不得因为“更合理”而自行改变已批准需求、验收阈值、产品行为或正式 Baseline。

## 38.4 Human Project Owner 边界

只有下列情况才必须停止并请求 `HUMAN_PROJECT_OWNER`：

- 改变产品目标；
- 改变已批准 Requirement；
- 改变 Acceptance Threshold；
- 需要新的重大产品取舍；
- 裁定新的系统边界、公共接口、跨系统依赖、安全/数据完整性设计或重大不可逆架构取舍；
- 需要负责人接受重大风险；
- 建立或替换正式 Baseline，且不存在满足岗位交互与可执行治理政策第 5.1 节全部条件的精确 C00 预授权；
- 签发 Formal Seal；
- 执行未预授权 Release；
- 当前授权模糊、冲突或可能被解释为扩大副作用范围；
- 超出当前授权边界的重大操作。

Expert 输出 `HUMAN DECISION REQUIRED = NO` 时，Primary Executor 应在现有授权范围内自动恢复执行，不得把普通技术判断继续上抛给项目负责人。

C02 / Expert 可以分析所有候选架构并在已批准系统边界、公共接口和风险边界内决定普通技术实现。上述重大架构事项的最终裁定必须进入 `HUMAN_DETERMINATION`。Formal Seal 始终由 Human Project Owner 签发，不得预授权给 C00 或 AI。

## 38.5 Autonomy Mode

支持以下三种模式。当前模式、`AUTHORIZED_UNTIL` 和 `PREAUTHORIZED_GATES` 只由 `CURRENT_STATE.md` 维护。

### MANUAL_GATE

Primary Executor 可在当前明确批准的最小工作范围内执行，但在进入下一 Gate、Milestone、阶段或 `HUMAN_APPROVAL_REQUIRED` 事项前必须停止并获得明确人工批准。

### SUPERVISED_AUTO

模板推荐默认模式。Primary Executor 在当前已授权阶段和文件范围内连续自动执行；`QUESTION_PRIORITY / WORK_PRIORITY` 为 P2/P3 的普通问题、编译失败、测试失败、实现 Bug、测试缺陷、文档同步、Traceability 修复、状态同步和事实所属记录更新默认自动处理。复杂问题自动形成 Escalation Package 交给 Expert。不得自动跨越尚未人工批准的 Gate 或 Milestone。

### FULL_AUTO

`FULL_AUTO` 生效前，`CURRENT_STATE.md` 必须同时明确 `AUTONOMY_MODE: FULL_AUTO`、`AUTHORIZED_UNTIL` 和 `PREAUTHORIZED_GATES`；任一字段缺失时不得按 `FULL_AUTO` 运行。

Primary Executor 可以在既定 Current Truth 和授权范围内，自动跨越 `PREAUTHORIZED_GATES`，直到 `AUTHORIZED_UNTIL`。`FULL_AUTO` 可以：

- 自动执行已授权阶段；
- 自动实现、构建和测试；
- 自动整改 `QUESTION_PRIORITY / WORK_PRIORITY` 为 P2/P3 的普通问题；
- 自动调用 Expert Escalation；
- 自动运行独立 C04 Review Loop 并推进状态。

`FULL_AUTO` 仍不得自动：

- 修改 Current Truth；
- 改变产品目标；
- 降低 Acceptance Threshold；
- 接受重大风险；
- 执行未预授权 Release；
- 执行远程危险或破坏性操作。

任何 Autonomy Mode 都不得扩张实际文件、系统、账户或外部服务权限，也不得绕过 Current Truth、正式 Gate、测试治理或破坏性操作审批。

### 权限继承

```text
SUBAGENT_PERMISSION <= CALLER_PERMISSION
```

子 Agent、Model、Runtime、Harness、Session、CLI、API 或其他被调用工具只能在调用者的任务范围、文件范围和副作用权限内工作，不得通过嵌套调用扩大父任务授权。如果调用者当前仅获准 `READ_ONLY / NO_COMMIT / NO_PUSH`，所有被调用执行单元同样不得：

- 擅自修改文件；
- commit；
- push；
- 创建 PR；
- 修改远程系统；
- 扩大任务范围。

只有 `HUMAN_PROJECT_OWNER` 或获得明确授权的 C00 才能按正式流程扩大副作用范围；调用者不能借助更高能力 Model、不同 Harness 或可执行 CLI 绕过当前授权边界。

## 38.6 Escalation Package

Primary Executor 向 Expert 交接时必须提供最小问题包：

```text
ESCALATION ID
Problem
Current Requirement
Relevant Decision
Relevant Architecture/Design
Affected Code
Observed Evidence
Attempts Already Made
What Must Not Change
Exact Question For Expert
```

Expert 默认只读取 Escalation Package 和解决问题所需的最小相关文件，不重新扫描整个仓库。Expert 输出至少包含：

```text
ROOT CAUSE
AFFECTED LAYER
RECOMMENDED ACTION
DO NOT CHANGE
TEST/VALIDATION REQUIRED
HUMAN DECISION REQUIRED = YES/NO
```

## 38.7 C04 独立评审治理

> **AUXILIARY / ADVISORY != FORMAL C04.**
>
> 本节是 Review Readiness、Question Priority 与 C04 Finding Severity 的分离边界、C04 Finding Severity、Finding / Advisory 边界和 Review Decision Matrix 的唯一权威来源。Question Priority 的具体定义仍由第 10 章的质询规则维护；其他文件只能引用、执行或记录实例。

执行角色可以在现有授权范围内调用 Codex、DeepSeek、Kimi 或其他 Model / Runtime / Harness / Tool 进行只读分析、Bug 定位、方案咨询、设计预审或复杂问题辅助推理。这些输出只能视为 `ADVISORY / AUXILIARY`，不能直接作为正式 Gate 结论，也不能因为调用了 `codex exec` 或某个常用于 Reviewer 的 Model 就宣称完成 C04。C04 是治理角色，不是某个 Model、Runtime、Harness、Session、Reviewer Provider 或 Tool / CLI。

正式 C04 必须由独立评审流程明确发起，针对已冻结的 Review Target，使用精确不可变 Git Commit 或受控版本，与被评审对象的实现和整改过程保持角色独立，并产生正式 C04 Review Record。只有 Review Readiness 为 `READY` 时才能产生正式 `PASS / CHANGES_REQUESTED`。

正式 C04 是有边界的接受性评审，不是寻找项目中所有潜在问题的无限审计。Review Purpose、当前 Task/Change、批准 Acceptance Criteria、关键风险和 Explicit Exclusions 必须在开始前确定。Reviewer 只加载判断这些核心问题所需的 Target、规则和证据；当前信息足以判定时停止扩展阅读。

Primary Executor 的完成报告、变更摘要、测试摘要和自检结果可以作为导航与待核验证据输入，但不能预先决定 C04 结论。C04 必须从冻结 Target 和适用正式证据独立验证这些主张；报告缺失不自动证明 Target 失败，报告声称成功也不自动证明 Target 通过。

### 38.7.1 Review Readiness

正式 C04 进入实质评审前，必须先记录：

```text
REVIEW_ID: {{REVIEW_ID}}
REVIEW_PURPOSE: {{PURPOSE}}
REVIEW_SCOPE: {{CURRENT_TASK_OR_CHANGE_AND_DIRECTLY_AFFECTED_SURFACES}}
CORE_ACCEPTANCE_CONCERNS: {{REQUIREMENTS_GATES_AND_CRITICAL_RISKS}}
EXPLICIT_EXCLUSIONS: {{OUT_OF_SCOPE_AREAS}}
REVIEW_TARGET: {{TARGET}}
EXACT_GIT_COMMIT_OR_CONTROLLED_VERSION: {{COMMIT_OR_VERSION}}
TARGET_FROZEN: YES / NO
INDEPENDENT_REVIEW_SESSION: {{SESSION_ID_OR_REFERENCE}}
FORMAL_REVIEW_RECORD_LOCATION_DEFINED: YES / NO
FORMAL_REVIEW_RECORD: {{PATH_OR_ID}}
REVIEW_READINESS: READY / REVIEW_NOT_READY
```

`FORMAL_REVIEW_RECORD_LOCATION_DEFINED` 只要求 Review Record ID、模板或写入位置已预先定义，不要求记录在评审开始前已完成。允许先建立 Review Record shell。

`EXPLICIT_EXCLUSIONS` 必须在评审开始前填写具体排除项；确无排除项时写 `NONE` 并说明理由，不得保留空白或占位符。缺少该边界时先补齐范围再进入正式评审，不追溯改写历史评审包。排除项可以排除纯排版和措辞偏好，但不得用来豁免当前接受所需的 Target 身份、结论保真、授权或适用安全边界。

精确 Git Review Target 必须记录不可变的完整 Commit Hash。当前 Commit 或历史 Commit 都可以作为正式 C04 Target，但必须可读取、可复现，并明确适用 Baseline 和 Review Purpose；结论只适用于该精确 Commit，不自动覆盖后代或当前 `HEAD`。如果输入使用 `HEAD`，必须立即解析并记录其完整 Hash；只记录可移动的 `HEAD` 不满足正式评审条件。非 Git 文档必须记录可唯一定位的受控版本。具体触发与 Target 边界见 `00_project/governance/PROJECT_ASSURANCE_CADENCE_POLICY.md`。

以下任一情况必须记录 `REVIEW_NOT_READY`：

- Review Target 未冻结、不完整或不可复现；
- 无精确 Commit 或受控版本；
- 必要输入或证据缺失；
- 无法建立全新独立 C04 Session；
- Formal Review Record 写入位置未定义；
- 当前评审命中 `LOCKED` Invariant，但 Non-Regression Contract、必需 Guard 或可执行输入缺失；
- 权威 Current Truth 来源之间存在实质冲突，导致无法确定适用判定标准。

`REVIEW_NOT_READY` 是正式评审的前置状态，不是 Gate Decision。此时 Review Record shell 只记录未就绪原因、缺失输入、后续责任人和重新发起条件，不输出 `PASS`、`CHANGES_REQUESTED` 或正式 Finding。

Review Readiness 的规则定义归本节；每次评审的实例值只写入对应正式 C04 Review Record。`CURRENT_STATE.md` 只在需要时引用 Review ID / Record 和当前 Gate，不复制 Readiness 检查表。`REVIEW_NOT_READY` 不产生新的项目状态 Owner。

### 38.7.2 Question Priority != C04 Finding Severity

`QUESTION_PRIORITY` 的 P0～P3 定义见第 10 章，用于未决问题、澄清请求和设计前提。现有产物 Owner 内的 `WORK_PRIORITY` 字段仍可使用 `P0 / P1 / P2 / P3` 进行工作排序。两者都不是正式 C04 Finding Severity。

正式 C04 Finding 使用 `C04_FINDING_SEVERITY`。只有与冻结 Review Scope、当前任务和适用接受条件直接相关，并且阻止当前 Target 被接受的问题，才进入 S0～S3：

- `S0 — Critical`：可能造成严重安全、合规、数据完整性或不可逆后果；立即停止相关推进、通知 C00 并启动 Expert Escalation。
- `S1 — Major`：违反关键 Current Truth、已批准需求、系统边界、公共接口、架构约束或 Acceptance Threshold，或可能造成重大返工、系统性失效或 Gate 错误；启动 Expert Escalation。
- `S2 — Moderate`：对功能正确性、可测试性、可维护性、追溯性或受控交付有实质影响；通常由 Primary Executor 在授权范围内整改。
- `S3 — Minor`：范围有限但仍违反适用要求、标准或受控接受条件；通常由 Primary Executor 在授权范围内整改。

S0～S3 都是当前 Scope 内的正式 Finding，在当前 Review Target 被接受前都必须关闭。Severity 决定风险表达、整改优先顺序和默认路由；当前 Scope 内 Finding 是否 Open 决定能否 `PASS`。与当前接受无直接关系的问题不得为了提高严重感而分配 Finding Severity。

### 38.7.3 Finding、Advisory 与关闭

正式 Finding 是当前 Scope 内可验证的缺陷、遗漏、矛盾、不可验证性、证据不足、不可接受风险或其他实质阻断，导致 Review Target 无法满足适用的 Current Truth、已批准需求、Acceptance Criteria / Threshold、Gate、安全或合规要求、Traceability、已批准架构/接口/设计约束或工程治理要求。Finding 必须同时说明与当前 Task/Change 的关系、判定依据以及为什么不关闭就不能接受当前 Target。

必须区分：

- 权威 Current Truth 来源互相冲突，无法确定评审标准 → `REVIEW_NOT_READY`；
- Review Target 与清晰、已冻结的 Current Truth 冲突 → Finding → `CHANGES_REQUESTED`。

`ADVISORY / OBSERVATION / FUTURE_IMPROVEMENT` 用于不影响当前接受、范围外、改进性、证据尚不足或可以延期的事项，不分配 S0～S3，不阻断 `PASS`。所有实际发现且有可信依据的此类事项必须进入 Feedback Register 或被引用的现有问题记录，不得因“不阻断”而静默丢弃。正式 C04 结论禁止使用 `PASS_WITH_ACTIONS / CONDITIONAL_PASS / FAIL / APPROVED_WITH_COMMENTS` 或其他未定义的第三种 Gate Decision。

Reviewer 不主动扫描与当前 Review Purpose 无关的全部仓库。偶然发现安全、数据完整性、权限或不可逆风险时必须立即登记并报告 C00；是否扩大当前 Scope、停止推进或建立独立 Change，由正确 Owner 裁定。普通范围外问题只登记，后续按需处理。

AI/C04 可以提出“是 Finding、非阻断反馈、非问题、延期或风险接受”的建议，但争议项是否构成产品问题、是否解决以及何时解决，最终由适用的 Human Project Owner / Decision Owner / Risk Owner 裁定。人类裁定必须留下理由和适用范围，不能通过删除记录制造“从未发生”。

“可接受遗留项”不得表示仍然 Open 的 Finding，只能是：

1. `ADVISORY / OBSERVATION / FUTURE_IMPROVEMENT`；或
2. 由现有 Decision Owner、Risk Owner 或 Human Project Owner 在既有权限下正式批准的 Exception / Risk Acceptance。

C04 不批准 Exception / Risk Acceptance。批准记录必须说明批准人、范围、理由及有效边界。它可作为 Finding 的一种受控关闭方式，但只有面向新精确 Review Target 的全新独立 C04 Session 验证批准证据和适用范围后，才能将 Finding 标记为已关闭。Finding 状态至少使用：

```text
OPEN
CLOSED_BY_FIX
CLOSED_BY_APPROVED_EXCEPTION
```

Finding 关闭时还必须按 `NON_REGRESSION_CONTROL.md` 记录 `REGRESSION_GUARD_DISPOSITION`。已经关闭的 Finding 不得在原 Review Record 中重新打开；同类问题再次出现时使用新的 Finding ID，并通过 `REGRESSION_OF` 引用历史 Finding。

### 38.7.4 Review Decision Matrix

先按 `PROJECT_ASSURANCE_CADENCE_POLICY.md` 第 5 节判断是否触发正式 C04；纯评审记录归档按其第 5.1 节执行机械检查，不进入本矩阵制造新的 Gate Decision。

| 条件 | Readiness | 正式 Gate Decision | 默认后续路由 | Human Project Owner |
|---|---|---|---|---|
| Review Target 未冻结/不可复现、无精确版本、必要输入缺失、独立 Session 或 Record Location 未建立 | `REVIEW_NOT_READY` | 无 | Primary Executor / C00 补齐后重新发起 C04 | 通常不需要 |
| 权威 Current Truth 来源冲突，无法确定判定标准 | `REVIEW_NOT_READY` | 无 | C00 按现有事实 Owner 体系澄清，必要时调用 Expert | 只有需要改变 Current Truth 时 |
| Review Target 与清晰、已冻结的 Current Truth 或批准要求冲突 | `READY` | `CHANGES_REQUESTED` | 按 Finding Severity 路由 | 只有超出既有授权时 |
| 当前冻结范围存在任一 Open S0 Finding | `READY` | `CHANGES_REQUESTED` | 停止相关推进 → C00 / Expert → Primary Executor → 新 Review Target → 新 C04 | 仅命中保留决策时 |
| 当前冻结范围存在任一 Open S1 Finding | `READY` | `CHANGES_REQUESTED` | Expert → Primary Executor → 新 Review Target → 新 C04 | 仅命中保留决策时 |
| 当前冻结范围存在任一 Open S2 Finding | `READY` | `CHANGES_REQUESTED` | Primary Executor 整改 → 新 Review Target → 新 C04 | 通常不需要 |
| 当前冻结范围存在任一 Open S3 Finding | `READY` | `CHANGES_REQUESTED` | Primary Executor 整改 → 新 Review Target → 新 C04 | 通常不需要 |
| 适用的 Traceability Gate 未闭合且无正式批准的 Exception | `READY` | `CHANGES_REQUESTED` | 对应现有 Owner 整改 | 通常不需要 |
| 必需 Non-Regression Guard 已执行并确认违反 `LOCKED` Invariant | `READY` | `CHANGES_REQUESTED` | Primary Executor 按 Invariant 来源整改 → 新 Target → 新 C04 | 只有改变 Invariant 或超出授权时 |
| 必须改变已批准需求、产品目标、系统边界、公共接口、跨系统依赖、安全/数据完整性设计、重大不可逆架构取舍、Acceptance Threshold 或未预授权 Current Truth | `READY` | `CHANGES_REQUESTED` | C00 按现有权限体系转交保留决策 Owner | 需要 |
| 必须接受重大风险或执行未授权 Release | `READY` | `CHANGES_REQUESTED` | 现有 Risk / Release Owner | 需要 |
| 仅存在已登记的 Advisory / Observation / Future Improvement，当前 Scope 无 Open Finding | `READY` | `PASS` | 进入既有下一阶段；非阻断事项按记录后续处理 | 不需要 |
| 当前 Scope 的适用强制检查完成、证据充分、Open Findings = 0，所有 Exception 已由正确 Owner 批准 | `READY` | `PASS` | C00 / 既有下一阶段 | 不需要 |

机械判定：

```text
REVIEW_READINESS = REVIEW_NOT_READY
→ NO GATE DECISION

REVIEW_READINESS = READY
AND OPEN_IN_SCOPE_FINDINGS > 0
→ CHANGES_REQUESTED

REVIEW_READINESS = READY
AND ALL_APPLICABLE_MANDATORY_CHECKS_COMPLETED
AND OPEN_IN_SCOPE_FINDINGS = 0
AND REQUIRED_EVIDENCE_COMPLETE
AND ALL_APPLICABLE_EXCEPTIONS_APPROVED_BY_CORRECT_OWNER
AND (
  NON_REGRESSION_VALIDATION = PASS
  OR (NON_REGRESSION_VALIDATION = NOT_APPLICABLE AND NOT_APPLICABLE_REASON_COMPLETE)
)
→ PASS
```

### 38.7.5 C04 独立性与复审

关闭复审以原 Finding 的关闭条件及整改直接引入的实质回归为边界。纯措辞偏好不构成 Finding；措辞、计数或可机械修正的问题若影响接受结论、授权或证据真实性，仍按第 38.7.2～38.7.3 节判断，不一律降级为 Advisory。保存已形成的关闭结论按 `PROJECT_ASSURANCE_CADENCE_POLICY.md` 第 5.1 节处理，不把归档动作递归视为新的关闭验证。

C04 必须：

- 使用全新独立上下文；
- 不继承实现 AI 的私有推理或自我辩护；
- 从项目正式文件和精确 Git Review Target 重建事实；
- 只审 Review Purpose、当前任务/Change、直接受影响面和适用关键风险，不默认复审未变化的全部项目；
- 当前证据足以判定时停止继续读取或扩大检查；
- 使用 fallback 时仍重新建立独立 C04 Session；
- 先检查 Readiness；只有 `READY` 时才执行“发现 Finding → 定级 → 给出关闭条件 → `PASS / CHANGES_REQUESTED` → 停止”；
- 不参与被审对象的整改设计或实现；
- 不得批准 Exception / Risk Acceptance；
- 不得自行关闭自己提出的 Finding；Finding 只能由面向新精确 Review Target 的全新独立 C04 Session 复核关闭；
- 在同一个 Review Record 中分别记录 `CURRENT_CHANGE_VALIDATION` 和 `NON_REGRESSION_VALIDATION`；不得把它们升级成新的角色、Owner 或第三种 Gate Decision；
- 只有当前变化命中适用 `LOCKED` Invariant、既有 Guard 或 Target Manifest 强制项时，才核验对应历史 Finding 和 Guard 证据；未命中时允许记录有依据的 `NOT_APPLICABLE`，不得仅因对象属于治理文件就扩大全量历史审查；
- 不因 Reviewer Provider、Model、Runtime 或 Harness 改变而改变评审输入、审查标准或结论格式。

C04 形成 S0/S1 Finding 后必须停止。Primary Executor 或 C00 根据 Finding 启动 Expert Escalation，完成受控整改并形成新的精确 Review Target 后，必须由新的独立 C04 Session 复审。S2/S3 Finding 由 Primary Executor 在现有授权范围内整改，同样必须形成新的精确 Review Target 并由新的独立 C04 Session 复审。非阻断反馈不触发该复审循环。

如果某 Expert 实质参与了当前整改方案，C04 优先选择另一 Reviewer Provider。若另一 Provider 不可用，允许使用同 Provider 的全新独立 Session，但上下文必须完全隔离。Reviewer Provider 只是 Reviewer Model/Runtime/Harness 的运行选择属性，不是新角色、新 Owner 或新 Current Truth 来源。C04 的判断权限来自角色和正式评审规则，不来自具体 Model、Runtime 或 Harness。

## 38.8 Model / Runtime / Harness Substitution

> **MODEL, RUNTIME OR HARNESS SUBSTITUTION DOES NOT CHANGE CURRENT TRUTH OR THE LOGICAL C00 CHANNEL.**

更换执行槽位的 Provider、Model、Runtime、Harness 或其组合，本身都不构成产品、需求、架构或 Baseline 变更，也不产生新的 Role、Tool 权限或独立性。

切换必须固定当前 Git Anchor，记录前后运行身份，并按岗位交互与可执行治理政策第 8 节选择：

- `KNOWLEDGE_CONTINUATION_CHECK`：Role、Task、Scope、Authority、Baseline、Gate 和上下文完整性均兼容时使用；
- `BASELINE_RELEARN`：上述事实变化、上下文连续性无法证明、发生混淆、高风险政策要求或负责人明确要求时使用。

逻辑 C00 可以在切换后继续服务项目负责人；物理 Session 是否复用由平台能力、上下文完整性和政策决定。正式 C04 无论 Model/Runtime/Harness 是否变化，都必须使用新的独立 Session。

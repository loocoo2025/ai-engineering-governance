> Authority：Human Determination 的工程衔接、文档修改分级、Work Package 和反馈闭环；由 `INDEX.yaml` 按触发条件加载。

# 41. 面向负责人的审批、变更与工作包治理

> 面向项目负责人的路线说明、阶段说明和审批可理解性由 `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md` 唯一定义。本章维护 Human Determination 的工程衔接、文档修改分级、语义识别、Work Package、影响驱动重审批和反馈闭环；具体实例状态仍由各自产物 Owner 维护。

## 41.1 不得假设负责人已读完正文

请求项目负责人批准 PRD、SRS、Baseline、架构、阈值、重大风险、Formal Seal、Release 或其他保留决策时，不得只给文件名或要求“确认通过”。必须按人机协作及审批可理解性规则解释路线、阶段、产物用途、内容变化、风险、选项和授权边界，并提供 `HUMAN_DETERMINATION_PACKAGE`。现有 `OWNER_DECISION_PACKAGE` 作为兼容名称，必须满足同一字段集合：

```text
DETERMINATION_ID
WHAT_MUST_BE_DECIDED
WHY_HUMAN_AUTHORITY_IS_REQUIRED
OVERALL_ROUTE_AND_CURRENT_STAGE
ARTIFACT_PURPOSE_AND_DOWNSTREAM_USE
CONTENT_SUMMARY_CHANGES_AND_EXCLUSIONS
TERMS_THRESHOLDS_AND_PRACTICAL_MEANING
CONFIRMED_FACTS
OPEN_QUESTIONS
OPTIONS_AND_DIFFERENCES
RISKS_AND_TRADEOFFS
RECOMMENDED_OPTION_AND_REASON
AUTHORIZATION_INCLUDED
APPROVED_CONSEQUENCE
CHANGES_REQUESTED_CONSEQUENCE
DEFERRED_CONSEQUENCE
REJECTED_CONSEQUENCE
EXPLICITLY_NOT_AUTHORIZED
AUTHORITATIVE_SOURCES
COPYABLE_RESPONSE_FORMAT
```

摘要只帮助负责人理解和决策，不成为第二 Current Truth。正文和正式记录仍是事实 Owner。

负责人标准决定为：

```text
APPROVED
CHANGES_REQUESTED
DEFERRED
REJECTED
```

AI 必须解释每个可选决定的直接后果。`DEFERRED` 保持当前 Baseline 有效，可以继续已授权范围，但不得越过被暂缓的边界。

负责人回复只有在能够唯一绑定当前 Package、Action、Scope、Target 和边界时才有效。存在多个待决 Package、Target 不明确或回复可能扩大副作用范围时，AI 必须请求澄清，不能把一句模糊“批准”扩展为文件修改、Commit、Tag、Baseline Adoption、独立 Session 创建、正式 C04 Dispatch、安装、真实 Model 调用、Push、PR、Release、远程修改或 Formal Seal 的组合授权。

## 41.2 缩写与技术术语

面向负责人的聊天、批准包和完成报告适用 `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md` 的可理解性要求。缩写或专业术语第一次出现时应给出英文全称和中文解释。例如：

```text
SRS (Software Requirements Specification，软件需求规格说明书)
```

随后可以使用缩写。正式文件可通过 `00_project/glossary.md` 统一解释，不要求在每一行重复全称。Git 的 tracked/untracked/staged/Commit、Fixture 等状态必须同时说明它对提交、丢失风险、升级或评审的实际影响。

## 41.3 阈值批准包

需要负责人批准的 Acceptance Criteria / Threshold 必须按人机协作及审批可理解性规则说明其实际含义，并至少包含：

- 数值和单位；
- 适用环境和前置条件；
- 测量开始/结束边界；
- 包含项与排除项；
- 对用户体验、成本和风险的实际意义；
- 推荐该值的依据与替代值；
- 验证方法和证据；
- 批准后未来修改所需的影响分析和重新批准。

禁止要求负责人批准没有测量语义的孤立数字。

## 41.4 多阶段路线和 Gate Package

中等以上多阶段工作开始前，应先展示：

```text
OVERALL_OBJECTIVE
PHASES
OUTPUTS_PER_PHASE
DEPENDENCIES
MERGEABLE_PHASES
DEFERRABLE_PHASES
GATES_AND_OWNERS
CURRENT_AUTHORIZATION_SCOPE
STOP_CONDITIONS
```

路线认可不自动授权后续全部阶段。Gate 针对决策边界，不针对文件数量；PRD/SRS 可以形成需求 Baseline Package，架构/ADR/详细设计/测试设计可以形成设计 Baseline Package，但合并审批不得跳过适用证据、Traceability、独立评审或 Current Truth 权限。

面向项目负责人的路线、阶段和 Gate Package 呈现方式归 `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md`；本节字段用于工程衔接，不建立第二套可理解性规则。

## 41.5 已批准文档的修改分级

已批准文档仍可完善，但修改前必须按语义分类：

- `EDITORIAL`：错别字、格式、失效链接等，不改变含义；
- `CLARIFICATION`：表达更清楚，必须证明需求、边界、阈值和行为没有变化；
- `SUBSTANTIVE`：改变需求、阈值、接口、架构、验收、风险或受控行为，必须执行影响分析和正确 Owner 的重新批准。

分类名称不能掩盖真实语义。无法证明为 `EDITORIAL / CLARIFICATION` 时，按 `SUBSTANTIVE` 或 `UNKNOWN` 处理并停止自动生效。

## 41.6 稳定语义优先于固定字段名

AI 应识别异名同义，但不得为了“智能”拼凑缺失事实：

1. 先识别受控语义和所属 Owner；
2. 字段名不同但语义、范围和状态一致时，可以建立显式 Alias Mapping；
3. 不得仅因标题或字段名不同就宣称信息缺失；
4. 多个来源含义冲突、Owner 不清或证据不足时标记 `UNKNOWN / CONFLICT` 并停止；
5. Alias Mapping 不创建新事实，也不能把非正式摘要提升为正式决定。

## 41.7 Impact-Based Reapproval

上游变化后必须先分析影响，再决定修改、验证和重审批范围：

- 只修改真实受影响的下游内容；
- 明确列出不受影响且继续有效的批准内容；
- 只重新验证受影响链路和必要回归范围；
- 编辑性变化不触发全链路重审批；
- 重大语义变化、安全/合规/数据完整性风险或无法确定影响时扩大范围；
- 不得用“影响较小”跳过正确 Owner 或适用 Gate。

具体实例使用 `13_change_management/impact_analysis/IMPACT_ANALYSIS_TEMPLATE.md`。

## 41.8 Bounded Work Package

大型项目可以按以下逻辑递归分解：

```text
Project -> Governed Subproject -> Module -> Work Package -> Sub-Work Package -> Leaf Work Package
```

只有 `LEAF_EXECUTION / INTEGRATION` 是直接写入执行单元。写入执行必须满足：

```text
ONE_WRITE_SESSION
= ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE
= ONE_OUTPUT_CONTRACT
= ONE_GIT_WORKTREE
= ONE_ACTIVE_WRITER
```

`ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE` 只允许 `LEAF_EXECUTION / INTEGRATION`。

多个并行 Writer 必须使用独立 Worktree 和 Branch；同一 Local Working Directory 同时只能有一个 Writer。Worktree 只提供物理隔离，写入范围重叠、共享接口未冻结或依赖顺序不明确时仍必须串行或建立 Integration Work Package。

父级接受不得重新审查所有子级细节，而应核验仍有效的 Child Acceptance Evidence、接口一致性、集成证据和系统级接受条件；证据缺失或过期时为 `REVIEW_NOT_READY`。任务实例归 `ACTIVE_TASKS.md`，当前结构关系归 `PROJECT_STRUCTURE_MAP.md`，稳定分解、父子事实和组合式评审规则只归 `00_project/governance/PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`。

## 41.9 治理反馈闭环

任何疑问、体验问题、治理缺口、改进建议、疑似缺陷或现场报告，在事实尚未完成判断时必须先登记为 FB，再分类和分流。不得在收到时直接把反馈宣称为 BUG、CR 或正式决定：

```text
USER_FEEDBACK
-> FEEDBACK_REGISTER
-> CLASSIFICATION
-> EXPLANATION / BUG / FIELD / CR / FUTURE_IMPROVEMENT / NO_ACTION
-> IMPLEMENTATION_OR_DISPOSITION
-> VERIFICATION
-> CLOSURE_EVIDENCE
```

FB 当前状态、类型、去向和责任角色只由 `12_issues/feedback/FEEDBACK_REGISTER.md` 维护；复杂反馈可使用同目录 `FEEDBACK_TEMPLATE.md`。C06 负责分流，确认后再建立 BUG、FIELD、CR 或其他下游记录并双向引用。`15_operations/field_feedback/FIELD_FEEDBACK_TEMPLATE.md` 只承载已分流的现场/运行反馈，不是通用反馈登记 Owner。

反馈本身不自动批准模板或产品变化，也不改变 Current Truth、Baseline 或 Gate；稳定版保护和预发布规则归 `00_project/versioning_rules.md`。

## 41.10 保障节奏和外部 AI 引用

- 何时必须执行保障活动或建立独立 Session：`00_project/governance/PROJECT_ASSURANCE_CADENCE_POLICY.md`；
- Session 连续、独立请求格式和结果返回：`00_project/governance/modules/sessions/INDEX.yaml`；
- 外部 AI 当前配置值：`00_project/governance/EXTERNAL_AI_TRANSFER_CONFIG.yaml`；
- 当前采用的 Profile、Autonomy Mode 和执行路由：`CURRENT_STATE.md`。

这些文件各自维护一种事实，不得互相复制当前值。

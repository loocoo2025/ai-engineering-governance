# CR-GOV-002：人类可理解审批、反馈分流与 ETC 质量治理

## 0. 文档控制

```text
CHANGE_TYPE: GOVERNANCE_CHANGE
SEMANTIC_LEVEL: SUBSTANTIVE
STATUS: APPROVED_FOR_CANDIDATE_IMPLEMENTATION
CURRENT_VERSION: v0.1.5
SOURCE_COMMIT: 8c327b65d19ef35db5c4ce3fae2a884176cab478
TARGET_IDENTITY: v0.1.6-candidate
HUMAN_PROJECT_OWNER: Project Owner
DATE: 2026-09-04
```

本 Change 只修改 AI 软件工程治理框架源仓库。参考项目目录只作为只读治理证据，不得修改，也不得把其中的项目实例、决定、路径或反馈记录复制到公开模板。

## 1. 问题

`v0.1.5` 已具备 Human Determination、反馈闭环和可维护性要求，但仍存在三处需要收口的治理缺口：

1. 人工审批有结构化字段，但缺少独立权威规则强制 AI 先解释路线、阶段、产物用途、风险、选项和授权边界；
2. 通用反馈直接落到现场反馈记录，缺少“先登记为 FB、完成证据判断后再分流”的当前状态 Owner；
3. ETC 只作为隐含设计倾向存在，尚未成为从需求到验证的正式质量属性和 C02/C04 判据。

## 2. 已批准目标

- 新增独立的人机协作及审批可理解性权威文件；
- 新增通用 `FEEDBACK_REGISTER` 和反馈明细模板，支持 `QUESTION / USABILITY / GOVERNANCE_GAP / IMPROVEMENT / DEFECT_SUSPECTED / FIELD_REPORT / UNKNOWN`；
- 反馈必须先登记，再分流到 `EXPLANATION / BUG / FIELD / CR / FUTURE_IMPROVEMENT / NO_ACTION`；
- 将 ETC（Easier To Change，更容易变更）提升为正式质量属性、设计输入和评审判据；
- PRD、SRS、架构、详细设计、测试和 C02/C04 形成可追溯的 ETC 链路；
- 形成 `v0.1.6-candidate`，等待独立 C04 和后续发布授权。

## 3. 事实所有权

```text
面向负责人的路线、阶段和审批可理解性
→ 00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md

反馈项当前状态、类型、去向和责任角色
→ 12_issues/feedback/FEEDBACK_REGISTER.md

ETC 稳定质量语义与 Change Amplification 判据
→ AI_ENGINEERING_RULES_V2.md 第 38.9 节
```

`GOVERNANCE_EXECUTION_CONTRACTS.yaml` 只提供上述治理语义的机器可读字段和枚举，不成为竞争性 Owner。需求、架构、设计、测试和 Review Template 只记录项目实例。

## 4. 不变量

- 不改变 Current Truth、One Fact One Owner、Baseline 或 Traceability Owner；
- 不改变 C00～C06 固定岗位和基本职责；
- 不改变 C04 Readiness、Finding Severity、Decision Matrix 或独立性；
- 不改变 V 模型、ADR、Testing Governance 的风险驱动原则或现有产品事实；
- 不把 ETC 解释为投机性抽象、无限测试或未经批准的重构授权；
- 不修改参考项目目录。

## 5. Candidate 授权边界

允许：

- 修改当前治理模板中的权威规则、Role Brief、需求/架构/设计/测试/Review Template、术语、索引和候选版本记录；
- 新增本 Change、影响分析、候选 Release Notes、审批规则和反馈模板；
- 执行文档、YAML、索引、链接、敏感信息和 Git whitespace 检查。

不允许：

- Commit、Tag、Push、PR 或 Release；
- 正式 C04、Baseline Adoption 或 Formal Seal；
- 修改参考项目或任何产品项目；
- 改变产品需求、架构、代码、测试事实或远程系统。

## 6. Candidate 停止条件

```text
HUMAN_APPROVAL_UNDERSTANDABILITY_READY: YES
FEEDBACK_REGISTER_AND_TRIAGE_READY: YES
ETC_REQUIREMENT_TO_EVIDENCE_CHAIN_READY: YES
ONE_FACT_ONE_OWNER_CHECK: PASS
MECHANICAL_VALIDATION: PASS
COMMIT_CREATED: NO
FORMAL_C04_STARTED: NO
FINAL_STATUS: V0.1.6_CANDIDATE_OUTPUT_READY
```

## 7. v0.1.6 正式发布授权

在候选输出完成后，Human Project Owner 于 2026-09-04 明确要求正式发布 `v0.1.6`，并在额度恢复后要求继续。本授权唯一绑定以下发布 Package：

```text
RELEASE_AUTHORIZATION_ID: HPO-RELEASE-v0.1.6-20260904
AUTHORITY_OWNER: Human Project Owner
TARGET_VERSION: v0.1.6
TARGET_REPOSITORY: loocoo2025/ai-engineering-governance
TARGET_REMOTE: origin
RELEASE_CHANNEL: STABLE

AUTHORIZED_ACTIONS:
- 将候选版本展示元数据收口为正式 v0.1.6
- 形成精确 Release Commit
- 对 Release Commit 执行全新独立正式 C04
- Push origin/main
- 创建并 Push v0.1.6 Tag
- 创建公开 GitHub Release v0.1.6
- 上传由该 Tag 生成的正式 Git archive

FORMAL_SEAL: NOT_AUTHORIZED / NOT_ISSUED
DOWNSTREAM_BASELINE_ADOPTION: NOT_AUTHORIZED / NOT_PERFORMED
GITEE_PUSH: NOT_AUTHORIZED
HISTORY_REWRITE: NOT_AUTHORIZED
FORCE_PUSH: NOT_AUTHORIZED
PREEXISTING_UNTRACKED_FILES: EXCLUDED_AND_UNTOUCHED
```

Release Commit、正式 C04 Target、Tag、GitHub Release 和 Git archive 必须解析到同一精确 Commit。正式 C04 和 Release 均不自动产生 Formal Seal，也不替任何下游项目采用新的 Governance Baseline。

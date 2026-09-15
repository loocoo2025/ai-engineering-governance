# 设计评审记录

## Review Readiness

```text
REVIEW_ID: {{REVIEW_ID}}
REVIEW_LINE: INDEPENDENT_REVIEW
INDEPENDENT_REVIEW_SUBTYPE: FORMAL_C04
REVIEW_TARGET: {{TARGET}}
EXACT_GIT_COMMIT_OR_CONTROLLED_VERSION: {{COMMIT_OR_VERSION}}
TARGET_FROZEN: YES / NO
INDEPENDENT_REVIEW_SESSION: {{SESSION_ID_OR_REFERENCE}}
NEW_SESSION_EVIDENCE: {{EVIDENCE}}
EXECUTION_OR_REMEDIATION_SESSIONS_EXCLUDED: {{SESSION_IDS_OR_NOT_APPLICABLE}}
PRIVATE_CONTEXT_INHERITED: NO
CONTEXT_PACKAGE_MANIFEST: {{MANIFEST_OR_REFERENCE}}
TARGET_BINDING_EVIDENCE: {{EVIDENCE}}
REVIEW_TARGET_ACCESS: READ_ONLY
ALLOWED_WRITE_PATHS: {{FORMAL_REVIEW_RECORD_ONLY_OR_NONE}}
GIT_WRITE_ALLOWED: NO
REMOTE_MUTATION_ALLOWED: NO
PRE_REVIEW_TARGET_STATUS: {{STATUS_EVIDENCE}}
POST_REVIEW_TARGET_STATUS: {{STATUS_EVIDENCE_OR_PENDING}}
FORMAL_REVIEW_RECORD_LOCATION_DEFINED: YES / NO
FORMAL_REVIEW_RECORD: {{PATH_OR_ID}}
REVIEW_READINESS: READY / REVIEW_NOT_READY
NOT_READY_REASONS: {{REASONS_OR_NOT_APPLICABLE}}
MISSING_INPUTS: {{INPUTS_OR_NOT_APPLICABLE}}
RESPONSIBLE_OWNER: {{OWNER_OR_NOT_APPLICABLE}}
RESTART_CONDITIONS: {{CONDITIONS_OR_NOT_APPLICABLE}}
```

`REVIEW_NOT_READY` 时只记录未就绪原因、责任人和重新发起条件，不填写 Finding 或正式 Gate Decision。独立性证据缺失同样属于未就绪。“只读”针对被评审对象，唯一 Scoped Write 只能是预定义 Review Record。完整规则见 `00_project/governance/modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md` 第 38.7 节。

## Review Scope

- 评审目的：
- 当前任务 / 变化：
- 核心接受关注点：
- 适用需求 / Baseline：
- 适用 ADR / 架构 / 接口 / 设计约束：
- 证据：
- 明确排除：

## ETC 与 Change Amplification 检查（适用时）

- 每个已批准变化是否局限到声明的模块和 Variation Point：
- 是否影响无关 Stable Core：
- 实际/预计变更范围是否超过批准预算：
- 兼容、独立测试与回退机制是否可执行：
- 是否产生多个需要同步维护的事实副本：

## Finding Summary

```text
OPEN_IN_SCOPE_FINDINGS:
S0: {{COUNT}}
S1: {{COUNT}}
S2: {{COUNT}}
S3: {{COUNT}}

ADVISORIES: {{COUNT}}
```

| Finding ID | Severity | Finding | Current Task / Core Acceptance Relation | Evidence | Violated Basis / Acceptance Impact | Required Closure Condition | Default Route | Status | Closure Evidence |
|---|---|---|---|---|---|---|---|---|---|
| REV-001 | S0/S1/S2/S3 | | CORE / IN_SCOPE | | | | | OPEN | |

## Non-Regression / 防回退

```text
APPLICABLE_NON_REGRESSION_INVARIANTS: {{IDS_OR_NOT_APPLICABLE_WITH_REASON}}
REGRESSION_GUARD_COMMAND: {{COMMAND_OR_NOT_APPLICABLE}}
REGRESSION_GUARD_RESULT: PASS / FAIL / NOT_RUN
PRIOR_CLOSED_FINDINGS_STATUS: REMAIN_CLOSED / REGRESSION_FOUND / NOT_APPLICABLE
CURRENT_CHANGE_VALIDATION: PASS / FAIL
NON_REGRESSION_VALIDATION: PASS / FAIL / NOT_APPLICABLE
NON_REGRESSION_EVIDENCE: {{EVIDENCE}}
```

| Finding ID | Regression Of | Guard Disposition | Invariant / Guard ID | Reason |
|---|---|---|---|---|
| | {{PRIOR_FINDING_ID_OR_NOT_APPLICABLE}} | REQUIRED/NOT_REQUIRED | | |

完整规则见 `00_project/governance/modules/engineering/NON_REGRESSION_CONTROL.md`。只有当前变化命中适用 `LOCKED` Invariant、既有 Guard 或 Target Manifest 的强制检查时才必须执行；不得仅因对象属于治理文件就自动扩大全量防回退审查。

## Advisory / Observation / Future Improvement

| Advisory ID | Type | Observation | Feedback ID / Disposition Owner | Suggested Follow-up | Non-blocking Confirmation |
|---|---|---|---|---|---|
| ADV-001 | ADVISORY / OBSERVATION / FUTURE_IMPROVEMENT | | | | YES |

## Formal Decision

只有 `REVIEW_READINESS: READY` 时才填写：

```text
ALL_APPLICABLE_MANDATORY_CHECKS_COMPLETED: YES / NO
REQUIRED_EVIDENCE_COMPLETE: YES / NO
ALL_APPLICABLE_EXCEPTIONS_APPROVED_BY_CORRECT_OWNER: YES / NO / NOT_APPLICABLE
CURRENT_CHANGE_VALIDATION: PASS / FAIL
NON_REGRESSION_VALIDATION: PASS / FAIL / NOT_APPLICABLE
FORMAL_DECISION: PASS / CHANGES_REQUESTED
DECISION_BASIS: {{SUMMARY}}
```

当前冻结评审范围内的任一 Open Finding，或适用 Non-Regression Validation 失败，都阻断 `PASS`。已实际发现的非核心、关联但非阻断或范围外可信问题必须登记为 Feedback 并交由正确 Owner 处置，但不因其存在自动阻断当前 `PASS`。Finding 不得由提出它的 C04 Session 自行关闭；整改或正式 Exception 批准后，必须由面向新精确 Review Target 的全新独立 C04 Session 复核。

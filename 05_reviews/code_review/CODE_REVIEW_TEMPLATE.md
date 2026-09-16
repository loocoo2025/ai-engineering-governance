# Code Review

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

- Review Purpose：
- Current Task / Change：
- Core Acceptance Concerns：
- Included Files / Components：
- Applicable Requirements / Architecture / Interface / ADR：
- Applicable Tests and Evidence：
- Explicit Exclusions：

## 需求一致性
-
## 设计一致性
- Review Scope 内的新增或行为变更代码是否可追溯到与风险相称的 Design Intent：
- 关键系统语义是否具有独立规范表达，而不是只由普通实现代码隐式定义：
- 代码与规范语义存在差异时，是否已经登记并由正确 Owner 处置：

权威规则见 `00_project/governance/modules/engineering/ARCHITECTURE_AND_DESIGN.md` 第 12.1 节。不得借此全量重建未变化代码的设计文档。
## 正确性/边界
-
## 并发/生命周期/资源
-
## 错误处理/安全
-
## 可测试性/测试缺口
-
## ETC / Change Amplification（适用时）
- 变化是否局限在设计声明的模块 / Variation Point：
- 是否修改了无关 Stable Core：
- 是否新增需要同步维护的事实副本：
- 是否具备替换性、兼容性、独立测试和回退证据：
- 实际影响范围是否超过批准的变更预算：

## Finding Summary

```text
OPEN_IN_SCOPE_FINDINGS:
S0: {{COUNT}}
S1: {{COUNT}}
S2: {{COUNT}}
S3: {{COUNT}}

ADVISORIES: {{COUNT}}
```

## Standard Finding Record

| Finding ID | Severity | Category | Current Task / Core Acceptance Relation | Evidence | Violated Basis / Acceptance Impact | Required Closure Condition | Default Route | Status | Closure Evidence |
|---|---|---|---|---|---|---|---|---|---|
| C04-CODE-S1-001 | S0/S1/S2/S3 | {{CATEGORY}} | | | | | | OPEN | |

Category 可使用：`CORRECTNESS / REQUIREMENT / ARCHITECTURE / INTERFACE / TRACEABILITY / TESTING / SECURITY / SAFETY / RELIABILITY / MAINTAINABILITY / CHANGEABILITY / GOVERNANCE / EVIDENCE`。Category 不产生新的治理 Owner。

Finding Status：

```text
OPEN
CLOSED_BY_FIX
CLOSED_BY_APPROVED_EXCEPTION
```

已关闭 Finding 再次出现时不得修改旧记录，必须创建新的 Finding ID，并填写：

```text
REGRESSION_OF: {{PRIOR_FINDING_ID_OR_NOT_APPLICABLE}}
```

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

| Finding ID | Repeatable Root Cause | Stable Invariant | Machine Checkable | Guard Disposition | Invariant / Guard ID | Reason |
|---|---|---|---|---|---|---|
| | YES/NO | YES/NO | YES/NO | REQUIRED/NOT_REQUIRED | | |

Guard 判定、`LOCKED` Invariant 和退出码语义见 `00_project/governance/modules/engineering/NON_REGRESSION_CONTROL.md`。只有当前变化命中适用 `LOCKED` Invariant、既有 Guard 或 Target Manifest 的强制检查时才必须执行；不得仅因对象属于治理文件就自动扩大全量防回退审查。

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
FORMAL_REVIEW_RECORD: {{PATH_OR_ID}}
```

当前冻结 Review Scope 内任一 Open Finding 或适用 Non-Regression Validation 失败都阻断 `PASS`。范围外或非阻断问题必须登记为 Feedback / Advisory，但不阻断当前 PASS。Finding 不得由提出它的 C04 Session 自行关闭；整改或正式 Exception 批准后，必须由面向新精确 Review Target 的全新独立 C04 Session 复核。

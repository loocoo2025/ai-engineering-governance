# Child Acceptance Package 模板

## 1. Package 身份

```text
PACKAGE_ID: {{CAP-XXX}}
CHILD_ID: {{PROJECT_MODULE_OR_REVIEW_PACKAGE_ID}}
PARENT_ID: {{PARENT_ID}}
SCOPE: {{EXACT_SCOPE}}
STATUS: DRAFT / READY_FOR_PARENT_REVIEW / ACCEPTED / STALE / REJECTED
GOVERNANCE_VERSION: {{EXACT_VERSION_AND_COMMIT}}
EXACT_COMMIT_OR_TARGET: {{FULL_IMMUTABLE_TARGET}}
APPLICABLE_BASELINE: {{BASELINE_ID_AND_ANCHOR}}
PARENT_CHILD_CONTRACT: {{EXACT_REFERENCE}}
```

## 2. 交付摘要

- Objective：
- Boundary：
- Outputs：
- Explicit Exclusions：
- Completion Capsule：

## 3. 接口与依赖

- Interface Contracts / Versions：
- Upstream Dependencies：
- Downstream Consumers：
- Compatibility Result：
- Dependency Impact：

## 4. 需求、验证与评审证据

- Requirement Coverage：
- Test / Validation Evidence：
- Formal C04 Review Record：
- Formal C04 Decision：`PENDING / PASS / CHANGES_REQUESTED`
- Open S0 / S1 / S2 / S3：
- Approved Exceptions：
- Residual Risks：

## 5. 回滚和有效性

- Rollback Anchor：
- Rollback Steps：
- Validity Conditions：
- Invalidation Conditions：

以下任一事实变化时必须标记 `STALE`：Target、适用 Baseline、接口合同、适用要求、验证证据或正式 C04 Finding 状态。

## 6. Parent Receipt

```text
PARENT_RECEIPT: NOT_REVIEWED / RECEIVED / ACCEPTED_FOR_INTEGRATION / REJECTED / STALE
PARENT_REVIEW_TARGET:
SYSTEM_INTEGRATION_MANIFEST:
RECEIPT_OWNER:
RECEIPT_EVIDENCE:
```

Child `PASS` 不自动等于 Parent Acceptance、系统 Gate、Baseline Adoption 或 Release。

进入 `READY_FOR_PARENT_REVIEW` 前，必需的 Child C04 Decision 必须为 `PASS`；`PENDING / CHANGES_REQUESTED` 不得作为 Parent 的正式可信输入。

# Parent–Child Project Contract 模板

## 1. 合同身份

```text
CONTRACT_ID: {{PC-XXX}}
CONTRACT_VERSION: {{VERSION}}
STATUS: PROPOSED / APPROVED / CURRENT / SUPERSEDED / RETIRED
PARENT_PROJECT_ID: {{PROJECT_ID}}
CHILD_PROJECT_ID: {{PROJECT_ID}}
PARENT_GIT_ANCHOR: {{FULL_COMMIT_OR_TAG}}
CHILD_GIT_ANCHOR: {{FULL_COMMIT_OR_NOT_ESTABLISHED}}
AUTHORITY_OWNER: {{OWNER}}
EFFECTIVE_FROM: {{DATE_OR_GATE}}
```

## 2. 委派目标与边界

- Child Objective：
- In Scope：
- Out of Scope：
- Parent 保留的系统责任：
- Child 被委派的内部责任：

## 3. 事实所有权

| Fact Scope | Owner | Authority Source | Child 是否可修改 | 变更路线 |
|---|---|---|---|---|
| 整体产品目标 | Parent | | NO | Human Determination / CR |
| 系统边界和跨项目接口 | Parent | | NO | C02 / Human Determination |
| Child 内部实现事实 | Child | | YES，限合同边界 | Child Governance |

> Child 对 Parent 事实只保留精确引用；携带副本时标记 `REFERENCE_SNAPSHOT`，不得成为 Current Truth。

## 4. 输入、接口和约束

- Parent Requirements / Acceptance Criteria：
- Interface Contracts / Versions：
- Shared Data / State / Error Semantics：
- Security / Compliance / Data Integrity Constraints：
- Governance Version Compatibility：

## 5. 输出合同

- Required Outputs：
- Exact Target / Commit Requirement：
- Required Verification：
- Required Review Package：
- Child Acceptance Package：
- Rollback Requirement：

## 6. 权限与禁止事项

- Allowed Actions：
- Allowed Write Scope：
- Forbidden Actions / Side Effects：
- Commit / Push / Merge / Release Authority：
- `SUBAGENT_PERMISSION <= CALLER_PERMISSION`：适用且不可扩大。

## 7. 依赖与集成

- Upstream Dependencies：
- Downstream Consumers：
- Integration Work Package：
- Integration Owner：
- Conflict / Escalation Route：

## 8. 变更、失效与回滚

- Change Classification：
- Contract Invalidation Conditions：
- Child Acceptance Invalidation Conditions：
- Supersedes / Superseded By：
- Rollback Anchor / Steps：

## 9. 采用决定

```text
DECISION: APPROVED / CHANGES_REQUESTED / DEFERRED / REJECTED
AUTHORIZED_SCOPE:
EXPLICITLY_NOT_AUTHORIZED:
DECISION_OWNER:
DECISION_EVIDENCE:
```

涉及新的系统边界、公共接口、跨系统依赖、Acceptance Threshold 或重大风险时，本合同只有在正确 Human Project Owner 裁定后才可生效。

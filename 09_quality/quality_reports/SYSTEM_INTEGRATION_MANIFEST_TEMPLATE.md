# System Integration Manifest 模板

## 1. Integration Target

```text
MANIFEST_ID: {{SIM-XXX}}
PARENT_PROJECT_ID: {{PROJECT_ID}}
PARENT_BASELINE: {{BASELINE_ID_AND_ANCHOR}}
INTEGRATION_WORK_PACKAGE: {{WORK_PACKAGE_ID}}
INTEGRATION_COMMIT: {{FULL_COMMIT}}
STATUS: DRAFT / READY_FOR_REVIEW / ACCEPTED / STALE
PARENT_REVIEW_READINESS: READY / REVIEW_NOT_READY
```

## 2. Child Inputs

| Child ID | Repository / Path Ref | Governance Version | Commit / Tag | Baseline | Parent–Child Contract | Acceptance Package | C04 Decision | Interface Version |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 3. Composition Evidence

- Cross-child Requirement / Traceability Coverage：
- Interface Compatibility：
- Shared Data / State Consistency：
- Error / Recovery Composition：
- Security / Compliance / Data Integrity：
- Integration Build：
- Integration / System / Acceptance Tests：
- Performance / Reliability Evidence：
- Residual Risks / Approved Exceptions：
- Rollback Combination：

## 4. Review Readiness

- [ ] 所有必需 Child Commit / Tag 为精确不可变 Target；
- [ ] 所有必需 Child Acceptance Package 与当前 Commit 一致且未 `STALE`；
- [ ] 所有必须执行的 Child C04 均为 `PASS`，Open S0～S3 为 0；
- [ ] Parent–Child Contract 和接口版本一致；
- [ ] Integration Commit 可读取、可复现；
- [ ] 系统级验证和风险证据完整；
- [ ] Parent C04 Review Record 位置已定义。

任一必需项失败时：

```text
PARENT_REVIEW_READINESS: REVIEW_NOT_READY
FORMAL_GATE_DECISION: NOT_PRODUCED
```

## 5. Parent Review Scope

Parent C04 默认评审 Child 接受证据、接口一致性、组合行为和系统级接受条件，不重复评审所有 Child 内部实现。需要穿透检查时记录精确 Drill-down Target、原因和范围。

## 6. 最终引用

```text
PARENT_C04_REVIEW_RECORD:
PARENT_C04_DECISION:
SYSTEM_BASELINE_ADOPTION:
RELEASE_REFERENCE:
```

# IA-GOV-002：CR-GOV-002 影响分析

关联 Change：`CR-GOV-002`

当前版本：`v0.1.5`

目标身份：`v0.1.6`

变更分类：`SUBSTANTIVE / GOVERNANCE_CHANGE`

## 1. 影响矩阵

| 范围 | 影响 | 说明 |
|---|---|---|
| 产品目标、行为与 Current Truth | NO | 只修改通用治理模板，不迁移或重写产品事实 |
| C00～C06 基本职责 | NO | 仅补充 C00/C01/C02/C04/C05/C06 在既有职责中的执行要求 |
| 人工保留决策边界 | NO | 不增加或删除保留事项，只改善决定前的信息可理解性 |
| Human Determination Package | YES | 保留原机器字段，增加必须解释的路线、产物、风险和授权边界 |
| 反馈治理 | YES | 新增先登记后分流的通用 FB Owner，现场反馈降为分流后的下游记录 |
| 需求与验收模板 | YES | 新增预计变化场景和可验证 ETC Requirement 字段 |
| 架构与详细设计模板 | YES | 新增 Stable Core、Variation Point、变化局限和回退边界 |
| Testing Governance | YES | 增加有正式来源时的替换性、兼容性和必要回归验证；不改变风险分级 |
| C04 Finding / Decision | NO | 不改变 Readiness、Severity、二值 Decision 或关闭规则 |
| C02/C04 评审判据 | YES | 对适用 ETC 要求增加 Change Amplification 检查 |
| Traceability / ADR / V 模型 | NO | 沿用既有机制，ETC 实例通过既有 Requirement 和证据链追溯 |
| Lite | YES | 必须保留审批可理解性权威和反馈登记入口 |

## 2. One Fact, One Owner

- 审批可理解性：`AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md`；
- 授权生命周期和保留决策：`ROLE_INTERACTION_EXECUTION_POLICY.md`；
- 机器字段：`GOVERNANCE_EXECUTION_CONTRACTS.yaml`；
- FB 当前状态：`FEEDBACK_REGISTER.md`；
- ETC 稳定语义：`AI_ENGINEERING_RULES_V2.md` 第 38.9 节；
- 项目实例：各 PRD、SRS、架构、设计、测试和 Review Record。

没有新增产品 Current Truth 来源，也不要求多个文件复制同一当前状态。

## 3. 兼容性与升级

- 已批准产品需求、架构、接口、代码、测试和历史 Review Record 保持有效；
- 既有项目升级后不追溯重写历史产物；只对以后新建或实质修改的产物，以及当前明确适用的变化场景采用 ETC 字段；
- 未经证据确认的旧疑问或建议可以登记为 `UNKNOWN`，不得直接批量转成 BUG 或 CR；
- 既有通用反馈记录应迁移到 `FEEDBACK_REGISTER`，既有现场反馈仍可保留在 FIELD 记录并建立引用；
- 当前待人工决定事项在升级后应按新可理解性规则重新呈现，但不得因此扩大原授权；
- 本版本改变治理语义，正式采用后应执行 Baseline Relearn。
- 消费 `GOVERNANCE_EXECUTION_CONTRACTS.yaml` 的工具必须兼容 Schema `1.1` 的新增字段；不支持时显式降级为 `PROCEDURAL_FALLBACK`，不得静默忽略控制。

## 4. 验证范围

直接验证：

- Markdown 结构、链接与代码围栏；
- YAML 解析和合同枚举；
- Human Determination、反馈流和 ETC 术语一致性；
- One Fact, One Owner；
- Full / Lite 引用完整性；
- Template File Index 与目标文件集一致；
- Git whitespace、敏感信息和项目专有事实扫描。

不执行：

- 产品构建、产品测试、真实 Model 调用或外部项目迁移；
- 正式 C04、Commit、Tag、Push 或 Release。

## 5. Remaining Risks

- ETC 的量化边界需要各项目根据实际变化成本和风险填写，框架不能替项目发明阈值；
- `PROCEDURAL_FALLBACK` 下，反馈先登记和审批可理解性仍依赖执行者遵循检查表；
- 历史项目的反馈可能缺少原始证据，必须保留 `UNKNOWN`，不能猜测分类；
- 替换性与兼容性测试若没有需求来源，可能再次造成测试膨胀，因此继续受 Testing Governance 限制。

## 6. 结论

```text
IMPACT_SCOPE: GOVERNANCE_CLARIFICATION_AND_CHANGEABILITY_QUALITY
REAPPROVAL_SCOPE: V0.1.6_RELEASE_CANDIDATE
REGRESSION_SCOPE: DOCUMENT_CONTRACT_LINK_AND_INDEX_CONSISTENCY
UNAFFECTED_APPROVALS_PRESERVED: YES
REMAINING_UNKNOWN: PROJECT_SPECIFIC_ETC_THRESHOLDS
NEXT_ACTION: CREATE_EXACT_RELEASE_COMMIT_THEN_RUN_FORMAL_C04
```

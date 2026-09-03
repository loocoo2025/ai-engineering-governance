# AI Software Engineering Governance Framework v0.1.6

# AI 软件工程治理框架 v0.1.6

面向长周期 AI 软件开发的模型无关工程治理框架。

## 新增

- 增加独立的人机协作及审批可理解性权威规则：正式请求决定前，必须解释路线、阶段、产物用途、内容变化、风险、选项和授权边界；
- 增加通用 `FEEDBACK_REGISTER` 与反馈明细模板，支持疑问、体验问题、治理缺口、改进建议、疑似缺陷和现场报告先登记、后分类；
- 将 ETC（Easier To Change，更容易变更）提升为正式质量属性、设计输入和评审判据；
- 增加 Stable Core、Variation Point、Change Amplification、替换性测试和兼容性测试的受控语义。

## 变更

- PRD 记录预计变化场景，SRS / Acceptance Criteria 将其转为可验证的可变更性要求；
- 架构区分稳定核心和变化点，详细设计说明变化应局限的模块、兼容与回退边界；
- C02/C04 对适用 ETC 要求检查变化实际影响的模块、接口、数据、事实副本、测试和回退范围；
- C05 对有正式来源的 ETC 要求执行最小充分的替换性、兼容性和必要回归验证；
- 通用反馈不再直接落到现场反馈模板；FIELD 成为完成 FB 分流后的下游记录。
- `GOVERNANCE_EXECUTION_CONTRACTS.yaml` Schema 升级为 `1.1`，为审批可理解性和反馈登记/分流提供机器字段与枚举。

## 兼容性

- 不改变 Current Truth、One Fact One Owner、C00～C06、C04 Decision Matrix、V 模型、ADR、Traceability 或既有产品事实；
- 不要求追溯重写历史需求、架构、设计、测试或 Review Record；
- ETC 不授权投机性架构、无来源测试、无关重构或超出当前权限的变更；
- 正式采用时需要增加新的审批权威和反馈登记文件，并执行 Baseline Relearn。
- 消费机器合同的工具必须兼容 Schema `1.1` 新增字段；不支持时显式降级为 `PROCEDURAL_FALLBACK`，不得静默忽略控制。

## 从 v0.1.5 升级

使用通用治理升级协议并锁定精确 `v0.1.6` Tag / Commit。迁移时：

1. 新增 `AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md`、`FEEDBACK_REGISTER.md` 和 `FEEDBACK_TEMPLATE.md`；
2. 将既有通用反馈状态迁移到 FB Register；现场记录继续作为 `FIELD` 下游产物，不复制 FB 当前状态；
3. 保留所有产品事实和历史产物；只为以后新建、实质修改或当前明确适用的产物补充 ETC 输入与证据；
4. 更新 C00～C06 Role Brief、治理合同和相关需求/架构/设计/测试/Review Template；
5. 验证工具兼容 Schema `1.1`，完成治理 Candidate、适用的独立 C04、显式 Baseline Adoption 和 Baseline Relearn。

升级不得自动重开已完成阶段，也不得把旧反馈猜测为 BUG / CR，或为历史产物批量发明 ETC 场景和阈值。

## 已知限制

- ETC 的量化边界必须由采用项目根据实际变化成本、风险和接受条件定义，框架不会替项目发明阈值；
- `PROCEDURAL_FALLBACK` 仍依赖执行者遵循审批说明与反馈登记检查；
- 消费治理合同的工具需要显式兼容 Schema `1.1`，否则只能声明为程序性执行；
- 上游稳定版发布不会自动替任何下游项目执行 Governance Baseline Adoption。

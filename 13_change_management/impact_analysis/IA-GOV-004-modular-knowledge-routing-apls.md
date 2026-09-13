# IA-GOV-004：CR-GOV-004 影响分析

关联 Change：`CR-GOV-004`

当前版本：`v0.1.7`

目标身份：`v0.1.8`

变更分类：`SUBSTANTIVE / GOVERNANCE_CHANGE`

## 1. 影响矩阵

| 范围 | 影响 | 说明 |
|---|---|---|
| 产品事实、需求、架构和代码 | NO | 只修改公开治理模板 |
| C00～C06 固定职责 | NO | C02 仍负责架构与详细设计，其他岗位边界不变 |
| 启动与知识加载 | YES | 最小启动内核通过 Router 和 Domain INDEX 按需加载 |
| 规则事实 Owner | COMPATIBLE | 正文迁移到原子文件；旧路径只做兼容映射 |
| Session 与 Worktree | NO_SEMANTIC_CHANGE | 仅物理拆分现有规则，不改变语义 |
| C04 / Traceability / Testing | NO_SEMANTIC_CHANGE | Gate 与 Decision 保持不变 |
| APLS | OPTIONAL_NEW | 默认 `DOCUMENT_BASED`；明确启用后才加载 |
| C02 | YES | 增加 Design Allocation 和 APLS 交付合同 |
| C03/C04/C05 | COMPATIBLE | 只在 APLS 启用且范围适用时消费、评审或验证 |
| 框架更新 | YES | 纳入 GitHub/Gitee、双语提醒和用户导向升级 |
| 既有项目 | COMPATIBLE | 未启用 APLS 的项目行为不变；旧入口仍可解析 |

## 2. One Fact, One Owner

- 最小知识加载和 Rule Gap 稳定语义：`ROLE_INTERACTION_EXECUTION_POLICY.md` 第 3 节；
- 机器路由配置：`GOVERNANCE_ROUTER.yaml`；
- 领域路由：各 Domain `INDEX.yaml`；
- 工程规则正文：`modules/engineering/*.md`；
- Session 规则正文：`modules/sessions/*.md`；
- APLS 设计分配：`integrations/apls/APLS_DESIGN_ALLOCATION_POLICY.md`；
- APLS 当前启用值：`CURRENT_STATE.md`；
- 旧根文件：仅兼容入口，不维护竞争正文。

## 3. 兼容与升级

- 已采用旧版的项目可以继续使用旧路径；进入新任务时由兼容入口转到新模块；
- 不要求追溯改写旧 HANDOFF、Review Record 或历史引用；
- 新版 Baseline Relearn 必须学习最小启动内核和 Router，不再默认读取所有大文件；
- 项目只有在明确选择 `APLS_ENABLED` 并固定精确 APLS 版本后才采用 APLS；
- APLS 工具不可用时保持 `DOCUMENT_BASED`，不得模拟 Verified IR。

## 4. 验证范围

直接验证：YAML 解析、Router/INDEX 引用、原子文件完整性、旧章节映射、Markdown Fence、文件索引、敏感信息、Git whitespace、公开源和精确版本字段。

不执行：外部产品 Build/Test、修改 APLS 项目、真实 APLS 项目迁移、Formal Seal 或历史改写。

## 5. Remaining Risks

- 文档拆分后，第三方 Agent 若忽略 Router 仍可能漏读规则；
- `PROCEDURAL_FALLBACK` 下无法强制工具只加载最小范围；
- APLS v0.1.0 的表达范围有限，项目必须显式处理 `APLS_PROFILE_GAP`；
- 旧版本的深层章节链接需要通过兼容入口映射，不能保证所有外部渲染器自动跳转；
- 过度细分会增加导航成本，因此 Router 深度限制为三层。

## 6. 结论

```text
IMPACT_SCOPE: GOVERNANCE_KNOWLEDGE_LOADING_AND_OPTIONAL_APLS_C02_INTEGRATION
REAPPROVAL_SCOPE: V0.1.8_RELEASE_CANDIDATE
REGRESSION_SCOPE: ROUTER_INDEX_OWNER_REFERENCE_COMPATIBILITY_AND_RELEASE_GATE
UNAFFECTED_APPROVALS_PRESERVED: YES
NEXT_ACTION: COMPLETE_MIGRATION_VALIDATE_EXACT_CANDIDATE_THEN_FORMAL_C04
```

# AI Software Engineering Governance Framework v0.1.8

# AI 软件工程治理框架 v0.1.8

面向长周期 AI 软件开发的模型无关工程治理框架。

## 本版本是什么

`v0.1.8` 将治理知识从每次全文加载的大文件转为“最小启动内核 → 总 Router → Domain INDEX → 原子规则”的按需加载结构，并增加 APLS 在 C02 的可选设计分配能力。同时包含 GitHub/Gitee 官方源、中英文更新提醒和用户控制的受控升级入口。

## 新增

- `GOVERNANCE_ROUTER.yaml`：按 Project、Role、Task、Action、Gate、Risk 和启用集成选择最小知识包；
- Startup、Engineering、Session 三类 Domain INDEX 和按语义拆分的原子规则；
- Router 深度上限、依赖递归、Knowledge Manifest 和 Rule Gap 失败关闭；
- APLS Design Allocation Table，以及 `APLS / DETAILED_DESIGN / ALGORITHM_SPEC / TARGET_PROFILE / SPEC_GAP / APLS_PROFILE_GAP` 分类；
- APLS Source、`apls check`、Verified IR、Digest、详细设计和追溯的 C02→C03 交付合同；
- GitHub 主发布源和 Gitee 官方镜像；
- C00 新物理 Session 的只读稳定版检查和中英文双语提醒；
- `VIEW_CHANGES / UPGRADE_LATEST_STABLE / UPGRADE_EXACT_VERSION / SKIP_FOR_CURRENT_SESSION` 用户动作。

## 兼容性

- 旧根文件继续存在，用于旧路径和旧章节号映射；历史 Review Record 不追溯改写；
- 未启用 APLS 的项目默认 `DOCUMENT_BASED`，不增加工具依赖；
- APLS 是外部可选能力，不被复制或绑定为框架必备组件；
- 不改变 C00～C06、Current Truth、Baseline、C04 Decision Matrix、Traceability、Testing Governance、Worktree 或 Release Gate；
- 更新检查只读，提醒不构成升级授权。

## APLS

- 官方 Repository：`https://github.com/loocoo2025/apls-language`；
- 本框架默认支持：`v0.1.0`；
- 精确 Release Commit：`fd8b59536fcdfdff2f3b199b882c15d97edb1993`；
- 项目必须明确选择 `APLS_ENABLED` 才进入 C02 APLS 路由；
- 编译器拒绝、版本不明或不能产生 Verified IR 时失败关闭，AI 不得猜测语义。

## 从 v0.1.7 升级

1. 使用精确 `v0.1.8` Tag / Commit 执行治理升级协议；
2. 保留旧根入口，同时增加 Router、Domain INDEX 和原子规则目录；
3. 新 Session 先完整阅读新的最小 `AI_START_HERE.md`，再按 Router 加载规则；
4. 默认保持 `BEHAVIOR_SPECIFICATION_MODE: DOCUMENT_BASED`；只有项目负责人批准采用 APLS 时改为 `APLS_ENABLED`；
5. 核验现有 Role、Task、Gate、Baseline、Review 和产品事实未被模板覆盖；
6. 完成适用 C04、明确 Baseline Adoption 和 Baseline Relearn。

## 已知限制

- `PROCEDURAL_FALLBACK` 不能强制第三方 Agent 正确执行按需加载；
- 部分旧文档的深层章节 URL 需要先经兼容入口映射；
- APLS v0.1.0 只表达其已发布 Profile 支持的行为，超出范围必须记录 `APLS_PROFILE_GAP`；
- 框架更新提醒发生在 C00 启动检查点，不是后台守护进程。

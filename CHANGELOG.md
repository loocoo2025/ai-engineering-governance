# 变更日志

## [0.1.3] - 2026-08-25
### 新增
- 将现有术语表扩展为中英文专有名词、缩写、编号前缀、治理角色、分级和受控状态索引。
- 增加可复用的跨版本治理升级执行协议，支持已知版本和 `UNKNOWN_LEGACY` 项目升级到精确指定版本或上游最新稳定版本。

### 变更
- 将治理模板升级记录扩展为完整执行流程：自动解析稳定 SemVer Tag、逐版本读取迁移信息、分类合并治理文件并形成独立本地 Commit。
- 增加只读 `UPGRADE_READINESS_GATE`，在工作区不干净、正式 C04 进行中、Current Truth 冲突、目标版本不可验证或存在未授权 Breaking Change 时停止升级。

## [0.1.2] - 2026-08-25
### 新增
- 增加最小 Review Decision Matrix 和正式 Review Readiness 前置状态。
- 为 Code Review 增加标准 Finding 记录、Severity、关闭状态和 Advisory 结构。

### 变更
- 分离 `QUESTION_PRIORITY / WORK_PRIORITY` P0～P3 与 `C04_FINDING_SEVERITY` S0～S3。
- 统一 Requirement、Architecture、Design 和 Code Review 的 Readiness、Finding、Advisory 与 `PASS / CHANGES_REQUESTED` 语义。
- 明确 Open Finding 阻断 `PASS`，非阻断项使用 Advisory / Observation / Future Improvement，正式 Exception 仍由现有 Decision / Risk Owner 批准。

## [0.1.1] - 2026-08-24
### 修复
- 澄清 `Role != Model != Harness != Tool`，明确高能力模型和工具调用不产生正式决策权或治理角色。
- 明确辅助调用不等于正式 C04，并规定子 Agent、子模型和工具不得扩大调用者授权。

## [0.1.0] - 2026-08-24
### 新增
- 增加 `Primary Executor + Expert Escalation + Independent Reviewer + Human Authority` 可配置执行路由。
- 增加 `SUPERVISED_AUTO` 默认 Autonomy Envelope、最小 Escalation Package 和模型替换恢复规则。
- 执行槽位增加 Model/Harness 双维配置，并完整定义 `MANUAL_GATE / SUPERVISED_AUTO / FULL_AUTO` 授权边界。
- 增加 Apache License 2.0、贡献指南、安全政策和 Full/Lite 开源采用指南。
- 准备独立干净历史的首次公开 Release Candidate。
### 变更
- C00～C06 与具体 Model/Harness 解耦；当前路由和授权只由 `CURRENT_STATE.md` 维护。
- P0/P1 默认先进入 Expert Escalation；修改 Current Truth、改变产品目标、降低 Acceptance Threshold、接受重大风险或执行未预授权重大 Gate/Release 时请求项目负责人。
- C04 强制使用全新独立上下文，并允许高能力 Reviewer fallback 而不改变评审标准。
- C04 形成 Finding 后停止且不得自行关闭，由 Primary Executor / C00 组织 Expert 整改和新独立 C04 复审。
- 旧项目迁移提示同步采用 Expert 优先、人工权威事项再转负责人的路由。
- 重写仓库首页与启动说明，明确框架定位、架构、五分钟入门、Agent 支持和 Full/Lite 差异。
### 修复
-

# AI Software Engineering Governance Framework v0.1.7

# AI 软件工程治理框架 v0.1.7

面向长周期 AI 软件开发的模型无关工程治理框架。

## 新增

- `SINGLE_PROJECT / MODULAR_PROJECT / FEDERATED_PROJECT` 三种项目结构模式；
- 任意层级 Work Package 递归分解，以及 `LEAF_EXECUTION / INTEGRATION` 写入执行单元；
- Parent–Child Project Contract、Child Acceptance Package 和 System Integration Manifest；
- 单写入 Session、单活动 `LEAF_EXECUTION / INTEGRATION` Work Package、单 Output Contract、单 Worktree、单活动 Writer 的绑定；
- 多个并行写入 Session 使用独立 Git Worktree，同一 Local Working Directory 同时只能有一个 Writer；
- Task-local Handoff、Write Lease 转移和 Completion Capsule；
- 子级独立评审证据向上汇总、父级聚焦组合与系统级风险的递归评审模型。

## 兼容性

- 既有项目默认保持 `SINGLE_PROJECT`；
- 不追溯重写已完成任务、Review Record 或 Handoff；
- 不改变 C00～C06、Current Truth、C04 Decision Matrix、Traceability、Testing Governance 或 Release Gate；
- 无法建立独立 Worktree 时禁止并行写入，允许退回串行单 Writer；
- 子级 `PASS` 不自动等于父级 Acceptance、系统 Baseline 或 Release。

## 从 v0.1.6 升级

1. 增加项目分解 Authority、`PROJECT_STRUCTURE_MAP` 和三个配套模板；
2. 未拆分项目选择 `SINGLE_PROJECT`，无需制造 Child 记录；
3. 新建/重新分解的任务补齐 Work Package、Output Contract 和 Workspace Binding；
4. 并行写入前为每个 Worker 分配独立 Worktree、Branch、Write Scope 和 Write Lease；
5. 联邦项目建立 Parent–Child Contract，并在 Parent Baseline 中精确固定 Child Commit / Tag；
6. 正式接受 Child Package 和系统集成 Target 时按新分层 C04 规则执行；
7. 正式采用后执行 Baseline Relearn。

上游发布不会自动替任何下游项目完成 Governance Baseline Adoption。采用项目仍必须使用精确 `v0.1.7` Tag / Commit，保留升级前回滚 Anchor，并按治理升级协议完成 Readiness、迁移、适用 C04、显式采用和 Baseline Relearn。

## 已知限制

- 本候选只定义治理合同，不提供 Worktree 调度软件；
- `PROCEDURAL_FALLBACK` 不能证明操作系统级写锁；
- 项目专有拆分深度、并行度和集成策略必须由项目根据架构与风险决定。

# CR-GOV-003：可扩展项目分解、分层评审与 Worktree 并行治理

## 0. 文档控制

```text
CHANGE_TYPE: GOVERNANCE_CHANGE
SEMANTIC_LEVEL: SUBSTANTIVE
STATUS: APPROVED_FOR_RELEASE_EXECUTION
CURRENT_VERSION: v0.1.6
SOURCE_COMMIT: 99f9ecc3f5f7d1be9b4391de7edc9bc9daaad8c3
TARGET_IDENTITY: v0.1.7
HUMAN_PROJECT_OWNER: Project Owner
DATE: 2026-09-11
```

## 1. 问题

长周期治理已经支持最小知识加载、递归 Work Package 和 Context Handoff，但大型项目仍可能要求单个 Session 理解过多模块细节。现有规则尚未完整定义：

1. 单写入 Session、单叶子任务、单 Output Contract 和单 Worktree 的绑定；
2. 多个写入 Session 使用独立 Git Worktree 并行、同一 Local Working Directory 只有一个 Writer；
3. 只交接当前未完成叶子任务上下文；
4. 父任务依赖子级独立评审证据并审核组合，而不是重新审查所有实现细节；
5. 多级 Subproject / Module / Work Package 的递归分解；
6. 多个独立项目文件夹或 Repository 的父子事实 Owner、版本固定和系统集成方式。

## 2. 已批准目标

- 显式支持 `SINGLE_PROJECT / MODULAR_PROJECT / FEDERATED_PROJECT`；
- Work Package 可以递归拆分，只有 `LEAF_EXECUTION / INTEGRATION` 成为写入执行单元；
- 一个写入 Session 绑定一个活动叶子 Work Package、一个 Output Contract、一个 Git Worktree 和一个活动 Writer；
- 多个并行写入 Session 必须使用不同 Worktree 和分支；同一本地目录同时只能有一个 Writer；
- 上下文交接只携带当前未完成叶子任务的最小相关上下文；
- 子级通过精确 Child Acceptance Package 向上交付；
- 父级评审依赖有效子级独立评审证据，聚焦接口、集成、系统要求和组合风险；
- Root / Parent 与 Child 各自维护不同事实，禁止复制形成竞争性 Current Truth；
- 形成 `v0.1.7` 正式 Release Candidate，经精确 Commit、独立 C04 和机械 Gate 通过后发布稳定版本。

## 3. 不变量

- 不改变 C00～C06 固定岗位和 C04 二值 Decision；
- 不降低 C04 独立性、Open Finding 关闭、Traceability、Testing 或 Release Gate；
- 不改变现有产品事实、需求、架构、接口、代码或测试；
- 不要求每个微小 Leaf Task 自动执行正式 C04；
- 不把 Worktree 隔离错误解释为语义冲突已经解决；
- 不允许 Child 扩大 Parent 授权；
- 不允许父级通过摘要绕过系统级集成和 Acceptance Criteria；
- 不修改任何采用本框架的外部产品项目。

## 4. 初始 Candidate 授权边界

允许修改本治理模板的权威规则、机器合同、Role Brief、Task/Handoff/Baseline 模板、README、使用文档、索引和 Candidate 记录，并执行本地机械检查。

不允许：

- Commit、Tag、Push、PR 或 Release；
- 正式 C04、Baseline Adoption 或 Formal Seal；
- 创建或修改任何外部产品项目、远程系统或真实项目 Worktree；
- 删除或处理既有未跟踪文件。

该边界记录最初形成 Candidate 时的授权，不得被解释为当时已经授权发布。

## 5. Release 授权

Human Project Owner 已于 `2026-09-11` 明确要求发布正式 `v0.1.7`。该授权允许：

- 将 Candidate 文案收口为稳定版本；
- 形成精确 Release Candidate Commit；
- 建立独立只读 C04 Session 并评审该精确 Commit；
- C04 `PASS` 且 Open S0～S3 为 0 后创建 `v0.1.7` Tag；
- Push `main` 和 Tag，生成 Git archive，并创建非 Draft、非 Prerelease 的 GitHub Release。

该授权不允许绕过正式 C04、改写历史、Force Push、修改外部产品项目或处理无关未跟踪文件。

## 6. Release Gate

```text
RECURSIVE_DECOMPOSITION_READY: YES
ONE_SESSION_ONE_OUTPUT_CONTRACT_READY: YES
WORKTREE_SINGLE_WRITER_READY: YES
TASK_LOCAL_HANDOFF_READY: YES
COMPOSITIONAL_REVIEW_READY: YES
FEDERATED_PROJECT_INTEGRATION_READY: YES
ONE_FACT_ONE_OWNER_CHECK: PASS
MECHANICAL_VALIDATION: PASS
FORMAL_C04: REQUIRED_ON_EXACT_COMMIT
OPEN_S0_TO_S3_REQUIRED: 0
TAG_TARGET_MUST_MATCH_RELEASE_TARGET: YES
PRERELEASE: NO
FINAL_STATUS: V0.1.7_RELEASED_OR_PUBLICATION_BLOCKED
```

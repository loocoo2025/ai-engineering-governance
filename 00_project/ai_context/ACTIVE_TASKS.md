# ACTIVE_TASKS.md
## 当前任务注册表（任务级状态唯一权威源）

> 本文件只负责“任务本身”的状态、责任角色、输入和输出。
>
> 项目当前阶段、评审/Gate 状态、授权边界和下一步由 `CURRENT_STATE.md` 维护，不要在任务描述中复制成另一套 Current Truth。
>
> 本文件同时是 Task / Work Package、Output Contract、Workspace Binding 和 Write Lease 当前状态的唯一实例 Owner。稳定的项目分解语义见 `PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`，Session/Worktree 操作规则见 `00_project/governance/modules/sessions/WORKTREE_WRITE_LEASE_AND_RETURN.md`。

| Task | 类型 | 责任角色 | 输入 | 输出 | 任务状态 |
|---|---|---|---|---|---|
| TASK-001 | PRODUCT/STANDARDIZATION | CXX | | | TODO |

任务状态只使用：

```text
TODO
READY
IN_PROGRESS
BLOCKED
OUTPUT_READY
READY_FOR_REVIEW
DONE
CANCELLED
```

## 任务状态机

正常主线：

```text
TODO
→ READY
→ IN_PROGRESS
→ OUTPUT_READY
→ DONE
```

只有当前任务确实命中适用 Review Line 时，才允许：

```text
OUTPUT_READY
→ READY_FOR_REVIEW
→ DONE
```

`READY_FOR_REVIEW` 必须同时引用 `SELF_REVIEW / CONTEXTUAL_REVIEW / INDEPENDENT_REVIEW` 中实际适用的路线。该状态本身不自动触发正式 C04；正式 C04 是否必须执行仍由 `PROJECT_ASSURANCE_CADENCE_POLICY.md` 判定。

受控分支：

| 当前状态 | 允许下一状态 | 条件 |
|---|---|---|
| `TODO` | `READY / CANCELLED` | 输入和依赖满足后才能 READY |
| `READY` | `IN_PROGRESS / BLOCKED / CANCELLED` | 开始执行前 Role Profile 和 Authorization 必须就绪 |
| `IN_PROGRESS` | `OUTPUT_READY / BLOCKED / CANCELLED` | 输出形成且 Self Review/最小验证完成后才能 OUTPUT_READY |
| `OUTPUT_READY` | `READY_FOR_REVIEW / DONE / BLOCKED` | 只有适用评审要求存在时进入 READY_FOR_REVIEW；否则满足 DoD 后 DONE |
| `READY_FOR_REVIEW` | `DONE / IN_PROGRESS / BLOCKED` | 通过适用检查后 DONE；要求整改时回 IN_PROGRESS |
| `BLOCKED` | `READY / IN_PROGRESS / OUTPUT_READY / READY_FOR_REVIEW / CANCELLED` | 阻断关闭后回到阻断前最近合法状态 |
| `DONE` | 无 | 终态；后续工作建立新 Task 并引用本 Task |
| `CANCELLED` | 无 | 终态；恢复工作必须建立新 Task 和新授权 |

禁止：

- 跳过 `READY / IN_PROGRESS` 直接把未执行任务标为 `DONE`；
- 用 `OUTPUT_READY` 宣称项目 Gate 已通过；
- 用 `READY_FOR_REVIEW` 宣称 C04 已成立或 `PASS`；
- 在没有证据时从 `BLOCKED` 恢复；
- 原地重开 `DONE / CANCELLED`，从而抹去历史终态；
- 让 Interaction、Review、Baseline 或 Release 状态反向覆盖 Task 状态 Owner。

规则：

- 一个任务 `DONE` 不等于项目 Gate `PASS`；
- 一个任务 `READY_FOR_REVIEW` 不等于 C04 `ACCEPTED`；
- 一个任务 `DONE` 不等于对应产物已形成 Formal Seal、Baseline Adoption 或 Release；
- 项目级结论只能写入 `CURRENT_STATE.md` 或正式 review/baseline 记录；
- 历史完成任务可归档，不应把旧任务状态复制回 `CURRENT_STATE.md`。

## 有边界的 Work Package

大型任务可以任意层级递归拆分为 Work Package。每个包的状态仍由本文件维护，不新增任务状态 Owner。

```text
WORK_PACKAGE_ID:
PARENT_WORK_PACKAGE_ID:
PROJECT_ID:
SUBPROJECT_ID: {{ID_OR_NOT_APPLICABLE}}
MODULE_ID: {{ID_OR_NOT_APPLICABLE}}
WORK_PACKAGE_TYPE: COORDINATION / LEAF_EXECUTION / INTEGRATION / REVIEW_PACKAGE
LEAF_EXECUTABLE: YES / NO
OBJECTIVE:
BOUNDARY:
INPUTS:
OUTPUTS:
OUTPUT_CONTRACT_ID:
DEPENDENCIES:
RISKS:
APPLICABLE_REQUIREMENTS_AND_DECISIONS:
OWNER_ROLE:
VERIFICATION:
DEFINITION_OF_DONE:
REVIEW_PACKAGE_ID: {{ID_OR_NOT_APPLICABLE}}
STATUS:
```

规则：

- 子包 `DONE` 不自动等于父包或项目 Gate 通过；
- 父包负责跨包关系、集成和剩余风险；
- 拆包不自动增加人工 Gate；
- 不得通过拆包隐藏跨包接口、追溯或集成风险。
- 只有 `LEAF_EXECUTION / INTEGRATION` 可以成为写入执行单元；`COORDINATION / REVIEW_PACKAGE` 不得混入多个子包实现；
- 跨兄弟包的修改必须拆成各自叶子包，并建立单独的 `INTEGRATION` Work Package；
- 叶子包进入 `READY` 前必须具备明确 Boundary、Inputs、Output Contract、Dependencies、Write Scope、Verification 和 Definition of Done；
- `EXECUTION_UNIT != REVIEW_UNIT`：一个 Review Package 可以覆盖多个已冻结叶子包，但子包 `DONE` 不自动产生正式 C04 `PASS`。

## Output Contract

每个写入执行单元只能绑定一个当前 Output Contract：

```text
OUTPUT_CONTRACT_ID:
WORK_PACKAGE_ID:
OBJECTIVE:
EXPECTED_OUTPUTS:
ALLOWED_PATHS:
FORBIDDEN_PATHS:
INPUT_COMMIT:
DEPENDENCY_CONTRACTS:
ACCEPTANCE_CRITERIA:
REQUIRED_VALIDATION:
OUTPUT_COMMIT: {{FULL_COMMIT_OR_NOT_ESTABLISHED}}
MERGE_TARGET:
INTEGRATION_OWNER:
STATUS: DRAFT / READY / IN_PROGRESS / OUTPUT_READY / ACCEPTED / STALE / CANCELLED
```

“一个 Output”可以由共同完成一个原子交付目的的代码、测试和必要文档组成，不等于只能修改一个文件。目标、边界或接受条件发生实质变化时，原 Contract 标记 `STALE`，重新校验 Task、Authorization 和 Workspace Binding。

## Workspace Binding 与 Write Lease

| Work Package | Session | Worktree ID / Path | Branch | Base Commit | Write Scope | Lease Status | Output Contract |
|---|---|---|---|---|---|---|---|
| | | | | | | `UNASSIGNED / ALLOCATED / ACTIVE / HANDOFF_PENDING / OUTPUT_READY / FROZEN / INTEGRATED / RETIRED` | |

机械规则：

```text
ONE_WRITE_SESSION
= ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE
= ONE_OUTPUT_CONTRACT
= ONE_GIT_WORKTREE
= ONE_ACTIVE_WRITER

ONE_LOCAL_WORKING_DIRECTORY
<= ONE_ACTIVE_WRITER
```

`ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE` 只允许 `LEAF_EXECUTION / INTEGRATION`。

- 多个并行写入 Session 必须使用不同 Git Worktree 和不同 Branch；
- 同一 Worktree / Local Working Directory 同一时间最多一个 `ACTIVE` Writer；
- 同一 Output Contract 不得由多个 Session 并行写入；上下文接续必须先冻结旧 Session，再转移 Write Lease；
- 不同 Worktree 的 Write Scope 默认不得重叠；必须修改共享文件或接口时，串行执行或先建立上游/Integration Work Package；
- 无 Git、无法建立 Worktree 或无法证明 Write Lease 唯一时，禁止并行写入，只能串行单 Writer；
- Worktree、Commit、Merge、Push 和 Release 分别受权，不因存在 Workspace Binding 自动获得权限；
- Parent / C00 通过精确 Commit 和 Completion / Acceptance Package 接收结果，不接收未锚定的“已经完成”声明。

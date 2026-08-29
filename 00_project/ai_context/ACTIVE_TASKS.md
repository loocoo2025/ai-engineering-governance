# ACTIVE_TASKS.md
## 当前任务注册表（任务级状态唯一权威源）

> 本文件只负责“任务本身”的状态、责任角色、输入和输出。
>
> 项目当前阶段、评审/Gate 状态、授权边界和下一步由 `CURRENT_STATE.md` 维护，不要在任务描述中复制成另一套 Current Truth。

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

大型任务可以递归拆分为 Work Package。每个包的状态仍由本文件维护，不新增任务状态 Owner。

```text
WORK_PACKAGE_ID:
PARENT_WORK_PACKAGE_ID:
OBJECTIVE:
BOUNDARY:
INPUTS:
OUTPUTS:
DEPENDENCIES:
RISKS:
APPLICABLE_REQUIREMENTS_AND_DECISIONS:
OWNER_ROLE:
VERIFICATION:
DEFINITION_OF_DONE:
STATUS:
```

规则：

- 子包 `DONE` 不自动等于父包或项目 Gate 通过；
- 父包负责跨包关系、集成和剩余风险；
- 拆包不自动增加人工 Gate；
- 不得通过拆包隐藏跨包接口、追溯或集成风险。

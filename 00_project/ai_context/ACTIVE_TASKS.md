# ACTIVE_TASKS.md
## 当前任务注册表（任务级状态唯一权威源）

> 本文件只负责“任务本身”的状态、责任角色、输入和输出。
>
> 项目当前阶段、评审/Gate 状态、授权边界和下一步由 `CURRENT_STATE.md` 维护，不要在任务描述中复制成另一套 Current Truth。

| Task | 类型 | 责任角色 | 输入 | 输出 | 任务状态 |
|---|---|---|---|---|---|
| TASK-001 | PRODUCT/STANDARDIZATION | CXX | | | TODO |

任务状态建议仅使用：

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

规则：

- 一个任务 `DONE` 不等于项目 Gate `PASS`；
- 一个任务 `READY_FOR_REVIEW` 不等于 C04 `ACCEPTED`；
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

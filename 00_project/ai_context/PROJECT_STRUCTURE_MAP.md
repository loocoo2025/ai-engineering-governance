# 项目结构与父子关系图

> 本文件是当前项目/模块/子项目拓扑、关系身份和关系生命周期的唯一实例 Owner。
>
> 它不维护任务状态、Session/Worktree Lease、项目 Gate、Baseline 组成或子项目内部 Current Truth。

## 1. 当前结构模式

```text
PROJECT_ID: {{PROJECT_ID}}
PROJECT_STRUCTURE_MODE: SINGLE_PROJECT / MODULAR_PROJECT / FEDERATED_PROJECT
ROOT_PROJECT_ID: {{ROOT_PROJECT_ID_OR_SELF}}
PARENT_PROJECT_ID: {{PARENT_PROJECT_ID_OR_NOT_APPLICABLE}}
PARENT_CONTRACT_REF: {{EXACT_REFERENCE_OR_NOT_APPLICABLE}}
REPOSITORY_MODE: SHARED_REPOSITORY / INDEPENDENT_REPOSITORY / NOT_APPLICABLE
GOVERNANCE_VERSION: {{EXACT_VERSION_AND_COMMIT}}
```

稳定语义见 `00_project/governance/PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`。

## 2. Governed Subproject 关系

| Child Project ID | 类型 | 关系状态 | Repository / Path Reference | Parent–Child Contract | 接口/边界引用 | 当前版本组合 |
|---|---|---|---|---|---|---|
| | `GOVERNED_SUBPROJECT` | `PROPOSED / ACTIVE / SUSPENDED / RETIRED` | | | | 见 `BASELINE_INDEX.md` |

> 这里只记录关系，不复制 Child 的当前阶段、任务、Finding 或内部 Baseline 正文。

## 3. Module 关系

| Module ID | Parent ID | 边界 | 接口引用 | 责任角色 | 关系状态 |
|---|---|---|---|---|---|
| | | | | | `PROPOSED / ACTIVE / RETIRED` |

Module 的任务状态见 `ACTIVE_TASKS.md`，模块架构正文见 `03_architecture/` 和 `04_design/`。

## 4. 集成关系

| Integration ID | Parent Scope | Child/Module Inputs | Contract References | Manifest / Evidence |
|---|---|---|---|---|
| | | | | |

## 5. 完整性检查

- [ ] 每个 Child / Module ID 唯一；
- [ ] 每个非根节点只有一个当前 Parent；
- [ ] 每个 Parent–Child 关系有精确 Contract；
- [ ] 没有在本文件复制 Task、Gate、Finding 或 Child Current Truth；
- [ ] 联邦项目的精确版本组合由 `BASELINE_INDEX.md` 维护；
- [ ] Retired 关系未继续作为当前集成输入。

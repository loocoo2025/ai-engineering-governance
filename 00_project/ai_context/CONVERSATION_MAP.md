# CONVERSATION_MAP.md
## AI 对话/角色拓扑（对话生命周期唯一权威源）

> 本文件只记录：**有哪些逻辑角色/对话、当前版本、对话生命周期状态、主要职责和写入范围。**
>
> 本文件不记录项目当前 Gate、R04/R05 结论、当前整改 finding、等待授权或下一步。
>
> 项目动态当前态统一见 `CURRENT_STATE.md`；任务明细见 `ACTIVE_TASKS.md`。

---

# 1. 对话地图

| ID | 角色 | 版本 | 对话状态 | 主要职责 | 主要写入范围 |
|---|---|---|---|---|---|
| C00 | Control | v01 | ACTIVE | 项目控制、Current State、阶段协调 | `00_project` |
| C01 | Requirements | v01 | READY | 产品/系统需求 | `01/02` |
| C02 | Architecture/Design | v01 | READY | 架构/详细设计 | `03/04` |
| C03 | Implementation | v01 | READY | 实现 | `07` + unit tests |
| C04 | Independent Review | v01 | READY | 独立评审 | `05_reviews` |
| C05 | Verification/Release | v01 | READY | 验证/质量/发布 | `06/08/09/10/11/14` |
| C06 | Issues/Change | v01 | READY | Bug/变更/运维闭环 | `12/13/15` |

## 1.1 持续 C00 控制通道

- 项目负责人默认停留在逻辑 C00 控制通道；
- Expert、C04 和阶段 Worker 可以作为子 Session 创建，结果返回 C00；
- 普通阶段切换不自动关闭逻辑 C00；
- 物理 C00 Session 达到上下文阈值、完整性失效或需要 Clean Context Reset 时，记录 `C00-v01 -> C00-v02`，旧实例标记 `READ_ONLY`，新实例标记 `ACTIVE`；
- 自动创建本地或手动配置外部独立 Session 的规则见对话编排与外部 AI 配置，本文件只记录实际生命周期实例。

---

# 2. 对话状态定义

`ACTIVE`：当前存在并可继续承担该角色工作。

`READY`：角色已定义，但当前没有活动对话或尚未启用。

`READ_ONLY`：旧对话已冻结，只允许历史查阅。

`RETIRED`：已正式退出，不再作为当前角色实例。

> 这些状态只描述“对话实例生命周期”，不能拿来表达项目阶段或评审结论。

---

# 3. 写入冲突规则

- 同一正式文件同一时间原则上只有一个主要写入者；
- 并行写入必须通过明确的 Git 分支/worktree/合并授权管理；
- 旧版本对话切换后标记 `READ_ONLY`；
- 当前任务由 `ACTIVE_TASKS.md` 管理，不在本文件复制；
- 当前项目状态由 `CURRENT_STATE.md` 管理，不在本文件复制。

---

# 4. 维护触发条件

只有以下事实发生变化时才更新本文件：

- 新增/删除逻辑角色；
- 对话版本切换，例如 C03-v04 → C03-v05；
- 对话生命周期变为 ACTIVE / READY / READ_ONLY / RETIRED；
- 主要写入范围或职责发生正式变化。

**R04 从 REWORK 变为 READY、某 Finding 从 OPEN 变为 CLOSED、某任务等待授权等，不属于本文件维护范围。**

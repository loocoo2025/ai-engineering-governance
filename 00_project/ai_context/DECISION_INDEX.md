# DECISION_INDEX.md
## 当前决策注册表

> 本文件回答：**对于当前项目的每一个重要事项，现在最后正式确认的选择到底是什么？**
>
> 本文件不是聊天摘要，也不是历史讨论流水账。
>
> 本项目遵守 Current Truth Principle：**同一个重要决策主题，在任意时刻原则上只能有一个当前有效决定。**

---

# 0. 事实所有权边界

本文件是“当前有效决定”的唯一权威索引。

本文件不复制维护：

- 当前 Baseline ID / Status / Anchor Commit → 见 `BASELINE_INDEX.md`；
- 当前项目阶段 / Gate / 授权 / 下一步 → 见 `CURRENT_STATE.md`；
- 当前任务状态 → 见 `ACTIVE_TASKS.md`。

当 Baseline Relearn 时，应把本文件与 `BASELINE_INDEX.md`、`CURRENT_STATE.md` 一起读取，但三者**各自维护不同事实，不要求重复抄写同一状态字段**。

---

# 1. 状态定义

| 状态 | 含义 | 可作为当前依据 |
|---|---|---|
| `PROPOSED` | 已提出但尚未确认 | 否 |
| `DISCUSSED` | 已讨论但尚未正式决定 | 否 |
| `APPROVED` | 已正式批准的普通项目决定 | 是 |
| `ACCEPTED` | 已正式接受，常用于 ADR | 是 |
| `CONFIRMED` | 已由项目负责人明确确认 | 是 |
| `CURRENT` | 当前正式基线或当前事实 | 是 |
| `SUPERSEDED` | 已被更新决定替代 | 否 |
| `REJECTED` | 已明确否决 | 否 |
| `ARCHIVED` | 仅保留历史 | 否 |
| `REFERENCE` | 仅供参考 | 否 |
| `UNKNOWN` | 无法确认 | 否 |
| `INFERRED` | 从旧资料推断但未确认 | 否 |

---

# 2. 决策注册表

| ID | 决策主题 | 决定 | 状态 | Supersedes | Superseded By | 确认依据 | 日期 | 影响范围 | 正式记录 |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

---

# 3. 当前有效决定摘要

> 这里只列出当前仍有效、且会明显影响当前开发的少数核心决定。不得放入 `SUPERSEDED / REJECTED / ARCHIVED` 项。

- 无 / 待建立

---

# 4. 决策替代规则

当新决定替代旧决定时，必须机械执行：

```text
1. 创建新的 DEC-XXX
2. 新决定标记 APPROVED / ACCEPTED / CONFIRMED / CURRENT
3. 旧决定标记 SUPERSEDED
4. 旧决定填写 Superseded By
5. 新决定填写 Supersedes
6. 更新受影响需求
7. 更新 ADR
8. 更新架构 / 详细设计
9. 检查代码影响
10. 更新测试
11. 更新需求追溯
12. 必要时更新 CURRENT_STATE.md
13. 必要时更新 BASELINE_INDEX.md
```

禁止只在聊天中说“以后按新方案”而不更新正式项目资料。

---

# 5. “最后说的话”不等于“最后决定”

```text
提出想法 → PROPOSED
讨论方案 → DISCUSSED
项目负责人明确确认 → APPROVED / CONFIRMED
ADR 正式通过 → ACCEPTED
后来被新决定替代 → SUPERSEDED
```

只有正式确认状态才能改变当前事实。

---

# 6. 唯一性检查

以下事件后必须检查本表：

- 重大需求确认；
- 架构决策；
- 用户改变重要想法；
- 接口/协议变化；
- 重大 Bug 导致设计变化；
- CR 被批准；
- Baseline Relearn；
- 正式发布。

同一个决策主题如果同时存在两个互相冲突的当前有效决定，则标记：

```text
DECISION-CONFLICT
```

冲突关闭前不得继续依赖该事项进行设计、编码或测试。

---

# 7. 与 ADR 的关系

```text
DECISION_INDEX.md
→ 告诉 AI 当前选了什么

ADR
→ 告诉 AI 为什么这么选
```

重大架构决定必须能追溯到相应 ADR。

---

# 8. 与 Git / Archive 的关系

历史决定不删除。历史由 Git、`SUPERSEDED` 决策、ADR、CR 和 Archive 保留。

AI 日常工作默认只使用当前有效决定。需要回答“以前为什么不是这样”时，再按需回溯历史。

---

# 9. Baseline Relearn 检查

每次 Baseline Relearn 前必须确认：

- [ ] 所有核心决策都有明确状态；
- [ ] 同一主题没有多个当前有效决定；
- [ ] `SUPERSEDED` 决策没有继续出现在当前基线；
- [ ] 当前需求与当前决策一致；
- [ ] 当前 ADR 与当前决策一致；
- [ ] 当前架构 / 设计与当前决策一致；
- [ ] 当前测试没有继续验证已废弃产品行为；
- [ ] `CURRENT_STATE.md` 没有把已 `SUPERSEDED` 的决定当作当前项目状态依据；
- [ ] `BASELINE_INDEX.md` 所包含的决策/ADR集合没有引用已失效决定。

> **讨论可以很多，历史可以很长，但当前正式答案只能有一个。**

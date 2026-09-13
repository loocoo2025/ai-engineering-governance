> Authority：跨 Session 通信和状态文件边界；由 `INDEX.yaml` 按触发条件加载。

# 9. 对话之间如何通信

多个 AI 对话之间，不应依赖：

> “你去看另一个聊天里我刚才说了什么。”

正确方式是：

> **通过项目正式文件通信。**

会影响任务、权限、Gate、受控产物或正式状态的跨岗位动作，还必须实例化 `INTERACTION_CONTRACT / INTERACTION_OPERATION`。字段、生命周期和授权边界由 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md` 与 `00_project/governance/GOVERNANCE_EXECUTION_CONTRACTS.yaml` 定义。自然语言可以作为说明或证据附件，但不能替代 Sender/Receiver、Action、Scope、Authority、Allowed/Forbidden Actions、Receipt、Status、Terminal State 和 Audit Reference。

必须建立：

```text
00_project/
└── ai_context/
    ├── CURRENT_STATE.md
    ├── CONVERSATION_MAP.md
    ├── DECISION_INDEX.md
    ├── OPEN_QUESTIONS.md
    ├── ACTIVE_TASKS.md
    ├── BASELINE_INDEX.md
    ├── ROLE_BRIEFS/
    │   ├── C00_CONTROL.md
    │   ├── C01_REQUIREMENTS.md
    │   ├── C02_ARCHITECTURE_DESIGN.md
    │   ├── C03_IMPLEMENTATION.md
    │   ├── C04_INDEPENDENT_REVIEW.md
    │   ├── C05_VERIFICATION_RELEASE.md
    │   └── C06_ISSUES_CHANGE.md
    └── HANDOFFS/
        └── ...
```

---

# 10. CURRENT_STATE.md 必须写什么

`CURRENT_STATE.md` 是所有新对话快速理解项目现状的入口。

至少包含：

```text
# 当前项目状态

项目：
当前版本：
当前 Git Commit：
当前开发阶段：
当前里程碑：
最后更新时间：

## 当前已经批准的基线
- 产品需求：
- 系统需求：
- 架构：
- ADR：
- 详细设计：
- 测试计划：

## 当前正在开发
- ...

## 当前正在测试
- ...

## 当前阻塞项
- ...

## 当前已知重大风险
- ...

## 当前未决问题
- ...

## 当前下一步
- ...
```

禁止把几个月历史全部复制进去。

它只描述：

> **现在是什么状态。**

---

# 11. CONVERSATION_MAP.md 必须写什么

至少记录：

| 对话ID | 角色 | 当前版本 | 生命周期状态 | 主要职责 | 主要写入范围 |
|---|---|---|---|---|---|
| C00 | Control | v02 | ACTIVE | 项目控制 | 00_project |
| C01 | Requirements | v03 | ACTIVE | 需求 | 01/02 requirements |
| C02 | Architecture | v02 | ACTIVE | 架构/设计 | 03/04 design |
| C03 | Implementation | v05 | ACTIVE | 实现 | src + unit tests |
| C04 | Review | v04 | ACTIVE | 独立评审 | READ ONLY + review |
| C05 | Verification | v03 | ACTIVE | 验证/发布 | tests/quality/ci |
| C06 | Issues | v01 | ACTIVE | 问题/变更 | issues/change |

同时记录稳定的对话写入边界和是否允许建立并行实例。当前 Task、Output Contract、Worktree、Branch、Write Scope 和 Write Lease 绑定只在 `ACTIVE_TASKS.md` 维护，不在本文件复制。

需要核对：

- 谁是某个文件或模块当前允许的主要修改者；
- 是否存在并行实现；
- 是否存在文件写入冲突。

---

# 12. 一个重要规则：同一正式文件不要让多个对话同时写

所有情况下：

> **同一个权威文档或同一个代码文件，在同一时间只允许一个主要写入者。**

多个写入 Session 并行时必须使用独立 Git Worktree 和不同 Branch；使用 Worktree 也不能允许同一 Local Working Directory 出现两个 Writer。Write Scope 重叠时默认串行，或先建立共享上游/Integration Work Package。

例如：

- C02 正在修改 `system_architecture.md`；
- C04 只能提交评审意见；
- C04 不应该直接偷偷改架构文件。

评审通过后：

- C02 根据评审意见修改；
- 或由 C00 明确转移写入权。

这样避免多个 AI 相互覆盖。

---

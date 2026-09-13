# AI 多对话 / 多智能体协作规范——模块化兼容入口

> 从 `v0.1.8` 起，本文件是旧路径和旧章节号的兼容入口。Session、上下文、交接、模型路由和 Worktree 正文已按语义迁移到 `00_project/governance/modules/sessions/`。

## 当前权威目录

`00_project/governance/modules/sessions/INDEX.yaml`

## 旧章节兼容映射

| 旧章节 | 当前权威文件 |
|---|---|
| §1～§8 | `modules/sessions/ROLE_SESSION_BOUNDARIES.md` |
| §9～§12 | `modules/sessions/COMMUNICATION_AND_STATE.md` |
| §13～§23 | `modules/sessions/SESSION_LIFECYCLE_AND_HANDOFF.md` |
| §24～§40 | `modules/sessions/PARALLELISM_GIT_AND_ROLE_SEPARATION.md` |
| §41.1～§41.4 | `modules/sessions/MODEL_ROUTING_AND_INDEPENDENT_SESSION.md` |
| §41.5 独立 Session 请求 | `modules/sessions/MODEL_ROUTING_AND_INDEPENDENT_SESSION.md#415-独立-session-请求与自动创建` |
| §41.6 当前 Session 外部 AI 调用 | `modules/sessions/MODEL_ROUTING_AND_INDEPENDENT_SESSION.md#416-当前-session-外部-ai-调用与独立-session-的分离` |
| §41.7 Worktree / Write Lease / Return | `modules/sessions/WORKTREE_WRITE_LEASE_AND_RETURN.md` |

旧 Review Record、历史 Commit 和旧版本文档中的章节引用继续按本表解释。新任务必须通过 Router 和 Domain INDEX 选择实际规则文件。

无法唯一解析时输出 `RULE_NOT_FOUND / RULE_CONFLICT / VERSION_AMBIGUOUS` 并停止依赖该规则的动作。

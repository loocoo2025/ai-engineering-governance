# CURRENT_STATE.md
## 当前项目动态状态（唯一权威源）

> **本文件是项目级“动态当前状态”的唯一权威来源（Single Source of Current Execution State）。**
>
> 它只回答：**项目现在处于什么阶段、正在做什么、当前门禁/评审状态是什么、当前允许做什么、下一步是什么。**
>
> 其他文件可以引用本文件，但不得复制维护同一组动态状态；否则极易产生“前面已更新、后面还残留旧状态”的冲突。

---

# 0. 事实所有权边界

本文件负责维护：

- 当前开发阶段与里程碑；
- 当前评审 / Gate 状态；
- 当前授权边界；
- 当前 Autonomy Mode 与运行路由；
- 当前执行焦点；
- 当前项目级阻塞状态；
- 当前重大风险摘要；
- 当前上下文健康状态；
- 当前下一步。

当前工作树的 `HEAD / Branch / Parent / Diff` 由 Git 直接解析；Git 是这些实时事实的唯一权威来源，本文件不复制维护。

本文件**不负责复制维护**：

```text
Baseline 身份与组成
→ BASELINE_INDEX.md

当前有效决定
→ DECISION_INDEX.md

任务清单与任务级状态
→ ACTIVE_TASKS.md

未决问题明细
→ OPEN_QUESTIONS.md

对话/角色拓扑与对话生命周期
→ CONVERSATION_MAP.md

历史迁移事件
→ MIGRATION_LOG.md

历史交接快照
→ HANDOFFS/*
```

如果这些文件与本文件发生冲突：

- 项目级动态状态 → 以 `CURRENT_STATE.md` 为准；
- Baseline 身份/组成 → 以 `BASELINE_INDEX.md` 为准；
- 决策状态 → 以 `DECISION_INDEX.md` 为准；
- 任务级状态 → 以 `ACTIVE_TASKS.md` 为准；
- 未决问题状态 → 以 `OPEN_QUESTIONS.md` 为准；
- 对话生命周期 → 以 `CONVERSATION_MAP.md` 为准；
- 历史事件 → 以 Git / 审计记录 / `MIGRATION_LOG.md` 为准。

不得通过在多个文件重复抄写同一动态状态来“解决一致性”。

---

# 1. 当前项目快照

项目：{{PROJECT_NAME}}
当前产品版本：0.0.0
当前开发阶段：INIT
当前里程碑：M0
最后更新时间：{{DATE}}

当前 Baseline：**见 `BASELINE_INDEX.md`，本文件不复制 Baseline ID/组成。**
当前有效决定：**见 `DECISION_INDEX.md`。**

---

# 2. 当前执行状态

当前项目状态：`INIT / IN_PROGRESS / REVIEW / REWORK / BLOCKED / READY_FOR_NEXT_STAGE / OTHER`

当前评审 / Gate：
- 无 / 待建立

当前执行焦点：
- 无

当前责任角色：
- C00

当前任务：
- 任务 ID / 详情以 `ACTIVE_TASKS.md` 为准

---

# 3. 当前授权边界

## 3.1 当前 Autonomy Envelope 与运行路由

```text
AUTONOMY_MODE: SUPERVISED_AUTO

AUTHORIZED_UNTIL:
{{GATE_OR_MILESTONE}}

PREAUTHORIZED_GATES:
- {{GATE}}

ASSURANCE_CADENCE_PROFILE: STANDARD
ASSURANCE_CADENCE_POLICY: 00_project/governance/PROJECT_ASSURANCE_CADENCE_POLICY.md

EXTERNAL_AI_TRANSFER_CONFIG: 00_project/governance/EXTERNAL_AI_TRANSFER_CONFIG.yaml

PERSISTENT_CONTROL_CHANNEL: C00

PRIMARY_EXECUTOR:
MODEL: DeepSeek V4 Flash High
HARNESS: OpenCode

EXPERT_ESCALATION_PRIMARY:
MODEL: GPT-5.6 Sol
HARNESS: Codex

EXPERT_ESCALATION_FALLBACK:
MODEL: Kimi K3 High/Max
HARNESS: OpenCode

INDEPENDENT_REVIEWER_PRIMARY:
MODEL: GPT-5.6 Sol
HARNESS: Codex

INDEPENDENT_REVIEWER_FALLBACK:
MODEL: Kimi K3
HARNESS: OpenCode

HUMAN_PROJECT_OWNER:
Project Owner
```

以上是可替换的当前运行配置，不属于产品 Current Truth。Role、Model、Harness 和 Tool 是四个独立维度；Model、Harness 或 Tool 替换本身都不改变需求、架构、Baseline 或 Gate。稳定语义、辅助调用边界和权限继承规则见 `AI_ENGINEERING_RULES_V2.md` 第 38 章。

`ASSURANCE_CADENCE_PROFILE` 只选择保障节奏 Profile；Profile 定义和不可关闭控制项由 `PROJECT_ASSURANCE_CADENCE_POLICY.md` 维护。外部 AI 的开关、预算和 Session 放置值只由 `EXTERNAL_AI_TRANSFER_CONFIG.yaml` 维护，本文件仅引用，不复制其中字段。

## 3.2 自动允许范围

`AUTO_ALLOWED` 仅在当前 Autonomy Mode 和已批准文件/系统权限内有效。`FULL_AUTO` 下，已列入 `PREAUTHORIZED_GATES` 且不超过 `AUTHORIZED_UNTIL` 的范围视为已预授权：

```text
AUTO_ALLOWED:
- read authorized project files
- modify authorized files
- build
- unit/integration/regression test
- static analysis
- local debugging
- fix implementation defects
- fix test defects
- resolve P2/P3 within approved scope
- update fact-owned records
- perform Baseline Relearn
- prepare review candidate
```

## 3.3 人工审批边界

```text
HUMAN_APPROVAL_REQUIRED:
{{PROJECT_SPECIFIC_GATES}}
```

```text
STOP_FOR_HUMAN_IF:
- Current Truth change requires owner authority
- product goal must change
- product behavior must change
- acceptance threshold must change
- unapproved major architecture tradeoff requires owner choice
- major risk acceptance requires owner approval
- unapproved release requires owner approval
- remote dangerous/destructive operation requires separate approval
```

## 3.4 当前文件修改边界

当前允许：
- 无 / 待建立

当前禁止：
- 无 / 待建立

> 授权边界、Autonomy Mode 或当前模型槽位变化时只在这里维护；历史事实写入审计/日志，不复制到 `BASELINE_INDEX`、`DECISION_INDEX`、`CONVERSATION_MAP` 或 `ACTIVE_TASKS`。

---

# 4. 当前项目级阻塞

当前是否阻塞：`YES / NO`

阻塞项：
- 无

明细来源：
- 未决问题 → `OPEN_QUESTIONS.md`
- 任务阻塞 → `ACTIVE_TASKS.md`
- 评审发现 → 对应 `05_reviews/` 正式记录

> 本节只保留项目级结论和必要 ID，不复制长篇问题正文。

---

# 5. 当前重大风险摘要

- 无

> 风险的详细分析应放在对应风险/设计/评审文件中，本文件只保留当前仍需管理的摘要或引用。

---

# 6. 当前下一步

1. 填写项目概览
2. 建立 PRD
3. 启动 C01 需求质询

---

# 7. 上下文健康

当前上下文健康状态：`HEALTHY / REVIEW / RESET_RECOMMENDED / RESET_REQUIRED`

上一次 Baseline Relearn：{{DATE_OR_NEVER}}
自上次 Baseline Relearn 后 HANDOFF 次数：0

## HEALTHY

- AI 能准确说明当前阶段、Gate、授权和下一步；
- 没有混淆新旧需求；
- 没有引用 `SUPERSEDED` 决策；
- 当前权威文件之间没有语义冲突。

## REVIEW

- HANDOFF 已累计约 3 次；
- 出现轻微状态歧义；
- AI 开始频繁回看历史。

## RESET_RECOMMENDED

- 连续 3～4 次 HANDOFF；
- 重大里程碑或大型重构刚完成；
- AI 出现一次明显新旧状态混淆。

## RESET_REQUIRED

- 连续 5 次 HANDOFF；
- AI 多次引用 `SUPERSEDED` 决策；
- AI 无法准确说明当前阶段/Gate/Baseline；
- 当前权威文件发生实质冲突；
- 项目负责人明确要求重新学习。

---

# 8. 当前允许使用的历史信息

默认：

```text
Git 历史：按需读取
Archive：默认不读
SUPERSEDED ADR：默认不读
旧 HANDOFF 链：默认不读
旧聊天：默认不读
已关闭 Bug：按需读取
```

需要历史信息时，必须说明当前问题为什么需要回溯。

---

# 9. 维护规则

以下事件发生后，检查本文件中**本文件负责的动态字段**是否变化：

- 当前阶段变化；
- 当前 Gate / 评审状态变化；
- 当前授权边界变化；
- 当前 Autonomy Mode 或运行路由变化；
- 当前执行焦点变化；
- 当前项目级阻塞变化；
- 当前下一步变化；
- Context Handoff；
- Baseline Relearn。

如果只是：

- Baseline 组成变化 → 更新 `BASELINE_INDEX.md`；
- 决策变化 → 更新 `DECISION_INDEX.md`；
- 单个任务状态变化 → 更新 `ACTIVE_TASKS.md`；
- 未决问题变化 → 更新 `OPEN_QUESTIONS.md`；
- 对话版本/生命周期变化 → 更新 `CONVERSATION_MAP.md`；

则不得为了“同步文字”而在本文件重复抄写全部明细。

> **一个事实只维护一个权威位置；其他文件只引用，不复制。**

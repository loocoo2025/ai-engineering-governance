# BASELINE_INDEX.md
## 当前项目 Baseline 索引（Baseline 唯一权威源）

> **本文件只负责回答：当前正式 Baseline 是什么，以及它由哪些受控产物组成。**
>
> 它不负责维护当前 R04/R05 状态、当前任务、当前 OPEN finding、等待授权、下一步等动态执行信息。
>
> 项目级动态状态统一见 `CURRENT_STATE.md`。

---

# 0. 事实所有权边界

本文件负责：

- Baseline ID；
- Baseline 状态；
- Baseline 建立日期；
- Baseline 锚定 Commit / Tag；
- Baseline 所包含的 PRD / SRS / ADR / 架构 / 设计 / 测试 / 代码版本；
- Baseline 自身已知偏差。

本文件不负责：

```text
当前评审/Gate状态 → CURRENT_STATE.md
当前授权/等待授权 → CURRENT_STATE.md
当前 Dynamic Role Profile / Interaction / Enforcement Mode → CURRENT_STATE.md
当前任务状态 → ACTIVE_TASKS.md
当前未决问题状态 → OPEN_QUESTIONS.md
当前有效决定正文/状态 → DECISION_INDEX.md
当前对话状态 → CONVERSATION_MAP.md
历史过程 → MIGRATION_LOG.md / Git / review records
```

禁止为了方便阅读，把上述动态状态复制到本文件中长期维护。

---

# 1. Baseline 元数据

Baseline ID：{{BASELINE_ID}}
Baseline Status：`DRAFT / CANDIDATE / CURRENT / SUPERSEDED / ARCHIVED`
产品版本：0.0.0
Baseline Anchor Commit：{{COMMIT}}
Baseline Tag：{{TAG_OR_NONE}}
建立日期：{{DATE}}

> `Baseline Anchor Commit` 是该 Baseline 的固定锚点。当前工作树的 `HEAD / Branch / Parent / Diff` 由 Git 直接解析，不在项目文档中复制维护。

---

# 2. Baseline 组成

| Baseline 对象 | 当前版本 / Commit | 状态 | 当前正式文件 |
|---|---|---|---|
| 产品需求 | 未建立 | DRAFT | `01_product_requirements/PRD.md` |
| 系统需求 | 未建立 | DRAFT | `02_system_requirements/SRS.md` |
| 接口/协议需求 | 未建立 | DRAFT | `02_system_requirements/interface_requirements.md` |
| 决策注册表 | 当前快照 | DRAFT | `00_project/ai_context/DECISION_INDEX.md` |
| 架构 | 未建立 | DRAFT | `03_architecture/` |
| 详细设计 | 未建立 | DRAFT | `04_design/` |
| 测试设计 | 未建立 | DRAFT | `06_test_design/` |
| 测试实现 | 未建立 | DRAFT | `08_tests/` |
| 质量验证 | 未建立 | DRAFT | `09_quality/` |
| 代码 | `{{COMMIT}}` | DRAFT | `07_src/` |
| 部署定义 | 未建立 | DRAFT | `10_ci_cd/environments/` |
| 发布产物 | 未建立 | DRAFT | `14_release/` |

---

# 3. Baseline 中的 ACCEPTED ADR 集

> 这里记录该 Baseline 所包含的 ADR 集。ADR 当前状态的权威来源仍是 ADR 文件及 `DECISION_INDEX.md`。

- 无

---

# 4. Baseline 已知偏差

> 只记录“这个 Baseline 本身与其声明产物之间”的偏差。
>
> 不要在这里维护当前评审 finding、当前任务、等待授权或下一步。

- 无

---

# 5. Baseline 成立条件

本 Baseline 只有满足以下条件时才可标记为 `CURRENT`：

- [ ] PRD 版本明确；
- [ ] SRS 版本明确；
- [ ] 接口/协议需求版本明确；
- [ ] Baseline 所包含的 ACCEPTED ADR 集明确；
- [ ] 架构版本明确；
- [ ] 详细设计版本明确；
- [ ] 代码锚定 Commit 明确；
- [ ] 测试基线明确；
- [ ] `DECISION_INDEX.md` 不存在同一主题多个冲突的当前有效决定；
- [ ] 不存在未说明的 Baseline 内部重大偏差。
- [ ] `CANDIDATE -> CURRENT` 存在 Human Project Owner / 既有 Baseline Owner 明确采用证据，或满足 `ROLE_INTERACTION_EXECUTION_POLICY.md` 第 5.1 节的精确 C00 预授权条件；

> 当前项目是否正在 REVIEW / REWORK / READY、是否允许进入下一阶段，不在本文件判定；见 `CURRENT_STATE.md`。

> Baseline Adoption 与 Formal Seal、Release、Commit、C04 和其他 Action Class 相互独立。Baseline `CURRENT` 不表示已经取得 Formal Seal。

---

# 6. 历史默认不进入当前 Baseline

以下内容不得因为“以前存在”而自动加入当前 Baseline：

- 旧 PRD / SRS；
- `SUPERSEDED` ADR；
- `SUPERSEDED` 决策；
- 旧架构；
- 旧详细设计；
- 旧测试预期；
- 旧 HANDOFF；
- 旧聊天；
- Archive 内容。

需要时按需回溯，但不能偷偷改变当前 Baseline。

---

# 7. Baseline Relearn 时核实

```text
1. 核实本文件的 Baseline ID / Status / Anchor Commit
2. 核实当前 PRD / SRS / IF
3. 核实 DECISION_INDEX 中当前有效决定
4. 核实 ACCEPTED ADR 集
5. 核实当前架构 / 详细设计
6. 核实当前测试与代码锚点
7. 再读取 CURRENT_STATE 获取当前执行阶段、Gate、授权和下一步
8. 读取 ACTIVE_TASKS / OPEN_QUESTIONS 获取任务和问题明细
```

新 AI 应输出 `BASELINE-RELEARN-CHECK`，确认理解无误后再继续工作。

---

# 8. 建立新 Baseline 的典型触发条件

- 正式发布；
- 重大里程碑形成新的受控产物集合；
- 正式需求 Baseline 变化；
- 重大架构/接口版本变化；
- 大型重构形成新的受控代码锚点；
- 正式 Baseline Relearn 后确认需要新基线。

新 Baseline 建立后：旧 Baseline 标记 `SUPERSEDED / ARCHIVED`，新 Baseline 标记 `CURRENT`。Git 历史继续保留。

> **普通评审状态从 OPEN → REWORK → READY → PASS 的变化，本身不要求反复改写本文件；只有 Baseline 身份或组成真正变化时才修改。**

# 工程治理模板中途升级模板

> 项目已经按旧版工程模板推进，现在公共治理模板升级。

## 核心原则

> 这是治理规则迁移，不自动等于产品变更。不因为模板升级而重新设计或重写已批准的产品、架构或代码。

## 1. 基本信息
- Migration ID：`GOV-MIG-XXX`
- 日期：
- 项目：
- 迁移前模板版本：
- 迁移后模板版本：
- 当前 Baseline ID：
- 当前 Git Commit：

## 2. 分类
```text
CHANGE_TYPE: GOVERNANCE_CHANGE
PRODUCT_BEHAVIOR_CHANGE: NO
REQUIREMENT_CHANGE: NO
ARCHITECTURE_CHANGE: NO
CODE_CHANGE: NO
```

如果实际需要改变产品行为、架构或代码，必须单独建立正式 Change。

## 3. 迁移目标
- 升级治理结构；
- 保留当前正式产品事实；
- 补齐新增治理文件和状态字段；
- 消除旧模板与新模板的治理冲突；
- 建立新的治理 Baseline；
- 不做无关业务修改。

## 4. 迁移前只读检查
先读取：
- 当前 `AI_START_HERE.md`
- 当前工程规则
- `CURRENT_STATE.md`
- `BASELINE_INDEX.md`
- `DECISION_INDEX.md`（如存在）
- 当前 APPROVED / CONFIRMED 需求
- 当前 ACCEPTED ADR
- 当前架构
- 当前详细设计
- 当前 Git 状态
- 当前测试状态

## 5. 新旧规则差异

| 项目 | 旧模板 | 新模板 | 动作 |
|---|---|---|---|
| Current Truth | | | |
| Decision Index | | | |
| Current State | | | |
| Baseline Index | | | |
| Context Reset | | | |
| Testing Governance | | | |
| C00～C06 | | | |
| HANDOFF | | | |
| Archive | | | |
| 其他 | | | |

## 6. 当前事实必须保留
模板升级不能自动推翻：
- 当前 APPROVED 产品需求；
- 当前 CONFIRMED 系统需求；
- 当前 ACCEPTED ADR；
- 当前正式接口；
- 当前架构；
- 当前详细设计；
- 已验证代码行为；
- 当前测试结论；
- 已批准发布结论。

## 7. Current Truth 检查
确认：
- 当前哪版 PRD 有效；
- 当前哪版 SRS 有效；
- 哪些 ADR 仍 ACCEPTED；
- 哪些 ADR 已 SUPERSEDED；
- 当前架构是什么；
- 当前详细设计是什么；
- 当前代码 Commit 是什么；
- 当前测试 Baseline 是什么；
- 同一主题是否存在两个冲突的当前决定。

## 8. 要迁移的治理文件
- [ ] `AI_START_HERE.md`
- [ ] `AI_ENGINEERING_RULES_V2.md`
- [ ] `AI_CONVERSATION_ORCHESTRATION_RULES.md`
- [ ] `AI_TESTING_GOVERNANCE_RULES.md`
- [ ] `AI_CONTEXT_RESET_AND_BASELINE_RELEARN_RULES.md`
- [ ] `CURRENT_STATE.md`
- [ ] `BASELINE_INDEX.md`
- [ ] `DECISION_INDEX.md`
- [ ] `OPEN_QUESTIONS.md`
- [ ] `ACTIVE_TASKS.md`
- [ ] `CONVERSATION_MAP.md`
- [ ] `ROLE_BRIEFS/*`
- [ ] `HANDOFFS/*`
- [ ] `00_project/archive/`

## 9. 禁止事项
- 顺便重构业务代码；
- 顺便修改产品需求；
- 顺便替换技术路线；
- 顺便改变接口；
- 顺便扩大测试范围；
- 删除 Git 历史；
- 重写主分支历史；
- 把治理升级伪装成产品重构。

## 10. 是否需要 Baseline Relearn
`YES / NO / RECOMMENDED`

理由：

## 11. 迁移后基线
- 新 Governance Baseline ID：
- Git Commit：
- 当前 PRD：
- 当前 SRS：
- 当前 ACCEPTED ADR：
- 当前架构：
- 当前设计：
- 当前测试：

## 12. 给 Codex / AI 的直接指令
```text
当前项目已经按照旧版工程模板推进了一段时间。

现在项目级工程治理模板已经升级。

这是一次 GOVERNANCE_CHANGE，不是产品需求重做，也不是要求重新设计或重写现有代码。

请：
1. 先不要修改业务代码、需求、架构或测试；
2. 阅读当前项目已有治理文件；
3. 阅读新版治理模板；
4. 对比新旧规则；
5. 列出新增、修改、废弃和需要迁移的治理项；
6. 保留当前已正式批准的产品需求、ADR、架构、设计、代码和测试结论；
7. 只迁移治理规则和状态文件；
8. 做一次 Current Truth 检查；
9. 如果新规则会实际改变产品、架构、接口、代码或测试要求，停止自动修改并单独列出；
10. 更新 CURRENT_STATE、BASELINE_INDEX、DECISION_INDEX 等必要治理文件；
11. 必要时执行 Baseline Relearn；
12. 建立新的治理 Baseline；
13. 完成后继续迁移前的原开发任务。

不要把工程治理升级等同于产品重构。
```

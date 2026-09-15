> Authority：Anti-Regression / Non-Regression Control（防回退控制）的唯一语义权威；由 `INDEX.yaml` 按触发条件加载。

# 42. 防回退与不可变量治理

## 42.1 核心规则

```text
已经被正式接受的正确事实不得被后续变更静默重新决定。
默认只能继承；需要改变时必须通过正确 Owner 的显式 Change Decision。
```

本规则不把所有历史内容永久冻结，也不阻止正常演进。它只禁止后续版本、复制、生成、重构或迁移在没有正式变更依据时，把已经关闭的问题或已经接受的约束重新带回来。

防回退闭环为：

```text
Finding / Bug
→ Fix
→ Regression Guard Disposition
→ 可重复、长期有效且可机械判断时登记 Invariant
→ 增加永久 Regression Guard
→ Pre-C04 Validation
→ Formal C04 同时验证本轮变更与历史非回退
```

## 42.2 事实所有权

- 本文件拥有防回退流程、状态和判定语义；
- `00_project/governance/NON_REGRESSION_CONTRACT.yaml` 拥有当前有效 Non-Regression Invariant 及其 Guard 定义；
- Finding 实例仍只由对应正式 Review Record 拥有；
- Bug 实例仍只由对应 BUG / RCA 记录拥有；
- Current Truth、Decision、Baseline、Task、Authorization 和 Release 仍由既有 Owner 维护；
- Guard 的本次运行结果写入质量证据或正式 Review Record，不回写成第二套 Invariant 注册表。

框架级 Invariant 使用 `scope: FRAMEWORK`。下游项目专有 Invariant 使用 `scope: PROJECT`，只保存在该项目自己的 Contract 中；不得把具体产品需求、接口值、服务器、用户数据或内部项目事实加入公开框架的 `framework_invariants`。

## 42.3 哪些 Finding 必须形成 Guard

只有准备建立或评估永久 Guard 的正式 Finding 才需要完整记录下列字段；普通一次性问题可以直接记录 `REGRESSION_GUARD_DISPOSITION: NOT_REQUIRED`，无需为了填满表格继续分析：

```text
REGRESSION_GUARD_DISPOSITION: REQUIRED / NOT_REQUIRED
REGRESSION_GUARD_REASON: {{REASON}}
INVARIANT_ID: {{ID_OR_NOT_APPLICABLE}}
GUARD_ID: {{ID_OR_NOT_APPLICABLE}}
```

同时满足以下条件时必须选择 `REQUIRED`：

1. 根因可以在后续复制、生成、升级、重构或实现中重复出现；
2. 所保护的语义在声明的有效范围内长期成立；
3. 可以通过确定性机械检查判断是否满足；
4. Guard 的维护成本与被防止的风险相称。

S0/S1 Finding 同时满足可重复、长期有效、可机械判断且成本相称时，默认建立 Guard。S2 只有重复发生或后果明显高于长期检查成本时才建立。S3、一次性编辑问题和非阻断 Feedback 默认 `NOT_REQUIRED`，不要求额外论证。Severity 不单独决定是否建立 Guard；预期损失与长期治理成本的比较才是最终依据。

真实产品 Bug 继续适用 Testing Governance 的最小回归测试规则。治理 Guard 不替代产品测试，产品测试也不自动证明治理 Invariant 成立。

## 42.4 Invariant 状态与修改规则

Invariant 只使用：

```text
PROPOSED
LOCKED
SUPERSEDED
```

- `PROPOSED`：尚未作为强制 Guard 生效；
- `LOCKED`：当前有效，必须继承并在适用 Gate 前验证；
- `SUPERSEDED`：已由新的显式 Invariant 替代，仅保留历史。

`LOCKED` Invariant 不得原地改写其 statement、scope、适用条件、Guard 或强度。需要改变时必须：

```text
正确 Owner 的显式 Change Decision
→ Impact Analysis
→ 新 Invariant ID
→ 新记录填写 supersedes
→ 旧记录标记 SUPERSEDED 并填写 superseded_by
→ 更新或替换 Guard
→ 新精确 Target 的正式 C04
```

无论 `FRAMEWORK` 还是 `PROJECT` scope，旧 Invariant 只有在替代者已经进入 `LOCKED` 后才能标记为 `SUPERSEDED`。任一 `SUPERSEDED` 链的当前终点必须是 `LOCKED`；`PROPOSED` 不能接管已生效 Invariant，也不能使旧 Guard 提前停止执行。

不得通过删除 Guard、降低期望值、扩大 Exception、修改验证器使其不再检查，来伪造非回退通过。

## 42.5 单调历史

历史审计记录必须单调追加：

- 已关闭 Finding 不得从 `CLOSED_BY_FIX / CLOSED_BY_APPROVED_EXCEPTION` 原地改回 `OPEN`；同类问题再次出现时创建新的 Finding ID，并填写 `REGRESSION_OF`；
- 已完成的正式 Review Record 和 Gate Decision 绑定原精确 Target，不因后代变化而修改；新 Target 创建新 Review Record；
- `LOCKED` Invariant 只能保持 `LOCKED`，或由新记录显式替代为 `SUPERSEDED`；
- Task 的 `DONE / CANCELLED` 保持既有终态；后续工作创建新 Task；
- 已发布 Tag、Release、Baseline Anchor 和历史 Commit 不得移动或重写。

这里的“单调”针对历史记录，不表示产品永远不能改变。产品或治理语义发生批准变更时，必须创建新的事实、Task、Finding、Invariant 或 Review Record，而不是篡改旧记录。

## 42.6 Inherit + Delta

任何新版本、迁移、生成或重构都按以下原则执行：

```text
NEW_TARGET = ACCEPTED_PREDECESSOR + EXPLICIT_CHANGE_SET
```

没有列入本次 Change Set、且未被正确 Owner 显式替代的 Current Truth、批准约束和 `LOCKED` Invariant 必须保持不变。不得整份重新生成后仅凭“看起来一致”宣称语义继承完成。

适用时优先使用 Git Diff、结构化字段比较和 `NON_REGRESSION_CONTRACT.yaml` 中的 Guard 证明 Delta 边界。无法确认某项差异是否改变受保护语义时，标记 `UNKNOWN` 并停止接受该变更。

## 42.7 机械 Guard

模板提供：

```bash
python3 09_quality/non_regression/validate_non_regression.py
```

验证器只执行 Contract 明确声明的确定性断言，不执行 Contract 中的任意 Shell 命令。当前支持的 Guard Kind 由 Contract 和验证器共同限定。

退出码：

- `0`：所有适用 `LOCKED` Invariant 的 Guard 通过；
- `1`：Guard 已执行并发现 Invariant 违反；
- `2`：Contract、Guard 定义、输入文件或验证过程无效，无法形成有效结论。

对应治理结果：

```text
退出码 2 / 必需 Guard 未运行 / Contract 无法解析
→ REVIEW_NOT_READY

退出码 1 / Invariant 被违反
→ 正式 Finding + CHANGES_REQUESTED

退出码 0
→ NON_REGRESSION_VALIDATION: PASS
```

验证器 PASS 只证明已声明的机械 Invariant，不替代语义评审、产品测试、Traceability Gate 或 C04。

## 42.8 C04 非回退检查

正式 C04 不拆分成新的角色或 Gate。C04 在同一个 Review Record 中记录两个证据维度：

```text
CURRENT_CHANGE_VALIDATION: PASS / FAIL
NON_REGRESSION_VALIDATION: PASS / FAIL / NOT_APPLICABLE
```

`NOT_APPLICABLE` 必须说明当前 Target 为什么没有命中适用的 `LOCKED` Invariant、既有 Guard 或 Target Manifest 强制项。框架治理变更也只核验与本次 Delta 和 Review Scope 有关的 Invariant；不得仅因文件属于治理框架就把全部 `framework_invariants` 自动加入范围。

C04 只核验当前 Review Scope 实际适用的项目：

- 所有适用 Guard 已运行且绑定当前精确 Target；
- 与本次 Delta 直接相关的先前已关闭 Finding 仍满足关闭条件，或本次出现的新问题使用新 Finding ID 并引用 `REGRESSION_OF`；
- 已接受的 Baseline / Current Truth 没有在 Change Set 之外改变；
- `LOCKED` Invariant 未被删除、弱化或原地改写；
- 需要改变 Invariant 时存在正确 Owner 的 Change Decision、影响分析和替代链。

最终 Gate Decision 仍只有：

```text
PASS
CHANGES_REQUESTED
```

本轮变化正确且非回退验证通过，或有证据证明不适用，才允许 `PASS`。本机制不改变 C04 独立性、Finding Severity、整改路由或 Human Project Owner 边界。

## 42.9 Pre-C04、Commit 与 Release

- 对命中 `LOCKED` Invariant 的变更，在送正式 C04 前必须运行 Guard；
- Guard 失败时先整改，不把可机械发现的问题浪费给 C04；
- 关闭需要 Guard 的 Finding 时，Guard 与修复必须位于同一受控 Review Target；
- Public / Production Release 必须记录当前 Target 的 Non-Regression Validation 结果；
- `PROCEDURAL_FALLBACK` 下仍必须执行随模板提供的可用机械 Guard；只有环境确实不能运行时才记录 `REVIEW_NOT_READY`，不得把未运行写成 PASS；
- `TOOL_ENFORCED` 可以把相同验证器接入 CI、Commit Gate 或 Review Dispatch，但不得改变规则语义。

## 42.10 一句话总纲

```text
不要要求 AI 永久记住已经修过的问题；
把值得长期防御的关键、重复且可机械判断的正确性转成 LOCKED Invariant 和 Guard，
让后续版本只能显式改变，不能静默回退。
```

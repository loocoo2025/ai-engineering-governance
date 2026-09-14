# CR-GOV-005：Non-Regression Control

## 1. 文档控制

```text
CHANGE_ID: CR-GOV-005
CHANGE_CLASS: GOVERNANCE_CHANGE
SOURCE_VERSION: v0.1.8
TARGET_IDENTITY: v0.1.9
DATE: 2026-09-14
STATUS: APPROVED_FOR_CANDIDATE_IMPLEMENTATION
AUTHORITY_OWNER: Human Project Owner
```

## 2. 背景

现有框架已经具备 Current Truth、Decision Supersession、Bug 回归测试、Task 状态机、受控治理升级和独立 C04 复审，但治理 Finding 关闭后仍主要依赖后续 Agent 阅读历史并主动保持。复制、生成、升级或重构可能把已经解决的问题重新带回，而 Pre-C04 目前没有统一的永久机器 Guard。

## 3. 目标

建立最小闭环：

```text
Finding
→ Fix
→ Invariant
→ Regression Guard
→ Pre-C04 Validation
→ C04 Non-Regression Validation
```

使可重复、长期有效且可机械判断的问题在首次关闭后转化为机器约束，后续 Target 不能静默回退。

## 4. 范围

- 增加防回退语义 Authority、机器可读 Invariant Contract 和无第三方依赖的验证器；
- 为 Authorization 单次独立 Session 约束、C04 Finding 单调关闭、Task 终态和 C04 非回退证据建立首批框架 Invariant；
- Finding 关闭时记录 Regression Guard Disposition；
- 正式 C04 同时记录 Current Change Validation 与 Non-Regression Validation，但最终仍只输出 `PASS / CHANGES_REQUESTED`；
- Pre-C04 和 Release Gate 执行适用 Guard；
- 下游项目可在自己的 Contract 中增加 `PROJECT` Invariant，公开模板不预置产品事实。

## 5. 不在范围

- 不改变 C00～C06 职责；
- 不新增 Gate、Reviewer Role、审批 Owner 或 Current Truth 来源；
- 不让所有 Finding、Advisory 或历史事实自动成为 `LOCKED` Invariant；
- 不修改产品需求、架构、代码或测试事实；
- 不引入第三方依赖或允许 Contract 执行任意 Shell；
- 不改写 `v0.1.8` Tag、Release 或历史 Review Record。

## 6. 核心裁决

1. 已接受事实不得被静默重新决定；批准变化仍可通过正确 Owner 的显式 Change Decision 演进。
2. 每个 Finding 关闭前都评估 Guard；只有根因可重复、语义长期有效、可机械判断且成本合理时强制建立。
3. `LOCKED` Invariant 不原地改变；需要变化时创建新 ID 并建立 `supersedes / superseded_by`。
4. 已关闭 Finding 再次出现时创建新 Finding ID 和 `REGRESSION_OF`，不把旧记录改回 `OPEN`。
5. Guard 无法有效运行属于 `REVIEW_NOT_READY`；Guard 确认违反属于 Finding 和 `CHANGES_REQUESTED`。
6. C04 的两个验证维度不形成新角色、新 Gate 或第三种正式结论。

## 7. 当前授权

Human Project Owner 已明确批准升级当前 `v0.1.8` 治理框架。本轮允许修改治理模板、增加验证器、运行最小机械验证并形成内容预先固化为正式 `v0.1.9` 身份的 Candidate Commit 与外部 C04 复审包。

本轮暂不自动授权：

```text
COMMIT
FORMAL_C04_IN_CODEX
TAG
PUSH
RELEASE
BASELINE_ADOPTION
FORMAL_SEAL
```

正式 C04 由 Human Project Owner 在 ChatGPT 网页独立聊天模式执行。Primary Executor 必须在候选完成后停止并提供精确 Target、Diff、验证证据和可复制审查指令。

## 8. 接受条件

- Contract 可由 Python 3 标准库解析；
- 当前全部 `LOCKED` Invariant Guard 通过；
- 故意破坏一个受保护条件时验证器以退出码 `1` 失败；
- Contract 无效时验证器以退出码 `2` 失败；
- C04 Readiness、Finding、Decision Matrix 和最终二值结论不被改变；
- Current Truth、Baseline、Traceability、Testing Governance、Worktree 和既有 Release Gate 不被弱化；
- 无项目专有事实、用户路径或敏感信息进入模板；
- `git diff --check` 通过；
- 停在 `READY_FOR_INDEPENDENT_C04`。

## 9. 最终状态

```text
FINAL_STATUS: V0.1.9_CANDIDATE_READY_FOR_EXTERNAL_C04_OR_BLOCKED
```

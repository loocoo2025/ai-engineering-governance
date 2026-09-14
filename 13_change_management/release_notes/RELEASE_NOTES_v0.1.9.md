# AI Software Engineering Governance Framework v0.1.9

# AI 软件工程治理框架 v0.1.9

面向长周期 AI 软件开发的模型无关工程治理框架。

## 本版本是什么

`v0.1.9` 增加 Anti-Regression / Non-Regression Control，把可重复、长期有效且可机械判断的 Finding 根因转化为 `LOCKED` Invariant 和永久 Regression Guard。

## 新增

- `NON_REGRESSION_CONTROL.md`：防回退语义唯一 Authority；
- `NON_REGRESSION_CONTRACT.yaml`：框架级和项目级 Invariant/Guard 注册表；
- `validate_non_regression.py`：只依赖 Python 3 标准库的确定性验证器及其最小回归测试；
- Finding 的 Regression Guard Disposition 与 `REGRESSION_OF`；
- C04 的 `CURRENT_CHANGE_VALIDATION` 和 `NON_REGRESSION_VALIDATION` 证据维度；
- Guard 退出码到 `REVIEW_NOT_READY / CHANGES_REQUESTED / PASS` 的机械映射。

## 首批锁定 Invariant

- 单次独立 Session 授权必须保持 `dispatch_limit: 1` 且禁止自动重试；
- 已关闭 C04 Finding 不得原地重开，复发必须创建新 ID；
- Task 的 `DONE / CANCELLED` 保持终态；
- 正式 C04 必须同时核验本轮变化和历史非回退，同时保持二值 Gate Decision。

## 兼容性

- 不改变 C00～C06、Current Truth、Baseline、Traceability、Testing Governance、Worktree 或 Release Owner；
- 不把所有 Finding 自动变成 Invariant；
- 不追溯改写历史 Review Record；
- 下游项目的产品专有 Invariant 只保存在自己的 Contract；
- 正式采用后需要 Baseline Relearn。

## 已知限制

- 首版验证器提供封闭的文件、文本和正则断言，不代替语义评审；
- `PROCEDURAL_FALLBACK` 仍依赖 Agent 正确运行 Guard；
- 历史 Finding 不会自动转换为 Invariant，需要项目按风险选择。

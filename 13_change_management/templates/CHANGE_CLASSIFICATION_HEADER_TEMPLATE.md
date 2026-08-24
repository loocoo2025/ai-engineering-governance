# 变更分类头模板

> 任何中途变化开始前，AI 必须先完成分类。没有完成分类前，不得直接开始大范围修改。

## 1. 基本信息
- Change ID：`CHG-XXX`
- 日期：
- 项目：
- 当前 Baseline ID：
- 当前 Git Commit：

## 2. 变更类型
从以下选择一个主要类型：

`DISCUSSION_ONLY / REQUIREMENT_CHANGE / ARCHITECTURE_CHANGE / DESIGN_CHANGE / INTERFACE_CHANGE / IMPLEMENTATION_FIX / TEST_CHANGE / GOVERNANCE_CHANGE / RELEASE_CHANGE / OPERATIONS_CHANGE / UNKNOWN`

本次类型：

## 3. 状态
`PROPOSED / DISCUSSED / APPROVED / CONFIRMED / ACCEPTED / SUPERSEDED / REJECTED`

本次状态：

## 4. 是否正式决定
`IS_FORMAL_DECISION: YES / NO`

- `NO`：当前 Baseline 继续有效，不得因为讨论自动修改正式需求、ADR、架构、代码或测试预期。
- `YES`：必须执行正式变更和影响分析流程。

## 5. 原当前事实
- 原决定 ID：
- 原正式内容：
- 原正式文件：
- 原状态：

## 6. 新提议 / 新决定
- 内容：
- 新状态：
- `SUPERSEDES:`：

## 7. 影响层级

| 层级 | 是否受影响 | 说明 |
|---|---|---|
| PRD | YES / NO / UNKNOWN | |
| SRS | YES / NO / UNKNOWN | |
| 接口/协议 | YES / NO / UNKNOWN | |
| ADR | YES / NO / UNKNOWN | |
| 架构 | YES / NO / UNKNOWN | |
| 详细设计 | YES / NO / UNKNOWN | |
| 代码 | YES / NO / UNKNOWN | |
| 单元测试 | YES / NO / UNKNOWN | |
| 集成/系统测试 | YES / NO / UNKNOWN | |
| CI / 质量规则 | YES / NO / UNKNOWN | |
| 部署 | YES / NO / UNKNOWN | |
| 运维 | YES / NO / UNKNOWN | |

## 8. 当前允许动作
-

## 9. 当前禁止动作
-

## 10. 是否需要新 ADR
`YES / NO / REVIEW`

理由：

## 11. 是否需要新 Baseline
`YES / NO / REVIEW`

理由：

## 12. AI 最终分类结论

```text
CHANGE CLASSIFICATION

类型：
状态：
是否正式决定：

当前 Baseline 是否继续有效：
YES / NO / PARTIAL

受影响层级：
-

不得改变的层级：
-

下一步：
-
```

> “最后讨论过”不等于“最后正式决定”。只有明确批准的变更才允许覆盖 Current Truth。

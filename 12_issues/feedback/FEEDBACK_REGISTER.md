# 反馈登记表

> 本表是 FB（Feedback，反馈项）当前状态、分类去向、责任角色和关联记录的唯一权威来源。复杂反馈可以使用 `FEEDBACK_TEMPLATE.md` 建立独立记录，但当前状态仍回到本表维护。
>
> 登记只表示“已收到并可追踪”，不自动改变 Current Truth、Baseline、Gate、批准产物或实现范围。

## 1. 登记与分流原则

任何尚未完成事实判断的疑问、体验问题、治理缺口、改进建议、疑似缺陷或现场报告，必须先登记为 FB，再由 C06 分类。不得在收到时直接把它宣称为 BUG、CR 或正式项目决定。

```text
FEEDBACK_RECEIVED
→ REGISTER_AS_FB
→ TRIAGE
→ EXPLANATION / BUG / FIELD / CR / FUTURE_IMPROVEMENT / NO_ACTION
→ IMPLEMENTATION_OR_DISPOSITION
→ VERIFICATION
→ CLOSURE_EVIDENCE
```

## 2. 状态

| 状态 | 含义 | 使用条件 |
|---|---|---|
| `NEW` | 新收到 | 已登记，尚未完成分类 |
| `TRIAGED` | 已分类 | 已确认类型和去向，尚未形成执行安排 |
| `ACTION_PLANNED` | 已安排处理 | 已关联解释、任务、缺陷、现场问题、变更或后续计划 |
| `DEFERRED` | 已暂缓 | 由正确 Owner 明确延期，并保留恢复条件 |
| `CLOSED` | 已关闭 | 已解释、完成或转派，并有可验证的关闭依据 |
| `REJECTED` | 已拒绝 | 正确 Owner 有依据地决定不采纳 |

## 3. 类型与去向

反馈类型：

```text
QUESTION
USABILITY
GOVERNANCE_GAP
IMPROVEMENT
DEFECT_SUSPECTED
FIELD_REPORT
UNKNOWN
```

处理去向：

| 去向 | 含义 |
|---|---|
| `EXPLANATION` | 通过解释即可关闭，不改变正式事实 |
| `BUG` | 已确认实现偏离批准要求，转缺陷记录 |
| `FIELD` | 转现场问题或运行反馈记录 |
| `CR` | 需要改变正式需求、设计、规则或流程，转变更请求 |
| `FUTURE_IMPROVEMENT` | 作为后续改进保留，不阻断当前阶段 |
| `NO_ACTION` | 有依据地决定无需处理 |
| `UNKNOWN` | 信息不足，暂不能判断 |

BUG、FIELD 和 CR 是完成分流后的受控去向，不是所有反馈的默认身份。创建下游记录后，FB 与下游 ID 必须双向引用；下游记录的状态由其自身 Owner 维护，本表只维护 FB 的当前状态。

`优先级` 使用 `QUESTION_PRIORITY / WORK_PRIORITY` 的 P0～P3，不是 C04 Finding Severity。反馈类型为 `QUESTION` 只表示“需要解释或判断的反馈”；如果它同时产生项目未决事实，应另在 `OPEN_QUESTIONS.md` 建立条目并交叉引用，两个文件分别维护 FB 状态和未决问题状态，不复制同一事实。

## 4. 当前反馈

| ID | 反馈摘要 | 类型 | 优先级 | 状态 | 去向 | 责任角色 | 关联记录 / 下一步 |
|---|---|---|---|---|---|---|---|
| FB-XXX | | UNKNOWN | P0/P1/P2/P3 | NEW | UNKNOWN | C06 | |

## 5. 关闭条件

FB 只有满足以下之一时才可关闭：

- 已提供充分解释，且不需要改变正式事实；
- 已由正确 Owner 作出处置决定并留下依据；
- 已建立下游受控记录，并明确后续责任和状态关系；
- 实施与必要验证已经完成，并记录证据；
- 已证明反馈不成立、重复或不适用。

“已回复”本身不是充分关闭依据。涉及正式变更时，必须引用对应 CR、实现、Review 或验证证据。

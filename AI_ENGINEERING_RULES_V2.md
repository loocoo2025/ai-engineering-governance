# AI 软件工程项目总则——模块化兼容入口

> 从 `v0.1.8` 起，本文件不再承载全部治理正文。它是旧路径和旧章节号的兼容入口。
>
> 每个 Session 先完整阅读 `AI_START_HERE.md`，再由 `00_project/governance/GOVERNANCE_ROUTER.yaml` 和相应 Domain INDEX 按需加载原子规则。不得因为旧指令引用本文件就默认全文加载所有工程治理模块。

## 权威入口

- 工程治理目录：`00_project/governance/modules/engineering/INDEX.yaml`
- Session 治理目录：`00_project/governance/modules/sessions/INDEX.yaml`
- APLS 集成目录：`00_project/governance/integrations/apls/INDEX.yaml`

## 旧章节兼容映射

| 旧章节 | 当前权威文件 |
|---|---|
| §1～§4 | `modules/engineering/DEVELOPMENT_METHOD_AND_STRUCTURE.md` |
| §5～§7 | `modules/engineering/REQUIREMENTS_AND_TRACEABILITY.md` |
| §8～§13 | `modules/engineering/ARCHITECTURE_AND_DESIGN.md` |
| §14～§19 | `modules/engineering/IMPLEMENTATION_CI_AND_VALIDATION.md` |
| §20～§24 | `modules/engineering/ISSUES_AND_CHANGE.md` |
| §25～§27 | `modules/engineering/COMPLETION_AND_RELEASE.md` |
| §28～§35 | `modules/engineering/TASK_EXECUTION_AND_PERMISSIONS.md` |
| 原“多对话/多智能体协作规范”附录 | `modules/sessions/INDEX.yaml` |
| §36～§37 | `modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md` |
| §38.1～§38.8 | `modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md` |
| §38.7 Review Decision Matrix | `modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md#387-c04-独立评审治理` |
| §38.9 ETC | `modules/engineering/ETC_CHANGEABILITY_QUALITY.md` |
| §41 | `modules/engineering/HUMAN_APPROVAL_AND_WORK_PACKAGES.md` |

旧 Review Record、历史 Commit 和旧版本文档中对本文件章节号的引用继续按本表解释，不追溯改写历史证据。

## 失败关闭

无法通过本表或 Router 唯一解析适用规则时，输出：

```text
RULE_NOT_FOUND
RULE_CONFLICT
VERSION_AMBIGUOUS
```

不得从旧记忆补写规则。

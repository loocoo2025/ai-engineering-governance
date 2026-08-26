# 版本管理规则

- 功能分支：`feature/<id>-<name>`
- Bug 分支：`fix/BUG-xxx-<name>`
- AI 分支：`ai/<role>/<task-id>`
- 每个重要发布必须可追溯到 Commit、测试报告、构建产物和发布记录。

## 发布身份与历史

- 正式版本使用 `vMAJOR.MINOR.PATCH`；Prerelease 使用 SemVer 后缀，例如 `v0.1.4-beta.1`、`v0.1.4-rc.1`。
- 已发布的稳定版本和 Prerelease Tag 都是不可变审计锚点；不得 amend、rebase、force-push 或移动 Tag 来模拟修复。
- 稳定版本发布后即冻结。普通问题进入后续版本；不得重写已发布历史。
- Tag、Release 元数据和完整 Commit 必须一致。发生冲突时状态为 `UNKNOWN`，不得猜测目标。
- `LATEST_STABLE_VERSION` 只选择不带 Prerelease 后缀、不是 Draft/Prerelease 的最高有效稳定版本。

## Prerelease 采用

- Prerelease 必须显式选择，默认不得进入现有项目 Baseline。
- 受控升级至少需要 `ALLOW_PRERELEASE: YES`、精确版本 Tag 和完整不可变 Commit；三者不完整或不一致时停止。
- 采用前必须有可恢复的项目 Commit / Baseline 锚点，并记录回滚条件和回滚步骤。
- Prerelease 不替代当前最新稳定版本；未选择 Prerelease 的项目继续使用既有稳定版本。

## 回滚与修复

- 回滚通过新的受控 Commit 或恢复到已记录的不可变锚点完成，不删除历史记录。
- 发布后发现问题时，在后续 Patch、Prerelease 或新 Release 中正常修复；不得修改已经发布的 Tag 内容。
- 治理升级、Baseline 采用和产品 Release 分别记录，不因共享一个版本号而互相自动授权。

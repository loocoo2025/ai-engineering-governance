# v0.1.8 发布记录

版本：`v0.1.8`

Commit：由不可变 Tag `v0.1.8^{commit}` 精确解析，并必须与 GitHub Release Target 一致。

发布日期：`2026-09-13`

Release Authorization ID：`HPO-RELEASE-v0.1.8-20260913`

Authority Owner：`Human Project Owner`

授权 Target / Scope：`loocoo2025/ai-engineering-governance` 的稳定版本 `v0.1.8`，限本次 Router/模块化规则、APLS C02 集成、受控更新功能、正式 Release Candidate Commit、独立 C04、官方远程、`v0.1.8` Tag、GitHub Release 和对应 Git archive。

## 发布 Gate

| 检查项 | 要求 | 证据 |
|---|---|---|
| 正式 C04 | Release 前强制执行 | 精确 Candidate 的正式 C04 Review Record |
| Open Finding | S0～S3 必须为 0 | 正式 C04 Review Record |
| Router / INDEX / YAML / Markdown / Link | PASS | Release Gate 机械检查 |
| Git whitespace / fsck | PASS | Release Gate 机械检查 |
| 敏感信息与产品事实扫描 | PASS | Release Gate 扫描 |
| 产品 Build / Test | `NOT_APPLICABLE` | 本版本只修改治理模板，不修改产品代码 |
| APLS 项目修改 | `NOT_PERFORMED` | 只读核对公开 Release 身份 |
| Release Authorization | PASS | Human Project Owner 当前明确发布指令 |

## 发布包

- GitHub 自动生成的 Source code archives；
- `ai-engineering-governance-v0.1.8.tar.gz`，由正式 Tag 使用 `git archive` 生成；
- Archive SHA-256 在 GitHub Release 和最终发布报告中记录；
- 正式 C04 Review Record 作为 Release Asset 保留。

## Release Notes

- `13_change_management/release_notes/RELEASE_NOTES_v0.1.8.md`

## 回滚点

- 上一公开稳定版本：`v0.1.7`；
- 回滚通过新的受控 Commit 或下游项目已记录的不可变升级前 Anchor 完成，不移动或删除已发布 Tag。

## Formal Seal

- 状态：`NOT_ISSUED`
- Human Project Owner 只授权 Release，未单独签发 Formal Seal。

## Baseline Adoption

- 下游项目 Governance Baseline Adoption：`NOT_PERFORMED`
- 上游 Release 不自动替任何采用项目完成升级或 Baseline Adoption。

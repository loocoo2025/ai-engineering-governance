# v0.1.7 发布记录

版本：`v0.1.7`

Commit：由不可变 Tag `v0.1.7^{commit}` 精确解析，并必须与 GitHub Release Target 一致。

发布日期：`2026-09-11`

Release Authorization ID：`HPO-RELEASE-v0.1.7-20260911`

Authority Owner：`Human Project Owner`

授权 Target / Scope：`loocoo2025/ai-engineering-governance` 的稳定版本 `v0.1.7`，限正式 Release Candidate Commit、独立 C04、`origin/main`、`v0.1.7` Tag、GitHub Release 和对应 Git archive。

## 发布 Gate

| 检查项 | 要求 | 证据 |
|---|---|---|
| 正式 C04 | Release 前强制执行 | GitHub Release 附件中的 C04-GOV-003-v0.1.7-release-review.md |
| Open Finding | S0～S3 必须为 0 | 正式 C04 Review Record |
| YAML / Markdown / Link / Index | PASS | Release Gate 机械检查 |
| Git whitespace / fsck | PASS | Release Gate 机械检查 |
| 敏感信息与产品事实扫描 | PASS | Release Gate 扫描 |
| 产品 Build / Test | `NOT_APPLICABLE` | 本版本只修改治理模板，不修改产品代码 |
| Release Authorization | PASS | Human Project Owner 当前明确发布指令 |

## 发布包

- GitHub 自动生成的 Source code archives；
- `ai-engineering-governance-v0.1.7.tar.gz`，由正式 Tag 使用 `git archive` 生成；
- Archive SHA-256 在 GitHub Release 和最终发布报告中记录；
- 正式 C04 Review Record 作为 Release Asset 一并保留。

## Release Notes

- `13_change_management/release_notes/RELEASE_NOTES_v0.1.7.md`

## 已知限制

- 本版本定义治理合同，不提供 Worktree 调度或操作系统级写锁软件；
- `PROCEDURAL_FALLBACK` 下 Write Lease 仍依赖执行者正确登记和转移；
- 项目专有拆分深度、并行度和集成策略必须按架构与风险决定；
- 多治理版本联邦必须显式验证 Parent–Child Contract 兼容性。

## 回滚点

- 上一公开稳定版本：`v0.1.6`；
- 回滚通过新的受控 Commit 或下游项目已记录的不可变升级前 Anchor 完成，不移动或删除已发布 Tag。

## Formal Seal

- 状态：`NOT_ISSUED`
- Seal ID：`NOT_APPLICABLE`
- 精确 Target / Purpose / Scope：`NOT_APPLICABLE`
- Human Project Owner 明确决定与证据：本次只授权正式 Release，没有单独签发 Formal Seal。

## Baseline Adoption

- 下游项目 Governance Baseline Adoption：`NOT_PERFORMED`
- 说明：发布上游稳定版本不会自动替任何使用该模板的项目采用新 Baseline。

# Optional APLS Bundle

APLS（AI Programming Language Specification）是本框架的可选行为规格能力。本目录随框架分发，包含固定版本的语言说明、Schema 和参考编译器；其存在不表示项目已经采用 APLS。

## 默认行为

```text
BEHAVIOR_SPECIFICATION_MODE: DOCUMENT_BASED
```

在默认模式下，Agent 不读取本目录中的语言细节，不构建或运行编译器，也不把 APLS 产物加入交付要求。只有 Human Project Owner 或已授权 C00 明确选择：

```text
BEHAVIOR_SPECIFICATION_MODE: APLS_ENABLED
```

才按当前任务需要加载本目录内容。

## 按需入口

| 需要解决的问题 | 最先读取 |
|---|---|
| 学习和试用 APLS | `docs/APLS_0.1_USER_TUTORIAL.md` |
| 确认中文语法 | `04_design/language/APLS_0.1_ZH_CN_LANGUAGE_PROFILE.md` 和 `APLS_0.1_ZH_CN_GRAMMAR.ebnf` |
| 确认语义或歧义边界 | `04_design/language/` 中对应专题文件 |
| 确认 Canonical IR | `04_design/ir/APLS_0.1_CNL_CANONICAL_IR.md` 和对应 Schema |
| 确认诊断格式 | `04_design/diagnostics/APLS_0.1_CNL_DIAGNOSTICS.md` 和对应 Schema |
| 理解编译器设计 | `04_design/compiler/APLS_0.1_COMPILER_MVP_DESIGN.md` |
| 构建或检查编译器 | `07_src/` |

找到足以解决当前问题的入口后停止，不要求完整阅读整个 APLS 说明书。

## 编译器

需要 Rust 1.86。仅在 `APLS_ENABLED` 且当前任务确实需要编译器时运行：

```bash
cargo run --manifest-path optional/apls/07_src/Cargo.toml --bin apls -- --help
```

对编译器本身进行变更或验证时，可运行：

```bash
cargo test --manifest-path optional/apls/07_src/Cargo.toml --workspace --locked
```

构建输出位于 `optional/apls/07_src/target/`，不进入版本控制。

## 来源与许可证

- Upstream: <https://github.com/loocoo2025/apls-language>
- 固定来源、版本关系和导入范围：`SOURCE_MANIFEST.yaml`
- APLS bundle：Apache License 2.0，许可证副本见 `LICENSE`

APLS 不改变 C00～C06、Current Truth、Baseline、权限、正式 C04 或 Release Owner。能运行 APLS CLI 也不扩大当前 Session 的授权。

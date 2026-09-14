# Non-Regression Guard

本目录提供防回退合同的确定性机械校验。

运行：

```bash
python3 09_quality/non_regression/validate_non_regression.py
```

验证器本身的最小回归测试：

```bash
python3 09_quality/non_regression/test_validate_non_regression.py
```

默认读取：

```text
00_project/governance/NON_REGRESSION_CONTRACT.yaml
```

该文件使用 YAML 1.2 兼容的 JSON 子集，因此验证器只依赖 Python 3 标准库。支持：

- `FILE_EXISTS`；
- `TEXT_CONTAINS`；
- `TEXT_NOT_CONTAINS`；
- `REGEX_COUNT`。

验证器还会固定核验 Contract Owner、语义 Authority、不可原地改写策略、必需核心框架 Invariant ID 和 Supersession 链，避免通过删除核心规则或把 `LOCKED` 偷改为 `PROPOSED` 绕过 Guard。

退出码：

- `0`：全部适用 `LOCKED` Invariant 通过；
- `1`：至少一个 Guard 确认违反 Invariant；
- `2`：Contract 或输入无效，无法形成可靠结论。

治理解释：退出码 `2` 或必需 Guard 未运行时为 `REVIEW_NOT_READY`；退出码 `1` 时形成 Finding 并输出 `CHANGES_REQUESTED`；退出码 `0` 可作为 `NON_REGRESSION_VALIDATION: PASS` 的机械证据。

本验证器不运行 Contract 提供的任意命令，不替代语义评审、产品测试、Traceability Gate 或正式 C04。

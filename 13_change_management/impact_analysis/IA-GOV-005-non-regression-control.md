# IA-GOV-005：Non-Regression Control 影响分析

## 1. 变更身份

```text
CHANGE_ID: CR-GOV-005
SOURCE_VERSION: v0.1.8
TARGET_IDENTITY: v0.1.9
IMPACT_TYPE: GOVERNANCE_SEMANTIC_AND_EXECUTABLE_VALIDATION
```

## 2. 影响面

| 范围 | 影响 | 处理 |
|---|---|---|
| Current Truth / Decision | 不改变 Owner | 增加禁止静默回退和显式替代引用 |
| C00～C06 | 不改变岗位 | C00 编排、C05 验证、C06 关闭 Finding、C04 独立核验各增加现有职责内动作 |
| C04 | 增加证据维度 | 保持一个 C04、一个 Review Record、二值 Gate Decision |
| Finding | 增加 Guard Disposition 和单调历史 | 关闭状态终结；复发创建新 ID |
| Authorization | 补齐 `dispatch_limit` 机器合同 | 固化现有 Session 规则，不扩大权限 |
| Testing Governance | 增加治理 Guard 来源 | 不制造产品测试，不改变 T0～T3 风险逻辑 |
| Release | 增加适用 Guard 证据 | 不改变 Release 授权 Owner |
| Router / Lite | 增加按需加载与必备文件 | 不要求默认全文读取 |
| 下游项目 | 支持项目级 Invariant | 具体产品事实只留在项目自己的 Contract |

## 3. One Fact, One Owner

```text
防回退流程语义
→ modules/engineering/NON_REGRESSION_CONTROL.md

当前 Invariant 与 Guard 定义
→ NON_REGRESSION_CONTRACT.yaml

本次 Guard 运行证据
→ Quality Evidence / Formal Review Record

Finding 实例
→ 对应 Review Record
```

Router、Role Brief、Review Template、README 和 Prompt 只引用或执行，不复制完整规则。

## 4. 兼容性

- `v0.1.8` 历史保持不可变；
- 既有 Finding 和 Review Record 不追溯改写；
- 已关闭历史 Finding 在首次采用时可作为 Guard 候选，但不得自动升级为 `LOCKED`；
- 没有项目级 Invariant 的项目仍执行框架级 Invariant；
- `PROCEDURAL_FALLBACK` 仍可运行随模板提供的 Python Guard；不能运行时失败关闭为 `REVIEW_NOT_READY`；
- Lite 必须保留 Policy、Contract 和 Validator，避免把不可关闭控制裁掉。

## 5. 风险与控制

| 风险 | 控制 |
|---|---|
| 把所有事实锁死，阻止正常变化 | 明确允许显式 Change Decision 和替代链 |
| 每个小问题都增加 Guard | 使用四项资格条件和最小充分原则 |
| Guard 本身被弱化 | 验证器固定检查首批必需框架 Invariant ID；Contract 或验证器变更仍须进入明确 Change Set 和正式 C04 |
| 文本 Guard 误报 | 首版只保护稳定、精确、低歧义字段；语义仍由 C04 核验 |
| Contract 执行任意命令 | 验证器只支持封闭断言类型，不执行 Shell |
| 项目事实污染公开框架 | 分离 `FRAMEWORK` 与 `PROJECT` scope，模板项目列表为空 |
| C04 复杂度扩张 | 只增加两个证据字段，不新增 Role/Gate/Decision |

## 6. 验证范围

- Contract Schema、唯一 Invariant ID、唯一 Guard ID；
- 正常 Guard PASS；
- 故意破坏受保护内容的负向测试；
- 无效 Contract 的退出码测试；
- YAML/JSON、Markdown fence、Router 路径和 Template Index；
- `git diff --check`、敏感信息和项目事实扫描；
- 外部独立 C04 仅审 `v0.1.8..candidate` 及直接依赖。

## 7. Baseline Relearn

本版本增加启动内核、强制 Pre-C04 控制、C04 证据和 Finding 关闭语义。下游项目正式采用后：

```text
BASELINE_RELEARN: REQUIRED
```

采用不自动改变产品 Current Truth、当前阶段、Gate、Acceptance Threshold 或 Release 状态。

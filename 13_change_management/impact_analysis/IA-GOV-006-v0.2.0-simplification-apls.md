# IA-GOV-006：v0.2.0 治理收口与可选 APLS 集成影响分析

## 1. 变更身份

```text
CHANGE_ID: CR-GOV-006
SOURCE_VERSION: v0.1.9
TARGET_IDENTITY: v0.2.0-candidate
IMPACT_TYPE: GOVERNANCE_SIMPLIFICATION_AND_OPTIONAL_TOOLCHAIN
```

## 2. 影响面

| 范围 | 影响 | 保持不变 |
|---|---|---|
| Knowledge Routing | 首条充分匹配后停止，INDEX 前置互斥条件 | Rule Gap 仍失败关闭 |
| Optional Controls | 只在触发或负责人采用时实例化 | 权限上限不扩大 |
| Governance Upgrade | 累计 Delta + Target Manifest | 精确版本、回滚、产品事实保护 |
| Baseline Relearn | 只重建当前任务、受影响治理 Delta 和直接依赖 | 冲突仍需登记并回到唯一 Owner 解决 |
| C04 | 聚焦当前任务核心接受问题 | 独立性、精确 Target、二值 Decision |
| Feedback | 非阻断问题完整登记并保留处置历史 | 正确 Owner 最终裁决 |
| Non-Regression | 高价值 Guard，普通问题默认不永久化 | 已有 Locked Invariant 不弱化 |
| APLS | 内置可选说明书和编译器 | 默认关闭、C02 Owner、权限边界 |
| Design Intent / Semantic Authority | 正式 Baseline 行为变化必须可恢复；普通代码不是规范语义的唯一 Owner | 风险分级、Brownfield As-Is、Spike 和紧急修复仍可受控处理 |

## 3. 主要兼容性变化

本版本是 `0.2.0` 而不是 Patch，因为它改变默认知识加载、可选控制激活、升级执行和 C04 Scope 解释。旧项目采用时只迁移治理语义，不重写产品事实。

```text
BREAKING_GOVERNANCE_CHANGE: YES
PRODUCT_BEHAVIOR_CHANGE: NO
PRODUCT_CURRENT_TRUTH_CHANGE: NO
BASELINE_RELEARN: AFFECTED_GOVERNANCE_DELTA_ONLY
```

## 4. 风险与控制

| 风险 | 最小控制 |
|---|---|
| 过早停止阅读遗漏关键规则 | 互斥/排除条件必须在对应 INDEX 前置；信息不足才下钻 |
| 人类纠偏意外绕过关键控制 | 普通范围可即时缩小；关键保留决策要求明确裁决和记录 |
| 非阻断问题丢失 | 所有可信发现进入 Feedback Register 并保留处置历史 |
| C04 Scope 被故意缩窄 | Scope 必须绑定任务、批准接受条件和关键风险；偶遇关键风险必须上报 |
| 可选合同被误认为不存在 | Contract 保留 Schema，仅在触发后要求实例化 |
| APLS 增加默认 Token/依赖成本 | 默认关闭；Router 未命中时禁止读取、构建和运行 |
| APLS 快照漂移 | 精确 Commit、文件清单、许可证和 Digest 固定 |
| 升级 Fast Path 覆盖项目事实 | 累计 Diff 分类、项目 Owner 文件字段级合并、产品文件禁止修改 |
| Design Intent 被机械扩大成全量文档负担 | 只约束新增或行为变更代码；深度按风险分级；C04 不重建未变化代码设计 |

## 5. 验证边界

- Router / INDEX 结构与停止条件；
- C04 Decision Matrix、Feedback 分流及 Design Intent / 规范语义边界一致性；
- 可选控制的激活条件；
- Upgrade Manifest 与简化协议；
- APLS 快照来源、文件清单、Cargo Build/Test；
- 现有 Non-Regression Validator 和最小回归测试；
- Template File Index、YAML、Markdown、敏感信息和 `git diff --check`。

## 6. 评审范围

正式 C04 只审 `v0.1.9..v0.2.0-candidate` 的变更语义、直接受影响 Owner、APLS 可选边界和验证证据，不重新评审未变化的历史治理内容。

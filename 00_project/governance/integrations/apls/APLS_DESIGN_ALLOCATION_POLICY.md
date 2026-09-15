# APLS 设计分配策略

> 本文件是项目启用 APLS 后，C02 在 APLS 行为规格、详细设计、算法规格和 Target Profile 之间进行设计事实分配的唯一权威来源。
>
> APLS 是可选集成，不改变 C00～C06、Current Truth、Baseline、C04、Testing Governance 或 Authorization。当前是否启用只由 `CURRENT_STATE.md` 的 `BEHAVIOR_SPECIFICATION_MODE` 记录。

## 1. 核心判定

> 如果不同解释会导致系统产生不同的外部可观察行为，优先进入 APLS；如果更换实现仍保持同一行为契约，则进入详细设计、算法规格或 Target Profile。

APLS 采用 `Minimum Sufficient Specification`：只表达高价值、稳定且必须无歧义的行为，不复制类、函数、Task、驱动和代码组织。

## 2. Owner 分配

| 内容 | 默认 Owner |
|---|---|
| 状态、事件、允许/禁止条件、故障行为、恢复条件、安全联锁 | `APLS` |
| Deadline、行为级时间约束、跨组件行为契约、验收条件 | `APLS` |
| 模块、类、函数、线程/RTOS Task、缓存、资源和驱动组织 | `DETAILED_DESIGN` |
| PID、滤波、控制律、数学和数值算法 | `ALGORITHM_SPEC` |
| ADC/PWM/DI/DO/总线映射、硬件绑定和部署目标参数 | `TARGET_PROFILE` |
| 需求尚未决定且 C02 无权补齐的行为 | `SPEC_GAP` |
| APLS 当前 Profile 无法完整表达的规范行为 | `APLS_PROFILE_GAP` |

一个数值是否进入 APLS，不取决于它看起来像需求还是实现，而取决于改变该数值是否改变系统合同。

## 3. Design Allocation Table

C02 在正式详细设计前必须对重要事项形成：

| 事项 | 是否影响可观察行为 | 是否涉及安全/状态/时序 | APLS Profile 能否表达 | Owner | 理由 | 上游 Requirement/Decision |
|---|---|---|---|---|---|---|
| | YES / NO | YES / NO | YES / NO / PARTIAL | `APLS / DETAILED_DESIGN / ALGORITHM_SPEC / TARGET_PROFILE / SPEC_GAP / APLS_PROFILE_GAP` | | |

Allocation 未完成、存在双 Owner 或上游事实不明确时，不得进入正式设计输出。

## 4. C02 机械流程

```text
确认 APLS_ENABLED
→ 固定 APLS 精确 Tag / Commit / Language Profile / Compiler Version
→ 读取已批准需求、ADR 和接口
→ 生成 Design Allocation Table
→ 关闭 SPEC_GAP 或 APLS_PROFILE_GAP
→ 编写最小充分 APLS Source
→ 执行 apls check
→ 执行 apls emit-ir
→ 固定 Source、Verified IR、Digest 和诊断证据
→ 形成 Detailed Design / Algorithm Spec / Target Profile
→ 建立追溯
→ 交付 C03 或进入适用评审
```

只有 `apls check` 成功且 `apls emit-ir` 退出码为 `0` 的输出才能标记为 `VERIFIED_IR`。被拒绝、部分生成、版本不明或无法重现的输出必须标记 `APLS_INPUT_NOT_READY`。

## 5. One Fact, One Owner

- APLS Source 拥有已分配的规范行为语义；
- 详细设计引用 APLS Rule/Requirement ID，不复制或重新解释该行为；
- 算法规格拥有 APLS Profile 无法表达的数学细节，由 APLS 或详细设计精确引用；
- Target Profile 拥有硬件和部署绑定；
- C03 不得通过代码偷偷增加、削弱或替代 APLS 已冻结行为；
- C04/C05 的记录是评审和验证证据，不成为行为语义 Owner。

## 6. 下游交付合同

启用 APLS 时，C02 向 C03 交付至少包含：

```text
APLS_VERSION:
APLS_EXACT_TAG:
APLS_EXACT_COMMIT:
APLS_LANGUAGE_PROFILE:
APLS_COMPILER_VERSION:
APLS_SOURCE:
APLS_SOURCE_DIGEST:
APLS_CHECK_RESULT: PASS
VERIFIED_IR:
VERIFIED_IR_DIGEST:
DESIGN_ALLOCATION_TABLE:
DETAILED_DESIGN:
ALGORITHM_SPEC:
TARGET_PROFILE:
TRACEABILITY:
```

C03 发现这些输入缺失、冲突或过期时输出 `APLS_INPUT_NOT_READY` 并返回 C02，不得自行解释 Source 补齐行为。

## 7. C04 与 C05

适用 Review Scope 包含 APLS 时，C04 检查：

- 本应进入 APLS 的行为是否被埋在详细设计或代码中；
- 同一事实是否存在多个 Owner；
- `SPEC_GAP / APLS_PROFILE_GAP` 是否被掩盖；
- APLS Source、Verified IR、版本、Digest 和 Review Target 是否一致；
- 实现是否偏离冻结行为契约。

C05 根据已批准 APLS Acceptance、需求和风险选择最小充分验证；APLS 不自动制造全量测试或绕过现有 Testing Governance。

## 8. 权限和变更

- C02 不得用 APLS 补写未经批准的产品行为；
- 改变 APLS 规范行为必须回到正确 Requirement/Decision Owner；
- APLS Profile 或编译器版本变化必须做兼容性和影响分析；
- 技术上能运行 APLS CLI 不扩大 Role、文件写入、Commit、Push、Release 或远程权限；
- 框架在 `optional/apls/` 随附精确 Commit 固定的可选说明书、Schema 与编译器快照；上游 APLS 仓库仍是该语言的来源 Owner，导入边界由 `optional/apls/SOURCE_MANIFEST.yaml` 维护。默认 `DOCUMENT_BASED` 不读取、构建或运行该 Bundle，且模板不得记录任何本机路径。

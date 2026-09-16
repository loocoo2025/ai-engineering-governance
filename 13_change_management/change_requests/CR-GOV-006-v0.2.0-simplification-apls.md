# CR-GOV-006：v0.2.0 治理收口与可选 APLS 集成

## 1. 文档控制

```text
CHANGE_ID: CR-GOV-006
CHANGE_CLASS: GOVERNANCE_CHANGE
SOURCE_VERSION: v0.1.9
TARGET_IDENTITY: v0.2.0-candidate
DATE: 2026-09-15
STATUS: REMEDIATED_AWAITING_FORMAL_C04_REREVIEW
AUTHORITY_OWNER: Human Project Owner
```

## 2. 背景

`v0.1.9` 已具备完整治理能力，但升级协议、可选执行合同和评审准备可能使普通任务读取过多文件、重复审查未变化内容并消耗过多 Token。框架需要把复杂度封装在 Router、精确 Delta 和工具中，而不是让每个任务承担全部治理成本。

同时，APLS 已作为 C02 可选集成存在，但语法说明书和编译器仍只从外部仓库引用。`v0.2.0` 将固定版本快照内置为可选工具链，默认关闭。

## 3. 已批准原则

1. 阅读永远是按需动作；当前信息足以决定和执行时必须停止继续读取。
2. Router 与每级 INDEX 必须公开本级全部互斥、排除和停止条件；Leaf 不得突然增加会改变上层选择的全局条件。
3. 人类可以随时纠正 AI 的过度执行并缩小范围；关键安全、权限和不可逆边界仍需明确裁决。
4. Dynamic Role Profile、Knowledge Manifest、Interaction、Authorization、Task Contract 和 Worktree 控制按触发条件启用，不要求普通单任务全部实例化。
5. 治理不追求消灭所有问题。所有实际发现且有可信依据的问题必须登记，但只有与当前任务和批准接受条件直接相关的核心 Finding 阻断当前 C04。
6. 是否解决、延期、接受风险或判定为非问题，最终由正确的人类 Owner 裁决；AI/C04 提供证据、分类和建议，不得静默丢弃问题。
7. 防回退只保护关键、重复且低成本可机械判断的约束，不把每个普通问题永久升级成 Guard。
8. 升级只读取精确目标 Manifest 和累计 Delta，不逐版本重读全部 Release Notes，不全量复审未变化内容。
9. APLS 默认 `DOCUMENT_BASED`；只有明确选择 `APLS_ENABLED` 才允许加载内置说明书或运行编译器。
10. 所有学习都遵守按需原则，包括升级采用后的 Baseline Relearn；只重建当前任务所需最小知识集，允许后续在实际使用中发现、登记并解决冲突。
11. 任何进入正式产品 Baseline 的新增或行为变更代码必须具有与风险相称、可恢复的设计意图；普通实现代码可以作为 `As-Is Evidence`，但不得成为状态机、公共接口合同、错误语义、安全约束、恢复规则或关键不变量的唯一隐式规范来源。

## 4. 范围

- 收口启动内核、知识路由、可选控制激活和人类纠偏规则；
- 将治理升级协议改为精确版本累计 Delta Fast Path；
- 收口 C04 Finding / Advisory / Feedback 的任务边界；
- 限制 Non-Regression Guard 的长期治理成本；
- 内置固定、可追溯、Apache-2.0 的 APLS 说明书和编译器快照；
- 增加 `v0.2.0` Upgrade Manifest、最小验证和迁移说明。
- 收口 Design Intent 与规范系统语义的权威边界，同时保留 Brownfield、Spike、紧急修复和生成代码的风险相称处理。

## 5. 不在范围

- 不改变 C00～C06 固定岗位；
- 不新增 Current Truth Owner、Reviewer Role 或第三种 C04 Decision；
- 不改变产品项目事实、需求、架构、接口、代码或测试结论；
- 不自动启用 APLS；
- 不要求普通问题全部修复后才能推进；
- 不增加新的复杂审批链、Bot 或远程服务；
- 不重写已发布 Tag、Release 或历史 Review Record。

## 6. 必须保留的关键控制

- Current Truth 与 One Fact, One Owner；
- 人类保留的产品目标、公共接口、重大架构、安全、数据完整性、风险接受和 Release 决定；
- 权限继承、远程/破坏性操作授权；
- 正式 C04 的独立 Session、精确 Target、Review Record 和二值 Decision；
- 适用 Baseline、Traceability、Acceptance Threshold 和 Release 证据；
- Git 历史、已关闭问题、已发布版本和关键 Locked Invariant 的不可变审计锚点。

## 7. 授权时间线与 C04-GOV-006-F001 处置

### 7.1 初始授权

初始范围允许修改治理模板、导入只读 APLS 可选快照、运行最小验证并形成 `v0.2.0-candidate`，当时暂不授权 Commit、正式 C04、Baseline Adoption、Tag、Push、Release 或 Formal Seal。

该初始边界在后续 Human Project Owner 已明确扩展 Commit 授权后没有及时更新，是 `C04-GOV-006-F001` 所识别的审计冲突来源之一。

### 7.2 两次历史 Commit 的实际授权与缺口

Human Project Owner 在对应 Commit Action 发生前分别给出：

```text
“commit吧，然后我去网页c04”
→ ACTION: COMMIT
→ CONSUMPTION_EVENT: 75743a1191f107d430dbfec324c0540b6d3c86df 创建成功

“好的，下一步吧，先commit”
→ ACTION: COMMIT
→ CONSUMPTION_EVENT: 4d20560ebfbf558130b0dda69f7b087968068efe 创建成功
```

2026-09-17，Human Project Owner 通过 `HUMAN DETERMINATION — C04-GOV-006-F001` 确认：两次 Commit 都具有先行 Human Owner 授权意图，但执行前没有按 `v0.1.9` 实例化完整的结构化 Authorization Contract，且本 CR 没有及时记录授权变化。这被裁定为程序性治理违规，不是未经 Human Owner 同意的 Commit。

本记录不声称事前结构化合同曾经存在，不把后续 C04 Dispatch 解释为追溯 Commit 授权，也不改写、删除或替换已有 Commit 历史。

### 7.3 本次 Finding 整改授权

```text
AUTHORIZATION_ID: AUTH-GOV-006-F001-FILE-MODIFICATION
AUTHORITY_OWNER: Human Project Owner
ACTION: FILE_MODIFICATION
SCOPE: 保存正式 C04 Record；记录真实授权时间线、程序性违规、Human Determination 与 Caller Correction；机械更新 Template File Index
TARGET: 05_reviews/C04-GOV-006-v0.2.0-candidate.md + 本 CR + TEMPLATE_FILE_INDEX.md
ALLOWED_SIDE_EFFECTS: 上述精确本地文件修改
FORBIDDEN_SIDE_EFFECTS: 其他治理语义、产品事实、历史改写、Push、Tag、Release、Baseline Adoption、Formal Seal
VALIDITY: ONE_REMEDIATION_EXECUTION
CONSUMPTION_EVENT: 上述精确工作树整改形成并进入授权的本地整改 Commit
TERMINAL_STATE: EXECUTION_COMPLETED_BY_COMMIT_CONTAINING_THIS_RECORD
RETRY_POLICY: NO_AUTOMATIC_RETRY
STATUS: CONSUMED_BY_COMMIT_CONTAINING_THIS_RECORD
AUDIT_REFERENCE: Human Project Owner message “HUMAN DETERMINATION — C04-GOV-006-F001” dated 2026-09-17

AUTHORIZATION_ID: AUTH-GOV-006-F001-COMMIT
AUTHORITY_OWNER: Human Project Owner
ACTION: COMMIT
SCOPE: 创建一个只包含上述证据整改的本地 Commit
TARGET: DIRECT_CHILD_OF 4d20560ebfbf558130b0dda69f7b087968068efe
ALLOWED_SIDE_EFFECTS: ONE_LOCAL_REMEDIATION_COMMIT
FORBIDDEN_SIDE_EFFECTS: Push、Tag、Release、Baseline Adoption、Formal Seal、历史改写、产品事实修改
VALIDITY: ONE_REMEDIATION_EXECUTION
CONSUMPTION_EVENT: 包含本记录的直接子 Commit 创建成功
TERMINAL_STATE: EXECUTION_COMPLETED_BY_COMMIT_CONTAINING_THIS_RECORD
RETRY_POLICY: NO_AUTOMATIC_RETRY
STATUS: CONSUMED_BY_COMMIT_CONTAINING_THIS_RECORD
AUDIT_REFERENCE: Human Project Owner message “HUMAN DETERMINATION — C04-GOV-006-F001” dated 2026-09-17
```

该授权不产生 C04 `PASS`，不自行关闭 `F001`。整改后必须针对新的精确 Commit 建立全新独立 C04 Session 复审。

## 8. 接受条件

- 普通任务能够在首个充分路由结果后停止阅读；
- 未启用的可选控制不产生缺失错误或实例化负担；
- 升级协议不再要求逐版本阅读和全量复审；
- Baseline Relearn 不再要求先学习全部需求、架构、设计、代码、测试或历史记录；
- C04 只让当前范围内的核心 Finding 阻断，其他可信问题进入 Feedback；
- APLS 默认关闭且未命中时不读取、不构建、不运行；
- APLS 快照绑定精确来源、许可证和验证命令；
- 正式 Baseline 的行为变化能够追溯到与风险相称的 Design Intent，关键系统语义不只隐含在普通实现代码中；
- 所有现有关键 Non-Regression Guard 继续通过；
- 无具体产品事实、本机路径、凭据或内部项目名称进入模板；
- `git diff --check` 通过。

## 9. 候选验证证据

```text
YAML_PARSE: PASS
MARKDOWN_FENCE_CHECK: PASS
TEMPLATE_FILE_INDEX: PASS (240 files)
NON_REGRESSION_UNIT_TESTS: PASS (9)
LOCKED_INVARIANT_GUARDS: PASS (5 invariants / 22 guards)
APLS_SOURCE_SNAPSHOT_MATCH: PASS
APLS_COMPILER_FORMAT: PASS
APLS_COMPILER_TESTS: PASS (43 passed / 2 intentionally ignored / 0 failed)
SENSITIVE_AND_LOCAL_PATH_SCAN: PASS
GIT_DIFF_CHECK: PASS

INITIAL_C04_TARGET: 4d20560ebfbf558130b0dda69f7b087968068efe
INITIAL_FORMAL_C04: CHANGES_REQUESTED
OPEN_FINDING: C04-GOV-006-F001 — S1 Major
REMEDIATION_TARGET: RESOLVE_FROM_THE_COMMIT_CONTAINING_THIS_RECORD
FORMAL_C04_REREVIEW: REQUIRED_NOT_STARTED
```

APLS Bundle 绑定上游精确 Commit `25c38b494e4e52dfe16945d8930f7d47088eb6de`，选定上游 Archive SHA-256 为 `309636fdf195132b603fc7a1703b05078ec4de5b5e6c6a8bbf56617d87c16651`。编译器与上游 `v0.1.0` Tag 内容一致；完整来源关系见 `optional/apls/SOURCE_MANIFEST.yaml`。

### 9.1 Formal C04 Record 与 Caller Correction

正式初审记录：`05_reviews/C04-GOV-006-v0.2.0-candidate.md`。

Reviewer 返回文本中的 Candidate ZIP SHA-256 被误抄为包含重复片段的字符串。Caller 依据生成时记录和独立 `shasum -a 256` 结果确认正确值为：

```text
20e02241c481927a83b420c964075fe11bcfb496debf08b70336d715c532f8e5
```

该 Caller Correction 只修正 Review Package Hash 的转录错误，不修改 Reviewer 原文、Finding、Severity、关闭条件或 `CHANGES_REQUESTED` 结论。

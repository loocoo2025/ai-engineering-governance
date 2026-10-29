# CR-GOV-007：v0.2.1 评审减负与可选工控 Profile

## 1. 身份与批准范围

```text
CHANGE_ID: CR-GOV-007
CHANGE_CLASS: GOVERNANCE_CLARIFICATION / TEMPLATE_CHANGE
SOURCE_VERSION: v0.2.0
SOURCE_COMMIT: 54c05933f21f7e129ae08b22e1437f465427c0a8
IMPLEMENTATION_BASE_COMMIT: 95a4f1e7eccd903abe1f34f4a503adda7e29588c
TARGET_IDENTITY: v0.2.1
DATE: 2026-10-29
STATUS: C04_PASS_RELEASE_READY
AUTHORITY_OWNER: Human Project Owner
```

负责人在修改前明确要求：“按照你的建议修正一下，然后发布个 v0.2.1”，并补充“把新增的两个 Profile 也放进去”。本记录保存此次真实授权，不复用 CR-GOV-006 的历史授权，不声称本候选已通过正式 C04。

已批准内容及唯一规则位置：

| 内容 | 处理位置 |
|---|---|
| 消除无条件全量验证措辞 | 开发方法、实现验证、问题变更模块引用既有 Testing Governance |
| 阶段质询不自动等于正式 C04 | 架构设计模块引用保障政策 |
| 严重 Finding 后按剩余检查价值结束评审 | CURRENT_TRUTH_AUTHORITY_AND_REVIEW §38.7.5；其他入口仅引用 |
| 同一精确 Target 合并兼容触发事件，任务层级不增加 Gate | PROJECT_ASSURANCE_CADENCE_POLICY §5；分解政策引用 |
| 限定治理维护与等价检查的非触发边界 | 同一保障政策；既有 LOCKED 替代链保持不变 |
| 可选 PLC/MCU Profile | docs/profiles/ 两份已有文档；Manifest、索引和发布说明纳入 |

本轮不改变 C00～C06、事实 Owner、Finding 严重度、二值结论、独立性、关闭验证、权限上限、Traceability 或产品接受标准。不修改现有 LOCKED Contract、校验器、产品仓库、APLS 快照或历史评审。

## 2. 影响与接受条件

本版本修正导致过度评审的入口和执行边界，不要求已有项目追溯重写历史。属于 `0.2.x` 的定向补丁，但包含评审执行语义变化；下游不能只替换版本号或自动豁免当前 Gate，采用时必须按累计 Delta 进行增量 C04。

主要风险及控制：

- 严重问题后继续检查被误读为继续实现：只允许冻结范围和预算内仍有效的只读检查，停止受影响推进，不参与整改，不要求穷尽。
- 合并评审被用于跨版本沿用 PASS：必须同一精确 Target、兼容的标准、明确覆盖范围；缺失的集成证据不能被子级 PASS 替代。
- 治理维护例外被用于弱化检查：只适用于不改变规则效力的维护；新 LOCKED 声明、登记 Guard 定义或替代关系仍进入正式链，无法证明等价时不使用例外。
- 可选附件覆盖项目定制：Profile 默认不启用，已有项目文件做三方合并/人工裁决，不覆盖本地采用状态或自有约束。

接受条件：五项修改与提示词/角色/Session 入口一致；S0～S3 的接受阻断及独立复审保留；适用既有 Guard 通过；文件索引准确；两个 Profile 随包且默认不启用；正式增量 C04 PASS 后才发布。

验证限于修改文本和 YAML、引用/索引、适用既有 Guard、候选精确版本与 archive 保真。校验器、产品代码和 APLS 未改，不运行其全量测试。

## 3. 执行前授权

以下各行是独立 Action Class，共用本节范围和约束；发布意图不替代正式评审结论。本节是动作执行前的授权快照，各动作实际消费由对应 Git Commit、Tag、远端引用或 Release 产物证明，不把未执行动作记为已完成。

```text
AUTHORIZATION_ID: AUTH-GOV-007-V021-PUBLICATION
AUTHORITY_OWNER: Human Project Owner
AUDIT_REFERENCE: 本会话 2026-10-29 的 v0.2.1 修正与发布请求及 Profile 补充
SCOPE: 第1节所列治理增量、Profile附件、必要的候选/评审/版本/索引/发布记录
TARGET: 从上述 SOURCE_COMMIT 累计到冻结的 v0.2.1 候选；正式发布前另记完整发布 Commit
ALLOWED_SIDE_EFFECTS: 下表各动作及 output/ 中的候选评审包与正式 archive
FORBIDDEN_SIDE_EFFECTS: 产品事实修改、历史改写、force push、移动既有Tag、Baseline Adoption、Formal Seal、自动启用项目Profile、自动发起收费模型或外部会话
VALIDITY: THIS_V0_2_1_CHANGE_UNTIL_PUBLICATION_OR_CANCELLATION
CONSUMPTION_EVENT: 各行指定的动作产物首次成功形成
TERMINAL_STATE: EXECUTION_COMPLETED / CANCELLED / RESULT_UNKNOWN_RECONCILIATION_REQUIRED
RETRY_POLICY: NO_AUTOMATIC_RETRY；结果未知先只读对账
DISPATCH_LIMIT: 各行限定动作次数；不授权自动独立Session或模型派发
ESCALATION: 缺少必要评审结果、目标冲突或超出范围时停止对应动作，向负责人报告
STATUS: ISSUED_UNUSED
```

| Action | 精确范围/目标与生效条件 | 消费事件 | 次数上限 |
|---|---|---|---|
| FILE_MODIFICATION | 第1节范围及本记录、Manifest、Changelog、README版本、Router/机器合同版本、文件索引、v0.2.1发布说明、后续正式Review原文 | 候选及后续保真归档/版本登记各次完成 | 候选1次；PASS后归档与元数据1次 |
| COMMIT | 一个直接位于 IMPLEMENTATION_BASE_COMMIT 后的候选；PASS后一个仅归档和版本元数据的后代Commit | 对应Commit创建成功 | 每种1次 |
| TAG_CREATION | 未存在的 annotated v0.2.1，绑定通过评审的治理树加保真归档/版本元数据的精确Commit | Tag首次创建成功 | 1 |
| PUSH | origin及gitee的main快进与新的v0.2.1 Tag；目标一致且无远端分叉 | 各远端首次确认目标引用 | 每远端1次 |
| RELEASE | loocoo2025/ai-engineering-governance 的 v0.2.1 正式GitHub Release；英文说明，附精确Tag archive与SHA-256 | Release首次成功发布 | 1 |

如评审要求实质整改，先提交问题及建议，不能把本次有限 Commit 次数解释为无限重试授权。负责人沿用新的网页 ChatGPT Session 执行正式 C04；本实现会话只准备输入包，辅助核对不冒充正式 C04。

## 4. 评审与发布状态

本节保留候选提交前快照；最新评审结果及发布准备见第 5 节。

候选提交前准备检查：修改的三份 YAML 可解析且候选版本一致；累计文件索引 247 项准确包含两份 Profile 和本轮两份新记录；旧的无条件全量验证及 S0/S1 即停表述已在活动入口替换；`git diff --check` 无空白错误。现有轻量 Non-Regression 验证器一次执行 5 条 Locked Invariant / 22 个 Guard，结果 PASS、退出码 0；这些是机械检查，不是正式 C04。未改校验器、产品代码或 APLS，不执行其全量测试。

本轮独立评审目标为 v0.2.0 精确 Commit 到本候选的累计 Delta，包括已提交的两个 Profile。评审记录位置预定义为 `05_reviews/C04-GOV-007-v0.2.1-incremental.md`，无需在发起前填入结论。

```text
FORMAL_REVIEW_RESULT: NOT_YET_RECEIVED
PUBLICATION_STATUS: PENDING_INCREMENTAL_C04
```

收到结果后按保障政策 §5.1 保真归档并登记精确 Target。归档、版本登记本身不递归触发 C04；混入实质整改时重新判断。历史 v0.2.0 PASS 不能替代本轮结论。

## 5. 独立 C04 结果、保真归档与正式版准备

候选提交后，负责人明确改为“给 mydot 吧，别给网页了”，并要求使用 Codex 内的入口。该后续要求替代第 3 节的原网页递交路线，不改变候选内容和判定标准。mydot 随后调度全新独立 Session，在只读精确候选后返回正式记录；本实现会话未代替 Reviewer 判定。

```text
REVIEW_ID: C04-GOV-007-v0.2.1-incremental
REVIEW_TARGET: 6fb867df3f9eec9ca7557a6c285b291752e71dd4
REVIEW_READINESS: READY
CURRENT_CHANGE_VALIDATION: PASS
NON_REGRESSION_VALIDATION: PASS
OPEN_IN_SCOPE_FINDINGS: 0
FORMAL_DECISION: PASS
FORMAL_REVIEW_RECORD: 05_reviews/C04-GOV-007-v0.2.1-incremental.md
SOURCE_REVIEW_THREAD: 01a18778-5963-7317-998f-98e3cbeba027
PRE_EDIT_SOURCE_BODY_SHA256: 79806ed26b32f599d41bb20fd046d1295cd11a736b230471061c3ea825cccdde
ARCHIVED_BODY_SHA256: 79806ed26b32f599d41bb20fd046d1295cd11a736b230471061c3ea825cccdde
BODY_BYTES: 21108
BODY_LINES: 267
NORMALIZATION: NONE；UTF-8、LF、一个末尾LF
```

正文提取边界为 Reviewer 返回的 BEGIN_FORMAL_C04_RECORD / END_FORMAL_C04_RECORD 标记之间，从 `# Code Review` 开始至正文末尾 LF，不含标记和交付导语。来源为该 Session 实际发送参数及其完整正式回复，归档字节与 Reviewer 在发送前提供的 Hash 相同；未编辑原文或补造独立性证据。

按第 3 节已有授权，当前只新增上述评审原文，并更新本 CR、文件索引、README 基线、Changelog 日期、Release Notes、Router/执行合同/Upgrade Manifest 的正式版本元数据。保障/评审规则、两份 Profile、Locked Contract 和校验器保持已评审候选字节。执行合同的 `release_status` 随版本从 CANDIDATE 登记为 STABLE，不改变授权或控制语义。

这属于保障政策 §5.1 的保真归档及版本登记，不递归触发 C04；原 PASS 仍只绑定原候选。正式发布 Commit 是上述候选之后唯一的归档/元数据 Commit，创建后在 `output/v0.2.1-release/PUBLICATION_TARGET.json` 记录完整 Hash，随后才创建新 annotated `v0.2.1`、快进两端 main 和 Tag，并创建英文 GitHub Release。该输出记录不是新的事实 Owner；Git/Tag/Release 产物提供最终身份。

本节记录执行前发布准备，不预称远端成功。远端结果以实际引用、Release URL 和可下载 archive 的 SHA-256 为凭据；不得把发布失败登记为成功，也不得移动已发布版本修复问题。

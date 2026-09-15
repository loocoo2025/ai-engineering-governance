# 新项目 AI 启动指令

```text
你现在参与一个新的正式软件项目。第一步不要写代码。

必须首先完整阅读 `AI_START_HERE.md`，再读取 `00_project/governance/GOVERNANCE_ROUTER.yaml`，根据当前 Role、Task、Action、Gate、Risk 和启用的集成加载 Domain INDEX 标记的最小规则包。不得默认全文读取全部治理文件，也不得在本提示词中建立另一份竞争性的阅读顺序。

本项目采用：迭代式 V 模型 + 需求追溯 + ADR + AI 独立评审 + 自动化验证 + 真实环境验证 + 多对话交接。

先判断当前应该属于 C00~C06 哪个角色。项目刚开始时先作为 C00/C01，不要直接编码。

项目负责人默认停留在持续逻辑 C00 控制通道。需要独立 Expert/C04 Session 时，由 C00 按权威请求格式明确提出并在当前 AI 环境/当前项目优先自动创建；物理 C00 Session 只在上下文阈值或完整性触发时受控交接。

Role != Model != Runtime != Harness != Session != Tool。C00～C06 是固定标准岗位，不绑定具体运行实现。确定角色后，只在风险、跨 Session、正式 C04、受控副作用、并行写入或负责人选择等权威触发条件成立时，才生成或核验 Dynamic Role Profile、Knowledge Manifest、Interaction、Authorization、Output Contract 或 Worktree Control；未触发的普通本地单 Session 任务不制造空合同。从 CURRENT_STATE.md 读取 AUTONOMY_MODE、AUTHORIZED_UNTIL、PREAUTHORIZED_GATES、ASSURANCE_CADENCE_PROFILE、ENFORCEMENT_MODE、执行槽位和 HUMAN_PROJECT_OWNER 当前配置。辅助调用不等于正式 C04，任何被调用执行单元都不得扩大 Caller 权限。

涉及项目拆分、跨模块、并行写入或 Parent / Child 集成时，从 PROJECT_STRUCTURE_MAP.md 确认 SINGLE_PROJECT / MODULAR_PROJECT / FEDERATED_PROJECT。大型项目按稳定边界递归拆分；多 Session 或并行写入命中控制时，写入 Worker 必须绑定一个活动 Leaf / Integration Work Package、一个 Output Contract、一个 Git Worktree 和一个活动 Writer。并行 Writer 使用不同 Worktree 和 Branch，同一本地目录同时只能有一个 Writer。Parent 默认依赖精确 Child Acceptance Package 和独立评审证据，只审核接口、集成、系统接受和组合风险，不把所有子级实现细节加载进一个 Session。

默认由 Primary Executor 在已授权范围内连续执行；`QUESTION_PRIORITY / WORK_PRIORITY` 为 P0/P1 的问题或其他复杂问题，由 Primary Executor / C00 形成最小 Escalation Package 交给 Expert。C04 Finding 使用 S0～S3；C04 形成 S0/S1 Finding 时只记录 Finding、关闭条件和 `CHANGES_REQUESTED` 后停止，不参与整改设计，也不得自行关闭 Finding。需要修改 Current Truth、改变产品目标或 Acceptance Threshold、裁定新的系统边界/公共接口/跨系统依赖/安全或数据完整性设计/重大不可逆架构取舍、接受重大风险、签发 Formal Seal，或执行未获精确预授权的 Baseline Adoption / Release / 重大副作用时，使用 Human Determination Package 请求项目负责人。

重要需求、决策、质询、测试结果、Bug 和变更必须落入正式项目文件。

已接受事实和已关闭问题不得被后续变更静默带回。只有当前变化命中适用 `LOCKED` Invariant、既有 Guard、Finding Guard 判定或 Target Manifest 强制项时，才加载 `NON_REGRESSION_CONTROL.md` 和 `NON_REGRESSION_CONTRACT.yaml`。只有关键、重复、高影响、长期有效、可机械判断且防御成本合理的根因才转成 `LOCKED` Invariant 和 Guard；普通、一次性或非阻断问题保留记录即可。适用的必需 Guard 未运行或无效时不得进入正式 C04 判定，Guard 确认违反时不得 `PASS`。

如果 `CURRENT_STATE.md` 明确配置 `BEHAVIOR_SPECIFICATION_MODE: APLS_ENABLED`，C02 必须加载 APLS 集成目录并先完成 Design Allocation；默认 `DOCUMENT_BASED` 时不得无故加载或强制使用 APLS。

先输出：
- 当前角色
- 当前 Dynamic Role Profile / Knowledge Manifest 状态（未触发时为 NOT_APPLICABLE）
- 当前 Model/Runtime/Harness 执行槽位、Autonomy Mode、Enforcement Mode 和授权上限
- 当前 Interaction / Authorization 状态
- 当前项目结构模式、Project / Subproject / Module / Work Package 绑定
- 当前 Output Contract / Worktree / Branch / Write Lease（未触发或只读任务说明 NOT_APPLICABLE）
- 当前阶段
- 项目目标理解
- 当前缺少的关键输入
- 下一步
- 是否存在需要 Expert Escalation 的 `QUESTION_PRIORITY` P0/P1 问题
- 是否存在必须由 Human Project Owner 决策的事项
- 当前变化命中的 Non-Regression Invariant 与 Guard 状态（未命中时为 NOT_APPLICABLE）
```

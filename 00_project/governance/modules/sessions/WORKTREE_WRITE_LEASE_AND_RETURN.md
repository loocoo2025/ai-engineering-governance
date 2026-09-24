> Authority：单 Output Worker、Git Worktree、Write Lease、Task-local Handoff 和结果返回；由 `INDEX.yaml` 按触发条件加载。

## 41.7 单 Output Worker Session 与 Git Worktree 隔离

项目分解、Leaf / Integration Work Package、Parent–Child Contract 和分层接受语义由 `00_project/governance/PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md` 维护。本节只规定 Session、Worktree、Writer 和 Handoff 如何执行。

写入 Worker 的机械绑定为：

```text
ONE_WRITE_SESSION
= ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE
= ONE_OUTPUT_CONTRACT
= ONE_GIT_WORKTREE
= ONE_ACTIVE_WRITER

ONE_LOCAL_WORKING_DIRECTORY
<= ONE_ACTIVE_WRITER
```

`ONE_ACTIVE_EXECUTABLE_WORK_PACKAGE` 只允许 `LEAF_EXECUTION / INTEGRATION`。

规则：

1. 一个写入 Worker Session 完成一个明确 Output Contract 后必须结束或冻结；新的无关 Output 使用新的 Worker Session；
2. 多个写入 Session 并行必须使用不同 Git Worktree 和不同 Branch；每个 Worktree 在 `ACTIVE_TASKS.md` 只有一个 `ACTIVE` Write Lease；
3. 单 Writer 串行工作可以使用当前项目 Worktree，但 C00 必须明确绑定；无法建立 Worktree 时不得启动多个 Writer；
4. 默认项目目录推荐作为 Integration Worktree，由唯一 Integration Owner 接收精确子 Commit、解决冲突、运行集成验证并形成 Parent Review Target；普通 Worker 不直接在该目录并行开发；
5. Worktree 隔离不扩大授权。文件修改、Commit、Merge/Cherry-pick、Push、PR 和 Release 仍为独立 Action；
6. 不同 Worktree 的 Write Scope 默认不得重叠。共享文件、接口或事实 Owner 必须先冻结上游合同、串行执行，或建立单独 Integration Work Package；
7. C04 对精确不可变 Commit 只读评审。它可以使用独立只读 Checkout/Worktree，但不得持有实现 Write Lease，也不得修改 Target；
8. Session、Worktree、Branch、Base Commit、Write Scope、Output Contract 和 Lease 当前绑定只写入 `ACTIVE_TASKS.md`；`CONVERSATION_MAP.md` 只维护 Session 生命周期。

为边界明确且输入自足的 Leaf / Integration Work Package 建立隔离 Worker Session 时，使用 `NEW_INDEPENDENT_SESSION_REQUEST`，并将：

```text
reason_code: BOUNDED_WORK_PACKAGE_EXECUTION
formal_gate_authority: NONE
```

该 Reason Code 只证明需要独立任务上下文，不产生 C04 身份或 Gate 权威。默认在当前 AI/Harness 的当前项目中创建；只有外部配置已由负责人手动启用并选择 Profile 时，才允许自动创建到外部 AI。

### 41.7.1 Write Lease 转移

上下文耗尽但 Output 尚未完成时，允许新物理 Session 接续同一个 Worktree 和 Output Contract，但禁止新旧 Session 同时写入：

```text
OLD_SESSION stops writing
→ WRITE_LEASE: HANDOFF_PENDING
→ record Git status / diff / branch / base commit
→ create Task-local HANDOFF
→ OLD_SESSION: READ_ONLY / FROZEN
→ NEW_SESSION verifies Task / Output / Scope / Authority
→ OLD WRITE_LEASE: FROZEN
→ NEW WRITE_LEASE: ACTIVE
→ NEW_SESSION continues
```

无法证明旧 Writer 已停止、Git 状态未知或存在双重 Lease 时，标记 `WRITE_LEASE_CONFLICT` 并停止写入。

### 41.7.2 Task-local Handoff 与向上返回

Handoff 只包含当前未完成 Leaf / Integration Work Package 所需的需求、决定、接口、依赖、Diff、测试、风险和下一步。不得默认携带整个 Parent、兄弟 Module、已完成任务、完整聊天或私有推理。

完成的子任务不通过 Handoff 无限向上传递上下文，而是返回：

```text
OUTPUT_COMMIT
OUTPUT_CONTRACT_RESULT
COMPLETION_CAPSULE_OR_CHILD_ACCEPTANCE_PACKAGE
TEST_AND_REVIEW_EVIDENCE_REFERENCES
OPEN_RISKS
```

Parent / C00 消费受控摘要和精确证据；只有命中 Drill-down Trigger 时，才为指定子链路建立新的定向 Session。

### 41.7.3 可选 Multi-agent 自动委派

本节是自动委派的稳定规则 Owner。当前选择只由 `CURRENT_STATE.md` 的 `MULTI_AGENT_MODE: OFF | AUTO_DELEGATE` 维护；字段缺失按 `OFF` 处理，不追溯改变既有任务或要求下游自动启用。

负责人明确启用 `AUTO_DELEGATE` 后，Root 可以在当前任务授权和已批准资源边界内，自行将适合并行的 Bounded Task / 工作切片交给 Subagents，无需逐次重复询问普通派发。`OFF` 不自动委派；单次显式委派授权仅对该次有效，不永久改变开关。

Root / Subagent 是执行关系，不是新增 C00～C06 岗位、审批 Owner 或项目结构模式；多 Agent 使用现有任务、Output、Session、Worktree 和结果返回记录，不增加第二套任务体系。

派发前确认：

1. 子任务产出和接受条件明确，输入自足，只需当前切片及直接依赖；
2. 依赖已稳定，写入范围不冲突，并行收益大于上下文、协调及集成成本；
3. 强依赖或需要连续上下文的工作优先留在 Root；前置输入稳定后可以再委派下游，不为并行而拆碎小任务；
4. 写入 Worker 复用第 41.7 节的独立 Session、Worktree 和单 Writer 规则；共享目录的 Harness 不能保障写入隔离时，只并行派发只读任务，写入改为串行。只读任务不为形式创建 Worktree，不持有 Write Lease；
5. Root 不得在子 Writer 所占目录同时写入；Root 亲自实现或集成时也须绑定一个适用的执行包与写入范围。

`SUBAGENT_PERMISSION <= CALLER_PERMISSION` 始终成立。启用开关不等于授予 Commit、Merge、Push、PR、Release、远程/破坏性动作或额外模型费用权限。默认使用当前 AI/Harness 项目；自动创建外部 AI Session 仍受 `EXTERNAL_AI_TRANSFER_CONFIG.yaml` 的负责人选择约束。不支持所需工具或超出资源边界时，报告限制并退回串行，不伪装已经派发。

Root 负责协调、核验返回证据、处理冲突、集成和风险相称的最终验证，不默认重读所有子实现或重跑已有有效内部测试。子任务结论缺少证据时不能自动接受；正式 Child Acceptance、Baseline、Release 仍适用原保障触发。

Subagent 自检、Root 集成核验及普通辅助审阅均不自动成为正式 C04。派发工具的“新 Agent”不证明上下文独立；正式 C04 仍需单独发起、冻结精确 Target、核验隔离、满足授权并形成正式记录。

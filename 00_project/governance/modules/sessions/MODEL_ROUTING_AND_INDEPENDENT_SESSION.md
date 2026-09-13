> Authority：模型路由、Expert/C04 独立 Session 创建和外部 AI Session 边界；由 `INDEX.yaml` 按触发条件加载。

# 41. 模型路由下的对话编排

固定 Role、动态 Profile、Role / Model / Runtime / Harness / Session / Tool 定义、Interaction、通用授权、四条运行线、Formal Seal 和执行保障模式，以 `00_project/governance/ROLE_INTERACTION_EXECUTION_POLICY.md` 为唯一权威来源；执行槽位、Expert 路由、权限继承和正式 C04 语义见 `00_project/governance/modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md`。本文件只规定 Session、上下文和交接如何编排；当前实际运行槽位值、Autonomy Mode、Enforcement Mode 和自动授权上限见 `CURRENT_STATE.md`。

## 41.1 三类执行 Session

```text
Primary Session
→ 承担 C00/C01/C02/C03/C05/C06 的默认连续执行

Expert Escalation Session
→ 接收最小 Escalation Package
→ 只加载回答精确问题所需的最小文件
→ 输出技术结论和 HUMAN DECISION REQUIRED

C04 Independent Review Session
→ 使用全新独立上下文
→ 从正式文件和精确 Git Review Target 重建事实
→ 不继承实现 AI 的私有推理
→ 先记录 Review Readiness，只有 READY 时才产生 Gate Decision
```

任何受控 Session 执行前必须存在 `DYNAMIC_ROLE_PROFILE` 和 `KNOWLEDGE_MANIFEST`，并与当前 Role、Task、当前或适用 Gate、适用事实 Owner、Interaction、Authority、Model/Runtime/Harness/Session 绑定一致。Profile 未就绪时不得通过提示词猜测权限。

执行角色在 Session 内发起的辅助 Model / CLI / API 调用不是新的治理 Session，沿用调用者 Role 和权限边界，其输出仅为 `ADVISORY / AUXILIARY`。只有按照正式独立评审流程建立的 `C04 Independent Review Session` 才能产生 C04 Gate 结论。

项目负责人默认停留在持续的逻辑 C00 控制通道。C00 可以协调兼容的 Primary 工作、发起当前 Session 内 Auxiliary/Advisory Tool 调用、建立 Expert/C04 子 Session，并把受控结果收回当前任务。子 Session 不要求负责人手工切换查看；只有命中负责人保留决策时才向负责人提出问题。

```text
DEFAULT_SESSION_ACTION: CONTINUE_CURRENT_SESSION
```

需要独立 Session 时必须先明确输出并形成第 41.5 节请求包；不得静默停止并假设负责人会自行创建会话。

Role、Model、Runtime、Harness、Session 和 Tool 是六个独立维度。`CONVERSATION_MAP.md` 继续只维护角色、对话版本和生命周期，不登记 Model/Runtime/Harness 路由或工具调用。

## 41.2 升级与返回

检查或裁决意图必须先按岗位交互与可执行治理政策唯一分类为：

```text
INDEPENDENT_REVIEW
CONTEXTUAL_REVIEW
SELF_REVIEW
HUMAN_DETERMINATION
```

`INDEPENDENT_REVIEW` 进一步区分 `FORMAL_C04` 与 `INFORMAL_INDEPENDENT`。只有 `FORMAL_C04` 能产生正式 C04 Gate Decision；非正式独立评审、Contextual Review 和 Self Review 都不能冒充 C04。普通实现、查询和机械动作不因完成后需要自检就自动进入正式评审。

Primary 命中工程总则的 Expert Escalation 触发条件时：

1. 固定问题范围和 What Must Not Change；
2. 生成最小 Escalation Package；
3. 优先启动 `EXPERT_ESCALATION_PRIMARY`；
4. Expert Primary 不可用时启动 `EXPERT_ESCALATION_FALLBACK`；
5. Expert 输出 `HUMAN DECISION REQUIRED = NO` 时，结论返回原角色和原 `ACTIVE_TASK` 自动继续；
6. 只有输出 `YES` 且命中人工权威边界时，才由 C00 向项目负责人提出一个最重要问题。

Primary 执行中 `QUESTION_PRIORITY / WORK_PRIORITY` 为 P0/P1 的问题首先触发 Expert Escalation，不直接等同于人工阻塞。P2/P3 在当前批准范围内默认由 Primary 自动处理。P0～P3 不是 C04 Finding Severity。

C04 形成 S0/S1 Finding 时只记录 Finding、给出关闭条件和 `CHANGES_REQUESTED`，然后停止。后续编排必须为：

```text
Primary Executor / C00
→ 根据 Finding 启动 Expert Escalation
→ 完成受控整改
→ 形成新的精确 Review Target
→ 启动全新独立 C04 Session 复审
```

C04 不得加入被审对象的整改设计 Session，也不得自行关闭自己提出的 Finding。Finding 只能由面向新精确 Review Target 的全新独立 C04 Session 复核关闭。

S2/S3 Finding 由 Primary Executor 在现有授权范围内整改，同样必须形成新的精确 Review Target 并启动全新独立 C04 Session 复审。Severity 只决定风险表达、优先顺序和默认路由；任一 Open Finding 都阻断 `PASS`。

## 41.3 C04 Provider 与独立性

`AUXILIARY / ADVISORY != FORMAL C04`。Primary、Expert 或其他执行 Session 调用一次 Codex、DeepSeek、Kimi、`codex exec` 或其他 Tool，只能产生辅助结论；正式 C04 的冻结 Review Target、精确 Git Commit / HEAD、角色独立性、Review Record 和结论要求见 `00_project/governance/modules/engineering/CURRENT_TRUTH_AUTHORITY_AND_REVIEW.md` 第 38.7 节。

C04 默认使用 `INDEPENDENT_REVIEWER_PRIMARY`，不可用时使用 `INDEPENDENT_REVIEWER_FALLBACK`，具体 Model/Runtime/Harness 只从 `CURRENT_STATE.md` 解析。每次切换和每次复审都必须新建独立 C04 Session；不得复用实现或整改 Session，也不得因 Reviewer Provider、Model、Runtime 或 Harness 替换而改变评审输入、标准或结论格式。

某 Expert 实质参与当前整改方案时，C04 优先使用另一 Reviewer Provider。另一 Provider 不可用时，可使用同 Provider 的全新独立 Session，但必须保持上下文完全隔离。

Reviewer Provider 只是 Reviewer Model/Runtime/Harness 的运行选择属性，不是新角色、新 Owner 或新 Current Truth 来源。

## 41.4 Model / Runtime / Harness 替换后的恢复

逻辑 C00 在 Provider、Model、Runtime 或 Harness 切换时保持连续。物理上下文按岗位交互与可执行治理政策第 8 节执行 `KNOWLEDGE_CONTINUATION_CHECK` 或 `BASELINE_RELEARN`，并记录前后运行身份、Git Anchor、Task、Authority、检查结果和证据。切换不增加 Role、Tool、Gate 或批准权，也不能满足正式 C04 独立性。

## 41.5 独立 Session 请求与自动创建

何时必须建立独立 Session 由 `00_project/governance/PROJECT_ASSURANCE_CADENCE_POLICY.md` 唯一定义。请求格式由本节唯一维护。

```yaml
NEW_INDEPENDENT_SESSION_REQUEST:
  schema_version: "1.3"
  request_id: "{{UNIQUE_REQUEST_ID}}"
  action: "CREATE_INDEPENDENT_SESSION"
  independent_session_required: true
  reason_code: "{{ALLOWED_INDEPENDENCE_REASON}}"
  trigger_rule_reference: "{{AUTHORITATIVE_RULE_REFERENCE}}"
  trigger_evidence: "{{FACT_OR_RECORD_PROVING_THE_TRIGGER}}"

  caller:
    session_id: "{{CURRENT_SESSION_ID}}"
    role: "{{CURRENT_ROLE}}"
    dynamic_role_profile: "{{PROFILE_ID}}"
    interaction_id: "{{INTERACTION_ID}}"

  governance_identity:
    target_role: "{{C01|C02|C03|C04|C05|C06|EXPERT|ADVISORY}}"
    formal_gate_authority: "{{C04_ONLY|NONE}}"
    execution_slot: "{{EXECUTION_SLOT}}"
    runtime: "{{RUNTIME_OR_HARNESS_NATIVE}}"
    provider_separation_required: false

  task:
    self_contained: true
    project_structure_ref: "{{PROJECT_STRUCTURE_MAP_REFERENCE}}"
    project_id: "{{PROJECT_ID}}"
    subproject_id: "{{ID_OR_NOT_APPLICABLE}}"
    module_id: "{{ID_OR_NOT_APPLICABLE}}"
    work_package_id: "{{WORK_PACKAGE_ID}}"
    work_package_type: "{{LEAF_EXECUTION|INTEGRATION|REVIEW_PACKAGE|EXPERT_ANALYSIS}}"
    output_contract_ref: "{{OUTPUT_CONTRACT_ID_OR_REVIEW_OUTPUT_CONTRACT}}"
    objective: "{{ONE_PRECISE_OBJECTIVE}}"
    exact_question: "{{QUESTION_TO_ANSWER}}"
    exact_git_target: "{{FULL_COMMIT_HASH_OR_NOT_APPLICABLE}}"
    applicable_baseline: "{{BASELINE_ID_OR_NOT_APPLICABLE}}"
    required_inputs:
      - "{{PATH_OR_CONTROLLED_REFERENCE}}"
    must_not_assume:
      - "{{EXCLUDED_CONTEXT_OR_UNAPPROVED_FACT}}"
    expected_output: "{{OUTPUT_CONTRACT}}"

  context_package:
    mode: "MINIMUM_SUFFICIENT_SELF_CONTAINED"
    package_complete: true
    include_full_chat_history: false
    include_private_reasoning: false
    handoff_or_review_record: "{{PATH_OR_NOT_APPLICABLE}}"

  permissions:
    filesystem: "{{READ_ONLY|SCOPED_WRITE}}"
    allowed_write_paths:
      - "{{PATH_OR_NONE}}"
    commit: false
    push: false
    pull_request: false
    release: false
    remote_mutation: false

  workspace_binding:
    access_mode: "{{READ_ONLY|SCOPED_WRITE}}"
    worktree_id: "{{WORKTREE_ID_OR_NOT_APPLICABLE}}"
    worktree_path: "{{LOCAL_PATH_OR_NOT_APPLICABLE}}"
    branch: "{{BRANCH_OR_DETACHED_TARGET_OR_NOT_APPLICABLE}}"
    base_commit: "{{FULL_COMMIT}}"
    write_scope: "{{PATHS_OR_NONE}}"
    write_lease_status: "{{ACTIVE|NOT_APPLICABLE}}"
    active_writer_session: "{{NEW_SESSION_ID_OR_NOT_APPLICABLE}}"

  enforcement:
    mode: "{{PROCEDURAL_FALLBACK|TOOL_ENFORCED}}"
    evidence: "{{CONTROL_EVIDENCE_REFERENCE}}"

  authorization:
    contract_refs:
      independent_session_creation: "{{INDEPENDENT_SESSION_CREATION_AUTHORIZATION_ID}}"
      formal_c04_dispatch: "{{FORMAL_C04_DISPATCH_AUTHORIZATION_ID_OR_NOT_APPLICABLE}}"
      real_model_invocation: "{{REAL_MODEL_INVOCATION_AUTHORIZATION_ID_OR_NOT_APPLICABLE}}"
    required_action_classes:
      independent_session_creation: "INDEPENDENT_SESSION_CREATION"
      formal_c04_dispatch: "{{FORMAL_C04_DISPATCH|NOT_APPLICABLE}}"
      real_model_invocation: "{{REAL_MODEL_INVOCATION|NOT_APPLICABLE}}"
    applicability_evidence:
      independent_session_creation: "{{ALWAYS_APPLICABLE_EVIDENCE}}"
      formal_c04_dispatch: "{{APPLICABILITY_OR_NOT_APPLICABLE_EVIDENCE}}"
      real_model_invocation: "{{APPLICABILITY_OR_NOT_APPLICABLE_EVIDENCE}}"
    authority_owner: "{{AUTHORITY_OWNER}}"
    action_scope_target: "{{ACTION_SCOPE_AND_EXACT_TARGET}}"
    allowed_side_effects: "{{ALLOWED_SIDE_EFFECTS}}"
    forbidden_side_effects: "{{FORBIDDEN_SIDE_EFFECTS}}"
    source_type: "{{PREAUTHORIZED_GATE|EXPLICIT_CONFIRMATION}}"
    source_reference: "{{GATE_OR_CONFIRMATION_RECORD}}"
    validity: "ONE_INDEPENDENT_SESSION"
    consumption_event: "SESSION_DISPATCHED"
    terminal_state: "{{EXECUTION_COMPLETED|RESULT_UNKNOWN_RECONCILIATION_REQUIRED}}"
    retry_policy: "NO_AUTOMATIC_RETRY"
    dispatch_limit: 1
    capability_enablement_is_authorization: false

  placement:
    target: "RESOLVE_FROM_CONFIG"
    default_target: "CURRENT_AI_ENVIRONMENT"
    project_binding: "CURRENT_PROJECT"
    external_profile: "RESOLVE_FROM_CONFIG_OR_NULL"

  return_route:
    destination_session_id: "{{CALLER_SESSION_ID}}"
    result_record: "{{PATH_OR_MESSAGE_CHANNEL}}"

  failure_policy:
    automatic_retry: false
    on_failure: "RETURN_TO_CALLER"
```

机械要求：

1. 请求必须通过 Schema、Reason Code、触发证据、自足输入、权限、Authorization Contract 和唯一 `request_id` 校验；Session 创建、正式 C04 Dispatch 与真实 Model 调用是独立 Action Class，必须分别有适用授权；
2. 默认在当前 AI/Harness 的当前项目自动创建；
3. 同一环境的新 Session 也必须拥有真正独立上下文，不继承实现/整改私有推理；
4. 只有 `EXTERNAL_AI_TRANSFER_CONFIG.yaml` 已由负责人手动启用并选择外部 Profile 时，才允许把独立 Session 建到外部 AI；
5. 本地创建失败不得自动 fallback 到外部；应输出 `LOCAL_INDEPENDENT_SESSION_CREATION_UNAVAILABLE` 和可复制的手动创建指令；
6. 子 Session 权限不得超过 Caller；一个 `request_id` 最多创建一次；失败或超时不得自动再次付费调用；
7. 正式 C04 还必须满足 Review Readiness，且 `formal_gate_authority` 只能由正式分配的 C04 使用。
8. `authorization.source_reference` 必须指向适用于本请求的预授权 Gate 或明确确认记录，`validity` 必须为 `ONE_INDEPENDENT_SESSION`，`dispatch_limit` 必须为 `1`；外部能力开关、Profile 启用或技术可调用性本身都不是调用授权。
9. 正式 C04 还必须记录 `00_project/governance/GOVERNANCE_EXECUTION_CONTRACTS.yaml` 定义的独立性证据：新 Session、排除的实现/整改 Session、上下文包、精确 Target、Target 只读、允许写入范围、Git/远程写入禁止和评审前后 Target 状态。
10. `INDEPENDENT_SESSION_CREATION` 对本请求始终适用；只创建独立 Session 而不发起正式 C04、也不触发真实 Model 调用时，后两项必须分别标记 `NOT_APPLICABLE` 并给出证据。
11. 当请求把任务作为正式 C04 发出时，`FORMAL_C04_DISPATCH` 适用；如果该 Operation 只完成 Dispatch、没有触发新的真实 Model 推理调用，则 `REAL_MODEL_INVOCATION` 可以标记 `NOT_APPLICABLE`，但必须给出证据。
12. 当一次 Operation 同时创建独立 Session、发起正式 C04 并触发真实 Model 调用时，三项 Action Class 必须同时出现，并分别引用各自的有效 Authorization Contract；任何一项不得隐含另一项。
13. `NOT_APPLICABLE` 不是授权 ID。Schema 校验必须拒绝以下请求：适用 Action Class 缺少独立合同、合同与 Action Class 不匹配，或 `NOT_APPLICABLE` 缺少适用性证据。
14. `BOUNDED_WORK_PACKAGE_EXECUTION` 必须绑定 `LEAF_EXECUTION / INTEGRATION`、唯一 Output Contract、独立 Worktree/Branch、精确 Base Commit、Write Scope 和单一 Write Lease；任一字段缺失、同一目录已有 Writer 或 Write Scope 冲突未关闭时拒绝 Dispatch。
15. C04 / Expert / Advisory 的只读任务将 Write Lease 标记为 `NOT_APPLICABLE` 并给出只读证据；不得为了满足字段而制造虚假 Worktree 或 Writer。

## 41.6 当前 Session 外部 AI 调用与独立 Session 的分离

必须区分：

```text
CURRENT_SESSION
-> EXTERNAL_AI_TOOL_CALL
-> AUXILIARY / ADVISORY RESULT
-> RETURN_TO_CURRENT_SESSION
```

和：

```text
INDEPENDENCE_TRIGGER
-> NEW_INDEPENDENT_SESSION_REQUEST
-> NEW LOCAL OR MANUALLY-CONFIGURED EXTERNAL SESSION
```

前者在配置和当前授权允许时可以静默调用，不创建新的治理 Session，由 Caller 提供上下文、保持任务 Owner、判断结果并继续工作；它不得产生正式 C04 Gate Decision。后者只用于权威规则明确要求独立性、且最小输入包已经自足的任务。

外部 AI 当前调用、确认、预算、重试、并发和放置值只由 `00_project/governance/EXTERNAL_AI_TRANSFER_CONFIG.yaml` 维护。本文件只维护交互语义和请求格式。

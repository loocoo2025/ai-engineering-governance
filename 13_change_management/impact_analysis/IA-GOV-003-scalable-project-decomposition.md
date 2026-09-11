# IA-GOV-003：CR-GOV-003 影响分析

关联 Change：`CR-GOV-003`

当前版本：`v0.1.6`

目标身份：`v0.1.7`

变更分类：`SUBSTANTIVE / GOVERNANCE_CHANGE`

## 1. 影响矩阵

| 范围 | 影响 | 说明 |
|---|---|---|
| 产品目标、行为与 Current Truth | NO | 只增加通用分解和执行治理能力 |
| C00～C06 固定职责 | NO | 仅增加各岗位在分解、局部执行和集成中的既有职责投影 |
| 项目结构与父子事实边界 | YES | 新增唯一稳定 Authority 和当前结构 Map |
| Task / Work Package | YES | 增加递归类型、Output Contract、Session/Worktree/Write Lease 绑定 |
| Session / Handoff | YES | 新 Output 使用新隔离 Worker Session；Handoff 限当前未完成叶子包 |
| Git / Worktree | YES | 并行 Writer 必须使用独立 Worktree；同一目录单 Writer |
| C04 Decision / Severity | NO | 保留 Readiness、S0～S3 和 PASS / CHANGES_REQUESTED |
| C04 Scope / Evidence | YES | 增加子级证据依赖和父级组合式 Review Target |
| Baseline | YES | 联邦 Baseline 可以精确固定 Child 版本组合 |
| Testing Governance | YES | 子级验证与系统集成验证分层，不重复无来源测试 |
| Authorization / Side Effect | NO | Worktree、Commit、Merge、Push 和 Release 仍分别授权 |
| Existing Single Project | COMPATIBLE | 默认解释为 SINGLE_PROJECT，不追溯重写历史 |

## 2. One Fact, One Owner

- 稳定分解、父子边界和组合评审语义：`PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`；
- 当前结构关系：`PROJECT_STRUCTURE_MAP.md`；
- Task、Output Contract 和 Write Lease 当前状态：`ACTIVE_TASKS.md`；
- Session、Worktree 和 Handoff：`AI_CONVERSATION_ORCHESTRATION_RULES.md`；
- 当前 Baseline 版本组合：`BASELINE_INDEX.md`；
- 机器字段：`GOVERNANCE_EXECUTION_CONTRACTS.yaml`；
- C04 触发和 Decision：现有 Assurance / Review Authority；
- 测试范围：`AI_TESTING_GOVERNANCE_RULES.md`。

## 3. 兼容性与升级

- 既有项目默认 `SINGLE_PROJECT`，现有任务和审批不失效；
- 以后新增或重新分解的 Work Package 才补齐新增字段；
- 既有进行中任务可完成后再迁移，不要求中途重写 Session 历史；
- 并行写入无法建立独立 Worktree 时必须降为串行单 Writer，不能模拟隔离；
- 正式拆分为 Governed Subproject 时必须建立结构 Map、Parent–Child Contract、回滚 Anchor 和 Baseline Relearn；
- 工具未兼容新合同字段时使用 `PROCEDURAL_FALLBACK`，不得声称已经机械执行 Write Lease。

## 4. 验证范围

直接验证：Markdown、YAML Schema、Owner 引用、文件索引、Work Package/Session/Worktree 字段一致性、C04 分层语义、链接、whitespace 和敏感信息扫描。

不执行：产品 Build/Test、真实 Worktree 并行、外部项目迁移、正式 C04、Commit、Tag、Push 或 Release。

## 5. Remaining Risks

- Worktree 解决物理隔离，不自动解决共享接口和语义冲突；
- `PROCEDURAL_FALLBACK` 下 Write Lease 依赖执行者正确登记和转移；
- 过细拆分会增加合同与集成成本，必须以可独立输出和验证为边界；
- 父级若只看摘要而不核验精确 Child Anchor，可能接受过期证据；
- 多治理版本联邦需要显式合同兼容性判断。

## 6. 结论

```text
IMPACT_SCOPE: PROJECT_DECOMPOSITION_SESSION_WORKTREE_AND_COMPOSITIONAL_REVIEW
REAPPROVAL_SCOPE: V0.1.7_CANDIDATE
REGRESSION_SCOPE: GOVERNANCE_CONTRACT_OWNER_LINK_AND_INDEX_CONSISTENCY
UNAFFECTED_APPROVALS_PRESERVED: YES
REMAINING_UNKNOWN: PROJECT_SPECIFIC_DECOMPOSITION_AND_PARALLELISM_LIMITS
NEXT_ACTION: EXACT_RELEASE_CANDIDATE_COMMIT_THEN_FORMAL_C04_AND_RELEASE_GATE
```

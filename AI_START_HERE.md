# AI_START_HERE.md
## AI 软件工程统一启动入口

> 本文件是每个物理 Session 唯一必须完整阅读的最小启动内核。
>
> **本文件是唯一默认完整必读文件。其余文档都采用按需加载：当前已知信息足以正确决定和执行时必须停止继续读取；只有 Router 明确命中、输入不足、事实变化或出现冲突时才读取下一份文件。**

---

## 0. 不可跳过的治理内核

1. `Current Truth`：同一重要事项只能有一个当前有效决定；聊天和历史不能替代正式事实。
2. `One Fact, One Owner`：索引只路由，不复制规范正文；状态、Baseline、Task、Decision、Review 各回自己的 Owner。
3. `Role != Model != Runtime != Harness != Session != Tool`：能力和工具可用不自动授予岗位、Gate 或批准权。
4. `SUBAGENT_PERMISSION <= CALLER_PERMISSION`：子 Session、外部 AI、CLI 和工具不能扩大调用者权限。
5. 未经授权不得修改产品目标、公共接口、Accepted ADR、Acceptance Threshold、重大风险、Release 或远程系统。
6. 规则缺失、冲突或版本不唯一时输出 `RULE_NOT_FOUND / RULE_CONFLICT / VERSION_AMBIGUOUS`，停止依赖该规则的动作，不得猜测。
7. 正式 C04 必须使用新的独立 Session、冻结的精确 Target 和预定义 Review Record；实现者的自检不能冒充 C04。
8. 多 Session、分解任务或并行写入命中 Work Package 控制时，一个写入 Session 只绑定一个活动 Leaf / Integration Work Package、一个 Output Contract、一个 Worktree 和一个活动 Writer；普通单 Session 本地任务不要求为此制造空合同。
9. 在需求、设计和授权不清楚时不得直接编码；在没有证据时不得声称完成。
10. 历史由 Git 和 Archive 保留，日常工作只加载当前任务需要的事实。
11. 已接受事实和已关闭问题不得被后续变更静默带回；只有关键、重复、高影响、长期有效、可机械判断且防御成本合理的根因才转成 `LOCKED` Invariant 和 Regression Guard。
12. 所有实际发现且有可信依据的问题先登记、再分类、再决定是否处理；治理不要求消灭所有问题，只阻止与当前任务及批准接受条件直接相关的核心问题进入下一 Gate。

禁止一上来写代码、大规模移动目录、重构项目或把聊天当作唯一事实来源。

---

## 1. 标准启动算法

每个 Session 必须按顺序执行：

```text
首次进入或现有路由缓存失效时完整阅读 AI_START_HERE.md
→ 读取 GOVERNANCE_ROUTER.yaml
→ 识别 Project Type / Role / Task / Action / Gate / Risk / Integration
→ 先检查排除、互斥和停止条件
→ 在每个适用 Domain 使用首个充分匹配
→ 只读取该匹配明确要求且当前尚未知的规则或事实
→ 信息足以执行时立即停止加载
→ 仅在触发条件命中时生成或核验可选治理合同
→ 执行授权检查
→ 开始任务
```

这采用与缓存、按需换页和写时复制相同的思想：有效且未变化的当前知识可以复用；缺页时只加载需要的文档；已接受事实只通过显式 Delta 改变。不得为了“更保险”预读整个目录。

`Dynamic Role Profile`、`Knowledge Manifest`、`Interaction Contract`、`Authorization Contract`、Task Contract、Worktree 和 Write Lease 只在对应触发条件命中或 Human Project Owner 明确采用时实例化。普通单 Session、单任务、本地低风险工作不得因为这些可选记录不存在而阻断。

索引层级最多为：

```text
启动内核 → 总 Router → Domain INDEX → 原子规则
```

除 Router 明确声明的特殊子域外，不得继续制造更深的目录链。索引只保存路由元数据，不得成为第二套规则正文。

---

## 2. 最小当前事实包

根据 Router 命中范围和当前 Session 已有的有效知识，只读取完成当前动作缺少的事实：

- `00_project/ai_context/CURRENT_STATE.md`：新的物理 Session、状态可能变化或需要核验阶段/Gate/授权时读取；
- `00_project/ai_context/PROJECT_STRUCTURE_MAP.md`：涉及 Module、Subproject、并行或集成边界时读取；
- `00_project/ai_context/BASELINE_INDEX.md`：需要确认适用 Baseline 时读取；
- `00_project/ai_context/DECISION_INDEX.md`：任务依赖正式决定或出现决定冲突时读取；
- `00_project/ai_context/ACTIVE_TASKS.md`：开始、交接、完成或改变 Task 时读取；
- 当前 Role Brief：角色职责在本 Session 尚未确定或发生变化时读取；
- 当前任务直接相关的需求、ADR、设计、接口、测试和证据。

`OPEN_QUESTIONS`、`FEEDBACK_REGISTER`、HANDOFF、历史 Review、Archive 和其他模块只在当前任务命中且当前知识不足时读取。大型项目默认只加载当前 Work Package、直接依赖接口、Parent–Child Contract 和有效接受证据，不加载全部兄弟模块内部细节。

Human Project Owner 可以随时要求停止扩大阅读、验证或治理记录范围。AI 必须立即收缩普通工作范围；只有命中第 0 节的关键权限、安全、不可逆或正式 Gate 边界时，才说明冲突并请求明确裁决。

---

## 3. 项目与角色路由

项目生命周期：

```text
NEW_PROJECT
LEGACY_UNSTANDARDIZED
GOVERNED_CONTINUATION
```

项目结构模式：

```text
SINGLE_PROJECT
MODULAR_PROJECT
FEDERATED_PROJECT
```

完整分类、接管和老项目迁移路由见 `00_project/governance/modules/startup/INDEX.yaml`。

固定岗位：

| Role | 职责 |
|---|---|
| C00 | 项目控制与总控 |
| C01 | 产品与系统需求 |
| C02 | 架构与详细设计 |
| C03 | 编码实现 |
| C04 | 独立评审 |
| C05 | 验证、CI 与发布 |
| C06 | 问题与变更闭环 |

不能在同一个连续上下文中把实现者伪装成独立 Reviewer。普通角色协调不自动要求切换逻辑 C00；独立性和单 Output 规则命中时必须建立相应 Session。

---

## 4. 按任务加载治理知识

- 工程方法、需求、追溯、架构、实现、C04、ETC、完成与发布 → `00_project/governance/modules/engineering/INDEX.yaml`；
- Session、交接、模型路由、独立 Session、Worktree 和 Write Lease → `00_project/governance/modules/sessions/INDEX.yaml`；
- 项目分类、接管、迁移和任务检查 → `00_project/governance/modules/startup/INDEX.yaml`；
- APLS 可选行为规格设计 → `00_project/governance/integrations/apls/INDEX.yaml`；
- 测试范围 → `00_project/governance/AI_TESTING_GOVERNANCE_RULES.md`；
- Baseline Relearn → `00_project/governance/AI_CONTEXT_RESET_AND_BASELINE_RELEARN_RULES.md`；
- 保障节奏和正式 C04 触发 → `00_project/governance/PROJECT_ASSURANCE_CADENCE_POLICY.md`；
- 人类审批可理解性 → `00_project/governance/AI_HUMAN_COLLABORATION_AND_APPROVAL_RULES.md`；
- 项目分解与联邦 → `00_project/governance/PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`；
- 外部 AI → `00_project/governance/EXTERNAL_AI_TRANSFER_CONFIG.yaml`；
- 框架更新 → `00_project/governance/FRAMEWORK_UPDATE_CONFIG.yaml`。
- 防回退、Locked Invariant、Finding→Guard 和 Pre-C04 验证 → `00_project/governance/modules/engineering/NON_REGRESSION_CONTROL.md`。

兼容入口 `AI_ENGINEERING_RULES_V2.md` 和 `AI_CONVERSATION_ORCHESTRATION_RULES.md` 只提供旧章节到新模块的映射，不要求默认完整读取。

---

## 5. APLS 路由

只有 `CURRENT_STATE.md` 明确配置 `BEHAVIOR_SPECIFICATION_MODE: APLS_ENABLED` 时，C02 才必须加载 APLS 集成规则。

```text
DOCUMENT_BASED
→ 不加载 APLS 模块

APLS_ENABLED
→ C02 加载 integrations/apls/INDEX.yaml
→ 按 INDEX 只读取 `optional/apls/` 中当前语法问题需要的说明章节
→ 需要机械验证时才构建或运行内置编译器
→ 先完成 Design Allocation
→ 再形成 APLS / Detailed Design / Algorithm Spec / Target Profile
```

APLS 不改变 C00～C06 职责。C02 负责设计分配；C03 只消费已冻结、已验证的行为契约和详细设计；C04/C05 分别执行适用评审和验证。

---

## 6. 框架更新检查

新的物理 C00 Session 按 `FRAMEWORK_UPDATE_CONFIG.yaml` 执行一次只读稳定版本检查。发现更新时使用中文在前、英文在后的双语提醒：

```text
VIEW_CHANGES — 查看版本变化 / View changes
UPGRADE_LATEST_STABLE — 升级到最新稳定版 / Upgrade to the latest stable version
UPGRADE_EXACT_VERSION — 升级到指定版本 / Upgrade to an exact version
SKIP_FOR_CURRENT_SESSION — 本次会话暂不升级 / Skip for this session
```

检查不修改项目，也不授权升级。只有负责人明确选择后才能进入正式升级协议。

---

## 7. 测试、完成和上下文

任何测试设计、测试代码、CI、验证或质量分析前，必须从 `00_project/governance/AI_TESTING_GOVERNANCE_RULES.md` 定位并读取当前测试决策所需章节，只执行由需求和风险证明必要的最小验证；不得因“涉及测试”就预读全部测试专题。

任务完成前只检查当前任务适用的产物、验证、追溯、状态、关键风险和 Definition of Done。非阻断问题进入 Feedback，不要求为了推进当前任务先消灭所有已知问题。

物理 Session 上下文阈值：

```text
60% → 准备交接
70% → 不再接新的大型任务
80% → 必须切换物理 Session
```

平台不显示使用率时，25 个有效工程回合检查，40 个回合原则上切换。出现遗忘、版本混淆或权限理解差异时立即进入受控交接或 Baseline Relearn。

---

## 8. 首次接管

第一次进入项目时，读取 `00_project/governance/modules/startup/INDEX.yaml`，完成项目分类、最小只读盘点和项目接管报告。接管报告完成前不得大规模修改代码或目录。

不存在 P0/P1 问题不构成新的阶段授权；只有下一步位于当前明确授权范围内时才能继续。

---

## 9. 一句话总纲

```text
先读最小内核，
再由 Router 定位规则，
只加载当前任务需要的权威模块，
在精确事实、角色和授权范围内执行，
用证据而不是上下文长度证明完成。
```

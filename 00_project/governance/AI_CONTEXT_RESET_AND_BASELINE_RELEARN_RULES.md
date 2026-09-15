# AI_CONTEXT_RESET_AND_BASELINE_RELEARN_RULES.md
## AI 上下文重置、知识压缩与基线再学习规则

> **用途**
>
> 本文件用于解决长期 AI 软件开发中最常见的问题之一：
>
> - 对话越来越长；
> - 旧需求和新需求混在一起；
> - 旧架构和新架构互相污染；
> - 多次 HANDOFF 后信息逐渐失真；
> - AI 记住了历史过程，却忘了当前有效事实；
> - AI 把已经废弃的方案重新当成当前方案。
>
> **核心原则：**
>
> > Git 保留完整历史，AI 不默认背负完整历史。
>
> > 历史必须可追溯，但 AI 默认只学习当前任务实际需要的“当前批准基线”部分。
>
> 本文件按 `GOVERNANCE_ROUTER.yaml#domains.baseline_relearn.section_selection` 选择章节；当前任务已经能够安全继续时停止读取，不要求每次 Baseline Relearn 全文学习本文件。
>
> > 需要解释历史时，再按需读取 Git、ADR、Archive 和历史评审记录。

---

# 0. 最重要的基本原则

AI 必须区分：

```text
项目历史 != AI 当前上下文
```

项目历史应该尽量完整保留。

AI 当前上下文应该尽量：

- 小；
- 准确；
- 当前有效；
- 无冲突；
- 可验证；
- 可重新加载。

禁止通过删除 Git 历史来解决 AI 上下文混乱问题。

---

# 1. Git 的职责

Git 是项目的历史档案馆。

Git 应用于：

- 保存历史版本；
- 回退；
- 比较；
- 定位 Bug 引入点；
- 查看某设计以前如何实现；
- 追踪某次发布对应的代码；
- 审计变更。

默认禁止为了“让 AI 少看点东西”而：

- 删除 Git 历史；
- 重写主分支历史；
- 删除重要 Tag；
- 清空历史 Commit；
- 把项目压成只剩最后一个 Commit。

**减少 AI 上下文，不等于删除工程历史。**

---

# 2. AI 默认读取什么

新 AI 或新对话必须首先完整阅读 `AI_START_HERE.md`，再严格遵循它维护的权威启动顺序。本文件不维护另一份竞争性的默认读取清单。

Baseline Relearn 也必须遵守按需原则：只重新加载受影响的治理 Delta、当前任务、直接依赖以及继续工作所缺少的 Current Truth / Baseline 引用。当前信息足以执行时停止读取，不要求先学习全部需求、架构、设计、代码、测试或 Open 问题；默认不扩展到旧聊天、历史 HANDOFF 链、Archive 或 `SUPERSEDED` 内容。

默认不读取：

- 全部 Git 历史；
- 所有旧聊天；
- 所有旧 HANDOFF；
- 所有历史 PRD；
- 所有历史架构版本；
- 所有已经关闭的 Bug；
- 所有旧测试方案；
- 所有 SUPERSEDED ADR；
- 所有 Archive 内容。

只有当前任务确实需要历史解释时，才按需读取。

---

# 3. 文档状态必须明确

推荐状态：

```text
DRAFT        正在编辑，尚未批准
CURRENT      当前有效版本
APPROVED     已经批准，可作为正式依据
ACCEPTED     通常用于 ADR，表示当前正式采用
SUPERSEDED   已经被新版本正式替代
DEPRECATED   正在退出，不应新使用
ARCHIVED     历史档案，默认不进入 AI 当前上下文
REFERENCE    仅供参考，不属于当前规范依据
REJECTED     已经明确否决
UNKNOWN      当前无法确认
INFERRED     从旧资料推断，但尚未正式确认
```

AI 不得把 `SUPERSEDED / ARCHIVED / REFERENCE / REJECTED` 自动当成当前设计依据。

---

# 4. 当前目录里原则上只保留当前有效版本

错误示例：

```text
03_architecture/
├── system_architecture_v1.md
├── system_architecture_v2.md
├── system_architecture_v3.md
├── system_architecture_final.md
└── system_architecture_final2.md
```

推荐：

```text
03_architecture/
└── system_architecture.md
```

当前目录中的文件表示当前有效版本。

旧版本原则上通过 Git 历史追溯。

如果确实需要独立保存历史文档，则归档到 `00_project/archive/`。

---

# 5. 推荐新增 Archive 结构

```text
00_project/
└── archive/
    ├── requirements/
    ├── architecture/
    ├── design/
    ├── reviews/
    ├── testing/
    ├── issues/
    ├── handoffs/
    └── baselines/
```

Archive 只保存仍有参考价值、但不应该默认进入 AI 当前上下文的历史资料。

注意：

- 源代码历史主要由 Git 保存；
- Archive 不是 Git 的替代品；
- 不要复制整个仓库到 Archive。

---

# 6. 两种上下文重置

项目必须区分：

```text
A. 小重置：Context Handoff
B. 大重置：Baseline Relearn
```

---

# 7. A 类：Context Handoff（小重置）

适用于：

- 当前角色工作仍连续；
- 当前任务还没结束；
- 只是对话上下文过长；
- 仍需要上一代对话中的近期工作状态。

例如：

```text
C03-v04
↓
C03-v05
```

执行：

```text
旧对话
↓
重要决策落盘
↓
更新 CURRENT_STATE
↓
更新 ACTIVE_TASKS
↓
更新 OPEN_QUESTIONS
↓
生成最新 HANDOFF
↓
记录 Git Commit / 分支 / 未提交修改 / 测试
↓
旧对话 READ ONLY
↓
新对话读取最新 HANDOFF
↓
继续当前任务
```

小重置只读取最新一个 HANDOFF，默认不读取更早的 HANDOFF 链。

## 7.1 分层任务的 Task-local Handoff

当项目存在多级 Work Package 时，Context Handoff 只携带当前未完成的 `LEAF_EXECUTION / INTEGRATION` Work Package 所需上下文：

- 当前任务边界、Output Contract 和写入范围；
- 直接依赖的精确接口、决定、Baseline Anchor 和验证要求；
- 当前 Worktree、Branch、未提交修改、测试状态和剩余步骤；
- Write Lease 转移记录。

默认排除已完成兄弟任务的实现细节、全部子项目历史、无关模块代码和旧 Session 私有推理。旧 Session 完成交接后冻结写入，Write Lease 只能一次转移给一个后继 Session；任务未完成不等于允许两个 Session 同时写入同一 Worktree。

---

# 8. B 类：Baseline Relearn（大重置）

Baseline Relearn 是：

> 丢弃不再可信的上下文缓存，从当前正式事实按需重建能够完成当前任务的最小知识工作集。

适用于：

- 正式发布完成；
- 重大里程碑完成；
- 大型重构结束；
- 重大架构版本切换；
- 开发阶段发生重大转换；
- 已经连续发生 3～5 次 HANDOFF；
- AI 开始频繁混淆新旧状态；
- AI 重复引用废弃方案；
- AI 无法准确说出当前基线；
- AI 对历史摘要产生明显“传话漂移”；
- 项目负责人明确要求“重新学习当前项目”。

大重置后，新 AI 默认不继承旧聊天，不依赖历史 HANDOFF 链。

## 8.1 Knowledge Continuation 不是 Baseline Relearn

Provider、Model、Runtime 或 Harness 切换时，逻辑 C00 可以保持连续。只有 Role、Task、Scope、Authority、Baseline、Gate 和上下文完整性均兼容时，才允许按 `ROLE_INTERACTION_EXECUTION_POLICY.md` 执行较小的 `KNOWLEDGE_CONTINUATION_CHECK`。

Knowledge Continuation 只确认当前岗位和任务能够安全续接，不清理或重建完整 Baseline。条件不满足、上下文连续性无法证明或出现事实混淆时，必须执行本文件定义的 Baseline Relearn。正式 C04 始终创建新的独立 Session，不适用 Knowledge Continuation 例外。

---

# 9. 大重置前的按需知识压缩

C00 只压缩本次 Relearn 原因、当前任务和受影响事实。下列内容仅在本次任务或变化实际涉及时确认，不得作为默认全量清单：

```text
1. 当前产品需求是什么？
2. 当前系统需求是什么？
3. 当前 ACCEPTED ADR 是什么？
4. 当前有效架构是什么？
5. 当前有效详细设计是什么？
6. 当前接口和协议是什么？
7. 当前代码 Commit 是什么？
8. 当前测试基线是什么？
9. 当前已知 Bug 是什么？
10. 当前未决问题是什么？
11. 当前技术债是什么？
12. 当前下一步是什么？
```

目标：一个完全没有参加过旧聊天的新 AI，可以从最小入口开始工作，并在遇到具体缺口或冲突时定位到正确 Owner 继续学习。

---

# 10. 大重置前必须清理“当前”和“历史”的边界

## 需求
当前目录只保留当前有效需求。旧需求标记 `SUPERSEDED / ARCHIVED`。

## ADR
当前工作只默认读取 `ACCEPTED` ADR。`SUPERSEDED / REJECTED` 保留历史，但不作为当前依据。

## 架构
必须存在一个明确 `CURRENT` 版本。

## 详细设计
必须与当前代码基线一致。

## 测试
必须明确哪些测试是当前强制、当前可选、已废弃、历史测试。

## Bug
已经关闭的 Bug 不默认进入新 AI 当前上下文，但回归测试继续保留。

---

# 11. 大重置只核实受影响 Owner

只检查和更新本次 Relearn 原因、当前任务或治理 Delta 实际命中的 Owner：

```text
00_project/ai_context/CURRENT_STATE.md
00_project/ai_context/BASELINE_INDEX.md
00_project/ai_context/DECISION_INDEX.md
00_project/ai_context/OPEN_QUESTIONS.md
00_project/ai_context/ACTIVE_TASKS.md
00_project/ai_context/CONVERSATION_MAP.md
00_project/ai_context/PROJECT_STRUCTURE_MAP.md
02_system_requirements/requirements_traceability.md
```

对应内容实际变化或冲突时才更新：

```text
01_product_requirements/
02_system_requirements/
03_architecture/
04_design/
06_test_design/
13_change_management/baselines/
```

---

# 12. Baseline Snapshot

只有 Baseline 身份/组成实际改变、里程碑要求或负责人明确要求时才建立新的正式基线记录。单纯清理上下文缓存不得制造新 Baseline，例如：

```text
13_change_management/baselines/BASELINE-2026-08-v1.2.md
```

至少记录：

```text
基线名称：
产品版本：
Git Commit：
日期：
当前 PRD：
当前 SRS：
当前 ACCEPTED ADR：
当前架构：
当前详细设计：
当前测试计划：
当前已知 Bug：
当前未决问题：
当前发布 / 部署状态：
```

如使用 Git，可同时创建 Tag，例如：

```text
baseline/v1.2
release/v1.2.0
milestone/M3
```

---

# 13. 大重置后新 AI 的读取入口

首先完整阅读 `AI_START_HERE.md`，再严格遵循它维护的最小知识加载与按需检索流程。本文件只补充 Baseline Relearn 的校验行为，不复制启动顺序。

在该流程内，只核实受影响治理 Delta、当前任务、权限、适用 Gate 和直接依赖事实。Dynamic Role Profile 与 Knowledge Manifest 仅在其触发条件命中或负责人已采用时生成或核验。需求、ADR、架构、设计、代码、测试、Open Questions 和其他事实只有当前任务实际依赖时才读取。C04 仍使用精确 Review Target，不继承实现 HANDOFF 或私有推理。

默认不读取旧聊天、旧 HANDOFF 链和 Archive。

## 13.1 分层项目的最小重学习范围

- Child / Leaf Worker 默认只学习自身当前 Baseline、Parent–Child Contract、直接接口、适用要求、任务和验证边界；
- Parent / Integration Session 默认学习 System Integration Manifest、Child Acceptance Package、接口合同和系统级 Current Truth，不加载全部 Child 内部实现上下文；
- 只有证据不一致、集成失败、系统 Finding、安全/合规/数据完整性风险或明确审核要求，才对精确 Child Target 定向下钻；
- Parent 和 Child 各自在自己的治理边界执行 Baseline Relearn；不得用一个无限上下文 Session 代替分层事实与证据。

稳定分解和组合式评审规则见 `PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`。

---

# 14. 大重置后的上下文校验

新 AI 完成最小加载后只输出本次实际需要的字段；未加载的领域明确列入排除范围，不得为了填表继续读取：

```text
BASELINE-RELEARN-CHECK

当前项目：
当前阶段：
当前 Git Commit：
当前正在进行的任务：
本次 Relearn 原因 / 受影响 Delta：
实际加载的事实与规则：
明确未加载的领域：
当前权限与适用 Gate：
当前发现的冲突：
我认为当前下一步是：
```

如果理解错误，先修正正式文件或 AI 理解，再开始工作。

---

# 15. 什么时候必须触发大重置

满足以下任一条件，C00 必须评估 Baseline Relearn：

1. 正式版本发布；
2. 重大里程碑关闭；
3. 重大架构重构完成；
4. 连续 3 次 HANDOFF；
5. 连续 5 次 HANDOFF 时原则上必须执行；
6. AI 两次以上引用已废弃需求；
7. AI 两次以上混淆旧 ADR 与当前 ADR；
8. AI 无法准确复述当前基线；
9. AI 开始依赖“之前聊天里说过”而不是正式文件；
10. 项目阶段发生重大转换；
11. Provider / Model / Runtime / Harness 更换且不满足 `KNOWLEDGE_CONTINUATION_CHECK` 条件，或 Human Project Owner 发生更换；
12. 项目负责人要求清空历史上下文。

---

# 16. 定期维护频率

## 每个正常任务结束
更新必要的 CURRENT_STATE、ACTIVE_TASKS、追溯、Bug / ADR / CR。

## 每个里程碑
检查 BASELINE_INDEX、DECISION_INDEX、文档状态和 Archive。

## 每个正式发布
只评估当前 Session 的知识缓存是否仍适用。发布本身不自动触发全量 Relearn；发布改变了当前任务、Baseline 或适用治理语义时，只重学受影响 Delta。

## 长期没有发布
至少每累计 3～5 次 HANDOFF 做一次大重置。

---

# 17. 不要让 HANDOFF 形成“传话链”

错误：

```text
AI A → 总结给 B → B 再总结给 C → C 再总结给 D
```

正确：

```text
A → B
使用 HANDOFF 保持短期连续性
↓
达到一定次数后
↓
停止继续传递摘要
↓
重新核实 CURRENT_STATE + BASELINE
↓
新 AI 从当前源文件学习
```

HANDOFF 用于短期连续工作，不用于无限代际记忆。

---

# 18. 什么历史应该按需读取

只有当前问题确实需要时才读取历史。

例如：

- “为什么当初选择 TCP？” → 相关 ADR、历史架构评审、必要 Git Commit。
- “这个 Bug 什么时候引入？” → Git history、git bisect、历史 Bug。
- “接口为什么保留兼容字段？” → ADR、旧接口规范、CR、发布记录。
- “需求以前是不是改过？” → Git diff、CR、历史需求基线。

不要把所有历史永久加载进当前上下文。

---

# 19. 历史回溯结束后必须回到当前基线

AI 查完历史后必须明确：

```text
历史事实：
当前有效事实：
历史是否改变当前基线：YES / NO
```

如果 NO，历史信息不得继续影响当前实现。

如果 YES，必须走正式需求 / ADR / CR / 基线变更流程。

---

# 20. 旧文档归档规则

示例：

```text
00_project/archive/architecture/
2026-05-10_system_architecture_SUPERSEDED.md
```

文件顶部写：

```text
状态：SUPERSEDED
替代它的当前文件：03_architecture/system_architecture.md
禁止作为当前设计依据。
```

不要只放进 `old/ backup/ temp/` 而不说明状态。

---

# 21. 禁止自动删除历史资料

AI 发现旧文件时不得直接删除，必须分类：

```text
仍当前有效 → CURRENT
已被替代 → SUPERSEDED / Archive
仅参考 → REFERENCE / Archive
无法确认 → UNKNOWN
确认无价值且允许删除 → 提出删除建议
```

真正删除历史资料前，必须确保 Git 中有记录、已有备份，或项目负责人批准。

---

# 22. 当前代码是否需要“清理历史”

源码目录应该呈现当前代码，历史代码由 Git 保存。

禁止长期保留：

```text
foo_old.cpp
foo_backup.cpp
foo_v2.cpp
foo_final.cpp
foo_final2.cpp
```

如果只是历史版本，应由 Git 保存，不应留在当前工作树污染 AI。

---

# 23. 当前文档比旧聊天更重要

如果：

```text
旧聊天说 A
当前 APPROVED 文档说 B
```

默认当前 APPROVED 文档优先。

如果怀疑当前文档错误，先建立冲突记录，再回溯历史证据。

不得仅凭 AI “记得以前是 A”就恢复旧方案。

---

# 24. C00 的责任

C00 是本规则的主要执行角色，必须：

- 监控上下文健康；
- 监控 HANDOFF 次数；
- 检查当前基线是否清晰；
- 组织大重置；
- 组织知识压缩；
- 维护 Archive 边界；
- 判断运行身份切换应使用 Knowledge Continuation Check 还是 Baseline Relearn；
- 维护逻辑 C00 连续性，同时防止物理上下文未经校验继承权威；
- 确保新 AI 不默认加载历史垃圾；
- 确保 Baseline Relearn 后项目仍可追溯。

---

# 25. C04 的责任

重要 Baseline Relearn 后，可以让 C04 做轻量独立检查：

- 当前需求有没有混入旧需求；
- ACCEPTED ADR 是否唯一明确；
- 当前架构是否与代码大体一致；
- BASELINE_INDEX 是否正确；
- 是否存在多个互相冲突的“当前版本”；
- 是否有历史文件仍可能误导 AI。

---

# 26. C03 的责任

C03 编码时默认只使用当前基线。

除非任务明确要求，不主动遍历历史 Git。

遇到“为什么以前这么写”，先检查当前 ADR / 设计；仍无法解释时，再按需回溯历史。

---

# 27. Clean Context Reset 标准操作

```text
1. 停止接受新的大型任务
2. 记录 Relearn 原因、当前未完成任务和直接依赖
3. 记录 Git Commit / 分支 / Worktree / 未提交内容，不改变或丢弃它们
4. 通过 Router 确认本次受影响的治理规则与事实 Owner
5. 只更新实际变化或冲突的 Owner；未变化领域不读取、不改写
6. 只有 Baseline 身份或组成实际改变时才更新 Baseline / Snapshot
7. 旧 Session 停止写入；需要交接时只交接当前未完成任务
8. 新 Session 完整读取最小 `AI_START_HERE.md`，再按需加载缺少内容
9. 只在触发时生成或核验 Dynamic Role Profile、Knowledge Manifest 等可选控制
10. 输出 BASELINE-RELEARN-CHECK；足以安全继续当前任务后停止学习并开始执行
```

---

# 28. 给旧 AI 的“大重置”指令

```text
现在执行一次 Baseline Relearn / Clean Context Reset。

目标不是继续传递旧聊天摘要，而是让下一代 AI 从当前正式项目事实重新学习。

请停止新的大型工作，并严格执行：
1. 记录本次 Relearn 原因、当前任务和受影响治理/事实 Delta；
2. 只读取继续当前任务所缺少的正式规则和事实；
3. 当前信息足以执行时立即停止读取；
4. 按事实所有权只更新真正发生变化的权威文件；
5. 发现缺口或冲突时先登记，再定向读取正确 Owner，不得猜测；
6. 不要默认读取旧聊天、历史 HANDOFF、Archive 或无关模块；
7. 不要删除 Git 历史，也不要为了 Relearn 自动建立新 Baseline；
8. 输出实际加载、明确排除、未解决冲突和下一步。

最后只输出：本次原因、当前任务、实际加载、明确排除、实际更新、未解决冲突、权限/Gate 和下一步；不得为了填充报告再读取其他领域。
```

---

# 29. 给新 AI 的“重新学习”指令

```text
这是一次 Baseline Relearn 后的新干净对话。

不要读取或依赖旧聊天。
请只从当前项目正式文件按需重新学习。

首先完整阅读 `AI_START_HERE.md`，按其最小知识加载与按需检索流程读取；本规则第 13 节只补充 Baseline Relearn 校验范围。
默认不要读取旧聊天、历史 HANDOFF 链、Archive、SUPERSEDED ADR、旧 PRD、旧架构。

从当前任务和受影响 Delta 开始；当前知识足以执行时停止读取。运行中遇到新缺口或冲突时先登记，再读取对应 Owner 并调整。完成最小加载后输出 BASELINE-RELEARN-CHECK，然后继续工作。
```

---

# 30. 最重要的十条机械规则

1. Git 保留历史，AI 不默认读取全部历史。
2. 当前目录只保留当前有效事实。
3. 历史文档必须标记 SUPERSEDED / ARCHIVED / REFERENCE。
4. 小重置用最新 HANDOFF。
5. 大重置不继承旧聊天和 HANDOFF 链。
6. 连续 3 次 HANDOFF 开始考虑大重置，5 次原则上必须大重置。
7. 正式发布只触发 Relearn 适用性评估，不触发默认全量读取。
8. 只更新本次变化命中的事实 Owner；未变化的 CURRENT_STATE 或 BASELINE_INDEX 不改。
9. 新 AI 先从当前源文件学习，需要历史时才按需回溯。
10. 历史回溯不能偷偷改变当前基线；改变基线必须走正式变更流程。

---

# 31. 一句话总纲

```text
Git 负责记住过去，
项目基线负责描述现在，
Archive 负责隔离历史，
HANDOFF 负责短期接力，
Baseline Relearn 负责定期洗掉上下文污染，
新 AI 永远优先从“当前事实”重新学习。
```

> **目标不是让 AI 记得更多，而是让 AI 默认只记住当前正确的东西。**

---

# 32. Current Truth 与 Baseline Relearn 的统一补充规则

> 本章补充前文，不替代前文。前文关于 Git 保留历史、Context Handoff、Baseline Relearn、Archive、知识压缩、读取顺序和 Clean Context Reset 的规则继续全部有效。

## 32.1 大重置之前先保证当前事实唯一

Baseline Relearn 的前提不是简单“清聊天”，而是先保证：

- 同一个重要主题只有一个当前有效决定；
- 最新确认决定已经正式落盘；
- 旧决定已经标记 `SUPERSEDED`；
- 当前需求、ADR、架构、设计、代码和测试没有继续依赖被替代方案。

如果同一主题存在两个互相冲突的当前有效决定，标记：

```text
DECISION-CONFLICT
```

先解决冲突，再进行 Baseline Relearn。

## 32.2 Current Truth 必须一致，但不得重复维护同一状态

每次 Baseline Relearn 前后只核实本次原因、当前任务和已发现冲突实际涉及的 Owner。下列文件是路由表，不是默认全部读取清单：

```text
CURRENT_STATE.md
BASELINE_INDEX.md
DECISION_INDEX.md
ACTIVE_TASKS.md
OPEN_QUESTIONS.md
CONVERSATION_MAP.md
```

但“一致”不等于“每个文件都抄一遍相同状态”。各文件事实所有权如下：

```text
CURRENT_STATE.md
→ 项目级动态状态：阶段 / Gate / 授权 / 当前焦点 / 下一步

BASELINE_INDEX.md
→ Baseline 身份与组成

DECISION_INDEX.md
→ 当前有效决定

ACTIVE_TASKS.md
→ 任务级状态

OPEN_QUESTIONS.md
→ 未决问题明细

CONVERSATION_MAP.md
→ 对话拓扑 / 生命周期

MIGRATION_LOG.md / HANDOFFS/*
→ 历史 / 快照，不是当前状态权威
```

冲突处理规则：

1. 先判断冲突事实属于哪个所有者；
2. 修正错误引用或过时副本；
3. 不得通过“所有文件都复制同一句最新状态”来解决；
4. `MIGRATION_LOG` 和旧 HANDOFF 保留当时事实，不回写成现在。

无法确定事实所有权或权威源自身冲突时，标记：

```text
CURRENT-TRUTH-CONFLICT
```

禁止让新 AI 自己猜哪个是真的。

## 32.2A 最小状态更新原则

普通状态变化时，只更新拥有该事实的文件。

例如：

```text
C04 finding 从 OPEN → CLOSED
→ 更新正式 C04 review record
→ 如果项目级当前 Gate/下一步因此变化，再更新 CURRENT_STATE.md
→ 不更新 BASELINE_INDEX，除非 Baseline 身份/组成也变化
→ 不更新 CONVERSATION_MAP，除非对话版本/生命周期也变化
→ MIGRATION_LOG 如需审计只追加事件，不承担当前状态
→ 旧 HANDOFF 不回写
```

这样避免“一个状态变化引发五六个文件同步”的审计循环。

## 32.3 大重置后不再继承旧 HANDOFF 链

Context Handoff 用于短期接力；Baseline Relearn 用于长期纠偏。

大重置完成后：

- 旧 HANDOFF 可以归档或按需查阅；
- 新 AI 默认不读取旧 HANDOFF 链；
- 新 AI 从 `AI_START_HERE + Router + 当前任务所需事实` 建立最小工作集；只有任务依赖或冲突命中时才读取 `CURRENT_STATE / BASELINE_INDEX / DECISION_INDEX` 等具体 Owner。

## 32.4 工作树保持当前，Git 保存过去

源码目录和当前文档目录不得长期堆积纯历史副本，例如：

```text
foo_old.cpp
foo_v2.cpp
foo_final.cpp
architecture_old.md
architecture_final2.md
```

如果只是旧版本：当前工作树只保留当前版本，旧版本由 Git 保存。

有独立审计价值的历史文档可以进入 Archive。

禁止为了整洁删除 Git 的可追溯历史。

## 32.5 “清空 AI 记忆”的正确定义

正确：

```text
Git / Archive 继续保存历史
↓
旧聊天停止作为默认上下文
↓
旧 HANDOFF 链停止无限传递
↓
新 AI 从当前任务所需的最小当前事实集重新学习
```

清的是 AI 的历史负担，不是工程的历史证据。

## 32.6 Baseline Relearn 成功标准

成功不是“新 AI 记住了以前所有事情”，而是：

> **一个完全没参加过旧聊天的新 AI 能用最小正式知识开始当前任务，并在使用过程中发现缺口或冲突时，先登记、再定位正确 Owner、按需补学和调整。**

> Authority：首次接管、任务前后检查和上下文阈值规则；由 `INDEX.yaml` 按触发条件加载。

# 9. 第一次必须输出“项目接管报告”

读完文件后，第一轮不得直接修改项目。

必须先输出：

```text
1. 当前项目类型：
   A 全新项目
   B 老项目待规范化
   C 已规范化持续开发

2. 当前建议角色：
   C00 / C01 / C02 / C03 / C04 / C05 / C06

3. 当前开发阶段：
   INIT / REQUIREMENTS / ARCHITECTURE / DESIGN /
   IMPLEMENTATION / VERIFICATION / VALIDATION /
   RELEASE / OPERATIONS

4. 项目目标：
   -

5. 当前技术栈：
   -

6. 当前有效基线：
   PRD：
   SRS：
   ADR：
   架构：
   详细设计：
   测试：
   Git Commit：
   当前版本：

7. 当前已有主要目录：
   -

8. 当前正在进行的工作：
   -

9. 当前未决问题：
   -

10. 当前重大风险：
    -

11. 当前缺失资料：
    -

12. 当前允许修改的范围：
    -

13. 当前禁止擅自修改的事项：
    -

14. 当前最合理的下一步：
    -

15. 是否存在需要 Expert Escalation 的 `QUESTION_PRIORITY` P0/P1 问题：
    YES / NO
```

如果存在 `QUESTION_PRIORITY` P0/P1：

> Primary Executor / C00 先形成最小 Escalation Package 交给 Expert。Expert 能依据现有 Current Truth 和授权解决时，自动返回执行。C04 Finding 不使用 P0～P3；C04 形成 S0/S1 Finding 时，只输出 Finding、定级、关闭条件和 `CHANGES_REQUESTED` 后停止，不得自行关闭 Finding；由 Primary Executor / C00 组织 Expert Escalation 和受控整改，产生新 Review Target 后再启动全新 C04 Session 复审。需要修改 Current Truth、改变产品目标、降低 Acceptance Threshold、接受重大风险，或执行未预授权重大 Gate/Release 时，才向项目负责人一次提出一个最重要问题。

如果不存在 `QUESTION_PRIORITY` P0/P1，且下一步位于 `CURRENT_STATE.md` 已明确授权范围内：

> 不要等待用户再次下令，直接执行当前最合理的下一步。

> 不存在 `QUESTION_PRIORITY` P0/P1 不构成新的阶段授权，也不允许跨越当前 Gate 或授权边界。

---

# 10. 每个任务开始前必须检查

中等以上任务开始前必须知道：

```text
需求是什么？
对应需求编号是什么？
相关 ADR 是什么？
相关设计是什么？
会修改哪些文件？
会影响什么？
需要什么测试？
如何证明完成？
```

如果这些信息不够：

- 普通工程细节可以采用成熟常规方案；
- 重大产品 / 接口 / 架构问题必须进入质询。

---

# 11. 每个任务结束后必须检查

完成后：

1. 构建是否通过；
2. 新测试是否通过；
3. 原测试是否通过；
4. 是否需要回归测试；
5. Sanitizer / 静态分析是否需要执行；
6. 文档是否更新；
7. 需求追溯是否更新；如涉及正式需求 Baseline 或追溯关系变更，Node Coverage + Edge Consistency 是否机械校验通过；
8. CURRENT_STATE 是否更新；
9. 是否产生新 ADR；
10. 是否产生 BUG / CR；
11. 是否有未记录 workaround；
12. 是否达到 Definition of Done。

未达到 DoD：

> 不得声称“开发完成”。

---

# 12. 物理 Session 上下文过长时必须切换

遵守：

`00_project/governance/modules/sessions/SESSION_LIFECYCLE_AND_HANDOFF.md`

如果平台显示上下文使用率：

```text
60% → 准备交接
70% → 不再接新的大型任务
80% → 必须换新对话
```

如果不显示：

```text
25 个有效工程回合 → 检查是否切换
40 个有效工程回合 → 原则上必须切换
```

出现明显遗忘、混淆旧版本、重复询问已确认决策时：

> 立即准备切换。

切换必须：

```text
重要决策落盘
→ 更新 CURRENT_STATE
→ 更新 ACTIVE_TASKS
→ 更新 OPEN_QUESTIONS
→ 生成 HANDOFF
→ 记录 Git Commit / 分支 / 测试
→ 旧对话 READ ONLY
→ 新对话继续
```

Harness 支持且权限允许时，C00 可以自动完成本地 `C00-vNext` 建立和受控交接；项目负责人仍停留在同一逻辑 C00 管理链。

---

\n# 14. 现在立即执行

如果你是第一次进入本项目：

1. 完整阅读本文件；
2. 阅读工程总则；
3. 阅读多对话规则；
4. 判断项目类型；
5. 判断当前角色；
6. 如果是老项目，阅读旧项目规范化迁移指南；
7. 只读检查项目；
8. 输出“项目接管报告”；
9. 如果存在 `QUESTION_PRIORITY` P0/P1，按工程总则由 Primary Executor / C00 组织 Expert Escalation；C04 Finding 使用 S0～S3，C04 只形成 Finding 和评审结论后停止。如果不存在 `QUESTION_PRIORITY` P0/P1，且下一步位于 `CURRENT_STATE.md` 已明确授权范围内，直接执行下一项最合理工作。不存在 `QUESTION_PRIORITY` P0/P1 不构成新的阶段授权。

**在完成项目接管报告之前，不得大规模修改代码或目录。**
\n

> Authority：启动阶段的项目分类与迁移规则；由 `INDEX.yaml` 按触发条件加载。

# 1. 先判断这是新项目还是老项目

首先检查项目目录。

将项目分类为以下三种之一：

## A. 全新项目

典型特征：

- 几乎没有业务代码；
- 还没有正式需求或架构；
- 项目刚开始；
- 当前工程模板是主要内容。

处理方式：

> 从 C00 项目总控 + C01 产品/系统需求开始。

## B. 已有代码但尚未规范化的老项目

典型特征：

- 已有大量代码；
- 已经能运行或部署；
- 已有历史文档；
- 目录结构不符合本工程模板；
- 需求、设计、测试可能散落；
- 可能已经有用户或测试人员使用。

处理方式：

> **先只读盘点，不得直接大规模移动、重构或改代码。**

必须阅读：

`AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md`

然后按照旧项目迁移流程执行：

```text
安全快照
→ 只读盘点
→ 建立 As-Is 状态
→ 建立需求 / 架构 / 测试基线
→ 建立追溯
→ 设置新的规范化基线
→ 小批量迁移
→ 每批重新构建和测试
```

## C. 已经按本规范持续开发的项目

典型特征：

- `CURRENT_STATE.md` 已维护；
- `BASELINE_INDEX.md` 已维护；
- 已有 PRD / SRS / ADR / 设计 / 测试；
- 已经有 C00~C06 对话分工；
- 有 HANDOFF 或任务状态。

处理方式：

> 根据当前状态继续，不重新从头建立项目。

## 1.1 再判断项目结构模式

项目生命周期分类完成后，读取 `00_project/ai_context/PROJECT_STRUCTURE_MAP.md`，确认：

```text
SINGLE_PROJECT
MODULAR_PROJECT
FEDERATED_PROJECT
```

结构模式、递归 Work Package、父子事实边界和分层接受规则见 `00_project/governance/PROJECT_DECOMPOSITION_AND_FEDERATION_POLICY.md`。如果当前项目是 Governed Subproject，只加载 Parent–Child Contract、父级精确 Anchor 和当前任务所需接口，不默认学习整个 Parent 或兄弟项目内部细节。
\n# 5. 新项目怎么处理目录

如果是全新项目：

> **工程模板中的目录和文件可以整体复制到项目根目录。**

然后：

1. 修改项目名；
2. 初始化 Git；
3. 填写项目概览；
4. 建立 PRD；
5. 开始需求质询；
6. 再进入 SRS；
7. 再进入架构；
8. 再进入详细设计；
9. 再进入测试设计；
10. 最后进入正式编码。

新项目中，模板文件本身已经在正确位置。

---

# 6. 老项目怎么处理目录

如果是老项目：

> **不要把旧代码和旧文档立即强行塞进新模板目录。**

正确做法：

## 第一步：把“规范体系”加入项目根目录

可以加入：

- `AI_START_HERE.md`
- `AI_ENGINEERING_RULES_V2.md`
- `AI_CONVERSATION_ORCHESTRATION_RULES.md`
- `AI_LEGACY_PROJECT_STANDARDIZATION_GUIDE.md`
- `00_project/`
- 缺失的规范目录骨架

但是：

> 如果已有同名业务目录或文件，禁止直接覆盖。

## 第二步：保留原工程原样

旧代码、旧构建脚本、旧配置、旧部署结构先不动。

先记录：

```text
As-Is
= 今天项目真实存在的状态
```

## 第三步：AI 只读盘点

AI 必须识别：

- 哪些是需求；
- 哪些是设计；
- 哪些是代码；
- 哪些是测试；
- 哪些是部署文件；
- 哪些是生成物；
- 哪些是第三方；
- 哪些是历史文件；
- 哪些用途未知。

建立“旧位置 → 新逻辑位置”的映射。

## 第四步：先建立逻辑归位

例如：

```text
旧文件 doc/spec_old.md
```

经过确认后，可能对应：

```text
02_system_requirements/SRS.md
```

第一阶段可以先从旧文档提炼出当前有效内容，写入新的 SRS。

而不是马上删除或移动旧文件。

## 第五步：物理移动最后做

只有确认：

- 不会破坏构建；
- 不会破坏 import；
- 不会破坏 CMake / qmake / 脚本；
- 不会破坏部署；
- 不会破坏测试；
- 有 Git 回退点；
- 有验证方法；

才允许小批量移动。

每批必须：

```text
移动
→ 修引用
→ 构建
→ 测试
→ 运行验证
→ Commit
```

---

# 7. AI 能不能自动帮你放到正确位置

可以，但必须分两种情况。

## 新项目

可以直接按照模板位置创建和填写文件。

例如：

```text
PRD
→ 01_product_requirements/PRD.md

SRS
→ 02_system_requirements/SRS.md

ADR
→ 03_architecture/architecture_decisions/

详细设计
→ 04_design/

测试设计
→ 06_test_design/

测试代码
→ 08_tests/

Bug
→ 12_issues/

变更
→ 13_change_management/
```

## 老项目

AI 不得直接自动大规模搬家。

必须先：

```text
识别
→ 分类
→ 建立映射
→ 确认风险
→ 形成迁移计划
→ 小批量执行
→ 每批验证
```

因此：

> **老项目中的“自动归位”是受控迁移，不是自动整理桌面。**

---
\n

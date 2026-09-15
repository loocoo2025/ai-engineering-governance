# 治理模板升级执行协议

> Governance Template Upgrade Protocol
>
> 适用于将采用过任一受支持旧版本的项目升级到指定目标版本。
>
> 本协议只负责治理模板升级，不授权修改产品需求、架构、代码、测试、远程仓库或发布状态。

## 1. 核心原则

```text
CURRENT EXACT VERSION
+ CUMULATIVE DELTA
+ TARGET UPGRADE MANIFEST
→ TARGET GOVERNANCE VERSION
```

升级不是重新学习整个项目，也不是逐个重放中间版本。

必须遵守：

1. 只读取完成当前升级所必需的文件；当前证据足够时立即停止。
2. 只比较当前精确版本与目标精确版本之间的累计 Delta。
3. 不依次阅读中间版本的 Release Notes、迁移记录或全部治理文档。
4. 不重新评审未变化且不受影响的项目事实。
5. 已知冲突先登记，再读取冲突事实的唯一 Owner 并处理；不得为了预防未知冲突全量阅读。
6. 可选控制只在目标 Manifest 命中触发条件或 Human Project Owner 明确采用时实例化。
7. 产品事实默认不可修改；治理升级不得顺便重构项目。
8. Human Project Owner 可以在执行中纠正 AI 的过度读取、验证、治理或执行习惯，AI 必须立即收窄；但不得静默绕过安全、权限、不可逆操作、正式 Gate 或精确 Target 等关键边界。

## 2. 最短调用指令

```text
请按 `13_change_management/templates/治理模板升级-GOVERNANCE_TEMPLATE_UPGRADE_TEMPLATE.md`
将当前项目治理框架从已采用的精确版本升级到 {{TARGET_VERSION_OR_COMMIT}}。

先自动检查升级条件；只使用当前版本到目标版本的累计 Delta 和目标
`13_change_management/UPGRADE_MANIFEST.yaml`，禁止逐版本重放或全仓重学。

权限：{{READ_ONLY_PREPARE / APPLY_NO_COMMIT / APPLY_AND_COMMIT}}
Push / Release：默认禁止，除非本指令另有明确授权。
```

## 3. 输入

必须能够确定：

```text
PROJECT_ROOT: {{PATH}}
CURRENT_FRAMEWORK_VERSION: {{EXACT_TAG_OR_COMMIT}}
TARGET_FRAMEWORK_VERSION: {{EXACT_TAG_OR_COMMIT_OR_LATEST_STABLE}}
UPSTREAM_SOURCE: {{GITHUB_OR_GITEE}}
EXECUTION_PERMISSION: {{READ_ONLY_PREPARE / APPLY_NO_COMMIT / APPLY_AND_COMMIT}}
```

若请求 `LATEST_STABLE`，先从项目已配置的框架发布源解析一个不可变 Tag 和完整 Commit Hash，再继续。不得以浮动分支名作为最终 Target。

## 4. 自动就绪检查

按顺序检查；得到足够结论后停止，不扩展扫描。

### 4.1 精确版本

- 当前项目必须有可验证的已采用版本或 Commit。
- 目标 Tag / Commit 必须存在、可读取且不可变。
- 目标必须包含有效的 `13_change_management/UPGRADE_MANIFEST.yaml`。
- Manifest 必须声明当前版本属于支持的升级来源；否则输出 `BLOCKED`，不得靠猜测兼容性继续。

### 4.2 工作树和写入隔离

- 读取 `git status --short`。
- 干净工作树可以继续。
- 存在未提交修改时，不得覆盖、丢弃、stash、reset 或混入升级 Commit。
- 若已获授权且可以创建独立 Git worktree，可在绑定当前精确 Commit 的干净 worktree 中准备升级。
- 无法隔离时输出 `BLOCKED_DIRTY_WORKTREE`，列出路径并停止写入。
- 同一 Local 工作目录同时只能有一个写入者；多个写入 Session 必须使用独立 worktree。

### 4.3 正式 C04

- 若同一治理 Target 正在正式 C04，输出 `BLOCKED_ACTIVE_FORMAL_C04`，不得改变该 Target。
- 若其他产品 Target 正在正式 C04，只允许在独立 worktree 中准备升级；不得在该评审结束前采用会改变其适用治理标准的 Baseline。
- 状态文件、Review Record 或 Git 证据互相矛盾时记为 `UNKNOWN` 并停止，不得推断“应该没有正在评审”。

### 4.4 权限

- `READ_ONLY_PREPARE`：只形成计划和报告，不写文件。
- `APPLY_NO_COMMIT`：允许修改治理模板文件，不 Commit、不 Push。
- `APPLY_AND_COMMIT`：允许形成一个独立升级 Commit；仍不允许 Push、PR、Tag、Release 或远程修改。
- 子 Agent、外部 AI、CLI 和工具不得扩大 Caller 权限。

## 5. 最小升级算法

### Step 1 — 读取最小控制面

只读取：

1. 本协议；
2. 当前项目记录的精确框架版本；
3. 目标版本的 `13_change_management/UPGRADE_MANIFEST.yaml`；
4. Manifest 明确列出的受影响 Owner 和验证命令。

不要先读取全部治理、需求、架构、设计、测试或历史 Review 文件。

### Step 2 — 固定 Source 与 Target

记录：

```text
SOURCE_TAG_OR_COMMIT:
SOURCE_FULL_COMMIT:
TARGET_TAG_OR_COMMIT:
TARGET_FULL_COMMIT:
TARGET_MANIFEST_HASH:
```

任何一个值无法精确解析时停止。

### Step 3 — 只生成累计 Delta

在框架上游仓库计算：

```bash
git diff --name-status <SOURCE_FULL_COMMIT>..<TARGET_FULL_COMMIT>
git diff <SOURCE_FULL_COMMIT>..<TARGET_FULL_COMMIT> -- <manifest-selected-paths>
```

禁止：

- 为每个中间版本重复执行迁移；
- 逐个阅读中间 Release Notes；
- 把未变化文件加入评审范围；
- 用全仓搜索代替 Manifest 路由，除非 Manifest 缺失且已因此停止并请求人工裁决。

### Step 4 — 按所有权分类

每个 Delta 路径只能属于一种处理方式：

| 类别 | 默认处理 |
|---|---|
| `FRAMEWORK_OWNED_UNCUSTOMIZED` | 使用目标版本替换 |
| `FRAMEWORK_OWNED_CUSTOMIZED` | 仅对本轮受影响语义做三方合并 |
| `PROJECT_GOVERNANCE_STATE` | 保留项目实例值，只迁移必要字段或结构 |
| `PRODUCT_OWNED` | 不修改 |
| `OPTIONAL_FEATURE` | 仅在已采用或本次明确选择时启用；否则可以随模板保留但不得加载、构建或运行 |

若一个文件同时承载框架规则和项目实例值，先按字段分离处理；不允许整文件覆盖项目事实。

### Step 5 — 应用最小变更

- 只修改 Manifest 声明的文件和直接冲突文件。
- 未列入 Delta 的语义保持不变。
- 不生成未触发的 Dynamic Profile、Knowledge Manifest、Authorization Contract、Task Contract、Worktree Lease 或其他可选记录。
- 发现实际冲突时：登记 → 确认唯一 Owner → 只读取解决该冲突所需内容 → 处理或交由 Human Owner 裁决。

### Step 6 — 最小验证

只运行目标 Manifest 声明且与实际 Delta 有关的检查。

最低机械检查：

```bash
git diff --check
git status --short
```

只有代码、脚本、Schema 或编译器发生变化时，才运行其直接相关的 Targeted Test。不得因升级治理文档自动运行全部产品测试。

### Step 7 — 独立评审判定

- 是否需要正式 C04 由目标 Manifest、当前项目 Profile 和 Human Project Owner 的要求共同决定。
- 需要时，正式 C04 只审累计 Delta、受影响 Owner、关键回归边界和升级证据。
- 不重新评审所有未变化的治理文件或产品事实。
- C04 只处理当前 Review Purpose / Scope / Core Acceptance Concerns 内的阻断问题；实际发现的其他可信问题登记为 Feedback。

### Step 8 — Commit 与采用

- 只有 `APPLY_AND_COMMIT` 才创建独立升级 Commit。
- Commit 不等于 Baseline Adoption。
- Baseline Adoption、Formal Seal、Push、PR、Tag、Release 必须分别获得其所需授权。
- 未获 Commit 授权时保留工作树 Diff 并报告。

## 6. Baseline Relearn

升级采用后的 Baseline Relearn 仍然是按需动作，不是全量重学。

只重新加载：

1. 本次累计 Delta 中改变的治理语义；
2. 当前待继续任务；
3. 当前任务的直接依赖；
4. 为解决已发现冲突所需的唯一事实 Owner；
5. 新增且已实际触发的关键权限、Gate 或安全边界。

不得默认读取：

- 全部需求、架构、设计、代码与测试；
- 全部历史 Review、Handoff、Issue 或 Release Notes；
- 所有可选合同和未采用功能；
- 与当前任务没有直接关系的细枝末节。

成功标准不是“已经读完所有文件”，而是：

```text
当前 Role、权限、任务、直接依赖和适用 Gate 已明确，
足以安全执行下一步；其余正式事实仍可按 Owner 路由检索。
```

后续使用中发现冲突时，先登记，再按需补读和调整。允许问题在使用中被发现；不得猜测、静默覆盖或要求预先穷尽所有潜在冲突。

## 7. 停止条件

命中任一项立即停止相应写入并报告：

- Source 或 Target 不是精确不可变版本；
- 目标 Manifest 缺失、无效或不支持当前 Source；
- 未提交修改无法安全隔离；
- 同一治理 Target 正在正式 C04；
- 关键状态证据冲突，无法判断是否可升级；
- 需要改变产品事实、Current Truth、产品目标、Acceptance Threshold、公共接口、安全或数据完整性边界；
- 需要未授权 Commit、远程操作、破坏性操作、Baseline Adoption、Tag、Push 或 Release；
- 升级无法在不丢失项目定制的情况下机械合并。

普通非核心问题不要求停止。登记为 Feedback 并交由正确 Owner 决定处置即可。

## 8. 输出格式

```text
GOVERNANCE_UPGRADE_REPORT

SOURCE_VERSION:
SOURCE_COMMIT:
TARGET_VERSION:
TARGET_COMMIT:
TARGET_MANIFEST:

READINESS: READY / BLOCKED
WORKTREE_ISOLATION:
ACTIVE_FORMAL_C04_CHECK:
EXECUTION_PERMISSION:

CUMULATIVE_DELTA_FILES:
FILES_CHANGED:
PROJECT_FACTS_PRESERVED:
OPTIONAL_FEATURES_ADOPTED:
OPTIONAL_FEATURES_NOT_ACTIVATED:

VALIDATION_RUN:
VALIDATION_RESULT:
FORMAL_C04_REQUIRED:
COMMIT:
BASELINE_ADOPTION_STATUS:
BASELINE_RELEARN_SCOPE:

RECORDED_NON_BLOCKING_FEEDBACK:
BLOCKERS_OR_HUMAN_DECISIONS:
FINAL_STATUS: PREPARED / APPLIED_NOT_COMMITTED / COMMITTED_NOT_ADOPTED / ADOPTED / BLOCKED
```

报告只列事实和必要证据，不复制全部 Diff 或长篇复述框架规则。

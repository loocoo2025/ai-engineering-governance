# CR-GOV-004：模块化治理知识路由与 APLS 设计集成

## 0. 文档控制

```text
CHANGE_TYPE: GOVERNANCE_CHANGE
SEMANTIC_LEVEL: SUBSTANTIVE
STATUS: APPROVED_FOR_RELEASE_EXECUTION
CURRENT_VERSION: v0.1.7
SOURCE_COMMIT: 5799bcff84e7166f9f09c65e59247b3dcbdec6df
INCLUDED_POST_RELEASE_COMMIT: f205b339ebabdc6bf4ac5c2d2f0c70011a99da2a
TARGET_IDENTITY: v0.1.8
HUMAN_PROJECT_OWNER: Project Owner
DATE: 2026-09-13
```

## 1. 问题

大型单体治理文件导致每个 Session 重复加载大量与当前任务无关的规则。现有“最小知识加载”只有原则，缺少可机械解析的总 Router、领域 INDEX、按需依赖和失败关闭规则。

同时，启用 APLS 的项目需要 C02 在行为规格、详细设计、算法规格和 Target Profile 之间机械分配事实，防止 AI 把行为埋进实现文档或凭自然语言猜测。

## 2. 已批准目标

- 将唯一完整必读入口压缩为最小治理内核；
- 建立总 Router、Startup/Engineering/Session Domain INDEX 和原子规则文件；
- 原有大文件保留为旧路径、旧章节兼容入口，不再要求全文加载；
- 索引只路由，不复制规则正文，保持 One Fact, One Owner；
- APLS 作为默认关闭的可选 C02 集成；
- 固定 APLS 官方 Repository、精确受支持 Tag/Commit 和浮动分支禁用；
- 建立 Design Allocation Table、Verified IR 和下游交付合同；
- 将此前已提交的 GitHub/Gitee 受控更新与中英文双语提醒纳入 v0.1.8；
- 完成精确 Release Candidate、正式 C04 和稳定 Release。

## 3. 不变量

- 不改变 C00～C06 固定岗位；
- 不改变 Current Truth、Baseline、Traceability、C04 Decision Matrix、Testing Governance 或 Release Gate；
- 不强制普通项目采用 APLS；
- 不修改、复制或发布外部 APLS 项目文件；
- 不把目录或摘要升级为第二事实 Owner；
- 不追溯改写历史 Review Record 和旧版本引用；
- 不处理现有无关未跟踪文件。

## 4. 发布授权

Human Project Owner 已于 `2026-09-13` 明确要求实现并尽快发布正式 `v0.1.8`。该授权允许修改本治理模板、形成 Commit、建立正式独立 C04、在 Gate 通过后创建并 Push `v0.1.8` Tag、同步官方远程并创建 GitHub Release。

该授权不允许修改外部产品或 APLS 仓库、Force Push、改写历史、绕过正式 C04、处理无关未跟踪文件或签发 Formal Seal。

## 5. Release Gate

```text
MINIMAL_BOOTSTRAP_READY: YES
GOVERNANCE_ROUTER_READY: YES
DOMAIN_INDEX_READY: YES
ATOMIC_RULE_OWNER_READY: YES
LEGACY_PATH_COMPATIBILITY_READY: YES
APLS_C02_ALLOCATION_READY: YES
CONTROLLED_SELF_UPDATE_INCLUDED: YES
ONE_FACT_ONE_OWNER_CHECK: PASS
MECHANICAL_VALIDATION: PASS
FORMAL_C04: REQUIRED_ON_EXACT_COMMIT
OPEN_S0_TO_S3_REQUIRED: 0
PRERELEASE: NO
FINAL_STATUS: V0.1.8_RELEASED_OR_PUBLICATION_BLOCKED
```

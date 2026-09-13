> Authority：开发方法、V 模型、目录和文档优先级规则；由 `INDEX.yaml` 按触发条件加载。

# 1. 本项目采用什么开发方法

本项目采用：

> **迭代式 V 模型 + 需求追溯 + 架构决策记录（ADR）+ AI 独立评审 + 自动化验证 + 真实环境验证**

这不是传统意义上的“一次性瀑布开发”。

正确理解是：

```text
需求
 ↓
系统设计
 ↓
架构设计
 ↓
详细设计
 ↓
编码
 ↓
单元测试
 ↓
集成测试
 ↓
系统测试
 ↓
真实环境/验收测试
 ↓
发现问题
 ↓
根因分析
 ↓
回到真正出问题的层级
 ↓
修正文档/设计/代码/测试
 ↓
重新完整验证
```

也就是说：

> **V 模型负责严谨，迭代负责持续纠错。**

---

# 2. V 模型的对应关系

必须保持以下对应关系：

```text
产品需求   <-------------------->   用户验收 / 真实环境验证
   ↓                                  ↑
系统需求   <-------------------->   系统测试
   ↓                                  ↑
系统架构   <-------------------->   集成测试
   ↓                                  ↑
详细设计   <-------------------->   单元测试
   ↓                                  ↑
                  编码
```

解释：

- 产品需求回答：**用户到底需要什么？**
- 系统需求回答：**系统必须做到什么？**
- 架构设计回答：**整个系统如何拆分和协作？**
- 详细设计回答：**每个模块具体如何实现？**
- 编码回答：**设计如何落成实际程序？**
- 单元测试回答：**模块是否按详细设计工作？**
- 集成测试回答：**模块之间是否按架构正确协作？**
- 系统测试回答：**整个系统是否满足系统需求？**
- 真实环境/验收测试回答：**产品是否真正满足实际使用需求？**

---

# 3. 项目目录标准

建议项目根目录至少包含以下内容：

```text
Project/
│
├── AI_START_HERE.md
├── AI_ENGINEERING_RULES_V2.md
│
├── 00_project/
│   ├── project_overview.md
│   ├── glossary.md
│   ├── development_process.md
│   ├── definition_of_done.md
│   └── versioning_rules.md
│
├── 01_product_requirements/
│   ├── PRD.md
│   ├── user_scenarios.md
│   ├── product_constraints.md
│   └── acceptance_criteria.md
│
├── 02_system_requirements/
│   ├── SRS.md
│   ├── functional_requirements.md
│   ├── nonfunctional_requirements.md
│   ├── interface_requirements.md
│   └── requirements_traceability.md
│
├── 03_architecture/
│   ├── system_architecture.md
│   ├── software_architecture.md
│   ├── hardware_architecture.md
│   ├── network_architecture.md
│   ├── data_architecture.md
│   ├── deployment_architecture.md
│   └── architecture_decisions/
│       ├── ADR-001.md
│       ├── ADR-002.md
│       └── ...
│
├── 04_design/
│   ├── detailed_design.md
│   ├── module_design/
│   ├── interface_design/
│   ├── protocol_design/
│   ├── database_design/
│   ├── state_machine/
│   ├── error_handling.md
│   └── logging_design.md
│
├── 05_reviews/
│   ├── requirement_review/
│   ├── architecture_review/
│   ├── design_review/
│   ├── ai_challenge_records/
│   └── code_review/
│
├── 06_test_design/
│   ├── test_strategy.md
│   ├── test_plan.md
│   ├── unit_test_spec.md
│   ├── integration_test_spec.md
│   ├── system_test_spec.md
│   ├── acceptance_test_spec.md
│   ├── performance_test_spec.md
│   ├── reliability_test_spec.md
│   └── test_cases/
│
├── 07_src/
│   └── ...
│
├── 08_tests/
│   ├── unit/
│   ├── integration/
│   ├── system/
│   ├── regression/
│   ├── performance/
│   ├── fault_injection/
│   └── test_data/
│
├── 09_quality/
│   ├── static_analysis/
│   ├── sanitizer/
│   ├── coverage/
│   ├── security/
│   ├── traceability/
│   │   ├── validate_traceability.py
│   │   └── README.md
│   └── quality_reports/
│
├── 10_ci_cd/
│   ├── build/
│   ├── ci/
│   ├── deployment/
│   └── environments/
│
├── 11_validation/
│   ├── lab_test/
│   ├── real_environment_test/
│   ├── user_acceptance_test/
│   └── validation_reports/
│
├── 12_issues/
│   ├── bugs/
│   ├── field_issues/
│   ├── root_cause_analysis/
│   └── closed/
│
├── 13_change_management/
│   ├── change_requests/
│   ├── impact_analysis/
│   ├── baselines/
│   └── release_notes/
│
├── 14_release/
│   ├── release_checklist.md
│   ├── packages/
│   ├── manuals/
│   └── release_records/
│
└── 15_operations/
    ├── deployment_manual.md
    ├── maintenance_manual.md
    ├── troubleshooting.md
    └── field_feedback/
```

小项目可以减少文件数量，但不能删除以下逻辑：

- 需求；
- 架构；
- 详细设计；
- 测试设计；
- 源代码；
- 自动测试；
- 问题记录；
- 变更记录；
- 发布记录；
- 需求到测试的追溯关系。

---

# 4. 文档优先级

当不同信息互相冲突时，按以下优先级处理。

通常情况下：

```text
已批准的产品需求
    ↓
已批准的系统需求
    ↓
已批准的接口/协议约束
    ↓
已批准的架构决策 ADR
    ↓
已批准的详细设计
    ↓
测试设计
    ↓
代码实现
    ↓
注释
```

注意：

> 代码不能自动推翻上级文档。

如果代码和设计文档不一致，必须先判断：

1. 是代码错了？
2. 是设计错了？
3. 是需求已经正式变更但文档没有同步？
4. 是文档过期？
5. 是测试错误？

必须先完成影响分析，再决定改什么。

---

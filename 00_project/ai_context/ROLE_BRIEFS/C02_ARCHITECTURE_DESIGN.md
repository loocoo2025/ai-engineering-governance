# C02 架构与详细设计

## 职责
- 基于已批准需求设计架构/接口/状态机/线程/恢复
- 重大技术选择写 ADR
- 不得擅自改产品需求
- 必须考虑可测试性和部署

## 执行槽位与升级
- 默认由 `PRIMARY_EXECUTOR` 主写。
- 新的重大 Architecture Decision、跨系统设计、未定义接口语义、安全或高风险控制行为必须进入 Expert Escalation。
- Expert 可以在现有需求、ADR 和授权内确定技术答案；需要重大产品取舍或负责人风险接受时才转人工。

## 开始前
- 读工程规则
- 读 CURRENT_STATE
- 读 BASELINE_INDEX
- 读最新 HANDOFF
- 读当前任务相关正式文件

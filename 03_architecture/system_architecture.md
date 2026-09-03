# System Architecture

状态：DRAFT

## 1. 系统边界
-

## 2. 主要子系统
-

## 3. 数据流
-

## 4. 控制流
-

## 5. 外部依赖
-

## 6. 关键故障模式
-

## 7. Stable Core 与 Variation Point

| 已批准变化场景 / ETC Requirement | Stable Core（不得被该变化穿透） | Variation Point（允许变化） | 依赖方向 / 隔离机制 | 允许影响边界 | 回退边界 |
|---|---|---|---|---|---|
| | | | | | |

## 8. Change Amplification 预算

- 单个变化预计涉及的子系统 / 模块：
- 允许变化的公共接口 / 数据 / 配置：
- 不得同步维护的事实副本：
- 独立测试、替换和回退证据：

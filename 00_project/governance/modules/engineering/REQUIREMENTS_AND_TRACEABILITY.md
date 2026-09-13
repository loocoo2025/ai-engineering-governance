> Authority：需求编号、可验证性和追溯规则；由 `INDEX.yaml` 按触发条件加载。

# 5. 需求必须编号

所有重要需求必须有唯一编号。

推荐格式：

```text
PRD-xxx    产品需求
SYS-xxx    系统需求
NFR-xxx    非功能需求
IF-xxx     接口需求
ARCH-xxx   架构设计项
DES-xxx    详细设计项
ADR-xxx    架构决策
TC-xxx     测试用例
BUG-xxx    Bug
CR-xxx     变更请求
```

可以增加领域前缀，例如：

```text
SYS-NET-001
SYS-DEV-003
ARCH-NET-002
DES-STORAGE-004
TC-NET-017
```

---

# 6. 每条重要需求必须可验证

禁止使用无法判断是否完成的模糊需求，例如：

```text
系统要稳定。
界面要流畅。
网络连接要可靠。
尽量避免崩溃。
系统性能要好。
```

必须尽可能改成可验证的要求。

例如：

```text
SYS-NET-001

要求：
当设备网络连接异常中断后，系统必须自动检测连接失效并执行重连。

验收条件：
1. 网络恢复后无需人工重启软件；
2. 自动恢复通信；
3. 主业务线程不得被重连阻塞；
4. 重连过程必须记录日志；
5. 连续执行 100 次断网/恢复测试后，不得发生崩溃；
6. ASan 不得报告非法内存访问；
7. 不得出现持续增长的资源泄漏。
```

---

# 7. 建立完整需求追溯关系

重要需求必须尽量形成如下链路：

```text
需求
 ↓
架构
 ↓
详细设计
 ↓
代码模块
 ↓
测试
 ↓
测试结果
```

例如：

```text
SYS-NET-001
    ↓
ARCH-NET-003
    ↓
DES-NET-012
    ↓
ConnectionManager
ReconnectController
    ↓
TC-NET-021
TC-NET-022
TC-NET-023
```

`requirements_traceability.md` 至少应能回答：

| 需求 | 架构/设计 | 代码模块 | 测试 | 状态 |
|---|---|---|---|---|
| SYS-NET-001 | ARCH-NET-003 / DES-NET-012 | ConnectionManager | TC-NET-021~023 | PASS |

如果一个重要需求找不到对应测试，视为测试缺口。

如果一个重要模块完全找不到对应需求或设计依据，需要检查是否存在无必要功能或设计漂移。

## 7.1 需求追溯必须同时验证“节点”和“关系边”

需求追溯闭合不得只证明需求 ID 都出现过。

必须分别验证：

```text
Node Coverage
节点覆盖

Edge Consistency
关系边一致性
```

> **节点完整不等于关系完整。**

### Node Coverage

对于当前正式 SYS / NFR / IF 集合，至少检查：

```text
Expected IDs
Covered IDs
Missing IDs
Unexpected IDs
```

正式需求 Baseline 的默认门禁要求：

```text
Missing IDs = 0
Unexpected IDs = 0
```

### Edge Consistency

默认情况下，详细 SYS / NFR / IF 元数据中的正式上游追溯关系，与 `requirements_traceability.md` 中的正式上游追溯关系，必须表达同一关系集合。

设：

```text
A = Detailed Metadata Edge Set
B = Traceability Matrix Edge Set
```

默认闭合要求：

```text
A - B = ∅
B - A = ∅
```

也就是：

```text
Detailed-only = 0
Matrix-only = 0
```

不得再使用“所有 ID 至少出现一次”作为关系边已经闭合的证明。

## 7.2 差异关系必须逐条分类，禁止机械覆盖

发现 Detailed-only 或 Matrix-only 关系时，不得直接把任意一侧批量覆盖到另一侧。

每条差异必须分类为：

```text
VALID_FORMAL_TRACE
关系有效，应在两侧同步。

INVALID_RELATION
关系无效，应从错误一侧删除。

DIFFERENT_RELATION_SEMANTICS
两侧表达的不是同一种关系。
```

若项目没有已经批准的多关系语义，默认只使用：

```text
FORMAL_TRACE
```

未经正式批准，不得为了消除差集临时发明 `SUPPORTS`、`ALLOCATES_TO`、`CONSTRAINS` 等新关系类型。

如果项目正式批准多种关系类型，机械比较单位必须从：

```text
(source, target)
```

升级为：

```text
(source, target, relation_type)
```

并明确每种关系的规范来源、允许方向和校验规则。

## 7.3 追溯机械门

模板提供：

```text
09_quality/traceability/validate_traceability.py
```

在建立或复审正式需求 Baseline 前，C01 必须先运行该机械校验；C04 在独立需求评审中必须独立复核。

默认只有同时满足：

```text
Missing Nodes = 0
Unexpected Nodes = 0
Detailed-only Edges = 0
Matrix-only Edges = 0
```

或所有非零差异均已有正式批准、逐条标注且可机械验证的关系语义例外时，才允许声明：

```text
TRACEABILITY_CLOSED
```

否则必须保持：

```text
TRACEABILITY_NOT_CLOSED
```

---

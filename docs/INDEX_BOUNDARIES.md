# Index Boundaries

这份文档专门回答一个问题：当前仓库里的几种索引到底分别包含什么，默认该用哪个。

## 结论

- `business_code_index.db`
  - 含义：代码索引
  - 内容：仅业务 DSL / UFT 代码文件
  - 不包含：`metadata` 元数据文件、`.uftstructure` 表结构
  - 用途：默认检索库，适合大多数“代码逻辑在哪里”“谁调用了谁”类问题

- `business_metadata_index.db`
  - 含义：元数据索引
  - 内容：`metadata` 目录下的标准字段、常量、错误号、宏、主题域、缓存表等
  - 不包含：业务代码、表结构
  - 用途：专门回答“常量定义在哪里”“topic 对应什么”“错误码是什么”类问题

- `business_full_index.db`
  - 含义：全量索引
  - 内容：代码文件 + `metadata` 元数据文件
  - 不包含：`.uftstructure` 表结构
  - 用途：需要跨代码和元数据做综合检索时使用

- `business_table_index.db`
  - 含义：表结构索引
  - 内容：`.uftstructure`、字段、索引、表空间关系
  - 用途：查表、字段、索引、表空间

- `uses_codes_index.db`
  - 含义：较小范围的子库回归索引
  - 内容：`uses_codes` 子目录
  - 用途：回归测试、小范围调试

## 默认策略

- CLI / HTTP / MCP 的默认代码检索库优先选择 `business_code_index.db`
- 如果代码索引不存在，才回退到 `business_full_index.db`
- 如果再不存在，最后回退到 `uses_codes_index.db`

这个策略的目标是：

1. 默认先查代码，减少 metadata 命中干扰
2. 需要综合检索时再明确切到全量索引
3. 保留小库用于回归，不让它冒充默认生产库

## 一个常见误区

`business_code_index.db` 现在不再表示“完整根目录所有内容都混在一起的默认总库”，它表示“完整根目录范围内的代码索引”。

如果你要同时检索代码和 metadata，请显式使用 `business_full_index.db` 或分开查代码索引和元数据索引。

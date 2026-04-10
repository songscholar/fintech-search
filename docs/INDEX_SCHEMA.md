# Index Schema

## 目标

这个文档描述当前 SQLite 索引库里每张表的职责，方便后续继续扩展。

数据库样例文件默认会生成到 `examples/uses_codes_index.db`，该文件体积较大，当前不纳入版本控制。

## 元数据

`metadata` 表当前除了记录 `source_root`、`file_count`、`schema_version`，还会记录：

- `fts_enabled`
- `vector_enabled`
- `embedding_provider`
- `embedding_model`
- `embedding_dimension`

这组字段用于在查询阶段判断当前 embedding 配置是否和索引库兼容。

## 表结构概览

### `files`

每个 DSL 文件一条记录。

主要字段：

- `path`
- `file_name`
- `unit_kind`
- `prefix`
- `name`
- `chinese_name`
- `object_id`
- `code_line_count`
- `attributes_json`

### `procedures`

当前和文件基本一一对应，用来表示“可调用过程”的主实体。

主要字段：

- `file_id`
- `name`
- `prefix`
- `unit_kind`
- `chinese_name`
- `object_id`

### `histories`

记录文件头里的历史修改信息。

### `params`

记录输入、输出、内部参数。

主要字段：

- `category`
- `param_id`
- `uuid`
- `param_type`
- `type_name`
- `name`
- `comments`
- `default_value`

### `statements`

当前最重要的一张表，保存结构化语句流。

主要字段：

- `kind`
- `line_start`
- `line_end`
- `raw`
- `tag`
- `name`
- `condition`
- `target`
- `groups_json`
- `arguments_json`
- `reads_json`
- `writes_json`

### `actions`

从 `statements` 中投影出来的动作/调用记录，方便检索和关系计算。

主要字段：

- `kind`
- `tag`
- `action_name`
- `target_name`
- `target_kind`

### `variable_refs`

记录变量读写引用。

主要字段：

- `var_name`
- `access_type`

### `edges`

记录过程之间和过程与目标对象之间的关系边。

主要字段：

- `edge_type`
- `source_name`
- `target_name`
- `target_kind`
- `detail_json`

### `chunks`

按过程内语义块切出来的检索单元。

主要字段：

- `seq`
- `chunk_type`
- `line_start`
- `line_end`
- `statement_start_seq`
- `statement_end_seq`
- `statement_count`
- `anchor_kinds_json`
- `action_names_json`
- `target_names_json`
- `variable_names_json`
- `content`
- `summary_text`

### `chunk_vectors`

为每个语义块保存一份向量，用于块级语义召回。

主要字段：

- `chunk_id`
- `provider`
- `model`
- `dimension`
- `vector_json`

### `blocks`

恢复出的稳定结构块，当前重点覆盖：

- 事务块
- SQL 查询块
- SQL 执行语句
- 失败处理块
- `EXCEPTION` 异常块
- `WHEN_OTHERS` 兜底异常块
- `goto svr_end` 一类退出跳转
- 退出标签
- 记录 / 记录池 / 组件循环块

主要字段：

- `block_type`
- `anchor_name`
- `line_start`
- `line_end`
- `statement_start_seq`
- `statement_end_seq`
- `summary_text`
- `excerpt`
- `action_names_json`
- `target_names_json`
- `table_names_json`
- `variable_names_json`

### `block_edges`

块级关系摘要表，用于快速回答“这个事务块里改了哪些表、调了哪些过程”。

现在也会汇总：

- 跳到了哪个标签
- 是否跳向退出标签
- 当前过程定义了哪些标签

主要字段：

- `block_id`
- `edge_type`
- `target_name`
- `target_kind`
- `detail_json`

### `procedures_fts`

过程级全文索引，主要用于过程名、中文名、路径检索。

### `statements_fts`

语句级全文索引，主要用于动作原文、条件、目标对象、过程上下文检索。

### `actions_fts`

动作级全文索引，主要用于动作名和动作目标检索。

### `edges_fts`

关系级全文索引，主要用于调用目标、表名、目标对象检索。

### `chunks_fts`

语义块级全文索引，主要用于比单条语句更稳定的上下文检索。

### `blocks_fts`

结构块级全文索引，主要用于事务、SQL、失败处理、循环这类结构问题检索。

## 当前边类型

- `calls_procedure`
- `uses_action`
- `reads_table`
- `writes_table`
- `uses_component`
- `writes_variable`
- `uses_target`
- `jumps_to_label`
- `jumps_to_exit`
- `defines_label`

其中 `reads_table / writes_table` 现在不仅来自 DSL 动作目标，也会从这类 SQL 语句中抽取：

- `select ... from ... join ...`
- `update ...`
- `insert into ...`
- `delete from ...`
- `merge into ...`

并且当前还会先尝试恢复动态 SQL 文本，覆盖这些常见模式：

- `@sql_str = "select ..."`
- `hs_strcpy(@sql_str, "...")`
- `sprintf(@sql_str, "select ... from %s", @table_name)`
- `hs_snprintf(@sql_str_tmp, ..., "%s ...", @sql_str_tmp, "...")`

如果能把动态 SQL 还原成具体文本，就继续抽取标准 `reads_table / writes_table`；如果只能恢复到变量级别，则保留原语句和变量关系，留给后续增强版处理。

## 当前检索方式

- 还没有完整块级 AST
- 还没有精确恢复 `if/while/transaction/exception` 的层级结构
- `reads_table/writes_table` 目前基于动作名和目标形态做启发式推断
- 动态 SQL 恢复当前是“最近一次字符串赋值 + 常见格式化函数”的轻量追踪，还不是完整数据流分析
- 检索目前采用：
- `chunks_fts` 块级召回
  - `chunk_vectors` 向量召回
  - 查询前会先做 embedding 空间兼容校验
  - `blocks_fts` 结构块召回
  - FTS5 召回
  - SQL `LIKE` fallback
  - Python 重排
  - 意图感知重排
  - 证据上下文组装
  - 覆盖当前证据的结构块补充
- 证据组装会补一跳过程关系摘要
- 当前已有零依赖的本地向量检索

当前意图感知重排会识别：

- 表 / SQL 问题
- 表写入 / 表读取问题
- 变量赋值 / 参数问题
- 调用链 / 被调用问题
- 失败处理 / 异常路径问题
- 过程 / 服务 / 函数定位问题

## 后续扩展方向

- 增加 `blocks` 表，恢复事务块、异常块、循环块、分支块
- 增加 `symbols` 或 `procedural_targets` 表
- 增加向量索引表或外部向量库映射
- 增加更精确的 `db_access` 表和 SQL 抽取结果

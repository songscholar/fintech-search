# Index Schema

## 目标

这个文档描述当前 SQLite 索引库里每张表的职责，方便后续继续扩展。

数据库样例文件默认会生成到 `examples/uses_codes_index.db`，该文件体积较大，当前不纳入版本控制。

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

## 当前边类型

- `calls_procedure`
- `uses_action`
- `reads_table`
- `writes_table`
- `uses_component`
- `writes_variable`
- `uses_target`

## 当前检索方式

- 还没有完整块级 AST
- 还没有精确恢复 `if/while/transaction/exception` 的层级结构
- `reads_table/writes_table` 目前基于动作名和目标形态做启发式推断
- 检索目前采用：
  - `chunks_fts` 块级召回
  - FTS5 召回
  - SQL `LIKE` fallback
  - Python 重排
  - 证据上下文组装
- 证据组装会补一跳过程关系摘要
- 还没有向量检索

## 后续扩展方向

- 增加 `blocks` 表，恢复事务块、异常块、循环块、分支块
- 增加 `symbols` 或 `procedural_targets` 表
- 增加向量索引表或外部向量库映射
- 增加更精确的 `db_access` 表和 SQL 抽取结果

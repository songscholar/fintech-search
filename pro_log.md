# 项目变更日志

## [1.0.7] - 2026-04-16

### 新增功能

1. **Skills 识别逻辑优化**
   - 优化配置开关识别：识别 char_config_xxx、int_config_xxx、str_config_xxx 等格式的配置变量
   - 优化表操作识别：识别 [宏定义][表名字/sql语句][执行结果] 格式的表操作
   - 优化错误信息识别：识别 [业务报错返回][ERR_xxx] 格式的错误信息
   - 更新 uses-codebase-multi-index/SKILL.md 中的识别逻辑

### 修改的文件

- `skills/uses-codebase-multi-index/SKILL.md`: 
  - 更新配置开关识别逻辑，从纯数字改为 char_config_xxx、int_config_xxx、str_config_xxx 等格式
  - 新增表操作识别：识别 [宏定义][表名字/sql语句][执行结果] 格式
  - 新增错误信息识别：识别 [业务报错返回][ERR_xxx] 格式
  - 优化多索引查询工作流的分析步骤

### 技术细节

1. **配置开关识别优化**
   - 之前：纯数字识别（如 "3674"）
   - 现在：识别 char_config_xxx、int_config_xxx、str_config_xxx 等格式（如 "str_config_3588"、"int_config_1234"）
   - 提高了配置变量识别的准确性和针对性

2. **表操作识别新增**
   - 识别模式：[宏定义][表名字/sql语句][执行结果]
   - 示例：[查询表][uses_stkcode][查询成功]
   - 帮助系统准确识别表的增删改查操作

3. **错误信息识别优化**
   - 识别模式：[业务报错返回][ERR_xxx]
   - 示例：[业务报错返回][ERR_USER_TABLERECORD_NOTEXISTS]
   - 提高了错误信息识别的准确性

## [1.0.6] - 2026-04-16

### 新增功能

1. **搜索权重优化 - 提高功能号、英文名、中文名的匹配权重**
   - 功能号（object_id）完全匹配：100分
   - 英文名（procedure_name）完全匹配：100分
   - 中文名（chinese_name）匹配：90分
   - 确保搜索功能号、英文名、中文名时，对应的文件优先显示

2. **修复查询结果字段显示**
   - 修复 `_row_to_hit` 函数，添加 `chinese_name` 和 `object_id` 字段
   - 确保查询结果中正确显示文件的中文名和功能号

### 修改的文件

- `src/uses_indexer/indexer.py`: 
  - 修复 `_row_to_hit` 函数，添加 chinese_name 和 object_id 字段处理
  - 增加 object_id 匹配的权重（100分）
  - 增加 procedure_name 完全匹配的权重（100分）
  - 增加 chinese_name 匹配的权重（90分）

### 技术细节

1. **搜索权重优化**
   - `object_id_exact_match`: 当查询与文件的功能号完全匹配时，增加100分
   - `procedure_name_exact_match`: 当查询与文件的英文名完全匹配时，增加100分
   - `chinese_name_match`: 当查询与文件的中文名匹配时，增加90分
   - 这些权重远高于代码中出现的匹配（通常10-20分），确保文件信息匹配优先于代码引用匹配

2. **字段显示修复**
   - 修复 `_row_to_hit` 函数，使用 `row.keys()` 检查字段是否存在
   - 确保 `chinese_name` 和 `object_id` 字段在查询结果中正确显示
   - 保持向后兼容，不影响现有功能

## [1.0.5] - 2026-04-15

### 新增功能

1. **完善的索引构建脚本 build_indexes.py**
   - 创建统一的索引构建脚本，支持 6 种构建模式
   - 支持分别构建单个索引（code/metadata/table/full）
   - 支持一次构建三个专用索引（three 模式：code + metadata + table）
   - 支持构建所有四个索引（all 模式）
   - 实时监控 SQLite WAL 文件大小变化
   - 完善的异常处理，单个索引失败不影响其他索引
   - 详细的构建结果汇总显示

2. **文档全面更新 - 索引构建指南**
   - 更新 QUICKSTART.md，详细说明三种构建场景
   - 更新 USAGE.md，添加完整的索引构建指南
   - 包含模式说明表格、使用场景推荐、输出说明

### 修改的文件

- `build_indexes.py`: 完善的索引构建脚本，支持多种模式和异常处理
- `docs/QUICKSTART.md`: 更新构建索引章节，添加便捷脚本使用说明
- `docs/USAGE.md`: 添加索引构建指南章节

### 技术细节

1. **构建模式说明**
   - `code`: 仅构建代码索引
   - `metadata`: 仅构建元数据索引
   - `table`: 仅构建表结构索引
   - `three`: 一次构建代码、元数据、表结构三个专用索引
   - `full`: 仅构建全量索引（包含代码+元数据）
   - `all`: 构建所有四个索引

2. **脚本特性**
   - 自动删除旧索引文件
   - 后台线程实时监控 WAL 文件大小
   - safe_build 包装器确保单个索引失败不影响整体
   - 构建结果汇总显示成功/失败状态

## [1.0.4] - 2026-04-15

### 新增功能

1. **表结构索引增强 - 补充表空间和存储介质字段**
   - 在 TableStructure 数据类中新增字段：
     - data_storage_medium: 数据存储介质
     - index_space: 索引表空间
     - history_space: 历史表空间
     - history_index_space: 历史索引表空间
     - archive_space: 归档表空间
     - archive_index_space: 归档索引表空间
   - 新增 load_tablespace_relations() 方法，从 mdbobject.mdbobject 文件加载表空间关系
   - 更新数据库表结构，新增对应字段
   - 更新全文搜索表，添加表空间相关字段到 FTS 索引
   - 支持通过表空间信息进行检索

2. **添加表结构索引 CLI 命令**
   - 新增 `build-table-index` 命令，用于构建表结构索引
   - 新增 `query-table-index` 命令，用于查询表结构索引
   - 支持通过 --stdfield 参数加载标准字段定义
   - 支持通过 --mdbobject 参数加载表空间关系配置

3. **文档更新 - 说明四种索引类型**
   - 更新 INDEX_SCHEMA.md，添加表结构索引的表结构说明
   - 更新 QUICKSTART.md，添加四种索引类型的构建方法
   - 更新 USAGE.md，添加四种索引类型的使用说明

### 修改的文件

- `src/uses_indexer/table_parser.py`: 新增表空间字段和加载方法
- `src/uses_indexer/table_indexer.py`: 更新数据库表结构和插入逻辑
- `src/uses_indexer/cli.py`: 添加 build-table-index 和 query-table-index 命令
- `docs/INDEX_SCHEMA.md`: 添加表结构索引说明
- `docs/QUICKSTART.md`: 添加四种索引类型构建方法
- `docs/USAGE.md`: 添加四种索引类型使用说明
- `.gitignore`: 更新忽略文件规则

### 技术细节

1. **表空间关系加载**
   - 从 mdbobject.mdbobject 文件解析表空间关系配置
   - 支持主表空间、索引表空间、历史表空间、归档表空间的关联
   - 根据表的 space 属性自动匹配对应的表空间关系

2. **数据库表结构更新**
   - tables 表新增 6 个表空间相关字段
   - tables_fts 全文搜索表新增表空间字段支持
   - 保持向后兼容，现有功能不受影响

3. **四种索引类型**
   - **全量索引 (all)**: 包含所有文件（代码+元数据）
   - **代码索引 (code)**: 仅包含代码文件
   - **元数据索引 (metadata)**: 仅包含元数据文件
   - **表结构索引**: 包含表结构信息

## [1.0.3] - 2026-04-15

### 新增功能

1. **排除不需要识别的文件夹**
   - 在 indexer.py 中添加文件夹排除逻辑
   - 排除的文件夹包括：通用数据、commondata、tools
   - 确保这些文件夹不会被索引，提高索引效率

### 修改的文件

- `src/uses_indexer/indexer.py`: 添加文件夹排除逻辑

### 技术细节

1. **文件过滤逻辑**
   - 在文件遍历过程中排除包含指定文件夹名称的路径
   - 排除的文件夹：通用数据、commondata、tools
   - 适用于所有索引类型（all、code、metadata）

## [1.0.2] - 2026-04-15

### 新增功能

1. **支持 .extinterface 格式外部接口文件**
   - 在 parser.py 中添加 .extinterface 到 SUPPORTED_CODE_SUFFIXES
   - 更新 indexer.py 中的 is_code_path() 函数，确保外部接口文件被识别为代码文件
   - 更新 indexer.py 中的 is_metadata_path() 函数，确保外部接口文件不被识别为元数据文件
   - 支持 RPC 调用识别，通过中文文件名调用外部接口时会被标记为远程调用

### 修改的文件

- `src/uses_indexer/parser.py`: 添加 .extinterface 到支持的代码后缀列表
- `src/uses_indexer/indexer.py`: 更新文件类型判断函数，支持 .extinterface 文件

### 技术细节

1. **文件过滤逻辑**
   - `is_code_path()`: 识别 .uftfunction、.uftservice、.uftatomfunction、.uftfactorservice、.extinterface 文件
   - `is_metadata_path()`: 识别路径包含 "metadata" 且非代码文件的文件

2. **RPC 调用识别**
   - 外部接口文件（.extinterface）被视为远程服务
   - 当代码中使用中文文件名调用这些接口时，会被识别为 RPC 调用
   - 支持追踪从核心服务到其他服务/应用的远程调用链路

## [1.0.1] - 2026-04-15

### 新增功能

1. **支持分离式索引构建**
   - 新增 `--index-type` 参数，支持 `all`（默认）、`code`、`metadata` 三种索引类型
   - 实现代码文件与元数据文件的分离索引，避免检索混淆
   - 代码索引文件名建议：`business_code_index.db`
   - 元数据索引文件名建议：`business_metadata_index.db`

2. **支持 .uftfactorservice 格式文件**
   - 确认 parser.py 中已支持 .uftfactorservice 格式
   - 更新 indexer.py 中的文件过滤逻辑
   - 确保代码索引类型包含 .uftfactorservice 文件

### 修改的文件

- `src/uses_indexer/cli.py`: 添加 `--index-type` 参数
- `src/uses_indexer/indexer.py`: 实现索引类型过滤逻辑，更新文件类型判断函数

### 使用示例

```bash
# 构建代码专用索引
PYTHONPATH=src python3 -m uses_indexer build-index \
  /path/to/code \
  --db examples/business_code_index.db \
  --index-type code

# 构建元数据专用索引
PYTHONPATH=src python3 -m uses_indexer build-index \
  /path/to/code \
  --db examples/business_metadata_index.db \
  --index-type metadata

# 构建完整索引（默认行为）
PYTHONPATH=src python3 -m uses_indexer build-index \
  /path/to/code \
  --db examples/business_full_index.db \
  --index-type all
```

### 技术细节

1. **文件过滤逻辑**
   - `is_code_path()`: 识别 .uftfunction、.uftservice、.uftatomfunction、.uftfactorservice 文件
   - `is_metadata_path()`: 识别路径包含 "metadata" 且非代码文件的文件

2. **向后兼容**
   - 默认保持 `--index-type all` 行为
   - 所有现有 API 和功能保持不变
   - 新参数仅影响文件选择范围

## [1.0.0] - 2026-04-15（初始版本）

### 初始功能

- 完整的 USES/UFT DSL 代码解析
- SQLite 索引构建与管理
- FTS 全文搜索和向量检索
- 调用链分析和语义块切分
- CLI、HTTP API、MCP Server 等多种接口

## [1.1.0] - 2026-04-20

### 提交记录

- `3be9ba8` `Refactor indexer into layered services and add incremental indexing`
- `d8f5038` `Add remaining project updates and utilities`
- `543d81d` `Add structured observability traces`
- `c335e7e` `Extract evidence context fetch service`
- `a973ed2` `Remove duplicated retrieval logic from indexer`

### 本轮核心改动

1. **重构 `indexer.py`，开始按职责分层**
   - 新增模块：
     - `src/uses_indexer/index_build.py`
     - `src/uses_indexer/retrieval.py`
     - `src/uses_indexer/rerank.py`
     - `src/uses_indexer/evidence.py`
     - `src/uses_indexer/semantic_recovery.py`
     - `src/uses_indexer/index_catalog.py`
     - `src/uses_indexer/answer_strategy.py`
   - `SQLiteIndexer` 逐步退化为门面层，建库、检索、证据组装、语义恢复开始迁移到独立服务模块。

2. **新增增量建库能力**
   - `build-index` 支持 `--incremental`
   - 新增 `indexed_files` 状态表，记录文件指纹
   - 支持按文件变更识别 `added / changed / removed`
   - 仅重建受影响的索引数据，并补齐缺失向量

3. **统一索引边界和默认库语义**
   - 新增 `docs/INDEX_BOUNDARIES.md`
   - 明确区分：
     - `business_code_index.db`：代码检索默认库
     - `business_metadata_index.db`：元数据检索库
     - `business_full_index.db`：代码 + 元数据综合库
     - `business_table_index.db`：表结构索引库
   - 更新 `README.md`、`docs/USAGE.md`、`docs/DEPLOYMENT.md` 文档口径

4. **增强检索可观测性**
   - 新增 `src/uses_indexer/observability.py`
   - `query-index` / `assemble-evidence` / API / MCP 支持稳定结构化 debug 输出
   - trace 中统一包含：
     - `schema`
     - `version`
     - `trace.stage`
     - query analysis
     - retrieval contributions
     - rerank preview
     - evidence pruning
     - incremental build change report

5. **继续拆分证据查询上下文逻辑**
   - 新增 `src/uses_indexer/context_fetch.py`
   - 从 `indexer.py` 中迁出：
     - `_fetch_context_block`
     - `_fetch_chunk_block`
     - `_fetch_block_context`
     - `_fetch_covering_blocks`
     - `_fetch_related_context`
     - 调用链邻居、别名解析、相关 procedure 摘要查询等辅助逻辑
   - `indexer.py` 保留薄封装，实际 SQL 查询由 `ContextFetchService` 负责

6. **清理旧的重复检索实现**
   - 删除 `indexer.py` 中与 `retrieval.py` 重复的一整套旧检索代码
   - 避免两份检索逻辑后续漂移，降低维护风险
   - `indexer.py` 文件规模从约 `4700+` 行逐步收缩到约 `3157` 行

7. **回答层策略升级**
   - `llm.py` 增加 provider / timeout / retry / backoff 配置能力
   - `answering.py` 接入 `AdaptiveAnswerStrategy`
   - 支持按问题类型切换回答 profile，并在回答前做一定的 evidence compression

### 本轮新增/重点文件

- `src/uses_indexer/observability.py`
- `src/uses_indexer/context_fetch.py`
- `src/uses_indexer/index_build.py`
- `src/uses_indexer/retrieval.py`
- `src/uses_indexer/evidence.py`
- `src/uses_indexer/rerank.py`
- `src/uses_indexer/semantic_recovery.py`
- `src/uses_indexer/answer_strategy.py`
- `docs/INDEX_BOUNDARIES.md`

### 验证结果

- `python3 -m py_compile src/uses_indexer/*.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_indexer.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_embeddings.py` 通过
- 本轮多次拆分后继续验证：
  - `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_cli.py`
  - 结果：`41 passed`

### 风险与结论

- 本轮重构主要是“职责迁移”和“结构化输出”升级，没有主动调整核心检索策略
- 中途发现一次调用语义标签字段搬迁遗漏，已通过测试修复
- 最终验证结果表明：
  - 检索质量未出现回退
  - 证据组装行为保持稳定
  - 模块边界更加清晰，后续继续拆分的风险更可控

## [1.1.1] - 2026-04-20

### Step 1: 继续拆分 `indexer.py` 的写库/建库 helper

### 本步目标

- 将 `indexer.py` 中剩余的大块写库逻辑继续下沉
- 保持外部方法名和行为不变，先做“服务委托”式拆分
- 继续降低 `SQLiteIndexer` 作为“上帝对象”的复杂度

### 本步改动

1. 新增 `src/uses_indexer/index_write.py`
   - 新增 `IndexWriteService`
   - 负责承接以下写库/建库相关逻辑：
     - `insert_unit`
     - `insert_statements`
     - `insert_chunks`
     - `populate_missing_chunk_vectors`
     - `insert_blocks`
     - `insert_variable_refs`
     - `insert_action_and_edges`
     - `insert_edge`
     - block 内部辅助查询

2. `src/uses_indexer/indexer.py`
   - 新增 `_index_write_service` 成员
   - 为 `_json / _maybe_int / _paths_match / _embedder_batch_size / _derive_target / _metadata_edges_for_statement / _classify_call_semantics / _classify_mc_publish` 增加薄包装方法，供写库服务复用
   - 将原有写库/建库相关方法改为委托到 `IndexWriteService`

### 效果

- `indexer.py` 从约 `3157` 行进一步压缩到约 `2502` 行
- 写库层职责边界比之前清晰很多
- 后续如果继续拆 `index_build` / persistence / semantic rules，会更容易推进

### 验证

- `python3 -m py_compile src/uses_indexer/index_write.py src/uses_indexer/indexer.py src/uses_indexer/index_build.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py` 通过
- 结果：`41 passed`

### 结论

- 这是一次纯结构性重构，没有主动修改检索策略
- 测试结果表明行为稳定，没有引入回归

## [1.1.2] - 2026-04-20

### Step 2: 统一 observability 出口并补 trace schema 文档

### 本步目标

- 给 retrieval / evidence / incremental build trace 增加统一 envelope
- 明确 CLI / API / MCP 的 debug 输出共用同一套结构
- 补一份正式的 trace schema 文档，方便后续排障和对接

### 本步改动

1. 更新 `src/uses_indexer/observability.py`
   - 所有 trace 增加统一 `metadata` 字段
   - `metadata` 包含：
     - `trace_id`
     - `producer`
     - `schema`
     - `version`
     - `generated_at`
   - retrieval / evidence / incremental build 统一使用 versioned trace envelope

2. 新增文档 `docs/TRACE_SCHEMA.md`
   - 明确说明三类 trace：
     - `uses_indexer.debug.retrieval`
     - `uses_indexer.debug.evidence`
     - `uses_indexer.debug.incremental_build`
   - 说明 CLI / API / MCP 的复用关系
   - 说明消费端应以 `schema + version` 作为兼容性判断依据

3. 更新测试
   - 补充 metadata 相关断言
   - 确认 retrieval / evidence / incremental build trace 均带统一 envelope

### 验证

- `python3 -m py_compile src/uses_indexer/observability.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- 结果：`36 passed`

### 结论

- debug 输出已经不只是“能看”，而是开始具备稳定消费的基础
- 后续不论是命令行排障、HTTP 接口接入，还是 MCP 诊断，都可以围绕统一 trace schema 展开

## [1.1.3] - 2026-04-20

### Step 3: 增强增量建库影响范围与变更报告

### 本步目标

- 让增量建库不仅返回文件级变更，还返回受影响的业务对象信息
- 帮助定位“这次增量到底动了哪些 procedure / unit”
- 为后续更细粒度的增量分析铺路

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 为增量建库新增 `incremental_impact`
   - 引入：
     - `_build_incremental_impact_report`
     - `_describe_source_unit`
     - `_describe_indexed_unit`
   - 现在对 `added / changed / removed` 三类文件，会生成对应的受影响 unit 描述
   - 影响信息包括：
     - `change_type`
     - `file_path`
     - `procedure_name`
     - `unit_kind`
     - `prefix`
     - `chinese_name`
     - `object_id`

2. 更新 `src/uses_indexer/observability.py`
   - 在 `incremental_trace.trace` 下新增 `impact`
   - 提供：
     - `affected_unit_count`
     - `affected_units`

3. 更新测试
   - 校验 `incremental_impact`
   - 校验 `incremental_trace.trace.impact`

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py src/uses_indexer/observability.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py::test_build_index_supports_incremental_updates tests/test_indexer.py::test_query_index_debug_includes_retrieval_trace tests/test_indexer.py::test_assemble_evidence_debug_includes_pruning_trace` 通过
- 结果：`3 passed`

### 结论

- 增量建库的调试视角已经从“文件级别”提升到“业务对象级别”
- 后续如果继续做更细粒度的局部重建，这一步会是非常关键的基础

## [1.1.4] - 2026-04-20

### Step 4: 补 retrieval / evidence 质量评测

### 本步目标

- 让评测不只覆盖 retrieval 命中，还覆盖 evidence 组装质量
- 增加按问题标签拆分的统计视角
- 帮助更快识别“检索命中了，但证据不够回答问题”的回归

### 本步改动

1. 更新 `src/uses_indexer/evaluation.py`
   - 在 case 级评测中加入 `assemble_evidence(...)`
   - 为每个 case 产出：
     - `evidence.evidence_count`
     - `evidence.matched_count`
     - `evidence.coverage`
     - `evidence.expectations`
     - `evidence.top_evidence`
   - 新增按 evidence block 匹配 expectation 的逻辑
   - 在 summary 中新增：
     - `evidence_coverage`
     - `by_tag`

2. 更新 `tests/test_evaluation.py`
   - 覆盖 summary 级 `evidence_coverage`
   - 覆盖 `by_tag`
   - 覆盖 case 级 `evidence.coverage`

### 验证

- `python3 -m py_compile src/uses_indexer/evaluation.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py` 通过
- 结果：`4 passed`

### 结论

- 评测体系已经从“检索是否命中”扩展到“证据是否足够支撑回答”
- 后续如果 rerank 或 evidence 选择发生回归，现在会更容易被评测发现

## [1.1.5] - 2026-04-20

### Step 5: 统一语义规则定义与测试入口

### 本步目标

- 把调用语义和消息发布语义收拢成单一规则源
- 避免 `indexer / context_fetch / evidence` 各自维护一套重复逻辑
- 增加独立的语义规则测试入口，降低后续改规则的回归风险

### 本步改动

1. 更新 `src/uses_indexer/semantic_recovery.py`
   - 新增统一语义规则常量：
     - `LOCAL_CALL_RULES`
     - `RPC_CALL_RULES`
     - `SEMANTIC_RULE_REGISTRY`
   - 新增公共语义 helper：
     - `classify_call_semantics`
     - `coerce_call_semantics`
     - `classify_mc_publish`
     - `format_call_edge_label`
     - `format_mc_topic_label`
   - 将 MC publish 语义补齐为统一结构，包含：
     - `communication_kind`
     - `communication_label`

2. 更新消费模块
   - `src/uses_indexer/context_fetch.py` 改为直接复用统一 call semantics
   - `src/uses_indexer/evidence.py` 改为直接复用统一 label formatter
   - `src/uses_indexer/indexer.py` 改为直接复用统一规则源，并在 `summarize_db()` 中暴露：
     - `semantic_rule_registry`

3. 新增测试入口 `tests/test_semantic_rules.py`
   - 直接校验规则注册表
   - 直接校验 call semantics helper
   - 直接校验 MC publish helper
   - 校验 summary 中暴露的规则信息

### 验证

- `python3 -m py_compile src/uses_indexer/semantic_recovery.py src/uses_indexer/context_fetch.py src/uses_indexer/evidence.py src/uses_indexer/indexer.py tests/test_semantic_rules.py` 通过
- `PYTHONPATH=. pytest -q tests/test_semantic_rules.py tests/test_indexer.py -k "call_semantics or mc_publish or related_context_exposes_call_semantics_labels or related_context_exposes_mc_published_topics"` 通过
- 结果：`5 passed`

### 结论

- 语义规则现在已经有明确的“单一事实来源”
- 后续如果要扩充调用类型、消息发布类型或规则标签，改动范围会明显更小

## [1.1.6] - 2026-04-20

### Step 6: 清理历史遗留 helper 与死代码

### 本步目标

- 删除 `indexer.py` 中已经被新模块替代、但仍然残留的旧 helper
- 降低“同一能力有两套实现”的维护风险
- 继续把 `indexer.py` 收缩成更明确的门面角色

### 本步改动

1. 清理 `src/uses_indexer/indexer.py`
   - 删除旧的 block recovery helper
   - 删除旧的 SQL access / string hint helper
   - 删除旧的 semantic chunk helper
   - 删除旧的 query intent / rerank helper
   - 删除旧的 excerpt / argument / truncate helper

2. 清理冗余 import 和常量
   - 移除已经迁移到 `semantic_recovery.py`、`rerank.py` 等模块后的重复定义
   - 保留仍被 `IndexWriteService` 等活跃路径使用的最小必要常量

### 验证

- `python3 -m py_compile src/uses_indexer/indexer.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py` 通过
- 结果：`49 passed`

### 结论

- `indexer.py` 本轮净删除 `1057` 行遗留实现
- 文件体量现在降到约 `1340` 行，已经明显更接近“编排门面”而不是“全能大文件”

## [1.1.7] - 2026-04-20

### Step 7: 重构并补全文档入口

### 本步目标

- 把文档整理成更清晰的三条主线：
  - 新手上手
  - 开发扩展
  - 问题排障
- 减少“README 太重、入口不清晰”的问题

### 本步改动

1. 新增文档入口
   - `docs/NEWCOMER_GUIDE.md`
   - `docs/DEVELOPER_GUIDE.md`
   - `docs/TROUBLESHOOTING.md`

2. 更新 `README.md`
   - 补充三条主线文档导航
   - 调整第一次阅读仓库的推荐顺序

### 验证

- 校验 `README.md` 与新文档入口链接
- 确认三条主线文档都已纳入仓库

### 结论

- 文档入口现在已经不再只靠 README 承担
- 新用户、继续开发的人、排障的人都可以直接进入对应路径

## [1.2.1] - 2026-04-20

### Step 8: 增强检索质量评测与趋势统计

### 本步目标

- 让评测报告更像“质量看板”，而不只是 pass/fail 汇总
- 增加 top-hit / top-3 命中质量视角
- 为后续检索和 rerank 调优提供更稳定的趋势指标

### 本步改动

1. 更新 `src/uses_indexer/evaluation.py`
   - 为每个 case 的 `retrieval` 新增：
     - `top_hit_expectation_coverage`
     - `top_three_expectation_coverage`
   - 为 summary 新增：
     - `top_hit_expectation_coverage`
     - `top_three_expectation_coverage`
     - `avg_candidate_count`
     - `avg_evidence_count`
   - 为 `compare_eval_reports()` 新增上述质量指标的 delta 对比

2. 更新 `tests/test_evaluation.py`
   - 覆盖新的 summary 质量指标
   - 覆盖 case 级 top-hit 质量指标
   - 覆盖 compare report 的质量指标 delta

### 验证

- `python3 -m py_compile src/uses_indexer/evaluation.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py` 通过
- 结果：`5 passed`

### 结论

- 评测现在已经不仅能回答“有没有命中”，还可以回答“最前面的命中质量如何”
- 后续 rerank 或 evidence 选择发生轻微退化时，会更容易被看板指标发现

## [1.2.2] - 2026-04-20

### Step 9: 升级 observability 为更稳定的诊断能力

### 本步目标

- 让 trace 不只是“结构化输出”，而是开始具备链路诊断能力
- 增加阶段耗时、父子 trace 关联和阶段摘要
- 帮助排障时更快看出“这一段到底做了什么”

### 本步改动

1. 更新 `src/uses_indexer/observability.py`
   - `metadata` 支持：
     - `parent_trace_id`
   - retrieval / evidence / incremental trace 新增：
     - `trace.elapsed_ms`
     - `trace.summary`

2. 更新调用方
   - `src/uses_indexer/retrieval.py` 记录 retrieval 阶段耗时
   - `src/uses_indexer/evidence.py` 记录 evidence 阶段耗时，并把 evidence trace 关联到 retrieval trace
   - `src/uses_indexer/index_build.py` 记录 incremental build 阶段耗时

3. 更新测试
   - 校验 retrieval / evidence / incremental trace 的新字段
   - 校验 `parent_trace_id`

### 验证

- `python3 -m py_compile src/uses_indexer/observability.py src/uses_indexer/retrieval.py src/uses_indexer/evidence.py src/uses_indexer/index_build.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py -k "query_index_debug_includes_retrieval_trace or assemble_evidence_debug_includes_pruning_trace or build_index_supports_incremental_updates"` 通过
- 结果：`3 passed`

### 结论

- trace 现在已经开始形成一条可串联的诊断链
- 排障时不仅能看“结果是什么”，还能看“这一阶段花了多久、处理了多少对象”

## [1.2.3] - 2026-04-20

### Step 10: 细化增量建库到更小影响范围

### 本步目标

- 让增量建库从“文件变更”进一步提升到“重建作用域”视角
- 直接看到本次重建涉及哪些 procedure，以及对应多少 statements / chunks / blocks
- 为后续继续推进真正的局部重建提供基础数据

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 新增：
     - `_describe_index_scope`
     - `_build_rebuild_scope_report`
   - 增量建库现在会同时生成：
     - `incremental_scope.summary`
     - `incremental_scope.items`
   - 每个作用域项包含：
     - `change_type`
     - `procedure_name`
     - `before`
     - `after`
   - `before / after` 中包含：
     - `statement_count`
     - `action_count`
     - `chunk_count`
     - `block_count`
     - `edge_count`

2. 更新 `src/uses_indexer/observability.py`
   - 在 `incremental_trace.trace` 下新增：
     - `rebuild_scope`
   - 在 trace summary 中加入：
     - `after_chunk_count`
     - `after_block_count`

3. 更新测试
   - 校验 `incremental_scope`
   - 校验 trace 中的 `rebuild_scope`

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py src/uses_indexer/observability.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py::test_build_index_supports_incremental_updates` 通过
- 结果：`1 passed`

### 结论

- 增量建库现在已经不只告诉你“哪些文件变了”，还会告诉你“这次到底重建了哪些过程和多少索引对象”
- 这一步让后续继续做更细粒度局部重建时，具备了更清晰的作用域基线

## [1.2.4] - 2026-04-20

### Step 11: 完善索引与回答策略配置层

### 本步目标

- 把 QA 和回答层的默认策略从隐式参数提升成显式配置对象
- 为后续接入 `.env` 与统一常量配置做准备
- 保持默认行为不变，但让覆盖策略更清晰

### 本步改动

1. 新增 `src/uses_indexer/strategy_config.py`
   - `QaPolicy`
   - `AnswerExecutionPolicy`
   - `PromptProfileConfig`
   - `AnswerStrategyConfig`

2. 更新回答策略层
   - `src/uses_indexer/answer_strategy.py` 改为使用 `AnswerStrategyConfig`
   - `src/uses_indexer/qa.py` 支持注入 `QaPolicy`
   - `src/uses_indexer/answering.py` 支持注入 `AnswerExecutionPolicy`

3. 更新测试
   - 覆盖 QA policy 默认值注入
   - 覆盖自定义 prompt profile
   - 覆盖 fallback policy

### 验证

- `python3 -m py_compile src/uses_indexer/strategy_config.py src/uses_indexer/answer_strategy.py src/uses_indexer/qa.py src/uses_indexer/answering.py` 通过
- `PYTHONPATH=. pytest -q tests/test_qa.py tests/test_answering.py` 通过
- 结果：`8 passed`

### 结论

- 回答层和 QA 层现在已经具备更明确的策略对象边界
- 后续如果要接环境变量、配置文件或不同问题类型的策略切换，代码会更容易扩展

## [1.2.5] - 2026-04-20

### Step 12: 统一 API / MCP 公共返回 schema

### 本步目标

- 让核心返回对象在 CLI / HTTP / MCP 三个入口之间保持稳定识别键
- 避免消费端只能靠“猜字段”判断当前拿到的是 query / evidence / ask / answer / summary 哪种结果

### 本步改动

1. 新增 `src/uses_indexer/response_schema.py`
   - `apply_response_envelope`
   - `RESPONSE_SCHEMA_VERSION`

2. 更新核心返回
   - `query_index()` 返回：
     - `response_schema`
     - `response_version`
     - `response_kind=query`
   - `assemble_evidence()` 返回：
     - `response_kind=evidence`
   - `qa.ask()` 返回：
     - `response_kind=ask`
   - `answer()` 返回：
     - `response_kind=answer`
   - `summarize_db()` 返回：
     - `response_kind=db_summary`

3. 更新测试
   - API 测试覆盖 response kind
   - MCP 测试覆盖 response kind

### 验证

- `python3 -m py_compile src/uses_indexer/response_schema.py src/uses_indexer/retrieval.py src/uses_indexer/evidence.py src/uses_indexer/qa.py src/uses_indexer/answering.py src/uses_indexer/indexer.py` 通过
- `PYTHONPATH=. pytest -q tests/test_api.py tests/test_mcp.py tests/test_qa.py tests/test_answering.py` 通过
- 结果：`13 passed`

### 结论

- 现在消费端至少可以通过稳定的 envelope 字段直接识别返回类型
- 这为后续继续统一 API / MCP 的公共 schema 打下了基础

## [1.2.6] - 2026-04-20

### Step 13: 补充检索调优与 DSL 语义扩展文档

### 本步目标

- 给后续继续演进检索质量和语义规则的人提供更直接的入口文档
- 把前面新增的评测、trace、语义规则统一起来

### 本步改动

1. 新增文档
   - `docs/RETRIEVAL_TUNING.md`
   - `docs/SEMANTIC_RULES_EXTENSION.md`

2. 更新 `README.md`
   - 增加上述两份文档导航入口

### 验证

- 校验 README 与新文档入口链接
- 确认新文档已纳入仓库

### 结论

- 现在“调检索”和“扩语义规则”都已经有单独文档入口
- 后续继续迭代时，开发说明会比原来更聚焦

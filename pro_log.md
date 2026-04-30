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

## [1.1.8] - 2026-04-20

### Step 8: 细化增量建库重建目标

### 本步目标

- 让增量建库输出不只告诉我们“哪个 unit 受影响”
- 还直接告诉我们“这次预计要重建多少 statement / chunk / block / vector target”

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 为 `added / changed` 文件增加源码侧 scope 估算
   - 为 `removed` 文件复用索引侧 scope 统计
   - 在 `incremental_impact.affected_units` 中新增：
     - `rebuild_targets`
   - 在 `incremental_scope.items` 中也补齐：
     - `rebuild_targets`
   - 在 `incremental_scope.summary` 中新增：
     - `rebuild_target_statement_count`
     - `rebuild_target_chunk_count`
     - `rebuild_target_block_count`
     - `after_vector_target_count`

2. 更新 `src/uses_indexer/observability.py`
   - 在 `incremental_trace.trace.summary` 中增加重建目标统计字段

3. 更新测试
   - 校验 `affected_units[].rebuild_targets`
   - 校验 `incremental_scope.summary`
   - 校验 `incremental_trace.trace.summary`

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py src/uses_indexer/observability.py tests/test_indexer.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py::test_build_index_supports_incremental_updates tests/test_indexer.py::test_query_index_debug_includes_retrieval_trace tests/test_indexer.py::test_assemble_evidence_debug_includes_pruning_trace` 通过
- 结果：`3 passed`

### 结论

- 增量建库现在已经能回答“本次改动大概要重建多少内容”
- 这为后面继续往 procedure / chunk / block 级局部重建推进打下了更直接的基础

## [1.1.9] - 2026-04-20

### Step 9: 补 `.env` 配置入口与集中常量模块

### 本步目标

- 让运行时配置支持项目根目录 `.env`
- 把部分散落的运行时常量收口到统一模块
- 避免环境变量逻辑继续散落在 `llm.py / embeddings.py / cli.py / mcp_server.py / retrieval.py / indexer.py`

### 本步改动

1. 新增 `src/uses_indexer/config.py`
   - 支持自动发现并加载项目根目录 `.env`
   - 支持 `USES_INDEXER_ENV_FILE` 指定自定义 env 文件

2. 新增 `src/uses_indexer/constants.py`
   - 集中管理：
     - `READ_ACTIONS`
     - `WRITE_ACTIONS`
     - `COMPONENT_ACTIONS`
     - `VECTOR_SIMILARITY_THRESHOLD`
     - `JSON_RPC_VERSION`
     - `MCP_PROTOCOL_VERSION`

3. 更新运行时模块
   - `llm.py` 与 `embeddings.py` 现在会先 bootstrap `.env`
   - `cli.py` 启动时也会先 bootstrap `.env`
   - `retrieval.py`、`mcp_server.py`、`indexer.py` 改为复用集中常量

4. 新增 `.env.example`
   - 提供 LLM 与 embedding 的项目内配置模板

5. 更新测试与文档
   - 新增 `tests/test_config.py`
   - 补 `.env` 自动加载测试
   - 补集中常量测试
   - 更新 `README.md` 与 `docs/DEPLOYMENT.md`

### 验证

- `python3 -m py_compile src/uses_indexer/config.py src/uses_indexer/constants.py src/uses_indexer/llm.py src/uses_indexer/embeddings.py src/uses_indexer/cli.py src/uses_indexer/retrieval.py src/uses_indexer/mcp_server.py src/uses_indexer/indexer.py tests/test_config.py tests/test_answering.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_config.py tests/test_embeddings.py tests/test_answering.py tests/test_mcp.py` 通过
- 结果：`19 passed`

### 结论

- 项目现在已经可以直接用仓库内 `.env` 驱动运行时配置
- 关键运行时常量也开始有统一落点，后续继续收口会更顺手

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

## [1.2.7] - 2026-04-20

### Step 14: 继续集中 query / rerank / schema 常量

### 本步目标

- 进一步减少“同一类常量散落在多个模块”的情况
- 让 query intent、rerank 词表、response schema 和评测默认值都从统一常量层读取

### 本步改动

1. 更新 `src/uses_indexer/constants.py`
   - 新增 `RESPONSE_SCHEMA_VERSION`
   - 新增 `DEFAULT_TOP_K`
   - 新增 query / rerank 相关词表与正则：
     - `TABLE_TOKEN_PREFIXES`
     - `TABLE_INTENT_KEYWORDS`
     - `WRITE_INTENT_KEYWORDS`
     - `READ_INTENT_KEYWORDS`
     - `VARIABLE_INTENT_KEYWORDS`
     - `CALL_CHAIN_INTENT_KEYWORDS`
     - `FAILURE_INTENT_KEYWORDS`
     - `PROCEDURE_INTENT_KEYWORDS`
     - `SQL_WRITE_HINTS`
     - `SQL_READ_HINTS`
     - `FAILURE_MATCH_HINTS`
     - `GENERIC_QUERY_TERMS`
     - `FOCUS_EXCLUDED_QUERY_TERMS`
     - `QUERY_TOKEN_RE`
     - `QUERY_PROCEDURE_RE`
     - `QUERY_VARIABLE_RE`
     - `CHINESE_QUERY_SPLIT_RE`

2. 更新 `src/uses_indexer/rerank.py`
   - 删除本地重复常量定义
   - 改为统一从 `constants.py` 导入

3. 更新 `src/uses_indexer/response_schema.py`
   - `RESPONSE_SCHEMA_VERSION` 改为从 `constants.py` 导入

4. 更新 `src/uses_indexer/evaluation.py`
   - `DEFAULT_TOP_K` 改为从 `constants.py` 导入

### 验证

- `python3 -m py_compile src/uses_indexer/constants.py src/uses_indexer/rerank.py src/uses_indexer/response_schema.py src/uses_indexer/evaluation.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py tests/test_indexer.py tests/test_semantic_rules.py` 通过
- 结果：`37 passed`

### 结论

- query intent 和 rerank 关键词不再散落在 `rerank.py` 内部
- response schema 版本与评测默认 top-k 也归到了统一常量入口
- 后续如果继续做配置化或调优，会更容易定位和复用

## [1.2.8] - 2026-04-20

### Step 15: 继续收口共享 regex / trace / semantic 常量

### 本步目标

- 把仍然散落在 `indexer.py`、`semantic_recovery.py`、`observability.py`、`embeddings.py` 里的共享常量继续集中
- 进一步降低 query 规则、trace schema 和语义恢复边界发生漂移的风险

### 本步改动

1. 更新 `src/uses_indexer/constants.py`
   - 新增 `TRACE_SCHEMA_VERSION`
   - 新增 `TRACE_PRODUCER`
   - 新增 `EXIT_LABEL_NAMES`
   - 新增 `TABLE_WITH_INDEX_RE`

2. 更新 `src/uses_indexer/indexer.py`
   - 删除本地重复定义的：
     - `TABLE_WITH_INDEX_RE`
     - `QUERY_TOKEN_RE`
     - `CHINESE_QUERY_SPLIT_RE`
     - `GENERIC_QUERY_TERMS`
     - `EXIT_LABEL_NAMES`
   - 改为统一从 `constants.py` 导入

3. 更新 `src/uses_indexer/semantic_recovery.py`
   - `EXIT_LABEL_NAMES`
   - `TABLE_WITH_INDEX_RE`
   - 改为统一从 `constants.py` 导入

4. 更新 `src/uses_indexer/observability.py`
   - `TRACE_SCHEMA_VERSION`
   - `TRACE_PRODUCER`
   - 改为统一从 `constants.py` 导入

5. 更新 `src/uses_indexer/embeddings.py`
   - 复用 `QUERY_TOKEN_RE` 作为 token 正则来源

### 验证

- `python3 -m py_compile src/uses_indexer/constants.py src/uses_indexer/indexer.py src/uses_indexer/semantic_recovery.py src/uses_indexer/observability.py src/uses_indexer/embeddings.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py tests/test_mcp.py` 通过
- 结果：`48 passed`

### 结论

- 共享 query / semantic / trace 常量进一步收敛到了单一入口
- `indexer.py` 内的历史重复定义又减少了一批
- 后续继续调 query token、exit label 或 trace schema 时，维护成本会更低

## [1.2.9] - 2026-04-21

### Step 16: 抽离 indexer 通用 helper 到独立工具模块

### 本步目标

- 继续压缩 `indexer.py`，把纯工具型 helper 从核心门面中迁出
- 消除 `indexer.py` 与 `retrieval.py` / `context_fetch.py` 之间的重复实现

### 本步改动

1. 新增 `src/uses_indexer/index_utils.py`
   - 收口通用 helper：
     - `maybe_int`
     - `embedder_batch_size`
     - `paths_match`
     - `json_dumps`
     - `json_loads_object`
     - `dedupe_strings`
     - `build_fts_query`
     - `tokenize_query`
     - `merge_candidate`

2. 更新 `src/uses_indexer/retrieval.py`
   - 改为直接复用 `build_fts_query`
   - 改为直接复用 `merge_candidate`
   - 不再通过 `SQLiteIndexer` 门面绕转这两个 helper

3. 更新 `src/uses_indexer/context_fetch.py`
   - 改为复用 `json_loads_object`
   - 删除本地重复 `_json_loads`

4. 更新 `src/uses_indexer/indexer.py`
   - 门面层改为复用 `index_utils.py` 中的：
     - `json_dumps`
     - `json_loads_object`
     - `maybe_int`
     - `paths_match`
     - `embedder_batch_size`
   - 删除已迁出的旧 helper：
     - `_row_to_hit`
     - `_merge_candidate`
     - `_build_fts_query`
     - `_tokenize_query`
     - `_public_hit`
     - `_maybe_int`
     - `_embedder_batch_size`
     - `_paths_match`
     - `_json`
     - `_json_loads`
     - `_dedupe_strings`

### 验证

- `python3 -m py_compile src/uses_indexer/index_utils.py src/uses_indexer/retrieval.py src/uses_indexer/context_fetch.py src/uses_indexer/indexer.py src/uses_indexer/index_write.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- `indexer.py` 进一步从“实现堆叠文件”向“编排门面”收敛
- `retrieval.py` 和 `context_fetch.py` 开始直接依赖共享工具层，重复实现继续减少
- `indexer.py` 文件长度从 `1328` 行下降到 `1171` 行

## [1.2.10] - 2026-04-21

### Step 17: 抽离 metadata / target 语义 helper

### 本步目标

- 把 `indexer.py` 里 metadata 边推导和 target 识别逻辑完整迁出
- 统一 `index_write.py` 与 `semantic_recovery.py` 对 target 推导规则的依赖，避免两套实现继续漂移

### 本步改动

1. 新增 `src/uses_indexer/metadata_semantics.py`
   - 收口：
     - `derive_target`
     - `metadata_edges_for_statement`
   - 以及其内部依赖的 metadata entity / target / ref 分类 helper

2. 更新 `src/uses_indexer/index_write.py`
   - 直接复用 `derive_target`
   - 直接复用 `metadata_edges_for_statement`
   - 不再通过 `SQLiteIndexer` 中转调用这两个 helper

3. 更新 `src/uses_indexer/semantic_recovery.py`
   - 改为复用统一的 `derive_target`
   - 删除本地重复 `_derive_target`

4. 更新 `src/uses_indexer/indexer.py`
   - 删除中转 wrapper：
     - `_derive_target`
     - `_metadata_edges_for_statement`
   - 删除整块已迁出的 metadata helper 实现

### 验证

- `python3 -m py_compile src/uses_indexer/metadata_semantics.py src/uses_indexer/index_write.py src/uses_indexer/semantic_recovery.py src/uses_indexer/indexer.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- metadata 边推导和 target 识别现在有了独立模块归属
- `index_write.py` 与 `semantic_recovery.py` 开始共享同一套 target 语义规则
- `indexer.py` 文件长度从 `1171` 行继续下降到 `909` 行

## [1.2.11] - 2026-04-21

### Step 18: 删除 indexer 中剩余的 context-fetch 门面

### 本步目标

- 让 `EvidenceService` 和 `RetrievalService` 直接依赖 `ContextFetchService`
- 删除 `indexer.py` 中那批只做转发、不再提供额外价值的 context wrapper

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - call-chain rerank 的邻居查询改为直接调用 `ContextFetchService.procedure_call_neighbors`

2. 更新 `src/uses_indexer/evidence.py`
   - 证据组装改为直接调用：
     - `fetch_chunk_block`
     - `fetch_block_context`
     - `fetch_context_block`
     - `fetch_covering_blocks`
     - `fetch_related_context`

3. 更新 `src/uses_indexer/indexer.py`
   - 删除剩余的 context-fetch 门面方法：
     - `_procedure_call_neighbors`
     - `_fetch_context_block`
     - `_fetch_chunk_block`
     - `_fetch_block_context`
     - `_fetch_covering_blocks`
     - `_fetch_block_relation_summary`
     - `_fetch_related_context`
     - `_fetch_related_metadata_relations`
     - `_fetch_related_mc_topics`
     - `_fetch_related_call_edges`
     - `_fetch_call_chain_paths`
     - `_procedure_aliases`
     - `_resolve_procedure_name`
     - `_fetch_related_procedure_summaries`
     - `_lookup_procedure_summary`

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py src/uses_indexer/evidence.py src/uses_indexer/indexer.py src/uses_indexer/context_fetch.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- `ContextFetchService` 不再需要通过 `SQLiteIndexer` 中转即可被核心服务使用
- `indexer.py` 继续收敛成编排入口，文件长度从 `909` 行下降到 `654` 行
- 当前剩余内容已经基本集中在 schema、summary 和 index-write 门面上

## [1.2.12] - 2026-04-21

### Step 19: 让 index-build / index-write 直接协作

### 本步目标

- 继续删除 `SQLiteIndexer` 中仅用于 write-side 中转的门面方法
- 让 `IndexBuildService` 直接调用 `IndexWriteService`
- 让 `IndexWriteService` 直接依赖共享工具函数与语义函数，而不是回绕 `owner`

### 本步改动

1. 更新 `src/uses_indexer/index_write.py`
   - 改为直接复用：
     - `json_dumps`
     - `maybe_int`
     - `paths_match`
     - `embedder_batch_size`
     - `classify_call_semantics`
     - `classify_mc_publish`
   - 使用常量：
     - `READ_ACTIONS`
     - `WRITE_ACTIONS`
     - `COMPONENT_ACTIONS`
     - `EXIT_LABEL_NAMES`
   - 新增内部 `_metadata()`，不再通过 `owner._metadata()` 读取 metadata

2. 更新 `src/uses_indexer/index_build.py`
   - 改为直接调用 `IndexWriteService`：
     - `insert_unit`
     - `insert_statements`
     - `populate_missing_chunk_vectors`
     - `validate_resume_source`
     - `store_embedding_metadata`
   - 增量构建和恢复向量也不再通过 `SQLiteIndexer` write-side 门面中转

3. 更新 `src/uses_indexer/indexer.py`
   - 删除一整批已经失去调用方的 write-side 门面方法
   - 同步清理相关无用 import

### 验证

- `python3 -m py_compile src/uses_indexer/index_write.py src/uses_indexer/index_build.py src/uses_indexer/indexer.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- `IndexBuildService` 和 `IndexWriteService` 现在已经形成直接协作关系
- `SQLiteIndexer` 的 write-side 中转职责再次收缩
- `indexer.py` 文件长度从 `654` 行进一步下降到 `473` 行

## [1.2.13] - 2026-04-21

### Step 20: 抽离 db-summary 统计服务

### 本步目标

- 把 `summarize_db` 相关统计和语义汇总逻辑从 `indexer.py` 迁出
- 让 `indexer.py` 进一步收敛到初始化和总入口职责

### 本步改动

1. 新增 `src/uses_indexer/db_summary.py`
   - 新建 `DbSummaryService`
   - 收口：
     - `summarize_db`
     - 调用语义统计
     - 消息发布语义统计
     - summary 内部 metadata 读取

2. 更新 `src/uses_indexer/indexer.py`
   - 初始化 `DbSummaryService`
   - `summarize_db()` 改为直接委托给服务
   - 删除原先内联在 `indexer.py` 中的 summary / semantic aggregation 实现

### 验证

- `python3 -m py_compile src/uses_indexer/db_summary.py src/uses_indexer/indexer.py src/uses_indexer/index_build.py src/uses_indexer/index_write.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- `db-summary` 现在有独立的服务归属，后续扩 summary 能力会更自然
- `SQLiteIndexer` 继续向轻量门面收敛
- `indexer.py` 文件长度从 `473` 行进一步下降到 `363` 行

## [1.2.14] - 2026-04-21

### Step 21: 一次性收口 schema 与 metadata 基础设施

### 本步目标

- 不再只拆一个点，而是把 `indexer.py` 中剩余的基础设施再整体收一轮
- 把 schema 定义和 metadata 读写都从 `SQLiteIndexer` 里剥离
- 让 retrieval / write / build / summary 统一复用同一套 metadata helper

### 本步改动

1. 新增 `src/uses_indexer/schema.py`
   - 抽离完整 `SCHEMA_SQL`

2. 新增 `src/uses_indexer/metadata_store.py`
   - 收口：
     - `read_metadata`
     - `write_metadata`
     - `write_metadata_map`

3. 更新 `src/uses_indexer/indexer.py`
   - `SCHEMA_SQL` 改为从 `schema.py` 导入
   - 删除 `_metadata`
   - 现在基本只保留：
     - 服务初始化
     - 顶层入口方法
     - 少量常量暴露

4. 更新 `src/uses_indexer/retrieval.py`
   - embedding / vector metadata 读取改为复用 `read_metadata`

5. 更新 `src/uses_indexer/index_write.py`
   - metadata 读取改为复用 `read_metadata`
   - embedding metadata 持久化改为复用 `write_metadata_map`
   - 删除本地 `_metadata`

6. 更新 `src/uses_indexer/index_build.py`
   - index metadata 写入改为复用 `write_metadata_map`
   - 增量 index_type 校验改为复用 `read_metadata`

7. 更新 `src/uses_indexer/db_summary.py`
   - embedding metadata 读取改为复用 `read_metadata`

### 验证

- `python3 -m py_compile src/uses_indexer/schema.py src/uses_indexer/metadata_store.py src/uses_indexer/indexer.py src/uses_indexer/index_build.py src/uses_indexer/index_write.py src/uses_indexer/retrieval.py src/uses_indexer/db_summary.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_cli.py tests/test_qa.py tests/test_answering.py tests/test_api.py tests/test_mcp.py tests/test_evaluation.py tests/test_semantic_rules.py tests/test_embeddings.py` 通过
- 结果：`61 passed`

### 结论

- schema 与 metadata 访问现在都有了独立基础模块
- retrieval / build / write / summary 对 metadata 的访问方式已经统一
- `indexer.py` 文件长度从 `363` 行进一步下降到 `92` 行

## [1.2.15] - 2026-04-21

### Step 22: 升级索引构建语义层

### 本步目标

- 把 chunk 从“仅存文本片段”升级成“带角色、特征、结构化向量文本”的语义索引单元
- 为 procedure 预计算关系和能力特征，减少后续检索阶段的临时拼装成本
- 让向量召回基于更结构化的输入，而不是只吃原始摘要和内容

### 本步改动

1. 更新 `src/uses_indexer/schema.py`
   - 为 `chunks` 新增：
     - `chunk_role`
     - `chunk_features_json`
     - `embedding_text`
   - 新增 `procedure_features`
   - 新增 `procedure_features_fts`
   - 扩展 `chunks_fts`，把 `chunk_role` 纳入 FTS

2. 更新 `src/uses_indexer/semantic_recovery.py`
   - `build_semantic_chunks()` 现在会为每个 chunk 生成：
     - `chunk_role`
     - `chunk_features`
     - `embedding_text`
   - 新增 chunk 角色推导：
     - `definition`
     - `failure_flow`
     - `call_chain`
     - `table_access`
     - `variable_flow`
     - `control_flow`
     - `logic`
   - 新增 retrieval feature 计算和结构化 embedding 文本生成

3. 更新 `src/uses_indexer/index_write.py`
   - `insert_chunks()` 持久化新字段
   - `populate_missing_chunk_vectors()` 优先使用结构化 `embedding_text`
   - `insert_statements()` 完成后自动 `upsert_procedure_features()`
   - 新增 procedure 预计算内容：
     - 调用出边 / 入边
     - 表读写
     - topic 发布
     - metadata 引用
     - 变量读写
     - feature flags
     - summary text

4. 更新 `tests/test_indexer.py`
   - 新增对 `chunk_role / chunk_features_json / embedding_text / procedure_features` 的回归测试

### 验证

- `python3 -m py_compile src/uses_indexer/schema.py src/uses_indexer/semantic_recovery.py src/uses_indexer/index_write.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py -k "build_index_creates_sqlite_tables_and_fts or build_index_populates_chunk_features_and_procedure_features or build_index_populates_vectors_in_global_batches or build_index_resume_vectors_skips_existing_vectors"` 通过
- 结果：`4 passed`

### 结论

- 索引构建阶段现在已经开始直接产出可供 retrieval/rerank 使用的语义特征
- 向量输入从“原始文本”升级成了“结构化语义摘要”
- procedure 级关系预计算已经具备，可直接支撑下一步 relation retrieval 和 feature rerank

## [1.2.16] - 2026-04-21

### Step 23: 升级检索链路与质量评测

### 本步目标

- 把 query understanding 从“几个粗 intent”升级成更细的 `query_type`
- 让 retrieval 不只查文本，还能利用 procedure 级关系特征做 relation expansion
- 让 rerank 真正使用 chunk/procedure feature
- 让评测报告能看出不同问题类型和 rerank 质量信号

### 本步改动

1. 更新 `src/uses_indexer/constants.py`
   - 补充 metadata / topic 相关 intent 关键词

2. 更新 `src/uses_indexer/rerank.py`
   - `analyze_query()` 新增：
     - `wants_metadata`
     - `wants_topic`
     - `wants_variable_write`
     - `wants_variable_read`
     - `query_type`
   - `_intent_bonus()` 加强：
     - table write/read
     - variable read/write
     - metadata
     - topic
     - failure block
   - `_feature_bonus()` 现在真正消费：
     - `chunk_role`
     - `chunk_features`
     - `feature_flags`

3. 更新 `src/uses_indexer/retrieval.py`
   - 增加 `procedure_features_fts` 检索
   - chunk 检索统一使用结构化 `embedding_text`
   - 新增 `relation_procedure_feature` 召回通道
   - relation expansion 按字段区分：
     - procedure relation
     - table relation
     - variable relation
     - metadata relation
     - topic relation
     - focus relation
   - `_row_to_hit()` 透传：
     - `chunk_role`
     - `chunk_features`
     - `procedure_summary`
     - `feature_flags`

4. 更新 `src/uses_indexer/observability.py`
   - retrieval trace 补充：
     - `score_before_rerank`
     - `score_after_rerank`
     - `score_after_call_chain`
     - `rank_after`

5. 更新 `src/uses_indexer/evaluation.py`
   - evaluator 改为消费 `query_index(..., debug=True)`
   - case 结果新增：
     - `query_type`
     - `relation_hit_count`
     - `fts_hit_count`
     - `vector_hit_count`
     - `rerank_feature_hit_count`
   - summary 新增：
     - `avg_relation_hit_count`
     - `avg_feature_rerank_hit_count`
     - `by_query_type`

6. 更新测试
   - `tests/test_indexer.py`
     - 新增 relation expansion + feature rerank 回归
     - debug trace 校验 rerank 前后分数字段
   - `tests/test_evaluation.py`
     - 校验 `by_query_type`
     - 校验新的 feature rerank 质量指标

### 验证

- `python3 -m py_compile src/uses_indexer/evaluation.py src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/observability.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py tests/test_indexer.py::test_query_index_uses_relation_expansion_and_feature_rerank tests/test_indexer.py::test_query_index_debug_includes_retrieval_trace tests/test_indexer.py::test_query_index_applies_intent_aware_rerank` 通过
- 结果：`8 passed`

### 结论

- 检索链路现在已经开始把“关系”和“语义特征”当一等公民，而不只是关键词命中
- rerank trace 现在能直接看出分数前后变化
- 评测层已经能按 query type 观察检索质量，不再只有整体平均值

## [1.2.17] - 2026-04-21

### Step 24: 升级回答规划、证据压缩与 fallback 分层

### 本步目标

- 在生成前先做 answer planning，而不是所有问题共用一个提示模板
- 把 evidence compression 从“简单截断”升级成按问题类型组织的压缩
- 让 draft answer 更 grounded、更模板化
- 让最终返回结果带出更清晰的 fallback tier

### 本步改动

1. 更新 `src/uses_indexer/strategy_config.py`
   - `PromptProfileConfig` 新增 `answer_sections`
   - 新增 profile：
     - `failure_flow`
     - `variable_flow`
     - `metadata`
     - `topic`
     - `procedure_lookup`

2. 更新 `src/uses_indexer/answer_strategy.py`
   - 引入 `analyze_query()`
   - `select_profile()` 改为按 `query_type` 选策略
   - 新增 `build_question_plan()`
   - prompt package 新增：
     - `question_plan`
     - `strategy_profile`
     - `compressed_llm_context`
   - `_compress_context()` 改为：
     - 去重同位置 evidence
     - 按 query type 额外压入 call chain / tables / failure flow / metadata 关系

3. 更新 `src/uses_indexer/qa.py`
   - draft answer 现在会先分析 `query_type`
   - 输出按问题类型切换：
     - `主调用链`
     - `表访问`
     - `失败处理路径`
     - `变量流向`
     - `元数据关系`
     - `主题关系`
     - `实现位置`
   - draft answer 新增：
     - `tier`
     - `query_type`

4. 更新 `src/uses_indexer/answering.py`
   - `final_answer` 新增 `tier`
   - 约定：
     - `llm_grounded`
     - `grounded_summary`
     - `retrieval_only`

5. 更新测试
   - `tests/test_qa.py`
     - 校验 `grounded_summary`
     - 校验 `retrieval_only`
   - `tests/test_answering.py`
     - 校验 `question_plan.query_type`
     - 校验 `final_answer.tier`

### 验证

- `python3 -m py_compile src/uses_indexer/qa.py src/uses_indexer/answering.py src/uses_indexer/answer_strategy.py src/uses_indexer/strategy_config.py` 通过
- `PYTHONPATH=. pytest -q tests/test_api.py tests/test_mcp.py tests/test_qa.py tests/test_answering.py` 通过
- 结果：`13 passed`

### 结论

- 回答链路现在会先识别问题类型，再决定提示策略和证据压缩方式
- draft answer 已经从“简单拼接命中”升级成“按问题类型组织的 grounded 摘要”
- 回答结果现在能更清楚地区分 LLM grounded、draft grounded 和 retrieval-only 三层能力

## [1.2.18] - 2026-04-21

### Step 25: 细化增量建库诊断与真实效果评测样例

### 本步目标

- 让增量建库报告不仅告诉我们“重建了多少”，还告诉我们“语义上变了什么”
- 给评测层补一组更贴近真实业务问法的样例，方便后续持续回归

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - `incremental_scope.before/after` 现在会携带：
     - `chunk_role_counts`
     - `block_type_counts`
     - `feature_flags`
   - 新增 `_scope_delta()`
   - changed/removed 项现在都会产出 `delta`
   - `incremental_scope.summary` 新增：
     - `delta_statement_count`
     - `delta_chunk_count`
     - `delta_block_count`
     - `delta_vector_target_count`

2. 更新 `tests/test_indexer.py`
   - 扩展增量建库测试
   - 覆盖：
     - 第一次新增文件
     - 第二次修改同一文件
     - 校验 `before/after/delta`
     - 校验 `chunk_role_counts / block_type_counts / feature_flags`

3. 新增 `eval/uses_codes_effect_cases.json`
   - 补充更贴近真实问题类型的效果评测样例：
     - failure handler
     - variable write flow
     - table write path
     - caller lookup
     - dynamic SQL table

4. 更新 `docs/EVALUATION.md`
   - 补充新的样例文件入口
   - 补充 `by_query_type / avg_relation_hit_count / avg_feature_rerank_hit_count / cases[].query_type`

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py::test_build_index_supports_incremental_updates` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py` 通过
- 结果：`6 passed`

### 结论

- 增量建库现在已经不仅能看文件变化，还能看语义结构变化
- 后续调 chunk/block/feature 规则时，可以直接借助 delta 做更细的线上诊断
- 评测样例开始更贴近真实业务问法，而不只是最早那批基础覆盖

## [1.2.19] - 2026-04-21

### Step 26: 强化调用链定向关系检索

### 本步目标

- 让“谁调用了谁”这类问题不只依赖 procedure summary 或 chunk 命中
- 直接利用 `calls_procedure` 边扩展 caller/callee 候选，提高调用链类问题稳定性

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 在 `_run_relation_queries()` 中新增 `relation_call_edge`
   - 对 `wants_call_chain` 问题：
     - `被谁调用` 直接按 `target_name` 反查 callers
     - 其他调用链问题按 `source_name` 查 callees
   - relation hit 会透传：
     - `match_source=caller_relation/callee_relation`
     - `matched_text=caller -> callee`
     - `feature_flags`

2. 更新 `tests/test_indexer.py`
   - 新增针对 `AF_DEEP 被谁调用` 的 direct call-edge relation 回归测试

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py -k "query_index_uses_direct_call_edge_relation_for_callers or query_index_applies_intent_aware_rerank or query_index_debug_includes_retrieval_trace"` 通过
- 结果：`3 passed`

### 结论

- 调用链类问题现在有了更明确的边关系召回，不再只靠文本摘要兜底
- 对“被谁调用/调用了谁”这类检索，候选来源更可信、更可解释

## [1.2.20] - 2026-04-21

### Step 27: 为增量建库增加 chunk 级向量复用

### 本步目标

- 让 changed 文件在 chunk 语义未变化时复用旧向量
- 减少增量建库的重新 embedding 成本
- 让增量建库更接近真正的 chunk 级执行粒度

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 新增 `_collect_reusable_chunk_vectors()`
   - 新增 `_restore_reusable_chunk_vectors()`
   - 增量建库时会：
     - 删除旧索引前收集 changed 文件旧 chunk 向量
     - 重建后按 `embedding_text` 回填可复用向量
   - `vector_stats` 新增：
     - `reused`
     - `reuse_candidates`
     - `reused_chunk_count`

2. 更新 `tests/test_indexer.py`
   - 新增增量建库向量复用回归测试
   - 覆盖“文件 fingerprint 变化，但 chunk 语义不变”的场景

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py -k "incremental_build_reuses_existing_chunk_vectors_when_embedding_text_matches or build_index_supports_incremental_updates"` 通过
- 结果：`2 passed`

### 结论

- 增量建库现在已经从“文件级重算”往“chunk 级复用”迈了一步
- 在大库场景下，这会直接减少 embedding 成本和更新时间

## [1.2.21] - 2026-04-21

### Step 28: 增强回答可信度与证据引用

### 本步目标

- 让回答结果不只返回文本，还返回“为什么能信”
- 给调用方直接暴露 confidence 和 grounded citations

### 本步改动

1. 更新 `src/uses_indexer/qa.py`
   - draft answer 新增 `confidence`
   - 新增 `_estimate_confidence()`
   - `insufficient_evidence` 场景固定返回低置信度

2. 更新 `src/uses_indexer/answering.py`
   - `final_answer` 新增：
     - `confidence`
     - `grounding.citations`
     - `grounding.supporting_locations`
     - `grounding.uncertainties`

3. 更新测试
   - `tests/test_qa.py`
     - 校验 `confidence`
   - `tests/test_answering.py`
     - 校验 `grounding citations`
     - 校验 `final_answer.confidence`

### 验证

- `python3 -m py_compile src/uses_indexer/qa.py src/uses_indexer/answering.py` 通过
- `PYTHONPATH=. pytest -q tests/test_qa.py tests/test_answering.py` 通过
- 结果：`8 passed`

### 结论

- 回答结果现在已经带出置信度和前 3 条 grounded citation
- 后续无论是 API、MCP 还是前端展示，都更容易做“可解释回答”

## [1.2.22] - 2026-04-21

### Step 29: 用 parse cache 降低增量建库重复解析成本

### 本步目标

- 避免 changed/added 文件在 impact report、scope estimate、indexing 阶段被反复 `parse_path()`
- 让增量建库对大库更友好

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 新增 `_parse_unit()` 缓存入口
   - `_index_files()` 改为使用 parse cache
   - `_build_incremental_impact_report()`
   - `_describe_source_unit()`
   - `_estimate_source_scope()`
     都改为复用同一份 parse cache
   - `build_index()` / `incremental_build_index()` 新增 `build_stats`
   - `build_stats` 现在包含：
     - `parsed_unit_count`
     - `parse_cache_hits`
     - `parse_cache_misses`

2. 更新 `tests/test_indexer.py`
   - 新增 `CountingParser`
   - 新增增量建库 parse cache 回归测试
   - 校验 changed/added 文件在一次 incremental build 中只被解析一次

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py` 通过
- `PYTHONPATH=. pytest -q tests/test_indexer.py -k "incremental_build_reuses_parsed_units_with_cache or incremental_build_reuses_existing_chunk_vectors_when_embedding_text_matches"` 通过
- 结果：`2 passed`

### 结论

- 增量建库现在已经把“重复解析同一 changed 文件”的成本收掉了
- `build_stats` 也开始能量化构建阶段的缓存收益

## [1.2.23] - 2026-04-21

### Step 30: 增加评测门槛守门与一键 debug bundle

### 本步目标

- 让 `eval-retrieval` 不只是出报告，还能做质量守门
- 让一次问题的 query/evidence/answer 能一键打包，方便线上排障和离线复盘

### 本步改动

1. 更新 `src/uses_indexer/evaluation.py`
   - 新增 `EvaluationThresholds`
   - 新增 `evaluate_thresholds()`
   - 支持检查：
     - `pass_at_k`
     - `evidence_coverage`
     - `top_hit_expectation_coverage`
     - `avg_feature_rerank_hit_count`

2. 更新 `src/uses_indexer/cli.py`
   - `eval-retrieval` 新增：
     - `--min-pass-at-k`
     - `--min-evidence-coverage`
     - `--min-top-hit-expectation-coverage`
     - `--min-avg-feature-rerank-hit-count`
     - `--fail-on-thresholds`
   - 新增 `debug-bundle` 命令
   - 新增 `_build_debug_bundle()`
   - threshold fail 时 CLI 退出码为 `2`

3. 更新测试
   - `tests/test_evaluation.py`
     - 新增 threshold fail 回归
   - `tests/test_cli.py`
     - 新增 threshold pair 解析测试
     - 新增 debug bundle 组装测试

4. 更新文档
   - `docs/EVALUATION.md`
     - 补充 threshold 用法
   - `docs/TROUBLESHOOTING.md`
     - 补充 `debug-bundle` 命令入口

### 验证

- `python3 -m py_compile src/uses_indexer/evaluation.py src/uses_indexer/cli.py tests/test_evaluation.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py tests/test_cli.py` 通过
- 结果：`11 passed`

### 结论

- 评测层现在已经可以做简单的质量守门
- 排障时不再需要手工拼 query/evidence/answer 三份输出，`debug-bundle` 可以直接复盘整条链路

## [1.2.24] - 2026-04-21

### Step 31: 把 debug bundle 接到 API / MCP，并修复 debug JSON 序列化

### 本步目标

- 让 `debug-bundle` 不只在 CLI 可用，也能从 HTTP API 和 MCP 工具直接调用
- 修复 retrieval debug payload 中 `set` 导致的 JSON 序列化问题

### 本步改动

1. 新增 `src/uses_indexer/debug_bundle.py`
   - 抽出公共 `build_debug_bundle()`
   - 统一生成：
     - `query`
     - `evidence`
     - `answer`

2. 更新 `src/uses_indexer/cli.py`
   - 改为复用 `build_debug_bundle()`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /debug-bundle`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `debug_bundle` 工具

5. 更新 `src/uses_indexer/observability.py`
   - 新增 `_json_safe()`
   - retrieval trace 里的 `query_analysis` 现在会把 `set` 正常转成 JSON-safe 列表

6. 更新测试
   - `tests/test_cli.py`
   - `tests/test_api.py`
   - `tests/test_mcp.py`
   - 新增 debug bundle 在 CLI / API / MCP 三端的回归覆盖

### 验证

- `python3 -m py_compile src/uses_indexer/observability.py src/uses_indexer/debug_bundle.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- 结果：`11 passed`

### 结论

- 现在无论是命令行、HTTP 还是 MCP 工具，都能统一拿到完整 debug bundle
- debug trace 的 JSON 序列化问题已经被收口，后续更适合直接落盘或透传给外部系统

## [1.2.25] - 2026-04-21

### Step 32: 增加分项评测守门与 debug bundle 归档导出

### 本步目标

- 让 `eval-retrieval` 不只看总体分数，还能对指定标签和问题类型单独设门槛
- 让 `debug-bundle` 不只输出单个 JSON，还能按查询、证据、回答拆分归档，方便排障留档

### 本步改动

1. 更新 `src/uses_indexer/evaluation.py`
   - `EvaluationThresholds` 新增：
     - `min_tag_pass_at_k`
     - `min_query_type_pass_at_k`
   - `evaluate_thresholds()` 现在支持检查：
     - `by_tag.<tag>.pass_at_k.<k>`
     - `by_query_type.<query_type>.pass_at_k.<k>`

2. 更新 `src/uses_indexer/cli.py`
   - `eval-retrieval` 新增：
     - `--min-tag-pass-at-k`
     - `--min-query-type-pass-at-k`
   - 新增 `_parse_scoped_threshold_pairs()`
   - `debug-bundle` 新增：
     - `--archive-dir`

3. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `write_debug_bundle_archive()`
   - 归档输出：
     - `bundle.json`
     - `bundle_summary.json`
     - `query.json`
     - `evidence.json`
     - `answer.json`

4. 更新测试
   - `tests/test_evaluation.py`
     - 新增 scoped threshold 守门回归
   - `tests/test_cli.py`
     - 新增 scoped threshold 解析测试
     - 新增 archive summary 回归

5. 更新文档
   - `docs/EVALUATION.md`
     - 补充分项 threshold 的用法和建议
   - `docs/TROUBLESHOOTING.md`
     - 补充 `debug-bundle --archive-dir` 的排障方式

### 验证

- `python3 -m py_compile src/uses_indexer/evaluation.py src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py tests/test_evaluation.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_evaluation.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 评测现在已经可以对关键标签和 query type 做更细粒度的质量守门
- `debug-bundle` 现在更适合做线上问题归档和跨版本复盘

## [1.2.26] - 2026-04-21

### Step 33: 增加 debug bundle 自动对比能力

### 本步目标

- 让两次 `debug-bundle` 结果可以直接自动 diff
- 把对比能力统一接到 CLI / API / MCP，减少各入口能力分叉
- 补详细文档，让问题复盘不只“能做”，而是“知道怎么做、怎么读结果”

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `compare_debug_bundles()`
   - 支持直接比较：
     - 单个 `bundle.json`
     - `debug-bundle --archive-dir` 输出目录
   - 输出：
     - `summary.query_hit_count`
     - `summary.candidate_count`
     - `summary.evidence_count`
     - `summary.query_type`
     - `summary.answer_source`
     - `summary.final_answer_changed`
     - `query.top_hit_changed`
     - `evidence.top_evidence_changed`
     - `answer.before_final_answer_excerpt`
     - `answer.after_final_answer_excerpt`
   - 增加 `warnings`：
     - `question_changed`
     - `db_path_changed`
     - `query_type_changed`

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `compare-debug-bundles`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /compare-debug-bundles`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `compare_debug_bundles` 工具

5. 更新测试
   - `tests/test_cli.py`
     - 新增 debug bundle compare 回归
   - `tests/test_api.py`
     - 新增 compare API 回归
   - `tests/test_mcp.py`
     - 新增 compare MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 新增 compare-debug-bundles 的使用方式、字段解释和诊断顺序
   - `docs/EVALUATION.md`
     - 新增“用 debug bundle 做 case 级复盘”流程

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 现在不仅能保存单次问题的完整诊断包，还能直接比较两个版本的 query / evidence / answer 差异
- 这让排障和效果复盘从“手工看两份 JSON”升级成了“结构化 diff”

## [1.2.27] - 2026-04-21

### Step 34: 增加 debug bundle reviewer 摘要

### 本步目标

- 让 debug bundle compare 结果不只适合机器消费，也适合人快速审阅
- 给对比结果增加“先看哪里”的判断层，降低手工阅读整份 JSON 的成本

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - compare 结果新增：
     - `review_summary.verdict`
     - `review_summary.priority`
     - `review_summary.focus_area`
     - `review_summary.findings`
     - `review_summary.next_steps`
   - 新增 `markdown_summary`
   - 新增 reviewer 逻辑：
     - `stable`
     - `behavior_changed`
     - `possible_regression`
     - `query_drift`
     - `invalid_comparison`

2. 更新 `src/uses_indexer/cli.py`
   - `compare-debug-bundles` 新增：
     - `--markdown-output`

3. 更新测试
   - `tests/test_cli.py`
     - 新增 reviewer summary 和 markdown summary 断言

4. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 reviewer summary 的读法
   - `docs/EVALUATION.md`
     - 补充 markdown compare 复盘建议

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- compare 结果现在不仅能 diff 两次 bundle，还能直接给出“该先看哪一层”的 reviewer 视角摘要
- 这一步让问题复盘从“结构化 diff”继续升级成了“可快速审阅的 diff”

## [1.2.28] - 2026-04-21

### Step 35: 增加批量 debug bundle 回归面板

### 本步目标

- 让一组固定问题可以批量跑 before/after 两套 debug bundle
- 把逐题 comparison 再汇总成一个适合 release review 的总览 panel

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `build_debug_bundle_regression_panel()`
   - 新增 `compare_debug_bundles_from_payloads()`
   - 新增 panel 汇总：
     - `summary.changed_case_count`
     - `summary.stable_case_count`
     - `summary.verdict_counts`
     - `summary.priority_counts`
     - `summary.focus_area_counts`
     - `summary.high_priority_cases`
   - 支持 `archive_dir` 输出每个 case 的：
     - `before/`
     - `after/`
     - `comparison.json`
     - `comparison.md`

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `compare-debug-bundle-panel`
   - 支持：
     - `--before-db`
     - `--after-db`
     - `--cases`
     - `--archive-dir`
     - `--markdown-output`

3. 更新测试
   - `tests/test_cli.py`
     - 新增 regression panel 回归

4. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 新增批量回归面板的使用方式和产物说明
   - `docs/EVALUATION.md`
     - 新增“批量问题面板”建议流程

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 现在不仅能复盘单题，还能对一组典型问题做批量链路级回归审阅
- 这一步让 debug bundle 从“问题排障工具”进一步升级成了“版本回归审阅工具”

## [1.2.29] - 2026-04-21

### Step 36: 增加 panel 级 fail gate

### 本步目标

- 让批量 debug bundle panel 不只是 review 看板，也能直接作为发布守门

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `DebugBundlePanelThresholds`
   - 新增 `evaluate_debug_bundle_regression_panel_thresholds()`
   - 支持检查：
     - `changed_case_count`
     - `high_priority_case_count`
     - `verdict_counts.<verdict>`
     - `focus_area_counts.<focus_area>`
   - panel markdown 新增 `Threshold Status`

2. 更新 `src/uses_indexer/cli.py`
   - `compare-debug-bundle-panel` 新增：
     - `--max-changed-cases`
     - `--max-high-priority-cases`
     - `--max-verdict-count`
     - `--max-focus-area-count`
     - `--fail-on-thresholds`
   - 新增 `_parse_named_int_pairs()`
   - threshold fail 时退出码为 `2`

3. 更新测试
   - `tests/test_cli.py`
     - 新增 named int threshold 解析测试
     - 新增 panel threshold fail 回归

4. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 panel threshold 配置示例
   - `docs/EVALUATION.md`
     - 补充 panel 守门在 CI 中的使用建议

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 批量 panel 现在已经可以直接承担“典型问题链路门槛”的角色
- 这一步让 panel 从 review 能力进一步升级成了 release gate

## [1.2.30] - 2026-04-21

### Step 37: 把 panel 能力接到 API / MCP

### 本步目标

- 让批量 debug bundle panel 不只在 CLI 可用，也能被 HTTP API 和 MCP 工具直接调用

### 本步改动

1. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /compare-debug-bundle-panel`
   - 同时支持 panel threshold 参数：
     - `max_changed_cases`
     - `max_high_priority_cases`
     - `max_verdict_counts`
     - `max_focus_area_counts`

2. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `compare_debug_bundle_panel` 工具
   - 支持同样的 panel threshold 参数

3. 更新测试
   - `tests/test_api.py`
     - 新增 compare-debug-bundle-panel API 回归
   - `tests/test_mcp.py`
     - 新增 compare_debug_bundle_panel MCP tool 回归

4. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 panel 在 API / MCP 下的使用入口

### 验证

- `python3 -m py_compile src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_api.py tests/test_mcp.py tests/test_cli.py` 通过

### 结论

- 现在无论是 CLI、HTTP 还是 MCP，批量 panel 和 panel gate 都已经能统一使用
- 这一步让 release gate 从本地命令进一步升级成了服务化能力

## [1.2.31] - 2026-04-21

### Step 38: 增加 panel baseline 对比

### 本步目标

- 让批量 panel 不只是一份当前快照，也能作为历史基线长期保存和比较

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - `build_debug_bundle_regression_panel()` 现在在 `archive_dir` 下会补写：
     - `panel.json`
     - `panel.md`
     - `panel_summary.json`
   - 新增 `write_debug_bundle_regression_panel_archive()`
   - 新增 `compare_debug_bundle_regression_panels()`
   - 新增 panel-level comparison markdown

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `compare-debug-bundle-panels`

3. 更新测试
   - `tests/test_cli.py`
     - 新增 panel baseline compare 回归

4. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 panel baseline compare 的使用方式
   - `docs/EVALUATION.md`
     - 补充长期 panel 趋势跟踪建议

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py tests/test_cli.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 批量 panel 现在已经可以作为长期基线产物保存下来
- 这一步让回归能力从“当前版本审阅”进一步升级成了“历史基线比较”

## [1.2.32] - 2026-04-21

### Step 39: 增加固定 baseline 管理并接到 API / MCP

### 本步目标

- 让 panel baseline 不只是“两个 archive 临时比较”，而是能保存、列出、按名字复用
- 让 panel archive compare 和 baseline 管理都能被 API / MCP 直接调用

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `save_debug_bundle_regression_panel_baseline()`
   - 新增 `list_debug_bundle_regression_panel_baselines()`
   - 新增 `load_debug_bundle_regression_panel_baseline()`
   - 新增 `compare_debug_bundle_regression_panel_baseline()`
   - 新增默认 baseline 目录解析和 baseline 元数据写入

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `save-debug-bundle-panel-baseline`
   - 新增 `list-debug-bundle-panel-baselines`
   - 新增 `compare-debug-bundle-panel-baseline`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /compare-debug-bundle-panels`
   - 新增 `GET /list-debug-bundle-panel-baselines`
   - 新增 `POST /save-debug-bundle-panel-baseline`
   - 新增 `POST /compare-debug-bundle-panel-baseline`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `compare_debug_bundle_panels`
   - 新增 `save_debug_bundle_panel_baseline`
   - 新增 `list_debug_bundle_panel_baselines`
   - 新增 `compare_debug_bundle_panel_baseline`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 baseline 保存 / 列表 / 命名比较回归
   - `tests/test_api.py`
     - 新增 panel archive compare 和 baseline 管理 API 回归
   - `tests/test_mcp.py`
     - 新增对应 MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充固定 baseline 的 CLI / API / MCP 用法
   - `docs/EVALUATION.md`
     - 补充固定 baseline 评测工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过

### 结论

- 现在 panel 不只支持“历史 archive 对比”，还支持“固定命名 baseline”
- 这一步让回归流程从临时产物管理进一步升级成了可复用的长期基线体系

## [1.2.33] - 2026-04-21

### Step 40: 增加 baseline 元数据、最近基线比较和清理能力

### 本步目标

- 让 panel baseline 不只是“能保存”，而是能作为长期仓库来管理
- 让基线比较不再强依赖人工记住 baseline 名称

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - `save_debug_bundle_regression_panel_baseline()` 现在支持：
     - `baseline_notes`
     - `baseline_tags`
   - `list_debug_bundle_regression_panel_baselines()` 现在支持：
     - `baseline_tag` 过滤
     - 返回更完整的 baseline 元数据
   - 新增 `resolve_latest_debug_bundle_regression_panel_baseline()`
   - 新增 `delete_debug_bundle_regression_panel_baseline()`
   - 新增 `compare_debug_bundle_regression_panel_latest_baseline()`
   - baseline compare 结果现在会带：
     - `saved_at`
     - `baseline_notes`
     - `baseline_tags`

2. 更新 `src/uses_indexer/cli.py`
   - `save-debug-bundle-panel-baseline` 新增：
     - `--note`
     - `--tag`
   - `list-debug-bundle-panel-baselines` 新增：
     - `--tag`
   - 新增：
     - `show-debug-bundle-panel-baseline`
     - `delete-debug-bundle-panel-baseline`
     - `compare-debug-bundle-panel-latest-baseline`

3. 更新 `src/uses_indexer/api.py`
   - `GET /list-debug-bundle-panel-baselines` 新增 `baseline_tag`
   - 新增：
     - `GET /show-debug-bundle-panel-baseline`
     - `POST /compare-debug-bundle-panel-latest-baseline`
     - `POST /delete-debug-bundle-panel-baseline`
   - `POST /save-debug-bundle-panel-baseline` 现在支持：
     - `baseline_notes`
     - `baseline_tags`

4. 更新 `src/uses_indexer/mcp_server.py`
   - `save_debug_bundle_panel_baseline` 新增：
     - `baseline_notes`
     - `baseline_tags`
   - `list_debug_bundle_panel_baselines` 新增：
     - `baseline_tag`
   - 新增：
     - `show_debug_bundle_panel_baseline`
     - `delete_debug_bundle_panel_baseline`
     - `compare_debug_bundle_panel_latest_baseline`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 baseline 元数据 / 最近基线比较 / 删除回归
   - `tests/test_api.py`
     - 新增 show / latest compare / delete API 回归
   - `tests/test_mcp.py`
     - 新增 show / latest compare / delete MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 baseline 备注、标签、最近基线比较和删除方式
   - `docs/EVALUATION.md`
     - 补充“最近一份同类 baseline”评测工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `21 passed`

### 结论

- 现在 baseline 已经具备“保存、筛选、查看、比较最近版本、删除”的完整管理闭环
- 这一步让 panel baseline 从“可复用”进一步升级成了“可运营、可长期维护”的回归资产

## [1.2.34] - 2026-04-21

### Step 41: 增加 baseline trend 视图

### 本步目标

- 让 baseline 不只是“单次比较对象”，而是能被当作一条长期趋势序列来观察
- 让 release / smoke / nightly 这类标签基线具备更直观的历史复盘能力

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `summarize_debug_bundle_regression_panel_baseline_trend()`
   - 新增 baseline trend markdown 渲染
   - trend 输出包含：
     - `timeline`
     - `transitions`
     - `latest`
     - `oldest`
     - `summary.overall_changed_case_delta`
     - `summary.overall_possible_regression_delta`

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `show-debug-bundle-panel-baseline-trend`
   - 支持：
     - `--baseline-dir`
     - `--tag`
     - `--limit`
     - `--markdown-output`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `GET /show-debug-bundle-panel-baseline-trend`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `show_debug_bundle_panel_baseline_trend`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 baseline trend 聚合回归
   - `tests/test_api.py`
     - 新增 trend API 回归
   - `tests/test_mcp.py`
     - 新增 trend MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 baseline trend 的使用方式和阅读顺序
   - `docs/EVALUATION.md`
     - 补充 baseline trend 在长期评测复盘中的定位

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `22 passed`

### 结论

- 现在同一组 tagged baseline 已经可以直接看长期走势，不再只能两两比较
- 这一步让 baseline 体系从“可管理”进一步升级成了“可做阶段性趋势复盘”的质量资产

## [1.2.35] - 2026-04-21

### Step 42: 增加 baseline promote 能力

### 本步目标

- 让“当前 panel 通过 gate 后提升为正式标准答案”成为一个明确动作
- 让 baseline 元数据里能区分“普通保存”与“正式提升”

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - `save_debug_bundle_regression_panel_baseline()` 现在支持 `promotion_source`
   - 新增 `promote_debug_bundle_regression_panel_baseline()`
   - promote 返回：
     - `bundle_kind = debug_bundle_regression_panel_baseline_promoted`
     - `promotion_source`
     - `baseline_notes`
     - `baseline_tags`

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `promote-debug-bundle-panel-baseline`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /promote-debug-bundle-panel-baseline`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `promote_debug_bundle_panel_baseline`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 promote 回归
   - `tests/test_api.py`
     - 新增 promote API 回归
   - `tests/test_mcp.py`
     - 新增 promote MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 promote 的使用方式和适用场景
   - `docs/EVALUATION.md`
     - 补充“通过 gate 后一键提升 baseline”的评测工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `23 passed`

### 结论

- 现在 baseline 不只支持保存和比较，还支持“正式提升为当前标准版本”
- 这一步让回归资产从“可管理”进一步升级成了“可治理、可显式切换当前标准答案”的流程能力

## [1.2.36] - 2026-04-21

### Step 43: 增加 promotion gate

### 本步目标

- 让 promote 不再只是“一个保存动作”，而是能受明确 gate 约束
- 让“当前 panel 有没有资格提升为正式 baseline”先变成可解释的检查结果

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `evaluate_debug_bundle_regression_panel_promotion_gate()`
   - 新增 `guarded_promote_debug_bundle_regression_panel_baseline()`
   - gate 现在支持：
     - `require_threshold_pass`
     - `blocked_latest_verdicts`
     - `baseline_tag`

2. 更新 `src/uses_indexer/cli.py`
   - `promote-debug-bundle-panel-baseline` 新增：
     - `--require-threshold-pass`
     - `--gate-tag`
     - `--block-latest-verdict`
   - 新增：
     - `evaluate-debug-bundle-panel-promotion-gate`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /evaluate-debug-bundle-panel-promotion-gate`
   - `POST /promote-debug-bundle-panel-baseline` 现在支持 gate 参数
   - gate 失败时返回明确的 `400`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `evaluate_debug_bundle_panel_promotion_gate`
   - `promote_debug_bundle_panel_baseline` 现在支持 gate 参数

5. 更新测试
   - `tests/test_cli.py`
     - 新增 threshold gate 拦截回归
   - `tests/test_api.py`
     - 新增 gate API 回归
   - `tests/test_mcp.py`
     - 新增 gate MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 gate 的使用方式和“阻止 promote”的意义
   - `docs/EVALUATION.md`
     - 补充 gate + promote 联动工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `24 passed`

### 结论

- 现在 promote 已经可以被 threshold 和 latest-baseline verdict 显式约束
- 这一步让 baseline 流程从“可治理”进一步升级成了“具备真正发布门槛”的质量控制机制

## [1.2.37] - 2026-04-21

### Step 44: 增加一键 release workflow

### 本步目标

- 把 `latest compare -> promotion gate -> promote` 三步收成一个完整工作流
- 让发布前后的质量动作可以一次执行并产出 reviewer 摘要

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `run_debug_bundle_regression_panel_release_workflow()`
   - 新增 release workflow reviewer summary
   - 新增 release workflow markdown 渲染

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `run-debug-bundle-panel-release-workflow`
   - 支持：
     - `--gate-tag`
     - `--require-threshold-pass`
     - `--block-latest-verdict`
     - `--no-auto-promote`
     - `--markdown-output`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /run-debug-bundle-panel-release-workflow`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `run_debug_bundle_panel_release_workflow`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 release workflow promote 回归
   - `tests/test_api.py`
     - 新增 release workflow API 回归
   - `tests/test_mcp.py`
     - 新增 release workflow MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充一键 release workflow 的使用方式
   - `docs/EVALUATION.md`
     - 补充“单命令完成 compare + gate + promote”的工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `25 passed`

### 结论

- 现在发布前后的质量动作已经可以一条命令跑完
- 这一步让 baseline 体系从“具备发布门槛”进一步升级成了“可直接执行的 release 质量工作流”

## [1.2.38] - 2026-04-21

### Step 45: 增加 release workflow archive

### 本步目标

- 让 release workflow 运行后不只返回结果，还能留下完整归档
- 让 release 审计、长期复盘和跨版本对比有稳定落盘产物

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `write_debug_bundle_regression_panel_release_workflow_archive()`
   - `run_debug_bundle_regression_panel_release_workflow()` 现在支持 `archive_dir`
   - workflow archive 输出包含：
     - `release_workflow.json`
     - `release_workflow.md`
     - `release_workflow_summary.json`
     - `promotion_gate.json`
     - `latest_comparison.json`
     - `promoted_baseline.json`

2. 更新 `src/uses_indexer/cli.py`
   - `run-debug-bundle-panel-release-workflow` 新增 `--archive-dir`

3. 更新 `src/uses_indexer/api.py`
   - `POST /run-debug-bundle-panel-release-workflow` 新增 `archive_dir`

4. 更新 `src/uses_indexer/mcp_server.py`
   - `run_debug_bundle_panel_release_workflow` 新增 `archive_dir`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 workflow archive 回归
   - `tests/test_api.py`
     - 新增 workflow archive API 回归
   - `tests/test_mcp.py`
     - 新增 workflow archive MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 workflow archive 的使用方式和输出内容
   - `docs/EVALUATION.md`
     - 补充 release 审计材料归档建议

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `25 passed`

### 结论

- 现在 release workflow 已经具备完整归档能力，不再只是一次即时执行
- 这一步让质量工作流从“可执行”进一步升级成了“可审计、可长期留存”的流程资产

## [1.2.39] - 2026-04-21

### Step 46: 增加 release workflow compare

### 本步目标

- 让 release workflow 不只可查看，还能直接比较两次运行结果
- 让“发布动作本身”的变化可以被 reviewer 快速感知

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `compare_debug_bundle_regression_panel_release_workflows()`
   - 新增 release workflow comparison reviewer summary
   - 新增 release workflow comparison markdown 渲染

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `compare-debug-bundle-panel-release-workflows`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `POST /compare-debug-bundle-panel-release-workflows`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `compare_debug_bundle_panel_release_workflows`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 release workflow compare 回归
   - `tests/test_api.py`
     - 新增 release workflow compare API 回归
   - `tests/test_mcp.py`
     - 新增 release workflow compare MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 release workflow compare 的使用方式和适用场景
   - `docs/EVALUATION.md`
     - 补充“比较两次发布动作”的评测工作流

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `26 passed`

### 结论

- 现在 release workflow 已经能直接做历史比较，不再只能单次查看
- 这一步让发布流程从“可审计”进一步升级成了“可对比、可长期复盘”的质量资产

## [1.2.39] - 2026-04-21

### Step 46: 增加 release workflow index / show

### 本步目标

- 让历史 release workflow archive 不只是目录产物，还能被统一列出和查看
- 让 release 工作流开始具备真正的“可索引、可运营”属性

### 本步改动

1. 更新 `src/uses_indexer/debug_bundle.py`
   - 新增 `list_debug_bundle_regression_panel_release_workflows()`
   - 新增 `load_debug_bundle_regression_panel_release_workflow()`
   - 支持两种路径模式：
     - 传 workflow archive 根目录
     - 传单个 workflow archive 目录

2. 更新 `src/uses_indexer/cli.py`
   - 新增 `list-debug-bundle-panel-release-workflows`
   - 新增 `show-debug-bundle-panel-release-workflow`

3. 更新 `src/uses_indexer/api.py`
   - 新增 `GET /list-debug-bundle-panel-release-workflows`
   - 新增 `GET /show-debug-bundle-panel-release-workflow`

4. 更新 `src/uses_indexer/mcp_server.py`
   - 新增 `list_debug_bundle_panel_release_workflows`
   - 新增 `show_debug_bundle_panel_release_workflow`

5. 更新测试
   - `tests/test_cli.py`
     - 新增 workflow list / show 回归
   - `tests/test_api.py`
     - 新增 workflow list / show API 回归
   - `tests/test_mcp.py`
     - 新增 workflow list / show MCP tool 回归

6. 更新文档
   - `docs/TROUBLESHOOTING.md`
     - 补充 workflow archive 的 list / show 用法
   - `docs/EVALUATION.md`
     - 补充 workflow archive 统一管理方式

### 验证

- `python3 -m py_compile src/uses_indexer/debug_bundle.py src/uses_indexer/cli.py src/uses_indexer/api.py src/uses_indexer/mcp_server.py tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过
- `PYTHONPATH=. pytest -q tests/test_cli.py tests/test_api.py tests/test_mcp.py` 通过，结果 `25 passed`

### 结论

- 现在 release workflow archive 已经可以被统一列出和查看，不再只是散落目录
- 这一步让 release 工作流从“可审计”进一步升级成了“可索引、可持续运营”的质量资产

## [1.2.40] - 2026-04-21

### Step 47: 增加第一版内置 Web UI

### 本步目标

- 为当前项目补一版真正可运行的本地前端页面
- 不引入额外前端框架，直接复用现有 `serve-api`
- 同时补齐前端设计文档、技术文档和回归测试

### 本步改动

1. 新增内置前端资源
   - `src/uses_indexer/web/index.html`
   - `src/uses_indexer/web/styles.css`
   - `src/uses_indexer/web/app.js`
   - 第一版页面包含：
     - Hero 区
     - 数据库概览
     - 检索 / evidence / answer 工作台
     - trace 摘要面板
     - 项目能力与路由视图

2. 更新 `src/uses_indexer/api.py`
   - 新增静态页面入口：
     - `GET /`
     - `GET /ui`
   - 新增静态资源托管：
     - `GET /assets/styles.css`
     - `GET /assets/app.js`
   - 现有 JSON API 保持不变

3. 更新 `pyproject.toml`
   - 新增 package data 配置
   - 确保 `web/*` 资源打包后仍可访问

4. 更新测试
   - `tests/test_api.py`
   - 新增 Web UI 入口和静态资源回归：
     - `/`
     - `/assets/styles.css`
     - `/assets/app.js`

5. 更新文档
   - 新增 `docs/FRONTEND_DESIGN.md`
   - 新增 `docs/FRONTEND_TECHNICAL.md`
   - 更新：
     - `README.md`
     - `docs/USAGE.md`
     - `docs/DEPLOYMENT.md`

### 设计结论

- 第一版前端不做成营销官网，而是做成“本地检索控制台”
- 视觉方向采用蓝白灰柔和配色，强调轻、静、现代
- 动画以慢节奏背景漂浮、卡片浮入、数字缓动和面板 shimmer 为主
- 页面重点放在真实使用链路，而不是堆砌展示型模块

### 技术结论

- 当前阶段使用零依赖静态前端最合适
- 这样可以把前端直接并入现有 `serve-api`，不额外引入 Node / 构建链 / 部署链
- 等后续页面复杂度进一步增长，再考虑独立前端工程

## [1.2.41] - 2026-04-22

### Step 48: 把长页面前端重构为单屏控制台

### 本步目标

- 去掉上一版依赖纵向滚动的长页面结构
- 把首页收敛成真正的单屏工作台
- 继续提升视觉质量、动效数量和交互流畅度

### 本步改动

1. 重写 `src/uses_indexer/web/index.html`
   - 顶部导航改成视图切换按钮
   - 首屏只保留：
     - 品牌
     - 服务状态
     - 关键统计
     - 主输入区
   - 主工作区改成单个 `workspace-panel`
   - 新增三类视图：
     - `results-view`
     - `system-view`
     - `insights-view`
   - 结果区再拆成四个可切换子面板：
     - `query-panel`
     - `evidence-panel`
     - `answer-panel`
     - `trace-panel`

2. 重写 `src/uses_indexer/web/styles.css`
   - 改成控制台式布局
   - 默认 `body` 不滚动
   - 使用固定工作区高度
   - 新增更丰富的背景动效：
     - mesh
     - halo
     - pulse grid
   - 优化按钮、卡片、状态条、标签页和切换面板动效

3. 重写 `src/uses_indexer/web/app.js`
   - 新增视图切换逻辑：
     - `setView`
     - `setSubpanel`
     - `activatePanelById`
   - 让不同动作自动激活最合适的结果子面板
   - 提升交互反馈和切换节奏

4. 更新文档
   - `docs/FRONTEND_DESIGN.md`
   - `docs/FRONTEND_TECHNICAL.md`
   - 补充单屏重构的设计与技术说明

### 结论

- 当前前端已经从“长页面原型”升级成“单屏可切换控制台”
- 页面首屏噪音更低，信息组织更聚焦
- 交互和动效都比上一版更贴近现代桌面产品，而不是 AI 模板页

## [1.2.42] - 2026-04-22

### Step 49: 修复视图切换失效并补回系统说明内容

### 本步目标

- 修复顶部菜单点击后内容区没有明显切换的问题
- 把系统视图中丢失的接口说明和工作流说明补回来
- 降低浏览器缓存导致的“页面没更新”错觉

### 本步改动

1. 更新 `src/uses_indexer/web/app.js`
   - `setView()` 现在会显式控制：
     - `hidden`
     - `workspace-view-active`
   - `activatePanelById()` 现在会显式控制：
     - `hidden`
     - `subpanel-active`
   - 初始化时会主动执行：
     - `setView("results-view")`
     - `activateDefaultPanels()`

2. 更新 `src/uses_indexer/web/index.html`
   - 为非激活子面板增加初始 `hidden`
   - 补回系统视图内容：
     - `Capabilities`
     - `Interface Guide`
   - 补充更多首屏小卡片，减少“元素变少”的空洞感

3. 更新 `src/uses_indexer/web/styles.css`
   - 为 `workspace-view[hidden]` 和 `subpanel[hidden]` 增加显式隐藏规则
   - 增加：
     - `mini-card`
     - `capability-card`
     - `guide-card`
   - 系统视图改为更完整的多区块布局

4. 更新 `src/uses_indexer/api.py`
   - 所有响应头增加：
     - `Cache-Control: no-store, max-age=0`
   - 避免浏览器继续使用旧版静态资源

5. 更新文档
   - `docs/FRONTEND_TECHNICAL.md`
   - 补充本轮交互修复说明

### 结论

- 现在顶部菜单和结果子面板都改成了更稳的显式切换
- 系统视图重新补回了接口与工作流说明，不再只有空框架
- 刷新后应能直接看到新资源，而不会继续命中旧缓存

## [1.2.43] - 2026-04-22

### Step 50: 把顶部菜单改成主页 + 三个独立页面

### 本步目标

- 解决横屏网页模式下“点按钮后内容需要往下滑但外层被锁住”的使用问题
- 把导航从“同页切块”升级成“主页 + 三个独立详情页”
- 保留固定框架，同时允许每个页面内容区单独滚动

### 本步改动

1. 更新 `src/uses_indexer/web/index.html`
   - 顶部导航改成：
     - `主页`
     - `结果视图`
     - `系统视图`
     - `设计说明`
   - 新增 `home-view`
   - 主页保留当前首屏语义
   - 结果 / 系统 / 设计 继续作为三个详情页面

2. 更新 `src/uses_indexer/web/app.js`
   - 新增 `setPage(pageId)`
   - 区分：
     - `home`
     - `results-view`
     - `system-view`
     - `insights-view`
   - 运行 query/evidence/answer 时自动跳到 `结果视图`
   - 路由信息同时同步到主页和系统页

3. 更新 `src/uses_indexer/web/styles.css`
   - 新增：
     - `.page-home`
     - `.page-detail`
     - `.home-board`
   - 详情页内容区支持单独滚动
   - 主页和详情页在横屏模式下不再混在一个不可滚动视野里

### 结论

- 现在顶部按钮语义已经变成真正的页面切换，而不是只切块
- 主页回到当前首屏
- 三个详情页都可以在固定框架内独立滚动

## [1.2.44] - 2026-04-22

### Step 51: 清理重复说明并收口主页布局

### 本步目标

- 去掉主页里和详情页重复的说明模块
- 让主页真正回到“概览 + 输入 + 主操作”的单屏结构
- 继续压缩无关说明文字，保留和项目直接相关的信息

### 本步改动

1. 更新 `src/uses_indexer/web/index.html`
   - 删除主页底部重复区：
     - `Home Overview`
     - `Quick Routes`
   - 保留：
     - 左侧索引概览
     - 右侧查询与分析入口
   - 主页不再重复展示系统页里已经存在的接口说明

2. 更新 `src/uses_indexer/web/app.js`
   - `setPage("home")` 改成真正的首页模式
   - 主页模式下不再尝试激活已删除的 `home-view`
   - 删除：
     - `home-route-cloud`
     - 对应的空状态和渲染逻辑

3. 更新 `src/uses_indexer/web/styles.css`
   - 主页模式下隐藏 `workspace-panel`
   - 主页改成只占用双栏主舞台
   - 删除：
     - `.home-board`
     - `.home-overview`
     - `.home-routes`
   - 调整首页高度分配，让左右主区在 16:9 横屏里更自然撑满

### 结论

- 当前主页已经从“首页 + 一段重复详情区”收口成真正的入口页
- 结果 / 系统 / 设计说明三个页面继续承担深入信息展示
- 页面结构更符合桌面单屏工作台，而不是拼接型长页面

## [1.2.45] - 2026-04-22

### Step 52: 增加智能体页面与 Agent Gateway

### 本步目标

- 给当前前端增加一个真正可用的智能体页面
- 新增后端 `/agent/providers` 和 `/agent/chat`
- 用后端代理的方式接外部 Hermes / OpenClaw / OpenAI-compatible 服务

### 本步改动

1. 新增 `src/uses_indexer/agent_gateway.py`
   - 新增 `AgentGateway`
   - 支持从 `.env` 加载 3 类 provider：
     - `openai-compatible`
     - `hermes`
     - `openclaw`
   - 当前 Hermes / OpenClaw 先按 `openai-compatible` HTTP chat 协议接入
   - 发送到外部智能体前，会先组装：
     - retrieval
     - evidence
     - answer draft

2. 更新 `src/uses_indexer/api.py`
   - 新增：
     - `GET /agent/providers`
     - `POST /agent/chat`
   - `CodebaseApi` 支持注入 `agent_gateway`
   - `/health.routes` 里补回 agent 接口，前端系统页能直接看到

3. 更新内置前端
   - `src/uses_indexer/web/index.html`
   - `src/uses_indexer/web/styles.css`
   - `src/uses_indexer/web/app.js`
   - 顶部导航新增：
     - `智能体`
   - 新增独立 `agent-view`
   - 页面包含：
     - provider 选择
     - 会话区
     - retrieval / evidence / draft 开关
     - context preview

4. 更新配置与导出
   - `.env.example` 补充：
     - `USES_INDEXER_AGENT_OPENAI_*`
     - `USES_INDEXER_AGENT_HERMES_*`
     - `USES_INDEXER_AGENT_OPENCLAW_*`
   - `src/uses_indexer/__init__.py` 导出：
     - `AgentGateway`
     - `AgentConfigError`
     - `AgentRequestError`

5. 更新测试与文档
   - `tests/test_api.py` 增加 `/agent/providers` 和 `/agent/chat` 回归
   - 更新：
     - `README.md`
     - `docs/USAGE.md`
     - `docs/DEPLOYMENT.md`
     - `docs/FRONTEND_DESIGN.md`
     - `docs/FRONTEND_TECHNICAL.md`

### 结论

- 当前前端已经不只是“检索工作台”，还多了一条“把本地代码上下文交给外部智能体”的入口
- 推荐的接法已经固定成：
  - `前端 -> uses-indexer API -> 外部 Hermes/OpenClaw`
- 这样后续继续扩协议、流式输出或多 provider 路由都更容易

## [1.2.46] - 2026-04-22

### Step 53: 把智能体页改成真正的聊天式界面

### 本步目标

- 去掉智能体页里过多的控制台说明和右侧配置卡片
- 改成更接近真实聊天产品的布局
- 让页面支持：
  - 上传图片
  - 上传文件
  - 选择模型
  - 通过弹层配置模型

### 本步改动

1. 重做 `src/uses_indexer/web/index.html`
   - 删除右侧大块配置区
   - 智能体页改成：
     - 顶部模型选择 + 配置按钮
     - 中间聊天消息区
     - 底部输入区
     - 附件条
   - 新增：
     - 图片上传入口
     - 文件上传入口
     - 模型配置弹层

2. 重做 `src/uses_indexer/web/styles.css`
   - 新增更贴近聊天产品的样式：
     - `agent-shell`
     - `agent-topbar`
     - `agent-attachment-chip`
     - `agent-composer-card`
     - `modal-backdrop`
     - `modal-card`
   - 当前智能体页更接近“聊天页”而不是“控制台配置页”

3. 更新 `src/uses_indexer/web/app.js`
   - 删除旧的右侧上下文预览与附带项切换逻辑
   - 新增：
     - 附件读取与移除
     - 自定义模型本地存储
     - 模型配置弹层开关
     - 自定义 provider 覆写请求
   - 当前自定义配置保存在浏览器本地 `localStorage`

4. 更新 `src/uses_indexer/agent_gateway.py`
   - 新增 `provider_override`
   - 新增 `attachments`
   - 支持前端用自定义模型配置直接发起请求
   - 文本文件会带内容摘要
   - 图片会带 `data_url`

### 结论

- 当前智能体页已经从“技术控制台式配置页”改成了“聊天式产品页”
- 页面上只保留用户真正需要的操作：
  - 传图
  - 传文件
  - 选模型
  - 配模型
  - 发消息

## [1.2.47] - 2026-04-22

### Step 54: 修正智能体页交互层级并拉满页面布局

### 本步目标

- 修复智能体页弹层不该默认出现的问题
- 把 `设置` 拆成：
  - `设置模型`
  - `添加模型`
- 让聊天区更占屏，输入区更薄
- 让 `设计说明` 页真正撑满整个工作区

### 本步改动

1. 更新 `src/uses_indexer/web/index.html`
   - `设置` 改成下拉菜单入口
   - 菜单项拆成：
     - `设置模型`
     - `添加模型`
   - 模型弹层仍保留，但不再默认展示
   - 输入区 `textarea` 从 `rows=5` 压到 `rows=3`

2. 更新 `src/uses_indexer/web/styles.css`
   - 增加：
     - `.agent-settings-wrap`
     - `.agent-settings-menu`
     - `.agent-settings-item`
   - `modal-backdrop[hidden]` 显式 `display: none`
   - 缩小聊天输入区卡片高度和整体 padding
   - 让 `agent-transcript` 更占高度
   - `insight-board` 改成更稳定的等高网格，撑满设计说明页

3. 更新 `src/uses_indexer/web/app.js`
   - 新增：
     - `toggleAgentSettingsMenu()`
     - `closeAgentSettingsMenu()`
   - 点击 `设置` 只展开菜单
   - 只有点击：
     - `设置模型`
     - `添加模型`
     才会真正打开弹层
   - 点击菜单外区域会自动关闭菜单
   - `openAgentConfigModal()` 支持区分：
     - 编辑已有模型
     - 新增自定义模型

### 结论

- 当前智能体页的交互层级已经更合理：
  - 先点 `设置`
  - 再选具体动作
  - 最后才弹配置层
- 聊天页的主视觉重心重新回到消息区
- `设计说明` 页也不再有明显的“悬空感”和未填满工作区的问题

## [1.2.48] - 2026-04-22

### Step 55: 强化检索关系召回与精确意图排序

### 本步目标

- 让 `表写入 / 变量写入 / 失败路径` 这三类问题拥有更直接的关系召回入口
- 保持原有 `assignment / failure block / call edge` 的高质量 top hit 不被新关系召回反压
- 给后续检索继续调优留下一组更贴近业务问题类型的回归测试

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增精确关系边召回：
     - `relation_table_edge`
     - `relation_variable_edge`
   - 新增失败处理块关系召回：
     - `relation_failure_block`
   - 让表名、变量名和失败处理块能够直接从 `edges / blocks` 进入第一层候选集合，而不只依赖 `procedure_features` 或 FTS 命中

2. 更新 `src/uses_indexer/rerank.py`
   - 新增：
     - `intent_exact_table_edge`
     - `intent_exact_variable_edge`
     - `intent_exact_failure_block`
   - 下调变量边关系的抢位权重，保证 `@var 在哪里赋值` 这类问题仍然优先落到真正的赋值语句上

3. 更新 `tests/test_indexer.py`
   - 新增回归：
     - `test_query_index_uses_exact_table_edge_relation_for_table_write_queries`
     - `test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries`
     - `test_query_index_uses_failure_block_relation_for_failure_queries`
   - 同时保住原有：
     - `intent_aware_rerank`
     - `direct_call_edge_relation`

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py -k "direct_call_edge_relation or exact_table_edge_relation or exact_variable_edge_relation or failure_block_relation or intent_aware_rerank"`
- 结果：`5 passed`

### 结论

- 当前检索链路已经不再只对“调用链”具备强关系召回，`表写入 / 变量写入 / 失败路径` 也有了更直接的第一层候选来源
- 新增关系召回没有破坏原本高质量的 top hit：
  - 变量赋值问题仍然优先命中真实赋值语句
  - 失败路径问题仍然优先命中真正的失败处理块

## [1.2.49] - 2026-04-22

### Step 56: 细化增量建库执行粒度，新增 metadata-only 刷新

### 本步目标

- 让增量建库不再把所有“文件有变化”的情况都视作结构重建
- 当文件只是 XML 头信息、中文名、对象号、参数历史等 metadata 变化时，只做 metadata refresh
- 保留原有结构重建、向量复用和 parse cache 行为

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 给 `indexed_files` 增加：
     - `code_fingerprint`
     - `unit_signature`
   - 新增：
     - `_unit_code_fingerprint()`
     - `_unit_signature()`
     - `_is_metadata_only_change()`
     - `_ensure_index_state_schema()`
   - 增量建库现在会区分：
     - `metadata_only`
     - `reindexed`
     - `removed`
   - 返回新增：
     - `incremental_changes.metadata_only`
     - `incremental_changes.reindexed`
     - `incremental_execution_plan`
   - `incremental_scope.summary` 现在也会单独统计 `metadata_refresh_count`

2. 更新 `src/uses_indexer/index_write.py`
   - 新增 `refresh_unit_metadata()`
   - 当代码语句未变时，只刷新：
     - `files`
     - `procedures`
     - `procedures_fts`
     - `histories`
     - `params`
   - 不再重建：
     - `statements`
     - `chunks`
     - `blocks`
     - `edges`
     - `chunk_vectors`

3. 更新 `tests/test_indexer.py`
   - 新增：
     - `test_incremental_build_refreshes_metadata_without_rebuilding_structure`
   - 同时调整原有向量复用测试，使其适配新的 `metadata_only` 分支

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py -k "incremental_build_supports_incremental_updates or metadata_without_rebuilding_structure or reuses_existing_chunk_vectors_when_embedding_text_matches or reuses_parsed_units_with_cache"`
- 结果：`3 passed`

### 结论

- 当前增量建库已经从“文件级变更即重建”推进到“结构变更重建、metadata 变更刷新”的双分支执行模型
- 这一步带来的直接收益是：
  - metadata-only 改动不再触发 statements/chunks/blocks/edges 重建
  - 向量填充和向量复用逻辑也不会被无意义地触发

## [1.2.50] - 2026-04-22

### Step 57: 强化问答证据压缩与 grounded answer 结构

### 本步目标

- 让回答层不只是“有 citations”，而是更明确地区分主候选、次候选和证据强度
- 让不同 query type 在压缩证据时优先保留更直接的证据
- 保持 `draft / llm_grounded` 两档行为不变

### 本步改动

1. 更新 `src/uses_indexer/answer_strategy.py`
   - 新增 `_evidence_priority()`
   - 新增 `_evidence_strength()`
   - 证据压缩不再简单按原始顺序截断，而是按 `query_type` 优先保留：
     - 调用链直连边
     - 表访问直连边
     - 变量赋值语句
     - 失败处理块
   - 压缩上下文中新增 `Evidence strength`

2. 更新 `src/uses_indexer/qa.py`
   - `draft_answer` 新增：
     - `primary_candidate`
     - `secondary_candidates`
   - 回答正文新增：
     - `主候选`
     - `次候选`

3. 更新 `src/uses_indexer/answering.py`
   - `final_answer.grounding.citations` 现在会带：
     - `retrieval_source`
     - `match_source`
   - `final_answer.grounding` 现在会带：
     - `primary_candidate`
     - `secondary_candidates`

4. 更新测试
   - `tests/test_qa.py`
   - `tests/test_answering.py`
   - 验证主候选、次候选和 grounding 引用结构

### 验证

- `PYTHONPATH=src pytest -q tests/test_qa.py tests/test_answering.py`
- 结果：`9 passed`

### 结论

- 当前问答链路已经不只是“基于 evidence 生成一段话”，而是开始产出可直接复核的回答结构：
  - 主候选
  - 次候选
  - 引用来源
  - 证据强度

## [1.2.51] - 2026-04-22

### Step 58: 优化建库性能，新增 no-op 增量短路与批量向量写入

### 本步目标

- 当增量建库发现没有任何文件变化时，直接短路返回
- 减少 `populate_missing_chunk_vectors()` 中逐条写库的细碎开销
- 保持已有增量更新、metadata refresh、向量复用行为不变

### 本步改动

1. 更新 `src/uses_indexer/index_build.py`
   - 新增无变更增量短路：
     - `noop = true`
   - 当 `added / changed / removed` 全为空时：
     - 不再进入 parse
     - 不再进入 delete / rebuild
     - 不再进入向量填充
   - 返回中新增：
     - `incremental_execution_plan.noop`
     - `noop`

2. 更新 `src/uses_indexer/index_write.py`
   - `populate_missing_chunk_vectors()` 改为批量准备 `batch_rows`
   - 使用 `executemany()` 批量写入 `chunk_vectors`
   - provider 计数也改为按 batch 汇总

3. 更新 `tests/test_indexer.py`
   - 新增：
     - `test_incremental_build_short_circuits_when_nothing_changed`
   - 验证：
     - 不触发 parser
     - 不触发 embedder
     - 直接返回 `noop`

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py -k "incremental_build_short_circuits_when_nothing_changed or incremental_build_supports_incremental_updates or metadata_without_rebuilding_structure or reuses_parsed_units_with_cache or reuses_existing_chunk_vectors_when_embedding_text_matches"`
- 结果：`4 passed`

### 结论

- 当前建库链路已经不再把“无变化增量”当成一次完整任务去执行
- 向量补齐阶段的写库动作也从逐条执行改成了批量提交，更适合后续大库场景

## [1.2.52] - 2026-04-22

### Step 59: 深化检索邻居扩展与增量建库状态缓存

### 本步目标

- 让检索在 `表 / 变量 / 失败路径` 这类问题里，不只看到直连命中，还能补上一跳邻居过程
- 让增量建库在写回 `indexed_files` 状态时，不再重新 parse 所有未变化文件

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增 `_run_neighbor_expansion_queries()`
   - 对以下意图开启邻居扩展：
     - `wants_table_sql`
     - `wants_variable`
     - `wants_failure_flow`
   - 基于直连关系候选，补充一跳：
     - `incoming` caller
     - `outgoing` callee
   - 新增召回源：
     - `relation_neighbor_context`

2. 更新 `src/uses_indexer/rerank.py`
   - 新增：
     - `intent_table_neighbor_context`
     - `intent_variable_neighbor_context`
     - `intent_failure_neighbor_context`
   - 让邻居上下文保留为“可见的辅助证据”，但不去抢掉直连主证据

3. 更新 `src/uses_indexer/index_build.py`
   - `indexed_files` 状态写回新增 `preserved_state`
   - 增量建库现在会复用未变化文件已有的：
     - `fingerprint`
     - `code_fingerprint`
     - `unit_signature`
   - 不再为了写回状态而重新 parse 未变文件

4. 更新测试
   - `tests/test_indexer.py`
   - 覆盖：
     - `test_query_index_expands_neighbor_context_for_table_flow_queries`
     - `test_incremental_build_reuses_parsed_units_with_cache`
     - `test_incremental_build_short_circuits_when_nothing_changed`

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py -k "reuses_parsed_units_with_cache or expands_neighbor_context_for_table_flow_queries or incremental_build_short_circuits_when_nothing_changed"`
- 结果：`3 passed`

### 结论

- 当前检索已经开始具备“主证据 + 一跳上下文”的组合能力，更适合回答带路径感的问题
- 当前增量建库除了 `noop` 和 `metadata_only` 之外，连状态写回阶段也不再会把未变文件重新 parse 一遍

## [1.2.53] - 2026-04-22

### Step 60: 增加受控多跳链路扩展与低置信度回答降级

### 本步目标

- 让调用链问题在出现“链路 / 路径”语义时，可以补充 2 到 3 跳上下文
- 让低置信度问题不再硬走 LLM 或普通 draft，而是显式降级成 guarded draft

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增 `_run_multi_hop_expansion_queries()`
   - 当问题满足：
     - `wants_call_chain = true`
     - 且 query token 包含 `链路 / 路径 / 调用链 / 上游 / 下游`
   - 会补充：
     - `relation_multi_hop_context`
   - 多跳候选只作为辅助链路证据，不替代直连调用边

2. 更新 `src/uses_indexer/rerank.py`
   - 新增 `intent_multi_hop_context`
   - 让多跳过程能进入结果区，但仍然弱于直连 `calls_procedure`

3. 更新 `src/uses_indexer/strategy_config.py`
   - `AnswerExecutionPolicy` 新增：
     - `low_confidence_threshold`
     - `prefer_guarded_draft_on_low_confidence`

4. 更新 `src/uses_indexer/answering.py`
   - 当 draft confidence 低于阈值时：
     - 不再继续走普通最终回答
     - 返回 `guarded_draft`
   - `final_answer` 新增：
     - `tier = guarded_low_confidence`
     - `review_required = true`

5. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_expands_multi_hop_context_for_call_chain_paths`
   - `tests/test_answering.py`
     - `test_answer_uses_guarded_draft_for_low_confidence_questions`

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py -k "multi_hop_context_for_call_chain_paths or expands_neighbor_context_for_table_flow_queries" tests/test_answering.py -k "guarded_draft_for_low_confidence_questions or uses_draft_when_llm_not_configured"`
- 结果：`2 passed`

### 结论

- 当前检索已经具备：
  - 直连关系证据
  - 一跳邻居上下文
  - 受控多跳链路补充
- 当前回答层也开始区分：
  - 正常 grounded answer
  - 低置信度 guarded draft

## [1.2.54] - 2026-04-22

### Step 61: 增加显式过程对的路径桥接与证据合流

### 本步目标

- 对“过程 A 到过程 B 的调用链路”这类显式双过程问题，补最短调用路径桥接
- 让路径桥接命中不会因为 evidence 去重而在问答阶段丢掉

### 本步改动

1. 更新 `src/uses_indexer/rerank.py`
   - `analyze_query()` 新增：
     - `procedure_terms_ordered`
   - 让显式过程名顺序可以被后续路径桥接逻辑直接使用
   - 新增 `intent_path_bridge`

2. 更新 `src/uses_indexer/context_fetch.py`
   - 新增 `find_shortest_call_path()`
   - 基于 `calls_procedure` 边做受控 BFS
   - 只求短路径，不展开无限调用图
   - 同时把过程别名解析改成大小写不敏感

3. 更新 `src/uses_indexer/retrieval.py`
   - 新增 `_run_path_bridge_queries()`
   - 当问题满足：
     - `wants_call_chain = true`
     - 且显式出现两个过程名
   - 会补充：
     - `relation_path_bridge`
   - 当前只把桥接路径中的中间过程作为高价值候选加入结果

4. 更新 `src/uses_indexer/evidence.py`
   - 同一上下文如果被多路召回同时命中：
     - 不再直接丢弃后来的重复候选
     - 而是把 `reasons` 与 `matched_via` 合并回已有 evidence block
   - 这样精确路径桥接不会在 evidence 去重时消失

5. 更新 `src/uses_indexer/qa.py`
   - 草答会优先提取 `path_bridge=` reason
   - 对调用链问题增加：
     - `调用链桥接路径为 A -> B -> C`
   - 让最终 draft 不只是给过程位置，还能给出链路骨架

6. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_uses_explicit_path_bridge_for_two_procedures`
     - 调整调用链上下文测试，让它接受更强的 `relation_path_bridge`
     - 调整过程特征关系测试，让它接受 `matched_via` 合流后的表达
   - `tests/test_qa.py`
     - `test_ask_surfaces_path_bridge_summary_for_call_chain_questions`

### 验证

- `python3 -m py_compile src/uses_indexer/context_fetch.py src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/qa.py src/uses_indexer/evidence.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_expands_call_chain_context_for_path_queries`
- `PYTHONPATH=src pytest -q tests/test_qa.py::test_ask_builds_prompt_and_draft_answer tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions tests/test_answering.py::test_answer_uses_draft_when_llm_not_configured`
- 结果：`6 passed`

### 结论

- 当前检索对“显式过程对路径题”已经不只会给：
  - 起点过程
  - 终点过程
- 还会额外给：
  - 中间桥接过程
  - 明确的路径字符串

- 当前 evidence 也更稳了：
  - 同一上下文的多路命中会合流
  - 精确路径信息不会在后续问答阶段被去重吃掉

## [1.2.55] - 2026-04-22

### Step 62: 强化过程级知识构建并修复跨文件调用特征顺序依赖

### 本步目标

- 让 `procedure_features` 里的调用图知识更完整
- 修复 `incoming_callers / bridge` 受文件建库顺序影响的问题
- 让问答层能更稳定利用“桥接过程”这种过程级知识

### 本步改动

1. 更新 `src/uses_indexer/index_write.py`
   - `upsert_procedure_features()` 新增：
     - `call_fan_in`
     - `call_fan_out`
     - `is_call_bridge`
   - `summary_text` 现在会补：
     - `called by ...`
     - `bridge in=X out=Y`
   - 新增 `refresh_all_procedure_features()`

2. 更新 `src/uses_indexer/index_build.py`
   - 全量建库完成主写入后，统一调用：
     - `refresh_all_procedure_features()`
   - 增量建库完成增量写入后，也统一调用：
     - `refresh_all_procedure_features()`
   - 这样过程级特征从“单文件即时统计”升级成了“全局二次刷新”

3. 更新 `src/uses_indexer/rerank.py`
   - 调用链类问题新增过程级特征加权：
     - `feature_call_bridge`
     - `feature_call_fan_balance`

4. 更新 `src/uses_indexer/qa.py`
   - 草答现在会从 `path_bridge=A->B->C` 中提取中间过程
   - 增加：
     - `桥接候选过程: ...`
   - 同时把桥接路径和桥接候选纳入置信度判断

5. 更新测试
   - `tests/test_indexer.py`
     - 验证 `procedure_features` 包含：
       - `call_fan_in`
       - `call_fan_out`
       - `is_call_bridge`
     - 验证桥接路径检索仍然成立
   - `tests/test_qa.py`
     - 验证草答会显式输出：
       - `桥接候选过程`
       - `调用链桥接路径`

### 验证

- `python3 -m py_compile src/uses_indexer/index_write.py src/uses_indexer/index_build.py src/uses_indexer/rerank.py src/uses_indexer/qa.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- 结果：`4 passed`

### 结论

- 当前“知识构建”这条线已经不只是存摘要文本了，而是开始稳定沉淀过程级调用图特征
- 当前 `procedure_features` 的质量不再受文件处理顺序影响
- 当前调用链问答不仅能给路径，还能更稳定地点出“桥接过程”

## [1.2.56] - 2026-04-22

### Step 63: 强化失败路径知识构建与失败题草答稳定性

### 本步目标

- 让失败处理结构进入过程级知识底座
- 让“失败在哪里处理”这类问题在草答阶段就能更稳定给出失败块信息

### 本步改动

1. 更新 `src/uses_indexer/index_write.py`
   - `procedure_features.feature_flags` 新增：
     - `failure_handler_count`
     - `exception_handler_count`
     - `when_others_handler_count`
     - `has_failure_handlers`
   - `summary_text` 新增：
     - `failure blocks failure=X, exception=Y, when_others=Z`

2. 更新 `src/uses_indexer/rerank.py`
   - `failure_flow` 问题新增过程级失败特征加权：
     - `feature_failure_handlers`
     - `feature_failure_handler_counts`

3. 更新 `src/uses_indexer/qa.py`
   - 失败题草答会优先提取 recovered blocks 中的：
     - `failure_handler`
     - `exception_handler`
     - `when_others_handler`
   - 新增：
     - `AF_SAMPLE 覆盖失败处理块 ...`
   - 失败题置信度估计新增：
     - `relation_failure_block` 命中加分
     - `failure_hints` 加分
   - 同时在缺少直接失败块证据时，显式补充不确定点

4. 更新测试
   - `tests/test_indexer.py`
     - 验证过程级失败特征和失败摘要已经写入 `procedure_features`
   - `tests/test_qa.py`
     - 新增 `test_ask_surfaces_failure_path_summary_for_failure_questions`
     - 验证失败题草答会输出失败处理块摘要，并提升到 `medium/high`

### 验证

- `python3 -m py_compile src/uses_indexer/index_write.py src/uses_indexer/rerank.py src/uses_indexer/qa.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_qa.py::test_ask_surfaces_failure_path_summary_for_failure_questions tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- 结果：`4 passed`

### 结论

- 当前“知识构建”对失败路径已经不再只停留在块级恢复，而是开始把失败结构沉淀到过程级摘要
- 当前“问答流程”对失败题也更像真实排障回答：
  - 会直接指出失败处理块
  - 并在证据不足时给出更明确的不确定点

## [1.2.57] - 2026-04-22

### Step 64: 强化结构化过程画像、focus-chain 检索与草答画像提示

### 本步目标

- 继续做正向增强，不再围绕失败路径展开
- 把过程级知识底座从“文本摘要”为主，推进到“结构化画像 + 文本摘要”并行
- 让表访问链、变量传递链这类问题具备更直接的链路补全能力
- 让草答阶段开始显式利用过程画像，而不是只看 excerpt

### 本步改动

1. 更新 `src/uses_indexer/schema.py`
   - `procedure_features` 新增：
     - `profile_json`
   - 用来稳定保存结构化过程画像，而不是只保留 `summary_text`

2. 更新 `src/uses_indexer/index_build.py`
   - 运行时 schema 检查新增：
     - 缺失 `profile_json` 时自动补列
   - 增量建库不再总是全量刷新所有过程画像
   - 改为调用：
     - `refresh_procedure_features_for_paths()`
   - 只刷新 changed / added / metadata-only 文件，以及一跳 caller / callee 邻居

3. 更新 `src/uses_indexer/index_write.py`
   - `procedure_features` 新增结构化过程画像：
     - `primary_inputs`
     - `primary_outputs`
     - `core_calls`
     - `core_callers`
     - `core_read_tables`
     - `core_write_tables`
     - `core_variable_writes`
     - `dynamic_tables`
     - `call_role`
     - `table_access_role`
     - `topic_role`
     - `metadata_role`
   - `summary_text` 继续增强：
     - 输入参数摘要
     - 输出参数摘要
     - 动态表摘要
   - 当动态表没有在 recovered blocks 中直接命中时，允许从 `read_tables/write_tables` 回退识别，避免画像遗漏

4. 更新 `src/uses_indexer/retrieval.py`
   - 检索候选开始显式携带：
     - `procedure_profile`
   - 新增 focus-chain 召回：
     - `relation_table_chain_context`
     - `relation_variable_chain_context`
   - 以“表访问命中 / 变量写入命中”为 seed，补一段反向调用链上下文
   - 不再只支持两过程调用链桥接

5. 更新 `src/uses_indexer/rerank.py`
   - query type 进一步细化并调整优先级：
     - 表问题优先于泛化 call-chain 词命中
     - 变量问题优先于泛化 call-chain 词命中
   - rerank 新增过程画像感知：
     - 更重视 `table_access_role`
     - 更重视 `call_role=bridge`
     - 更重视变量写入画像
     - metadata / topic 角色也开始显式参与加权

6. 更新 `src/uses_indexer/evidence.py`
   - evidence block 现在会保留：
     - `procedure_profile`
   - 后续 QA 和前端调试都能直接消费

7. 更新 `src/uses_indexer/qa.py`
   - `primary_candidate` / `secondary_candidates` 开始保留：
     - `procedure_profile`
   - `secondary_candidates` 新增稳定去重，避免同一过程多次重复输出
   - 针对不同 query type 新增画像提示：
     - 表问题：
       - `核心表访问包括 ...`
     - 变量问题：
       - `主要变量写入包括 ...`
     - metadata / topic 问题：
       - 角色型 hint
   - 草答开始更明确利用“过程画像”，而不只是依赖 evidence excerpt

8. 更新测试
   - `tests/test_indexer.py`
     - 验证 `procedure_features.profile_json` 已写入并包含：
       - `primary_inputs`
       - `table_access_role`
       - `dynamic_tables`
     - 新增：
       - `test_query_index_expands_table_chain_context_for_flow_queries`
   - `tests/test_qa.py`
     - 新增：
       - `test_ask_surfaces_profile_hints_for_table_queries`

### 验证

- `python3 -m py_compile src/uses_indexer/schema.py src/uses_indexer/index_build.py src/uses_indexer/index_write.py src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/qa.py src/uses_indexer/evidence.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_qa.py::test_ask_surfaces_profile_hints_for_table_queries tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions`
- 结果：`5 passed`

### 结论

- 当前“知识构建”已经从“摘要文本增强”进一步进入“结构化过程画像”阶段
- 当前“检索流程”不再只支持过程对桥接，也开始支持表访问链和变量传递链的正向扩展
- 当前“问答流程”在草答阶段就能显式输出更贴近业务语义的过程画像提示
- 当前“构建索引”在增量场景下也开始做更细粒度的过程画像局部刷新，避免每次都全量重算

## [1.2.58] - 2026-04-22

### Step 65: 对齐 query type、过程画像精排与问题类型草答模板

### 本步目标

- 继续做正向增强，不碰失败路径专项优化
- 让 query type 更细、更稳定地传导到 rerank 和草答
- 让主候选 / 次候选判定更稳，避免重复候选和同质化回答

### 本步改动

1. 更新 `src/uses_indexer/rerank.py`
   - query type 进一步细化：
     - `table_access`
     - `variable_flow`
     - `implementation_location`
     - `metadata_definition`
     - `topic_publish`
   - `feature_bonus` 开始更完整接入新的 query type
   - 新增 `procedure_profile` 精排：
     - `profile_exact_table_focus`
     - `profile_exact_variable_focus`
     - `profile_exact_caller_focus`
     - `profile_exact_callee_focus`
   - 这样 exact focus 不只看命中文本，也会看过程画像里是否真的覆盖对应核心表、变量和调用目标

2. 更新 `src/uses_indexer/qa.py`
   - 新增 query-type 对应的段落标题：
     - `上游调用`
     - `下游调用`
     - `表写入 / 表读取 / 表访问`
     - `变量写入 / 变量读取 / 变量链路`
     - `Metadata 定义`
     - `Topic 发布`
   - `top_evidence` 先按候选唯一性去重，避免多路召回把同一过程重复带进草答
   - `secondary_candidates` 增加稳定去重
   - 置信度开始参考主次候选分差：
     - 主候选明显领先时更自信
     - 多候选分数咬得很近时更保守

3. 更新测试
   - `tests/test_qa.py`
     - `test_ask_tracks_primary_and_secondary_candidates`
       - 验证次候选不重复
     - `test_ask_uses_query_specific_section_for_callers`
       - 验证“被谁调用”问题会走 `上游调用` 模板

### 验证

- `python3 -m py_compile src/uses_indexer/rerank.py src/uses_indexer/qa.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_qa.py::test_ask_tracks_primary_and_secondary_candidates tests/test_qa.py::test_ask_uses_query_specific_section_for_callers tests/test_qa.py::test_ask_surfaces_profile_hints_for_table_queries tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- 结果：`9 passed`

### 结论

- 当前“检索流程”不再只做召回和通用重排，而是开始更稳定地区分问题类型并利用过程画像做 exact focus 精排
- 当前“问答流程”也更像真正的产品回答层：
  - 不同问题类型有不同标题和表达方式
  - 次候选更干净
  - 置信度也不再只看命中数量

## [1.2.59] - 2026-04-22

### Step 66: 扩展 topic / metadata 画像并升级过程级候选聚合

### 本步目标

- 继续做正向增强，把 topic / metadata 也真正纳入过程画像
- 让主候选 / 次候选从“单条 evidence 排序”升级成“过程级聚合判定”
- 让 `fts_chunk / fts_action` 这类命中也能稳定带出过程画像

### 本步改动

1. 更新 `src/uses_indexer/index_write.py`
   - `profile_json` 新增：
     - `core_topics`
     - `core_metadata_refs`
   - 这样 `procedure_features` 不再只覆盖表访问、变量和调用，也开始显式覆盖：
     - topic 发布角色
     - metadata 引用角色

2. 更新 `src/uses_indexer/rerank.py`
   - `procedure_profile` 精排继续增强：
     - `profile_exact_topic_focus`
     - `profile_exact_metadata_focus`
   - 对 topic / metadata 问题，开始显式用画像里的 `core_topics / core_metadata_refs` 做 exact focus 加权
   - 同时把 `topic_publish` 的 query type 优先级提升到 `metadata_definition` 之前，避免 topic 问题被 metadata 抢走

3. 更新 `src/uses_indexer/evidence.py`
   - 当 retrieval candidate 自身没带 `procedure_profile` 时
   - evidence 组装阶段会回查 `procedure_features.profile_json`
   - 用 `procedure_id` 补全画像
   - 避免 `fts_chunk / fts_action` 命中在问答阶段丢失画像信息

4. 更新 `src/uses_indexer/qa.py`
   - 主候选 / 次候选不再只看单条 evidence
   - 改为按：
     - `procedure_name + file_path`
     - 聚合 `aggregate_score`
     - 汇总 `matched_via`
   - 主候选会选择该过程内分数最高的那条 evidence 作为代表位置
   - topic / metadata 问题新增更明确的画像提示：
     - `发布主题包括 ...`
     - `核心 metadata 引用包括 ...`
   - 置信度评估也开始参考聚合后的主次候选分差

5. 更新测试
   - `tests/test_indexer.py`
     - 新增 `test_build_index_populates_topic_profile_fields`
       - 验证 `core_topics / topic_role / has_mc_topics`
   - `tests/test_qa.py`
     - `test_ask_tracks_primary_and_secondary_candidates`
       - 额外验证 `aggregate_score`
     - 新增 `test_ask_surfaces_topic_profile_hints_for_topic_queries`

### 验证

- `python3 -m py_compile src/uses_indexer/evidence.py src/uses_indexer/index_write.py src/uses_indexer/rerank.py src/uses_indexer/qa.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_topic_profile_fields tests/test_qa.py::test_ask_tracks_primary_and_secondary_candidates tests/test_qa.py::test_ask_uses_query_specific_section_for_callers tests/test_qa.py::test_ask_surfaces_profile_hints_for_table_queries tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_qa.py::test_ask_surfaces_path_bridge_summary_for_call_chain_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- 结果：`11 passed`

### 结论

- 当前“知识构建”已经把 topic / metadata 也正式沉淀进过程画像
- 当前“问答流程”里的主候选 / 次候选更像过程级判断，不再受单条 evidence 排序抖动影响
- 当前 `procedure_profile` 也能更稳定地从 retrieval 贯穿到 evidence、QA 和前端调试视图

## [1.2.60] - 2026-04-23

### Step 67: 前移过程级聚合到检索层并暴露聚合指标

### 本步目标

- 把“过程级聚合”从 QA 层继续前移到 retrieval 层
- 让 topic / metadata / table / variable 这类问题在检索排序阶段就受益于同过程多路支撑
- 同时保持原有精确命中的排序优势，不降低准确度

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 在 `retrieve_candidates()` 进入 rerank 前新增：
     - `_hydrate_missing_procedure_profiles()`
   - 对来自 `fts_chunk / fts_action / fts_statement / vector_chunk` 等路径、但未携带画像的候选
   - 用 `procedure_id -> procedure_features.profile_json` 统一补齐 `procedure_profile`

2. 更新 `src/uses_indexer/retrieval.py`
   - 新增检索层的过程级聚合加权：
     - `_apply_procedure_aggregate_rerank()`
   - 按 `procedure_name + file_path` 聚合：
     - `aggregate_score`
     - `aggregate_hit_count`
     - `matched_via`
   - 对以下 query type 做适度聚合加权：
     - `topic_publish`
     - `metadata_definition`
     - `table_write / table_read / table_access`
     - `variable_write / variable_read / variable_flow`
   - reasons 新增：
     - `procedure_aggregate_hits=...`
     - `procedure_aggregate_bonus=...`

3. 更新 `src/uses_indexer/retrieval.py`
   - query 命中输出新增：
     - `aggregate_score`
     - `aggregate_hit_count`
   - 前端和 debug trace 现在都可以直接看到“这是单条命中强，还是同一过程多路支撑强”

4. 更新测试
   - `tests/test_indexer.py`
     - 新增 `test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries`
     - 新增 `test_query_index_prefers_aggregate_topic_hits_without_hurting_table_focus`
   - 继续回归已有：
     - 表边关系
     - 表链路扩展
     - 显式路径桥接
     - exact focus 优先于 vector-only 上下文

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py tests/test_indexer.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_indexer.py::test_query_index_prefers_aggregate_topic_hits_without_hurting_table_focus tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- `PYTHONPATH=src pytest -q tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_qa.py::test_ask_tracks_primary_and_secondary_candidates tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- 结果：`9 passed`

### 结论

- 当前“检索流程”已经开始在排序阶段利用同一过程的多路支撑信号
- 当前 `procedure_profile` 能更稳定地从 retrieval 开始贯穿到 query/evidence/QA
- 当前“过程级聚合”已经形成上下游闭环：
  - retrieval 负责聚合排序
  - QA 负责聚合候选表达

## [1.2.61] - 2026-04-23

### Step 68: 细化 topic / metadata 精排并收紧证据面

### 本步目标

- 继续做正向增强，重点优化 topic / metadata 这两类非失败问题
- 让这两类问题不只在检索排序更稳，也在 evidence 选择层更干净

### 本步改动

1. 更新 `src/uses_indexer/rerank.py`
   - topic / metadata 精排进一步细化：
     - metadata 问题对 `fts_procedure_feature / fts_edge` 额外加轻量 bonus
     - topic 问题对 `fts_procedure_feature / fts_action / fts_edge` 额外加轻量 bonus
   - 同时也显式利用画像里的：
     - `core_topics`
     - `core_metadata_refs`
   - 新增：
     - `feature_topic_profile`
     - `feature_metadata_profile`
     - `intent_topic_feature_source`
     - `intent_metadata_feature_source`

2. 更新 `src/uses_indexer/evidence.py`
   - evidence 选择开始感知 query type
   - 对：
     - `topic_publish`
     - `metadata_definition`
   - 同一过程的 evidence cap 从默认 `2` 收紧到 `1`
   - evidence block 现在显式保留：
     - `aggregate_score`
     - `aggregate_hit_count`
   - 并在 duplicate context merge 时同步维护这两个聚合指标

3. 更新测试
   - `tests/test_indexer.py`
     - 新增 `test_assemble_evidence_limits_topic_queries_to_one_procedure_context`
       - 验证 topic 问题的 evidence 面只保留一个过程上下文
   - 回归：
     - topic 聚合指标
     - topic 提示
     - 表链路 / 路径桥接 / exact focus 不回退

### 验证

- `python3 -m py_compile src/uses_indexer/evidence.py src/uses_indexer/rerank.py tests/test_indexer.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_indexer.py::test_query_index_prefers_aggregate_topic_hits_without_hurting_table_focus tests/test_indexer.py::test_assemble_evidence_limits_topic_queries_to_one_procedure_context tests/test_indexer.py::test_related_context_exposes_mc_published_topics tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- 结果：`10 passed`

### 结论

- 当前 topic / metadata 问题已经不只是“能命中”，而是开始具备更明确的专属精排配方
- 当前 evidence 选择层也会配合 query type 收紧证据面，让最终输出更干净
- 当前这类问题的优化仍然没有牺牲表链路、路径桥接和 exact focus 的已有准确度

## [1.2.62] - 2026-04-23

### Step 69: 让 evidence 选择按 query type 偏好证据块

### 本步目标

- 继续做正向增强，不只优化“检索结果是谁”，也优化“最终交给用户的第一块证据是什么”
- 让 evidence assembly 本身开始按 query type 偏好更合适的证据块

### 本步改动

1. 更新 `src/uses_indexer/evidence.py`
   - 在 `assemble_evidence()` 中新增：
     - `_sort_candidates_for_evidence()`
     - `_evidence_priority_score()`
   - 这层排序会根据 `query_type` 调整 evidence 候选顺序：
     - 表问题优先 `table_access / relation_table_edge / relation_table_chain_context`
     - 变量问题优先 `variable_flow / relation_variable_edge / relation_variable_chain_context`
     - 调用链问题优先 `call_chain / relation_path_bridge / relation_multi_hop_context`
     - topic / metadata 问题优先 `fts_procedure_feature / fts_action / fts_edge`

2. evidence 选择策略说明
   - 这层不是替代 retrieval 主排序
   - 而是把“已经较大概率找对的候选过程”再往更适合展示的证据块上收口
   - 目标是让最终 evidence block：
     - 更贴近问题类型
     - 更适合直接用于 QA / LLM / 前端展示

3. 更新测试
   - `tests/test_indexer.py`
     - `test_assemble_evidence_prefers_table_access_context_for_table_queries`
       - 验证表问题首证据会稳定携带表访问 reasons、画像和 SQL block 关系
   - 同时继续回归：
     - topic evidence 限制
     - topic 聚合指标
     - 表链路 / 路径桥接 / exact focus

### 验证

- `python3 -m py_compile src/uses_indexer/evidence.py tests/test_indexer.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_assemble_evidence_prefers_table_access_context_for_table_queries tests/test_indexer.py::test_assemble_evidence_limits_topic_queries_to_one_procedure_context tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_indexer.py::test_query_index_prefers_aggregate_topic_hits_without_hurting_table_focus tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_expands_table_chain_context_for_flow_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
- 结果：`10 passed`

### 结论

- 当前系统不只是“谁排第一”更合理了，“第一块证据长什么样”也开始更合理
- 当前 evidence 层已经开始按问题类型交付更贴近用户预期的证据面
- 当前这轮优化仍然没有破坏已有的表链路、路径桥接和 exact focus 准确度

## [1.2.63] - 2026-04-23

### Step 70: 收紧 topic 意图识别并统一 query-type 摘要模板

### 本步目标

- 继续做正向增强，进一步减少 query type 误判
- 让 table / variable / metadata / topic 这几类问题在：
  - 意图识别
  - rerank 配方
  - 草答首句
  三层更一致

### 本步改动

1. 更新 `src/uses_indexer/rerank.py`
   - topic 意图识别不再直接用宽泛的 `mc` 子串命中
   - 改为：
     - 先看显式 topic 关键词：
       - `topic / 消息 / 发布 / 消息中心 / 主题`
     - 再看 token 级单独的 `mc`
   - 这样像：
     - `CNST_MC_UFT_OPTSYNC metadata 定义`
   - 不会再被误分进 `topic_publish`

2. 更新 `src/uses_indexer/rerank.py`
   - table / variable 的专属精排继续细化：
     - `intent_table_feature_source`
     - `intent_variable_feature_source`
   - metadata / topic 的专属精排也继续细化：
     - `intent_metadata_feature_source`
     - `intent_topic_feature_source`
     - `feature_metadata_profile`
     - `feature_topic_profile`

3. 更新 `src/uses_indexer/qa.py`
   - 首句摘要标签进一步产品化：
     - `最关键的表访问过程`
     - `最关键的变量链路过程`
     - `最关键的 metadata 定义过程`
     - `最关键的 topic 发布过程`
   - 不再让不同 query type 共用同一种“实现位置”式表达

4. 更新测试
   - `tests/test_qa.py`
     - 新增 `test_ask_uses_metadata_specific_summary_for_metadata_queries`
       - 验证 metadata 问题不会误分到 topic
       - 验证会走 `Metadata 定义` 模板
   - 继续回归：
     - topic profile hints
     - table profile hints
     - primary/secondary candidates
     - topic 聚合指标
     - exact table / exact focus

### 验证

- `python3 -m py_compile src/uses_indexer/rerank.py src/uses_indexer/qa.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_surfaces_profile_hints_for_table_queries tests/test_qa.py::test_ask_tracks_primary_and_secondary_candidates tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- 结果：`8 passed`

### 结论

- 当前 query type 的误判面又收窄了一层，尤其是 metadata / topic 之间
- 当前 table / variable / metadata / topic 四类问题的产品化表达更统一
- 当前优化仍然没有破坏既有的 exact focus 和表链路准确度

## [1.2.64] - 2026-04-23

### Step 71: 统一 query-specific 摘要模板与 review_required 降级策略

### 本步目标

- 继续做正向增强，让 QA 草答从第一段开始就更像“按问题类型定制”
- 把 `draft_answer.review_required` 真正贯通到回答层
- 在多候选接近、需要人工复核的场景下，更稳地走 guarded draft，而不是硬给普通回答

### 本步改动

1. 更新 `src/uses_indexer/qa.py`
   - 新增 `QUERY_SUMMARY_HINT_LABELS`
   - 在 `_build_draft_answer()` 中增加 `_build_query_specific_summary()`
   - 这层摘要会直接读取 `primary_candidate.procedure_profile`，对不同 query type 输出更轻量、更贴近问题的第一段提示：
     - 表问题：
       - `表读取重点 / 表写入重点 / 表访问重点`
     - 变量问题：
       - `变量读取重点 / 变量写入重点 / 变量链路重点`
     - metadata / topic：
       - `metadata 定义重点 / topic 发布重点`
     - callers / callees：
       - `上游调用重点 / 下游调用重点`

2. 更新 `src/uses_indexer/answering.py`
   - `answer()` 现在会读取 `draft_answer.review_required`
   - guarded draft 不再只在明显低置信度时触发
   - 现在对于：
     - `review_required = true`
     - 且整体只有中等置信度
   - 也会主动走 guarded fallback
   - `_build_guarded_low_confidence_answer()` 现在会附带：
     - `其他近似候选`
   - `_build_result()` 也会把 `review_required` 显式带回最终结果

3. 更新测试
   - `tests/test_qa.py`
     - `test_ask_uses_metadata_specific_summary_for_metadata_queries`
       - 验证 metadata 问题会使用 metadata 专属摘要
     - `test_ask_keeps_review_not_required_for_clear_table_candidate`
       - 验证清晰表问题不会被误判成需要复核
   - `tests/test_answering.py`
     - `test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
       - 验证多候选接近且 `review_required = true` 时，会主动走 guarded draft

### 验证

- `python3 -m py_compile src/uses_indexer/qa.py src/uses_indexer/answering.py tests/test_qa.py tests/test_answering.py`
- `PYTHONPATH=src pytest -q tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_keeps_review_not_required_for_clear_table_candidate tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question tests/test_answering.py::test_answer_uses_draft_when_llm_not_configured tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_keeps_exact_call_focus_above_vector_only_context`
- 结果：`9 passed`

### 结论

- 当前 QA 首段摘要已经更像按 query type 定制出来的结果，而不是统一模板后面再补一个 section
- 当前回答层已经开始统一消费 `review_required`，多候选接近时会更稳、更诚实地降级
- 当前这轮优化仍然没有破坏 topic / metadata / table / call focus 的既有准确度

## [1.2.65] - 2026-04-23

### Step 72: 强化关系索引、结构化知识底座与回答决策状态

### 本步目标

- 不再做小幅打分微调，而是直接增强三类底层能力：
  - 更强的关系索引
  - 更硬的结构化知识底座
  - 更体系化的回答决策
- 保持“不降低原有准确度”的前提下，把变量流、表流、动态 SQL 和多候选回答这些高价值能力再往前推一层

### 本步改动

1. 更新 `src/uses_indexer/semantic_recovery.py`
   - 动态字符串恢复新增：
     - `a + b`
     - `a || b`
   - 新增单引号赋值字符串解析
   - `sprintf / snprintf` 中的变量占位保留更稳
   - 这样动态 SQL 不再只依赖直接字符串或 format 调用，拼接表达式也能稳定恢复

2. 更新 `src/uses_indexer/index_write.py`
   - 新增 `reads_variable` 显式边
   - `procedure_profile` 新增结构化知识字段：
     - `core_variable_reads`
     - `table_entities`
     - `variable_entities`
     - `dynamic_sql_templates`
     - `relation_graph`
   - `feature_flags` 新增：
     - `has_variable_reads`
     - `has_dynamic_sql`
   - `summary_text` 现在也会补：
     - `reads vars ...`
     - `dynamic sql ...`

3. 更新 `src/uses_indexer/retrieval.py`
   - 变量精确关系召回不再只支持写边：
     - `reads_variable`
     - `writes_variable`
   - 新增：
     - `relation_variable_flow_bridge`
     - `relation_table_flow_bridge`
   - 也就是变量流 / 表流开始具备自己的过程级桥接召回，而不再只是依赖普通 evidence 命中

4. 更新 `src/uses_indexer/rerank.py`
   - 修复变量问题中的一个更本质的误加分问题：
     - 以前 SQL 里的 `=` 也可能被误判成“变量写入信号”
     - 现在只在真正的 `writes_variable / assignment` 场景里加这部分分
   - 对变量读取问题，`reads_variable` 现在会得到更明确的 read-focused bonus
   - 对 `relation_variable_flow_bridge / relation_table_flow_bridge` 也补了专属 bonus
   - `profile_exact_variable_focus` 现在也会看 `core_variable_reads`

5. 更新 `src/uses_indexer/qa.py` 和 `src/uses_indexer/answering.py`
   - draft answer 新增 `decision`
     - `state`
     - `primary_score`
     - `secondary_score`
     - `score_gap`
     - `conflict_summary`
   - answering 最终结果也会把这层 `decision` 带回 grounding
   - guarded draft 会显式输出：
     - `决策提示`
     - `其他近似候选`
   - 这样“为什么保守、为什么需要人工复核”开始变成显式信息，而不是只藏在分数逻辑里

6. 更新测试
   - `tests/test_indexer.py`
     - 扩展动态 SQL fixture，覆盖字符串拼接恢复
     - 验证：
       - `core_variable_reads`
       - `dynamic_sql_templates`
       - `relation_graph`
       - `relation_variable_flow_bridge`
       - `relation_table_flow_bridge`
       - 变量读取精确边
   - `tests/test_qa.py`
     - 验证 decision 状态在清晰候选和接近候选下的行为
   - `tests/test_answering.py`
     - 验证 guarded answer 会带 `decision` 和更明确的 conflict 提示

### 验证

- `python3 -m py_compile src/uses_indexer/semantic_recovery.py src/uses_indexer/index_write.py src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/qa.py src/uses_indexer/answering.py tests/test_indexer.py tests/test_qa.py tests/test_answering.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_indexer.py::test_query_index_recovers_dynamic_sql_tables tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_expands_variable_flow_bridge_for_flow_queries tests/test_indexer.py::test_query_index_expands_table_flow_bridge_for_table_queries tests/test_qa.py::test_ask_keeps_review_not_required_for_clear_table_candidate tests/test_qa.py::test_ask_marks_decision_competitive_for_close_candidates tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
- 结果：`9 passed`

### 结论

- 当前变量流 / 表流已经开始具备更像“一等关系对象”的检索入口，而不再只是靠普通语句命中
- 当前知识底座开始从 profile 摘要继续推进到结构化 `relation_graph`
- 当前回答层已经不只给候选和置信度，而是开始显式表达决策状态和冲突说明

## [1.2.66] - 2026-04-23

### Step 73: 推进跨过程 flow path 检索与 conflict-kind 决策

### 本步目标

- 把变量流 / 表流从“bridge”进一步推进到“跨过程路径”
- 让 evidence / QA 真正消费这些 flow path，而不只是检索层内部知道
- 让回答决策不只停留在 `state`，继续升级成可分类的 conflict system

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增 `_run_entity_path_queries()`
   - 在出现：
     - `链路`
     - `路径`
     - `流转`
     - `透传`
   - 且问题指向 table / variable 时，新增：
     - `relation_variable_flow_path`
     - `relation_table_flow_path`
   - 这类候选不再只是单点 bridge，而是会携带：
     - `variable_flow_path=...`
     - `table_flow_path=...`
     - `..._flow_step=i/n`

2. 更新 `src/uses_indexer/rerank.py`
   - 对：
     - `relation_variable_flow_path`
     - `relation_table_flow_path`
   - 补专属 intent bonus
   - 保证它们在真正的 path 问题里比普通 bridge / 普通 chunk 更有机会排到前面

3. 更新 `src/uses_indexer/evidence.py`
   - evidence 选择层也开始优先考虑：
     - `relation_variable_flow_path`
     - `relation_table_flow_path`
   - 让最终展示给 QA / LLM / 前端的第一块证据更像“链路证据”，而不只是单条读写命中

4. 更新 `src/uses_indexer/qa.py`
   - 草答开始显式提取：
     - `变量链路为 ...`
     - `表访问链路为 ...`
   - `decision` 结构新增：
     - `conflict_kind`
     - `recommendation`
   - 当前可表达的冲突类型包括：
     - `candidate_competition`
     - `evidence_divergence`
     - `low_confidence`

5. 更新 `src/uses_indexer/answering.py`
   - guarded draft 现在会把：
     - `recommendation`
   - 也显式写进最终答案
   - 这样低置信度和多候选接近时，不只是“告诉你不稳”，还会告诉你下一步该怎么查

6. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_expands_variable_flow_path_for_path_queries`
     - `test_query_index_expands_table_flow_path_for_path_queries`
   - `tests/test_qa.py`
     - `test_ask_surfaces_flow_path_summary_for_variable_path_queries`
   - `tests/test_answering.py`
     - 验证 guarded answer 会输出 `处理建议`

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/evidence.py src/uses_indexer/qa.py src/uses_indexer/answering.py tests/test_indexer.py tests/test_qa.py tests/test_answering.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_expands_variable_flow_path_for_path_queries tests/test_indexer.py::test_query_index_expands_table_flow_path_for_path_queries tests/test_indexer.py::test_query_index_expands_variable_flow_bridge_for_flow_queries tests/test_indexer.py::test_query_index_expands_table_flow_bridge_for_table_queries tests/test_qa.py::test_ask_surfaces_flow_path_summary_for_variable_path_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
- 结果：`6 passed`
- 额外回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前变量流 / 表流已经不只是“读写角色桥接”，而是开始具备明确的跨过程路径召回
- 当前 flow path 已经贯通到 evidence 和 QA，而不是停留在检索内部
- 当前回答决策已经从 `state` 进一步升级成 `conflict_kind + recommendation`

## [1.2.67] - 2026-04-23

### Step 74: 让 relation_graph 直接参与检索，并细化路径与证据一致性

### 本步目标

- 让结构化 `relation_graph` 不再只是 profile 附带信息，而开始直接参与检索
- 让 flow path 从“存在路径”升级成“主路径 / 辅助路径 + 端点 / 桥接角色”
- 让回答决策继续从 `conflict_kind` 往“证据一致性”推进

### 本步改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增 `_run_relation_graph_queries()`
   - 新增召回来源：
     - `relation_graph_profile`
   - 当前会直接利用 `procedure_profile.relation_graph` 匹配：
     - tables
     - variables
     - topics
     - metadata_refs
   - 同时 `relation_*_flow_path` 现在新增：
     - `..._flow_priority=main|support`
     - `flow_path_role=endpoint|bridge`

2. 更新 `src/uses_indexer/rerank.py`
   - `relation_graph_profile` 现在对：
     - table
     - variable
     - topic
     - metadata
   - 都有专属加权
   - 这样结构化画像召回不再只是“能进来”，而是会在对应问题类型里拿到合理排序

3. 更新 `src/uses_indexer/evidence.py`
   - evidence 选择层开始优先照顾：
     - `relation_graph_profile`
   - 让最终展示给 QA/LLM 的证据，更可能是“结构化命中的过程画像”，而不只是文本片段

4. 更新 `src/uses_indexer/qa.py`
   - flow path 摘要现在会区分：
     - 主链路
     - 辅助链路
   - `decision` 新增：
     - `evidence_alignment`
       - `aligned`
       - `divergent`
       - `partial`

5. 更新 `src/uses_indexer/answering.py`
   - guarded answer 现在会把：
     - `证据一致性`
   - 也写回最终回答

6. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_uses_relation_graph_profile_for_variable_queries`
     - flow path 断言新增 `..._flow_priority=main`
   - `tests/test_qa.py`
     - `test_ask_decision_reports_evidence_alignment`
   - `tests/test_answering.py`
     - 验证 guarded answer 会输出 `证据一致性`

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/evidence.py src/uses_indexer/qa.py src/uses_indexer/answering.py tests/test_indexer.py tests/test_qa.py tests/test_answering.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_expands_variable_flow_path_for_path_queries tests/test_indexer.py::test_query_index_expands_table_flow_path_for_path_queries tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_qa.py::test_ask_surfaces_flow_path_summary_for_variable_path_queries tests/test_qa.py::test_ask_decision_reports_evidence_alignment tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
- 结果：`6 passed`
- 额外回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前 `relation_graph` 已经不只是知识底座，还开始直接参与检索
- 当前 flow path 已经从“能找出来”推进到“能解释主辅路径和桥接角色”
- 当前回答决策开始显式表达证据是否一致，而不只是冲突类型

## 1.2.52 - 结构化关系图角色直通 Retrieval / Evidence / QA

### 背景

上一轮已经让 `relation_graph` 直接参与召回，但结构化命中的“实体角色”还没有稳定贯穿到排序、证据和草答层。

这会带来两个问题：

- 检索虽然能命中 `relation_graph_profile`，但 rerank 还不知道它命中的到底是 `read / write / read_write`
- QA 也不一定会把这条“结构化关系图命中”明确说出来

### 本轮改动

1. 更新 `src/uses_indexer/retrieval.py`
   - `relation_graph_profile` 命中现在会显式带上：
     - `graph_focus_type`
     - `graph_focus_value`
     - `graph_focus_role`
   - 当前端、debug 和后续层拿到 hit 时，已经可以知道：
     - 命中的是 table / variable / topic / metadata 哪一类
     - 命中的具体值
     - 它在关系图里的角色

2. 更新 `src/uses_indexer/rerank.py`
   - 对 `relation_graph_profile` 新增 role-aware intent bonus
   - table / variable 问题现在不只看“命中了关系图”，还会看：
     - 当前问题偏 read 还是 write
     - 当前命中的 graph role 是否匹配
   - 这样结构化关系图开始真正参与“精排决策”，而不是只做补充召回

3. 更新 `src/uses_indexer/evidence.py`
   - evidence block 现在也保留：
     - `graph_focus_type`
     - `graph_focus_value`
     - `graph_focus_role`
   - 这样后续 QA / LLM / 前端调试面板都能看到结构化关系图命中的上下文

4. 更新 `src/uses_indexer/qa.py`
   - 当 top evidence 命中 `relation_graph_profile` 时，会显式输出：
     - `XX 的结构化关系图显示 YY 角色为 ZZ`
   - 同时新增兜底逻辑：
     - 即使 top evidence 不是 `relation_graph_profile`
     - 只要主候选过程画像里的 `relation_graph` 能匹配当前 table / variable focus
     - 也会补出同样的结构化关系图提示

5. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_uses_relation_graph_profile_for_variable_queries`
       - 验证 variable 查询会暴露 `graph_focus_type / graph_focus_role`
   - `tests/test_qa.py`
     - `test_ask_decision_reports_evidence_alignment`
       - 验证草答会显式带出“结构化关系图显示 ...”

### 验证

- `python3 -m py_compile src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/evidence.py src/uses_indexer/qa.py tests/test_indexer.py tests/test_qa.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_qa.py::test_ask_decision_reports_evidence_alignment tests/test_indexer.py::test_query_index_expands_variable_flow_path_for_path_queries tests/test_indexer.py::test_query_index_expands_table_flow_path_for_path_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
  - 结果：`5 passed`
- 额外保护回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_uses_explicit_path_bridge_for_two_procedures tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前 `relation_graph` 已经不只是“能召回”，而是开始把命中的角色语义真正传递到排序、证据和草答层
- 当前 table / variable 查询在结构化关系图上的 read/write 判断更稳定了
- 当前 QA 输出开始更明确地区分“这是文本命中”还是“这是结构化关系图命中”

## 1.2.53 - graph focus context 与 agent 决策对齐

### 背景

上一轮已经让 `relation_graph_profile` 能够直接参与召回和精排，但还有两个硬缺口：

- 结构化关系图更多还是“命中过程”，还没有稳定落成更适合最终展示的 chunk 级主证据
- 聊天页 agent 虽然能吃检索结果，但还没有和 grounded answer 共用同一套 `decision`

### 本轮改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 新增：
     - `relation_graph_focus_context`
   - 它会基于 `relation_graph_profile` 命中的过程，再从同一过程里挑选更贴合 query type 的 chunk 作为上下文主证据
   - 当前会优先按 query type 偏好：
     - table -> `table_access`
     - variable -> `variable_flow`
     - metadata -> `metadata_block`
     - topic -> `call_chain / control_flow`
   - 所以结构化关系图现在不只“指出哪个过程”，还开始“指出这个过程里哪块上下文最像主证据”

2. 更新 `src/uses_indexer/rerank.py`
   - 新增对 `relation_graph_focus_context` 的 query-type intent bonus
   - table / variable / metadata / topic 问题现在会更偏好这种“结构化图命中 + 过程内代表性 chunk”组合证据

3. 更新 `src/uses_indexer/evidence.py`
   - evidence 选择层开始把 `relation_graph_focus_context` 当作高价值候选
   - 当前最终展示给 QA/LLM 的第一块证据，更容易是“结构化关系图落到 chunk 上的上下文”

4. 更新 `src/uses_indexer/agent_gateway.py`
   - `answer_draft` 不再只传一个简化文本
   - 现在会把 grounded QA 的关键决策一起带进 agent 上下文：
     - `query_type`
     - `confidence`
     - `review_required`
     - `decision`
     - `primary_candidate`
     - `secondary_candidates`
     - `summary_points`
     - `uncertainties`
   - 同时修复了原来错误读取 `draft_answer.text` 的问题，改成正确使用 `draft_answer.answer`

5. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_uses_relation_graph_focus_context_for_variable_queries`
       - 验证变量链路查询已经能把 `relation_graph_focus_context` 暴露进公开 hit
   - `tests/test_api.py`
     - `test_agent_gateway_context_bundle_exposes_grounded_decision`
       - 验证聊天页 agent 上下文已经带上 grounded decision / primary_candidate / review_required

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_indexer.py::test_query_index_uses_relation_graph_focus_context_for_variable_queries tests/test_indexer.py::test_query_index_expands_variable_flow_path_for_path_queries tests/test_api.py::test_agent_gateway_context_bundle_exposes_grounded_decision tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
  - 结果：`5 passed`
- 额外保护回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前 `relation_graph` 已经不只会命中过程，还开始稳定地产出更像主证据的 chunk 上下文
- 当前聊天页 agent 已经开始和 grounded answer 共用同一套 `decision / candidate / review_required` 判断
- 当前“关系索引 / 知识底座 / 回答决策”这三条线开始真正收敛到同一套结构化语义上

## 1.2.54 - relation_graph 物化为结构化索引表

### 背景

前几轮已经让 `relation_graph`：

- 进入 `procedure_profile`
- 进入 `relation_graph_profile`
- 再进入 `relation_graph_focus_context`

但它还有一个明显短板：

- 当前检索仍然主要是从 `procedure_features.profile_json` 里现扫 `relation_graph`

这意味着：

- 关系索引虽然在变强，但仍然不够“索引化”
- 知识底座虽然在变厚，但很多结构化知识仍然没有被持久化成一等表

### 本轮改动

1. 更新 `src/uses_indexer/schema.py`
   - 新增结构化索引表：
     - `procedure_graph_entities`
   - 字段包括：
     - `procedure_id`
     - `file_id`
     - `procedure_name`
     - `entity_type`
     - `entity_name`
     - `entity_role`
     - `ordinal`
     - `detail_json`
   - 同时补了：
     - `idx_procedure_graph_entities_proc`
     - `idx_procedure_graph_entities_lookup`

2. 更新 `src/uses_indexer/index_build.py`
   - 运行时 schema 迁移现在会确保：
     - `procedure_graph_entities`
   - 在旧库上也能自动补这张表和索引

3. 更新 `src/uses_indexer/index_write.py`
   - `upsert_procedure_features()` 现在不只会写 `profile_json`
   - 还会把 `relation_graph` 里的：
     - tables
     - variables
     - topics
     - metadata refs
   - 同步物化到 `procedure_graph_entities`

4. 更新 `src/uses_indexer/retrieval.py`
   - `_run_relation_graph_queries()` 现在优先走：
     - `procedure_graph_entities`
   - 而不是先全量扫 `procedure_features.profile_json`
   - 如果旧库还没有这张表，才回退到原来的 JSON 扫描逻辑

5. 顺手更新 `src/uses_indexer/agent_gateway.py`
   - 在前一轮统一 `decision` 的基础上，又把 grounded QA 的决策摘要显式写进 agent prompt
   - 让聊天页 agent 更容易直接遵循：
     - query type
     - review_required
     - primary_candidate
     - evidence_alignment

6. 更新测试
   - `tests/test_indexer.py`
     - `test_build_index_populates_chunk_features_and_procedure_features`
       - 现在会验证 `procedure_graph_entities` 的实体行
   - 继续保护：
     - `relation_graph_profile`
     - `relation_graph_focus_context`
     - agent grounded decision 上下文

### 验证

- `python3 -m py_compile src/uses_indexer/schema.py src/uses_indexer/index_build.py src/uses_indexer/index_write.py src/uses_indexer/retrieval.py src/uses_indexer/agent_gateway.py tests/test_indexer.py tests/test_api.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_indexer.py::test_query_index_uses_relation_graph_focus_context_for_variable_queries tests/test_api.py::test_agent_gateway_context_bundle_exposes_grounded_decision tests/test_answering.py::test_answer_uses_guarded_draft_for_close_multi_candidate_table_question`
  - 结果：`5 passed`
- 额外保护回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前 `relation_graph` 已经从 profile 里的 JSON，进一步推进成数据库里的结构化索引表
- 当前“知识底座”开始不只是 rich profile，而是有了更像一等实体索引的持久化形态
- 当前后续 retrieval / evidence / QA 的很多增强，已经有了更稳的结构化基座

## 1.2.55 - procedure_graph_entities 升级为 FTS 主检索入口

### 背景

上一轮已经把 `relation_graph` 物化成：

- `procedure_graph_entities`

但它仍然主要承担：

- 精确实体匹配
- 结构化补召回

如果要继续解决“关系索引还不够强”和“知识底座还不够硬”，下一步更关键的是：

- 让这张结构化实体表本身成为 query-type 主检索配方的一部分

### 本轮改动

1. 更新 `src/uses_indexer/schema.py`
   - 新增：
     - `procedure_graph_entities_fts`
   - 这张 FTS 表索引：
     - `entity_type`
     - `entity_name`
     - `entity_role`
     - `procedure_name`
     - `file_path`

2. 更新 `src/uses_indexer/index_build.py`
   - 运行时 schema 迁移现在也会自动补：
     - `procedure_graph_entities_fts`
   - 保证旧库在增量/升级场景下也能得到这层能力

3. 更新 `src/uses_indexer/index_write.py`
   - 在写入 `procedure_graph_entities` 时，同步写入：
     - `procedure_graph_entities_fts`
   - 刷新过程画像时，也会先清理旧的 graph entity FTS 行，再重建新的行

4. 更新 `src/uses_indexer/retrieval.py`
   - 新增：
     - `_run_graph_entity_fts_queries()`
   - 当前 table / variable / topic / metadata 查询，会直接从 `procedure_graph_entities_fts` 做专门检索
   - 产出的召回来源是：
     - `fts_graph_entity`
   - 这样结构化知识图已经不只是“精确关系表”，而是开始拥有自己的全文主检索入口

5. 更新 `src/uses_indexer/rerank.py`
   - 对 `fts_graph_entity` 增加 query-type intent bonus：
     - table
     - variable
     - metadata
     - topic
   - 所以结构化实体 FTS 不只是“能进候选池”，还会参与主排序

6. 更新 `src/uses_indexer/evidence.py`
   - evidence 选择层也开始偏好：
     - `fts_graph_entity`
   - 这样最终证据面更容易出现“结构化实体命中 + 过程级画像 + 代表性 chunk”的组合

7. 更新测试
   - `tests/test_indexer.py`
     - `test_build_index_populates_chunk_features_and_procedure_features`
       - 现在会验证 `procedure_graph_entities_fts` 已写入
     - `test_query_index_uses_graph_entity_fts_for_topic_queries`
       - 验证 topic 查询已经能直接命中 `fts_graph_entity`
   - 变量关系图测试也更新为兼容：
     - 结构化关系图命中可能来自 `relation_graph_profile`
     - 也可能来自 `fts_graph_entity`

### 验证

- `python3 -m py_compile src/uses_indexer/schema.py src/uses_indexer/index_build.py src/uses_indexer/index_write.py src/uses_indexer/retrieval.py src/uses_indexer/rerank.py src/uses_indexer/evidence.py tests/test_indexer.py`
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_populates_chunk_features_and_procedure_features tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_indexer.py::test_query_index_uses_relation_graph_focus_context_for_variable_queries tests/test_indexer.py::test_query_index_uses_graph_entity_fts_for_topic_queries tests/test_api.py::test_agent_gateway_context_bundle_exposes_grounded_decision`
  - 结果：`5 passed`
- 额外保护回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前 `procedure_graph_entities` 已经不只是持久化表，还升级成了可全文检索的一等索引入口
- 当前 query-type 主检索配方开始真正优先消费结构化知识图，而不是只依赖普通文本 FTS
- 当前“关系索引”和“知识底座”两条主线开始在数据库层真正合并

## 1.2.56 - 代表性上下文前移到 Retrieval 层

### 背景

前几轮已经形成了这样一条结构化链路：

- `fts_graph_entity`
- `relation_graph_profile`
- `relation_graph_focus_context`

但还有一个重要问题没有彻底解决：

- 同一个过程里，虽然这些命中已经会合流
- 但 retrieval 层还没有稳定地把“最像主证据的那块上下文”显式提到前面

这会导致：

- query hits 看起来还是更偏过程级 summary
- 真正更像主证据的 `relation_graph_focus_context` 要等到 evidence 层才慢慢收口

### 本轮改动

1. 更新 `src/uses_indexer/retrieval.py`
   - 在 `_apply_procedure_aggregate_rerank()` 里新增“代表性上下文”判定
   - 当同一过程已经同时命中：
     - `relation_graph_focus_context`
     - `fts_graph_entity` 或 `relation_graph_profile`
   - 且问题类型属于：
     - table / variable / topic / metadata
   - 那么会把这组过程标记为：
     - `representative_context = true`

2. 在 retrieval 层增加 representative bonus
   - 如果候选本身就是 `relation_graph_focus_context`
   - 并且所在过程已经形成“结构化实体命中 + 代表性上下文”闭环
   - 就会拿到：
     - `representative_context_bonus`
   - 这样最像主证据的上下文块会更稳定地提前，而不是继续被过程级 summary 压住

3. 修正 group 统计方式
   - 之前过程聚合主要看单条 candidate 当前的 `retrieval_source`
   - 现在改成按 `matched_via` 全量统计
   - 所以像已经被合流的：
     - `fts_graph_entity`
     - `relation_graph_profile`
     - `relation_graph_focus_context`
   - 都会被正确识别进同一组结构化证据链

4. 更新公开命中结构
   - query hit 现在会带：
     - `representative_context`
   - 这样前端和调试视图可以直接区分：
     - 普通过程命中
     - 已经被判定为“代表性上下文”的过程/块命中

5. 更新测试
   - `tests/test_indexer.py`
     - `test_query_index_uses_relation_graph_focus_context_for_variable_queries`
       - 现在会验证 `representative_context` 已对外暴露

### 验证

- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_relation_graph_focus_context_for_variable_queries tests/test_indexer.py::test_query_index_uses_relation_graph_profile_for_variable_queries tests/test_indexer.py::test_query_index_uses_graph_entity_fts_for_topic_queries tests/test_api.py::test_agent_gateway_context_bundle_exposes_grounded_decision`
  - 结果：`4 passed`
- 额外保护回归：
  - `PYTHONPATH=src pytest -q tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries tests/test_indexer.py::test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries tests/test_indexer.py::test_query_index_uses_exact_table_edge_relation_for_table_write_queries tests/test_indexer.py::test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries tests/test_qa.py::test_ask_uses_metadata_specific_summary_for_metadata_queries tests/test_qa.py::test_ask_surfaces_topic_profile_hints_for_topic_queries tests/test_answering.py::test_answer_uses_guarded_draft_for_low_confidence_questions`
  - 结果：`7 passed`

### 结论

- 当前“结构化实体 -> 代表性上下文”这条链已经前移到 retrieval 层，而不只是 evidence 层
- 当前 query hits 开始更稳定地区分“过程命中”和“最像主证据的上下文命中”
- 当前 `graph entity -> focus context -> primary evidence` 的闭环更完整了

## 1.2.57 - 建库性能阶段化优化

### 背景

在关系图、过程画像和结构化实体索引变厚之后，全量代码索引构建开始明显变慢。只读排查确认：

- 当前构建进程持续满 CPU，不是死锁
- `.db-wal` 会持续增长到 GB 级
- 主库在大事务提交前仍显示很小
- `refresh_all_procedure_features()` 会对每个过程反复访问大表

### 本轮改动

1. 补齐建库阶段关键组合索引
   - `idx_params_file_category`
   - `idx_statements_procedure`
   - `idx_actions_procedure`
   - `idx_variable_refs_procedure_type`
   - `idx_edges_procedure_type`
   - `idx_edges_call_target`
   - `idx_edges_call_source`
   - `idx_blocks_procedure_type`

2. 拆分全量建库事务
   - `index_files` 单独提交
   - `refresh_procedure_features` 单独分批提交
   - `indexed_files` 状态写入单独提交
   - `populate_vectors` 继续保持独立批量事务

3. 过程画像分批刷新
   - `refresh_all_procedure_features()` 支持 batch 刷新
   - 默认每批 `500` 个过程
   - 每批独立提交，降低单次事务压力

4. 向量阶段可拆分
   - `build-index` 新增 `--skip-vectors`
   - `build_indexes.py` 新增 `--skip-vectors`
   - 后续可用 `--resume-vectors` 补齐 `chunk_vectors`

5. 构建阶段可观测性
   - `build-index` 新增 `--progress`
   - summary 的 `build_stats.phase_events` 会记录阶段耗时

### 验证

- `python3 -m py_compile src/uses_indexer/index_build.py src/uses_indexer/index_write.py src/uses_indexer/indexer.py src/uses_indexer/cli.py build_indexes.py build_all_indexes.py build_remaining_indexes.py tests/test_indexer.py`
  - 结果：通过
- `PYTHONPATH=src pytest -q tests/test_indexer.py::test_build_index_can_skip_vectors_and_creates_perf_indexes tests/test_indexer.py::test_build_index_populates_vectors_in_global_batches tests/test_indexer.py::test_build_index_resume_vectors_skips_existing_vectors`
  - 结果：`3 passed`

### 结论

- 下一次全量建库会更容易定位阶段耗时
- 过程画像刷新不再挤在一个超大事务里
- 大库可以先构建结构索引，再独立补齐向量
- 当前正在运行的旧构建进程不会被这些代码改动影响

## 1.2.58 - 文件索引阶段分批提交

### 背景

重新构建三类索引时，代码索引仍然在 `index_files` 阶段形成超大事务：

- `.db-wal` 在数分钟内增长到 GB 级
- 主库在文件索引阶段完成前仍然看不到已写入记录
- 上一轮优化已经拆开了阶段级事务，但 `index_files` 阶段内部还没有按文件批次提交

### 本轮改动

1. 全量构建先提交索引元数据
   - `_store_index_metadata()` 后立即 `commit`
   - 避免元数据也被包在文件索引大事务中

2. 文件索引阶段按批提交
   - `_index_files()` 新增 `batch_size`
   - 全量构建默认每 `500` 个文件提交一次
   - 最后一批不足 `500` 的文件也会在阶段结束时提交

3. 文件索引阶段输出批次进度
   - 开启 `--progress` 或脚本构建时输出：
     - `index_files_batch_committed`
     - `processed`
     - `total`

4. 同步更新文档
   - `docs/USAGE.md` 增加脚本输出说明
   - `docs/ARCHITECTURE.md` 增加文件索引分批提交说明
   - `docs/QUICKSTART.md` 修正 WAL 监控说明

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/index_build.py`
  - 结果：通过
- `PYTHONPATH=src python3 -m pytest tests/test_indexer.py tests/test_cli.py -q`
  - 结果：`73 passed`

### 结论

- 大库构建不再需要等整个 `index_files` 完成后才第一次提交
- 构建过程中可以通过 `index_files_batch_committed` 判断真实进度
- 如果中途失败，排查时可以看到已提交批次和主库落盘状态

## 1.2.59 - 表结构索引字段元数据补全

### 背景

查询 `uses_entrust` 表结构时，表结构索引可以命中表、字段和索引，但 `table_fields` 中的字段中文名、数据类型、字典类型为空。

排查确认：

- `business_table_index.db` 中存在 `uses_entrust`
- 表级信息、76 个字段、10 个索引均已入库
- 字段元数据为空不是表结构解析失败
- 根因是构建脚本默认把 `stdfield` 指向了 `upub_codes/uftstructure/stdfield.stdfield`
- 实际标准字段文件位于 `upub_codes/metadata/stdfield.stdfield`

### 本轮改动

1. 修正三索引构建脚本中的标准字段路径
   - `build_indexes.py`
   - 表结构索引默认使用 `upub_codes/metadata/stdfield.stdfield`

2. 增强表结构解析器
   - `TableField` 新增：
     - `description`
     - `public_type`
     - `comments`
   - `stdfield.stdfield` 解析：
     - `chineseName`
     - `dataType`
     - `dictionaryType`
     - `description`
     - `public_type`
   - `.uftstructure` 字段解析：
     - `properties.comments`

3. 增强表结构索引 schema
   - `table_fields` 新增：
     - `description`
     - `public_type`
     - `comments`
   - `table_fields_fts` 同步纳入这些字段，后续字段释义和展示类型也可被 FTS 检索

4. 增加标准字段路径自动发现
   - 如果未显式传 `--stdfield`
   - 或传入路径不存在
   - 会从 `source_root` 及其上级目录的 `metadata/stdfield.stdfield` 自动发现

5. 更新文档
   - `docs/QUICKSTART.md`
   - `docs/INDEX_SCHEMA.md`

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/table_parser.py src/uses_indexer/table_indexer.py build_indexes.py`
  - 结果：通过
- `PYTHONPATH=src python3 -m pytest tests/test_table_indexer.py tests/test_mcp.py::test_initialize_and_tool_listing -q`
  - 结果：`2 passed`
- 重建表结构索引：
  - `PYTHONPATH=src python3 -m uses_indexer build-table-index /Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure --db ./examples/business_table_index.db --stdfield /Users/songzuoqiang/Documents/agent/code/upub_codes/metadata/stdfield.stdfield --mdbobject /Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure/mdbobject.mdbobject --output ./examples/business_table_index_summary.json`
  - 结果：成功

### 重建后数据

- 表数量：`1204`
- 字段数量：`24672`
- 索引数量：`2542`
- 标准字段数量：`15262`
- 字段中文名覆盖：`24672 / 24672`
- 字段数据类型覆盖：`24672 / 24672`
- 字典类型覆盖：`5923 / 24672`

### uses_entrust 验证

现在只查索引库即可得到：

- `fund_account`：资产账户 / `HsFundAccount` / `C18`
- `entrust_no`：委托编号 / `HsSerialNo` / `N10`
- `branch_no`：分支机构 / `HsBranchNo` / 字典 `100` / `N5`
- `position_str`：定位串 / `HsPosStr` / `C100` / 注释为拼接规则

### 结论

- 这不是表结构索引整体构建失败，而是标准字段元数据没有加载
- 修复后表结构问答可以只依赖索引库回答字段含义、类型、字典和注释
- 后续查询表结构时不应回退原文件，除非明确是在调试索引构建问题

## 1.2.60 - 代码索引文件类型完整性检查

### 背景

检查代码索引和元数据索引构建内容是否完整时，对 `_collect_files()` 和当前数据库做了对账。

### 检查结果

1. 元数据索引
   - 当前收集并入库 `40` 个业务元数据文件
   - 已构建：
     - `55873` 个 metadata statement
     - `55873` 个 chunk
     - `55873` 个向量
     - `40` 条 procedure feature
   - 额外发现的 `30` 个 metadata 路径文件均属于 Eclipse 工作区 `.metadata/.plugins` 配置文件，不属于业务元数据，不应进入索引

2. 代码索引
   - 当前已构建数据库中有 `23798` 个文件
   - 对账发现 `code` 模式应收集 `23895` 个文件
   - 差异是 `97` 个 `.uftatomservice` 文件
   - `UftDslParser` 已支持 `.uftatomservice`
   - 但 `_collect_files(index_type="code")` 内部硬编码后缀列表时漏掉了 `.uftatomservice`

### 本轮改动

1. 修复代码索引文件收集规则
   - `_collect_files()` 的 `is_code_path()` 改为复用 `SUPPORTED_CODE_SUFFIXES`
   - 避免 parser 支持新代码后缀后，构建收集逻辑再次漏同步

2. 增加回归测试
   - `test_code_index_includes_uft_atom_service_files`
   - 验证 `index_type="code"` 会收集 `.uftatomservice`

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/index_build.py tests/test_indexer.py`
  - 结果：通过
- `PYTHONPATH=src python3 -m pytest tests/test_indexer.py::test_code_index_includes_uft_atom_service_files tests/test_indexer.py::test_build_index_can_skip_vectors_and_creates_perf_indexes tests/test_indexer.py::test_metadata_files_are_indexed_and_summarized -q`
  - 结果：`3 passed`
- 修复后文件收集数量：
  - `code`: `23895`
  - `metadata`: `40`
  - `all`: `23935`

### 结论

- 元数据索引边界基本合理
- 代码索引构建逻辑存在一个明确漏收集问题，已修复
- 当前磁盘上的 `business_code_index.db` 仍是旧构建结果，需要重建代码索引后才会包含这 `97` 个 `.uftatomservice`

## 1.2.61 - 前后端联调与功能号问答主候选修复

### 背景

对本地前端 `http://127.0.0.1:8000/` 做前后端联调时，接口整体可访问，但发现自然问题 `333002功能有哪些业务逻辑` 存在一个质量问题：

- `/query` 原先容易把包含 `@function_id == 333002` 的检查原子排在主服务前面
- `/answer` 草稿回答会因为同一检查原子多块命中，使用聚合分反超真正的功能号主服务
- 浏览器访问还会产生 `/favicon.ico` 404 噪音

### 本轮改动

1. 检索重排增强
   - `analyze_query()` 新增 `object_id_terms`
   - 对 `333002功能有哪些业务逻辑` 这类问题，把纯数字功能号识别为 `object_id` 焦点
   - `rerank_candidate()` 对候选 `object_id` 命中问题中的功能号增加 `object_id_focus_match`

2. 回答主候选判定增强
   - QA 草稿候选组保留 `best_item_score` 和 `first_rank`
   - 对 `location / implementation_location` 类型问题，优先使用最高单条证据决定主候选
   - 避免重复命中的次级检查块通过聚合分反超主服务

3. 前端服务静态资源补齐
   - `/favicon.ico` 返回 `204`
   - 清理浏览器联调时的无关 404

### 联调结果

- `GET /`：200
- `GET /ui`：200
- `GET /assets/styles.css`：200
- `GET /assets/app.js`：200
- `GET /favicon.ico`：204
- `GET /health`：200
- `GET /db-summary`：200，当前代码库 `files=23895`、`chunks=201368`
- `POST /query`：200，`333002功能有哪些业务逻辑` 第一命中 `LS_SESEXT_NORMALORDER_ENTER / object_id=333002`
- `POST /evidence`：200，第一证据 `LS_SESEXT_NORMALORDER_ENTER / object_id=333002`
- `POST /ask`：200，主候选 `LS_SESEXT_NORMALORDER_ENTER`
- `POST /answer`：200，最终回答主候选 `LS_SESEXT_NORMALORDER_ENTER`
- `POST /debug-bundle`：200，query/evidence/answer 打包正常
- `POST /agent/chat`：使用临时 OpenAI-compatible mock provider 验证通过，能携带检索上下文和附件返回

### 浏览器验证

- 主页 `整套分析` 可正常触发 query/evidence/answer/trace
- 结果页、系统页、设计说明页、智能体页、主页导航切换正常
- 智能体设置弹窗可正常打开

### 自动化验证

- `pytest tests/test_api.py::test_http_server_serves_json tests/test_indexer.py::test_query_index_prefers_object_id_for_business_logic_question tests/test_qa.py::test_ask_uses_best_object_id_hit_as_primary_for_location_question tests/test_qa.py::test_ask_builds_prompt_and_draft_answer -q`
  - 结果：`4 passed`

## 1.2.62 - 全局日志系统改造

### 背景

补齐生产化日志能力：API 链路、前后端错误、系统启动停止、业务操作、数据库操作摘要需要统一落盘到项目根目录 `log/`。

### 本轮改动

1. 新增 `logging_system.py`
   - 分类写入 `log/requests`、`log/errors`、`log/system`、`log/business`、`log/sql`
   - JSON Lines 格式，按日期拆分
   - 自动 `trace_id`、脱敏、截断，日志失败不影响主流程

2. API 链路接入
   - 每次 JSON API 请求记录入参、出参摘要、状态码、耗时、客户端信息
   - 响应头返回 `X-Trace-Id`
   - `ApiError` 和未捕获异常写入错误日志
   - API 服务启动/停止写入系统日志

3. 前端错误接入
   - 新增 `POST /client-log`
   - 前端监听 `window.error` 和 `unhandledrejection` 并上报

4. 核心业务接入
   - 检索、证据组装、DB summary、建库、增量建库、向量补齐、LLM、Agent 记录业务/SQL/错误摘要

5. 文档与目录
   - 新增 `docs/LOGGING.md`
   - README 增加日志文档入口
   - `.gitignore` 忽略运行期日志，仅保留 `log/.gitkeep`

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/*.py`

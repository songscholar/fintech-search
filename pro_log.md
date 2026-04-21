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

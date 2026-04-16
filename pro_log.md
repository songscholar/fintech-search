# 项目变更日志

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

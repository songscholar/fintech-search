# 项目变更日志

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

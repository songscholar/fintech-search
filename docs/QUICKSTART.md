# 快速开始指南

## 概述

本文档帮助新用户快速上手 USES Indexer，包含安装、基本使用和常见场景。

---

## 1. 环境准备

### 1.1 依赖要求

- Python 3.10+
- 无其他外部依赖

### 1.2 安装

```bash
# 进入项目目录
cd /Users/songzuoqiang/Documents/agent/condex/codes

# 安装项目
python3 -m pip install -e .

# 或者使用开发模式
python3 -m pip install -e . --dev
```

### 1.3 验证安装

```bash
python3 -m uses_indexer --help
```

应该看到帮助信息：

```
usage: uses_indexer <command> ...

Commands:
  parse-file      解析单个文件
  scan-dir        扫描目录
  build-index     构建索引
  db-summary      查看索引摘要
  query-index     检索代码
  assemble-evidence  组装证据
  ask-codebase    问答包
  answer-codebase  回答
  serve-api       启动 HTTP API
  serve-mcp       启动 MCP 服务
  eval-retrieval  检索评测
```

---

## 2. 快速示例

### 2.1 解析单个文件

```bash
python3 -m uses_indexer parse-file \
  /Users/songzuoqiang/Documents/agent/code/uses_codes/uftbusiness/customization/sesextmgt/LF_SESEXTMGR_BJSREALTIME_QRY.uftfunction
```

输出：

```json
{
  "path": "...",
  "unit_kind": "Function",
  "prefix": "LF",
  "name": "LF_SESEXTMGR_BJSREALTIME_QRY",
  "chinese_name": "实时行情查询",
  "statements": [
    {"kind": "action", "raw": "[获取记录]..."},
    {"kind": "call", "raw": "[AF_xxx]..."}
  ]
}
```

### 2.2 扫描目录

```bash
python3 -m uses_indexer scan-dir \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --limit 20 \
  --output summary.json
```

### 2.3 构建索引

项目提供两种方式构建索引：使用 CLI 命令逐个构建，或使用便捷脚本 `build_indexes.py` 批量构建。

#### 方式一：使用便捷脚本 build_indexes.py（推荐）

这个脚本支持 6 种构建模式，特别适合批量构建多个索引：

##### 场景 1：分别构建单个索引

```bash
# 仅构建代码索引
python3 build_indexes.py --mode code

# 仅构建元数据索引
python3 build_indexes.py --mode metadata

# 仅构建表结构索引
python3 build_indexes.py --mode table

# 仅构建全量索引（包含代码和元数据）
python3 build_indexes.py --mode full
```

##### 场景 2：一次构建三个专用索引（推荐）

```bash
# 同时构建代码索引、元数据索引、表结构索引
python3 build_indexes.py --mode three

# 大库可先跳过向量，结构索引建好后再补齐 chunk_vectors
python3 build_indexes.py --mode three --skip-vectors
```

这个模式会按顺序构建三个专用索引：代码索引、元数据索引、表结构索引；全量索引仍然通过 `--mode full` 单独构建。

##### 场景 3：构建所有四个索引

```bash
# 构建所有四个索引：代码、元数据、全量、表结构
python3 build_indexes.py --mode all
```

#### 方式二：使用 CLI 命令逐个构建

如果需要更精细的控制，可以使用 CLI 命令逐个构建：

##### 构建代码专用索引（仅代码文件）

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db ./examples/business_code_index.db \
  --index-type code \
  --progress
```

如果只想先建结构索引，可以加 `--skip-vectors`；后续再用 `--resume-vectors` 补齐向量。

##### 构建元数据专用索引（仅元数据文件）

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db ./examples/business_metadata_index.db \
  --index-type metadata
```

##### 构建全量索引（包含代码和元数据）

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db ./examples/business_full_index.db \
  --index-type all
```

##### 构建表结构索引

```bash
PYTHONPATH=src python3 -m uses_indexer build-table-index \
  /Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure \
  --db ./examples/business_table_index.db \
  --stdfield /Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure/stdfield.stdfield \
  --mdbobject /Users/songzuoqiang/Documents/agent/code/upub_codes/uftstructure/mdbobject.mdbobject
```

**参数说明**：
- `stdfield`：标准字段定义文件路径
- `mdbobject`：表空间关系配置文件路径

**注意**：首次建库需要较长时间（取决于代码库规模）

### 2.5 查看索引摘要

```bash
python3 -m uses_indexer db-summary \
  --db ./examples/my_index.db
```

输出示例：

```json
{
  "file_count": 21148,
  "procedure_count": 21148,
  "statement_count": 1122460,
  "chunk_count": 201030,
  "block_count": 40887,
  "call_edges": 54774
}
```

---

## 3. 核心使用场景

### 3.1 场景一：快速搜索

想找某个功能在哪里实现：

```bash
python3 -m uses_indexer query-index \
  --db ./examples/business_code_index.db \
  --query "证券代码获取" \
  --limit 10
```

### 3.2 场景二：准备证据

想让 AI 回答问题，需要准备证据：

```bash
python3 -m uses_indexer assemble-evidence \
  --db ./examples/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 6 \
  --context-window 2 \
  --related-limit 3
```

### 3.3 场景三：直接问答

直接获取答案：

```bash
python3 -m uses_indexer answer-codebase \
  --db ./examples/business_code_index.db \
  --question "证券代码获取的逻辑在哪里"
```

---

## 4. 使用外部 Embedding（可选）

### 4.1 配置环境变量

```bash
# OpenAI
export OPENAI_EMBEDDING_KEY="your-api-key"
export OPENAI_EMBEDDING_URL="https://oapi.aivue.cn/v1"
export OPENAI_EMBEDDING_NAME="text-embedding-3-small"

# 或使用项目特定变量
export USES_INDEXER_EMBEDDING_API_KEY="your-api-key"
export USES_INDEXER_EMBEDDING_MODEL="text-embedding-3-small"
```

### 4.2 使用外部 Embedding 建库

```bash
python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db ./examples/business_code_index_openai.db
```

### 4.3 断点续传

如果建库中断，可以续传：

```bash
python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db ./examples/business_code_index_openai.db \
  --resume-vectors
```

---

## 5. 使用外部 LLM 回答（可选）

### 5.1 配置环境变量

```bash
export USES_INDEXER_LLM_API_KEY="your-api-key"
export USES_INDEXER_LLM_MODEL="gpt-4o"
export USES_INDEXER_LLM_BASE_URL="https://oapi.aivue.cn/v1"
```

### 5.2 使用 LLM 回答

```bash
python3 -m uses_indexer answer-codebase \
  --db ./examples/business_code_index.db \
  --question "证券代码获取的逻辑在哪里"
```

返回结果会包含：
- `draft_answer`：本地生成的保底回答
- `llm_answer`：LLM 生成的回答
- `answer_source`：答案来源

---

## 6. HTTP API 服务

### 6.1 启动服务

```bash
python3 -m uses_indexer serve-api \
  --db ./examples/business_code_index.db \
  --host 127.0.0.1 \
  --port 8000
```

### 6.2 调用接口

**健康检查**：

```bash
curl http://127.0.0.1:8000/health
```

**检索查询**：

```bash
curl -X POST http://127.0.0.1:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"query": "证券代码获取", "limit": 5}'
```

**生成答案**：

```bash
curl -X POST http://127.0.0.1:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"question": "证券代码获取的逻辑在哪里", "evidence_limit": 3}'
```

---

## 7. MCP 服务

### 7.1 启动 MCP 服务

```bash
python3 -m uses_indexer serve-mcp \
  --db ./examples/business_code_index.db
```

### 7.2 可用工具

| 工具名 | 功能 |
|-------|------|
| `db_summary` | 获取数据库索引摘要 |
| `query_codebase` | 语义检索代码库 |
| `assemble_evidence` | 组装证据上下文 |
| `ask_codebase` | 生成问答包 |
| `answer_codebase` | 生成最终回答 |

### 7.3 Codex 集成

安装 Codex 技能：

```bash
python3 -m uses_indexer install-codex-integration
```

这会：
- 创建 plugin 符号链接
- 创建 skill 符号链接
- 配置 marketplace

---

## 8. 评测功能

### 8.1 运行检索评测

```bash
python3 -m uses_indexer eval-retrieval \
  --db ./examples/uses_codes_index.db \
  --cases ./eval/uses_codes_cases.json \
  --limit 10 \
  --top-k 1,3,5,10 \
  --output ./examples/eval_report.json
```

### 8.2 对比评测结果

```bash
python3 -m uses_indexer compare-eval \
  --before ./examples/before_report.json \
  --after ./examples/after_report.json \
  --output ./examples/compare_report.json
```

---

## 9. 常见问题

### 9.1 建库很慢怎么办？

- 减少扫描文件数量（使用 `--limit`）
- 使用本地哈希向量（跳过 embedding 计算）
- 分批建库，后续用 `--resume-vectors` 续传

### 9.2 检索结果不理想？

- 检查是否使用了正确的 embedding 配置
- 尝试增加 `--limit` 扩大搜索范围
- 使用 `query-index` 查看原始召回结果

### 9.3 向量召回被禁用？

通常是 embedding 配置不一致：

```bash
# 检查向量状态
python3 -m uses_indexer query-index \
  --db ./examples/business_code_index.db \
  --query "测试" | jq '.vector_status'
```

### 9.4 如何切换索引库？

```bash
# 方法一：使用 --db 参数
python3 -m uses_indexer query-index --db /path/to/your.db ...

# 方法二：设置环境变量
export USES_INDEXER_DB_PATH=/path/to/your.db
python3 -m uses_indexer query-index ...
```

---

## 10. 最佳实践

### 10.1 推荐工作流

1. **先查询**：`query-index` 看召回结果
2. **再证据**：`assemble-evidence` 看证据质量
3. **后回答**：`answer-codebase` 获取最终答案

### 10.2 提问技巧

好的提问：
- `AF_DATASEINIT_SECONDLOADUSESTABLE 中 @sql_str1 在哪里执行`
- `哪些流程调用证券代码获取`
- `ERR_SECU_QRY_ENTRUST_FAIL 在哪里报错`

不太好的提问：
- 太泛：`这个功能怎么实现`
- 太短：`证券`
- 歧义：`这个报错是哪来的`

### 10.3 调试建议

先用小范围测试：

```bash
# 扫描 10 个文件
python3 -m uses_indexer scan-dir /path/to/code --limit 10

# 用小库测试
python3 -m uses_indexer build-index /path/to/code --db test.db
```

---

## 11. 重要知识点：SQLite WAL 模式

### 什么是 WAL 模式？

项目使用 SQLite 的 **WAL（Write-Ahead Logging）模式** 来提高索引构建和查询性能。

### 三个文件的作用

当构建索引时，会看到三个文件：

| 文件名 | 说明 |
|--------|------|
| `xxx.db` | **主数据库文件**，存储持久化数据 |
| `xxx.db-wal` | **Write-Ahead Log 文件**，所有写入操作首先记录到这个文件 |
| `xxx.db-shm` | **Shared Memory 文件**，用于协调多个进程访问 |

### 为什么 .db-wal 文件大小一直在增加？

**这是正常行为！** 不要终止程序！

在 WAL 模式下：
1. 所有写入操作先写入 `.db-wal` 文件
2. 主数据库 `.db` 保持不变（或只在 checkpoint 时更新）
3. 当索引构建完成后，SQLite 会自动执行 checkpoint，将 `.db-wal` 数据合并到 `.db`

### 监控要点

构建索引时：
- ✅ **正常情况**：`.db-wal` 文件大小持续增加，程序正在正常运行
- ❌ **异常情况**：文件大小长时间不变或程序报错

### 如何确认完成？

- 等待程序正常结束
- 程序结束后，`.db-wal` 文件会变小或消失
- 主要数据会合并到 `.db` 文件中

## 12. 相关文档

- [USAGE.md](USAGE.md) - 详细使用说明
- [ARCHITECTURE.md](ARCHITECTURE.md) - 架构设计
- [INDEX_SCHEMA.md](INDEX_SCHEMA.md) - 索引结构
- [EVALUATION.md](EVALUATION.md) - 评测说明
- [DEPLOYMENT.md](DEPLOYMENT.md) - 部署指南

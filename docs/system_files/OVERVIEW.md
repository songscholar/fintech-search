# 系统说明文档

## 项目概述

USES Indexer 是一个面向 UFT/USES DSL 代码库的本地索引与问答系统，旨在帮助大语言模型（LLM）理解和检索代码库。

### 核心能力

| 能力 | 说明 |
|-----|------|
| **代码解析** | 解析 XML 外壳 + CDATA DSL 代码 + metadata 元数据 |
| **索引构建** | 将解析结果存储到 SQLite，支持 FTS 全文搜索 |
| **语义检索** | 支持 FTS + 向量混合检索，意图感知重排 |
| **问答系统** | 证据组装、prompt 生成、本地/外部 LLM 回答 |
| **多种接口** | CLI、HTTP API、MCP Server、Codex 集成 |

---

## 系统架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              用户层                                      │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────┐  │
│  │  CLI    │  │ HTTP API│  │   MCP   │  │ Codex   │  │  External   │  │
│  │         │  │         │  │ Server  │  │ Skill   │  │     LLM     │  │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └──────┬──────┘  │
└───────┼────────────┼────────────┼────────────┼──────────────┼────────┘
        │            │            │            │              │
        └────────────┴────────────┼────────────┴──────────────┘
                                   │
┌──────────────────────────────────┼──────────────────────────────────────┐
│                           核心功能层                                      │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │    CLI       │  │    API      │  │    MCP       │  │   LLM      │  │
│  │   入口       │  │   服务      │  │   服务       │  │   适配器   │  │
│  └──────────────┘  └─────────────┘  └──────────────┘  └────────────┘  │
│                                   │                                     │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │    QA        │  │  Answering  │  │ Retrieval   │  │  Indexer   │  │
│  │   问答包     │  │    回答     │  │   检索      │  │   索引     │  │
│  └──────────────┘  └─────────────┘  └──────────────┘  └────────────┘  │
│                                   │                                     │
└───────────────────────────────────┼─────────────────────────────────────┘
                                    │
┌───────────────────────────────────┼─────────────────────────────────────┐
│                           数据处理层                                      │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐                   │
│  │   Parser     │  │  Metadata   │  │ Embeddings   │                   │
│  │  DSL 解析器   │  │   解析器    │  │   向量生成   │                   │
│  └──────────────┘  └─────────────┘  └──────────────┘                   │
│                                   │                                     │
└───────────────────────────────────┼─────────────────────────────────────┘
                                    │
┌───────────────────────────────────┼─────────────────────────────────────┐
│                           数据存储层                                      │
│                         ┌────────┴────────┐                             │
│                         │    SQLite       │                             │
│                         │  + FTS5         │                             │
│                         │  + WAL 模式     │                             │
│                         └─────────────────┘                             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 核心模块

### 1. 解析层 (Parser)

**职责**：解析 UFT/USES DSL 代码

**输入**：
- `*.uftfunction` - UFT 函数
- `*.uftservice` - UFT 服务
- `*.uftatomfunction` - UFT 原子函数
- `metadata/` 目录下的元数据文件

**输出**：
```python
{
    "path": "...",
    "unit_kind": "Function",
    "prefix": "LF",
    "name": "LF_xxx",
    "chinese_name": "...",
    "statements": [
        {"kind": "action", "raw": "..."},
        {"kind": "call", "raw": "..."},
        {"kind": "control", "raw": "..."}
    ]
}
```

**支持的文件类型**：
- `LF` - 本地函数
- `LS` - 本地服务
- `AF` - 原子函数
- `RS` - 远程服务

---

### 2. 索引层 (Indexer)

**职责**：构建 SQLite 索引

**核心表**：

| 表名 | 说明 |
|-----|------|
| `files` | 索引的文件 |
| `procedures` | 过程/服务 |
| `statements` | 语句流 |
| `actions` | DSL 动作 |
| `edges` | 关系边 |
| `chunks` | 语义块 |
| `chunk_vectors` | 向量 |
| `blocks` | 结构块 |

**索引类型**：
- 主键索引
- FTS5 全文索引
- 向量索引（本地哈希 / OpenAI）

---

### 3. 检索层 (Retrieval)

**职责**：混合检索 + 重排序

**检索流程**：

```
1. FTS 召回
   ├── procedures_fts
   ├── chunks_fts
   ├── blocks_fts
   └── actions_fts

2. 向量召回
   ├── 本地哈希向量
   └── OpenAI 向量

3. SQL fallback
   └── LIKE 查询

4. Python 重排序
   ├── 意图感知重排
   ├── 调用链扩展
   └── 块级关系补充
```

---

### 4. 问答层 (QA + Answering)

**职责**：生成问答包和最终回答

**QA 模块**：
```python
{
    "system_prompt": "...",      # 系统提示
    "user_prompt": "...",        # 用户问题
    "draft_answer": "...",       # 本地生成的回答
    "evidence": [...]            # 证据列表
}
```

**Answer 模块**：
```python
{
    "answer": "...",             # 最终回答
    "answer_source": "llm/draft", # 回答来源
    "supporting_locations": [...], # 支撑位置
    "uncertainties": [...]        # 不确定性说明
}
```

---

### 5. 服务层

**HTTP API**：

| 接口 | 方法 | 功能 |
|-----|------|------|
| `/health` | GET | 健康检查 |
| `/db-summary` | GET | 数据库摘要 |
| `/query` | POST | 检索代码 |
| `/evidence` | POST | 组装证据 |
| `/ask` | POST | 生成问答包 |
| `/answer` | POST | 生成回答 |

**MCP 工具**：

| 工具名 | 功能 |
|-------|------|
| `db_summary` | 获取索引摘要 |
| `query_codebase` | 语义检索 |
| `assemble_evidence` | 组装证据 |
| `ask_codebase` | 生成问答包 |
| `answer_codebase` | 生成回答 |

---

## 数据流

### 索引构建流程

```
源码目录
    │
    ▼
┌─────────┐
│ Parser  │  解析 XML + CDATA + Metadata
└────┬────┘
     │
     ▼
┌─────────┐
│ Parsed  │  生成 ParsedUnit 结构
│  Unit   │
└────┬────┘
     │
     ▼
┌─────────┐
│Indexer  │  写入 SQLite + FTS + 向量
└────┬────┘
     │
     ▼
┌─────────┐
│SQLite   │  持久化存储
│   DB    │
└─────────┘
```

### 问答流程

```
用户问题
    │
    ▼
┌─────────┐
│ Retrieval│  混合检索 + 重排
└────┬────┘
     │
     ▼
┌─────────┐
│Evidence │  组装证据 + 上下文
│Assembler│
└────┬────┘
     │
     ▼
┌─────────┐
│   QA   │  生成 prompt + draft_answer
└────┬────┘
     │
     ▼
┌─────────┐
│Answer  │  调用 LLM 或使用 draft
└────┬────┘
     │
     ▼
  最终回答
```

---

## 特性详解

### 1. 混合检索

结合多种检索方式，确保召回质量：
- **FTS**：精确关键词匹配
- **向量**：语义相似度匹配
- **SQL**：兜底匹配
- **重排**：综合排序优化

### 2. 意图感知重排

识别问题类型，动态调整排序权重：

| 问题类型 | 提升权重 |
|---------|---------|
| 表写入 | writes_table, sql_block |
| 表读取 | reads_table, sql_block |
| 调用链 | calls_procedure, incoming_callers |
| 失败处理 | exception_block, failure_handler |

### 3. 动态 SQL 恢复

追踪变量赋值，还原动态 SQL：

```sql
-- 原始代码
@sql_str = "select * from users"
sprintf(@sql_str, "%s where id = %d", @sql_str, @user_id)
[通用SQL执行]@sql_str

-- 恢复后
select * from users where id = ?
```

### 4. 调用链分析

- 本地函数调用 (LS->AF, LF->LF)
- RPC 调用 (LF->LS, LS->LS)
- 两跳调用链扩展

### 5. 向量兼容性

确保索引和查询使用相同的向量空间：

```python
# 建库时记录
metadata.embedding_model = "text-embedding-3-small"
metadata.embedding_dimension = 1536

# 查询时校验
if current_model != stored_model:
    disable_vector_retrieval()  # 自动降级
```

---

## 性能指标

### 索引规模

| 指标 | 数值 |
|-----|------|
| 文件数 | 21,148 |
| 过程数 | 21,148 |
| 语句数 | 1,122,460 |
| 语义块 | 201,030 |
| 结构块 | 40,887 |

### 检索效果

| 指标 | 数值 |
|-----|------|
| pass@1 | 1.0 |
| pass@3 | 1.0 |
| pass@5 | 1.0 |
| pass@10 | 1.0 |
| expectation_recall@10 | 0.9 |

---

## 部署方式

### 1. CLI 方式

```bash
python3 -m uses_indexer <command> [options]
```

### 2. HTTP 服务

```bash
python3 -m uses_indexer serve-api --db path/to/db --port 8000
```

### 3. MCP 服务

```bash
python3 -m uses_indexer serve-mcp --db path/to/db
```

### 4. Codex 集成

```bash
python3 -m uses_indexer install-codex-integration
```

---

## 配置项

### Embedding 配置

| 环境变量 | 说明 | 默认值 |
|---------|------|-------|
| `OPENAI_EMBEDDING_KEY` | API Key | - |
| `OPENAI_EMBEDDING_URL` | API 地址 | OpenAI |
| `OPENAI_EMBEDDING_NAME` | 模型名 | text-embedding-3-small |
| `OPENAI_EMBEDDING_BATCH_SIZE` | 批量大小 | 100 |

### LLM 配置

| 环境变量 | 说明 | 默认值 |
|---------|------|-------|
| `USES_INDEXER_LLM_API_KEY` | API Key | - |
| `USES_INDEXER_LLM_MODEL` | 模型名 | gpt-4o |
| `USES_INDEXER_LLM_BASE_URL` | API 地址 | - |

---

## 适用场景

| 场景 | 推荐方式 |
|-----|---------|
| 本地快速检索 | CLI `query-index` |
| 集成到 Agent | MCP 服务 |
| 集成到前端 | HTTP API |
| Codex 集成 | Codex Skill/Plugin |
| 批量处理 | CLI 脚本 |

---

## 限制与局限

1. **语言限制**：目前仅支持 UFT/USES DSL
2. **规模限制**：建议 100 万文件以下
3. **向量依赖**：需要兼容的 embedding 模型
4. **非实时**：索引需要手动重建

---

## 相关文档

- [ARCHITECTURE.md](ARCHITECTURE.md) - 详细架构
- [TECH_SELECTION.md](TECH_SELECTION.md) - 技术选型
- [DEVELOPMENT_NOTES.md](DEVELOPMENT_NOTES.md) - 开发心得
- [QUICKSTART.md](QUICKSTART.md) - 快速开始
- [USAGE.md](USAGE.md) - 详细使用说明
- [INDEX_SCHEMA.md](INDEX_SCHEMA.md) - 索引结构
- [EVALUATION.md](EVALUATION.md) - 评测说明
- [DEPLOYMENT.md](DEPLOYMENT.md) - 部署指南
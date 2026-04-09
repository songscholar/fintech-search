# USES Indexer

`uses-indexer` 是一个面向 USES/UFT DSL 代码库的本地索引器原型。

当前已经完成两层基础能力：

1. 解析 XML 外壳 + `CDATA` DSL 代码体。
2. 把解析结果写入 SQLite，并提供混合检索与证据组装能力。

这还不是最终版问答系统，但已经具备了“理解仓库结构并沉淀索引”的第一版基础设施。

## 当前已实现

- 解析 `LF / LS / AF / RS` 文件
- 提取文件级元数据
- 提取 `histories / inputParameters / outputParameters / internalParams`
- 提取代码体中的：
  - 注释
  - DSL 动作语句
  - 过程调用
  - `if / else if / else / while / switch`
  - `break / continue / goto`
  - 标签
  - 通用原始代码语句
- 抽取语句中的变量引用与简单写入变量
- 提供 CLI 入口，可对单文件或目录进行解析并输出 JSON
- 提供 SQLite 索引构建能力
- 提供 SQLite FTS + SQL fallback 的混合检索能力
- 提供 Python 层重排能力
- 提供面向问答的证据组装能力，可直接生成 `llm_context`
- 已在完整目录 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 上完成一次全量扫描和索引验证

## 当前验证结果

### 解析层摘要

基于完整代码目录的当前扫描结果：

- 文件总数：`2564`
- `Function`：`1858`
- `Service`：`703`
- `FactorService`：`3`
- 语句统计：
  - `action`: `18140`
  - `call`: `8085`
  - `control`: `22026`
  - `assignment`: `23673`
  - `comment`: `33196`

摘要文件：

- `examples/uses_codes_summary.json`

### SQLite 索引摘要

- `files`: `2564`
- `procedures`: `2564`
- `histories`: `7380`
- `params`: `70004`
- `statements`: `159148`
- `actions`: `26225`
- `variable_refs`: `214948`
- `edges`: `61249`
- `procedures_fts`: `2564`
- `statements_fts`: `159148`
- `actions_fts`: `26225`
- `edges_fts`: `61249`

摘要文件：

- `examples/uses_codes_index_summary.json`
- `examples/uses_codes_db_summary.json`
- `examples/uses_codes_evidence_example.json`
- `examples/uses_codes_qa_example.json`

本地构建出的数据库默认路径示例为 `examples/uses_codes_index.db`，该文件体积较大，当前不纳入版本控制。

## 目录结构

```text
docs/
  ARCHITECTURE.md
  INDEX_SCHEMA.md
  WORKLOG.md
examples/
  uses_codes_summary.json
  uses_codes_index_summary.json
  uses_codes_db_summary.json
  uses_codes_evidence_example.json
  uses_codes_qa_example.json
src/uses_indexer/
  api.py
  __init__.py
  __main__.py
  cli.py
  indexer.py
  models.py
  parser.py
  qa.py
tests/
  test_api.py
  test_parser.py
  test_indexer.py
  test_qa.py
```

## 快速开始

安装：

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m pip install -e .
```

解析单文件：

```bash
python3 -m uses_indexer parse-file \
  /Users/songzuoqiang/Documents/agent/code/uses_codes/uftbusiness/customization/sesextmgt/LF_SESEXTMGR_BJSREALTIME_QRY.uftfunction
```

扫描目录并输出解析摘要：

```bash
python3 -m uses_indexer scan-dir \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --limit 20 \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_summary.json
```

构建 SQLite 索引：

```bash
python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index_summary.json
```

查看数据库摘要：

```bash
python3 -m uses_indexer db-summary \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_db_summary.json
```

执行简单关键词查询：

```bash
python3 -m uses_indexer query-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --query "证券代码获取" \
  --limit 10
```

组装可直接给大模型使用的证据上下文：

```bash
python3 -m uses_indexer assemble-evidence \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --query "证券代码获取的逻辑在哪里" \
  --limit 6 \
  --context-window 2 \
  --related-limit 3 \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_evidence_example.json
```

这个命令会返回：

- 重排后的证据块
- 每个证据块对应的代码片段
- 相关调用、来路调用、表访问
- 一段可直接交给 LLM 的 `llm_context`

生成完整的问答包：

```bash
python3 -m uses_indexer ask-codebase \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --question "证券代码获取的逻辑在哪里" \
  --evidence-limit 6 \
  --context-window 2 \
  --related-limit 3
```

这个命令会返回：

- 检索到的证据块
- 标准化 `system_prompt`
- 可直接发给模型的 `user_prompt`
- 一个本地生成的 `draft_answer`
- 支撑结论的文件路径和行号

启动本地 HTTP API：

```bash
python3 -m uses_indexer serve-api \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --host 127.0.0.1 \
  --port 8000
```

可用接口：

- `GET /health`
- `GET /db-summary`
- `POST /query`
- `POST /evidence`
- `POST /ask`

示例：

```bash
curl -s http://127.0.0.1:8000/health
```

```bash
curl -s http://127.0.0.1:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"证券代码获取的逻辑在哪里","evidence_limit":3}'
```

## 下一步

- 增加更稳定的块级 AST
- 补齐事务块、异常块、SQL 块的配对关系
- 增加向量索引
- 增加更精细的表访问与过程关系
- 增加真正的外部模型调用入口
- 增加 MCP/API 集成封装

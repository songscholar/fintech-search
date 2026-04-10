# USES Indexer

`uses-indexer` 是一个面向 USES/UFT DSL 代码库的本地索引器原型。

当前已经完成两层基础能力：

1. 解析 XML 外壳 + `CDATA` DSL 代码体。
2. 把解析结果写入 SQLite，并提供混合检索、问答包、本地 API/回答接口和 MCP 插件入口。

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
- 提供语义块 `chunk` 切分与 `chunks_fts` 检索能力
- 提供本地哈希向量 `chunk_vectors` 与向量式召回能力
- 提供 OpenAI-compatible embedding 接口接入能力，可替换本地哈希向量
- 提供向量空间兼容校验，避免“用 A 模型建库、用 B 模型查询”导致错误召回
- 提供结构块恢复：事务块、SQL 块、失败处理块、记录循环块
- 提供异常与控制流恢复：`EXCEPTION`、`WHEN_OTHERS`、`goto svr_end`、退出标签
- 提供 SQL 表访问抽取：从 `select/update/delete/insert/merge` 中恢复真实表名
- 提供动态 SQL 恢复：支持从 `@sql_str = "..."`、`sprintf/hs_snprintf/hs_strcpy` 这类字符串构造中还原 SQL 文本
- 提供两跳调用链扩展与重排
- 提供意图感知重排：对表访问、变量赋值、调用链、失败路径等问题使用不同证据权重
- 提供块级关系摘要，使证据能带上“在哪个事务/SQL/失败路径里”
- 提供 Python 层重排能力
- 提供面向问答的证据组装能力，可直接生成 `llm_context`
- 提供一跳关系过程摘要扩展，使证据不只停留在命中过程本身
- 提供本地 `answer-codebase` 回答入口
- 提供本地 HTTP API，包括最终回答接口 `POST /answer`
- 提供本地 stdio MCP server，包括 `db_summary / query_codebase / assemble_evidence / ask_codebase / answer_codebase`
- 提供可安装的 Codex 技能定义 `skills/uses-codebase-search`
- 提供 repo-local Codex 插件定义 `plugins/uses-codebase-plugin`
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
- `edges`: `62645`
- `chunks`: 由建库时按过程语义块自动生成
- `chunk_vectors`: 与 `chunks` 一一对应
- `blocks`: 由建库时按事务 / SQL / 失败处理 / 循环等稳定结构恢复生成
- `block_edges`: 聚合块内部的过程调用、表访问和控制流关系
- `procedures_fts`: `2564`
- `statements_fts`: `159148`
- `actions_fts`: `26225`
- `edges_fts`: `62645`
- `chunks_fts`: 与 `chunks` 一一对应
- `blocks_fts`: 与 `blocks` 一一对应

摘要文件：

- `examples/uses_codes_index_summary.json`
- `examples/uses_codes_db_summary.json`
- `examples/uses_codes_evidence_example.json`
- `examples/uses_codes_qa_example.json`
- `examples/uses_codes_answer_example.json`
- `examples/uses_codes_failure_flow_example.json`
- `examples/uses_codes_exit_flow_example.json`
- `examples/uses_codes_sql_table_example.json`
- `examples/uses_codes_call_chain_example.json`
- `examples/uses_codes_dynamic_sql_example.json`
- `examples/uses_codes_intent_rerank_example.json`

本地构建出的数据库默认路径示例为 `examples/uses_codes_index.db`，该文件体积较大，当前不纳入版本控制。

## Embedding 配置

默认情况下，索引器会使用本地零依赖的 `LocalHashedEmbedder`。

如果你希望用真实语义 embedding，可以设置：

- `USES_INDEXER_EMBEDDING_API_KEY`
- `USES_INDEXER_EMBEDDING_MODEL`
- `USES_INDEXER_EMBEDDING_BASE_URL`
- `USES_INDEXER_EMBEDDING_BATCH_SIZE`
- `USES_INDEXER_EMBEDDING_DIMENSIONS`

兼容规则：

- 建库时会把 `provider / model / dimension` 写入 SQLite 元数据
- 查询时会校验当前 embedding 配置是否和索引库一致
- 如果不一致，会自动禁用向量召回，并在返回结果里输出 `vector_status`
- 如果切换了 embedding 模型，应该重新执行一次 `build-index`

## 目录结构

```text
.agents/
  plugins/marketplace.json
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
  uses_codes_answer_example.json
  uses_codes_failure_flow_example.json
  uses_codes_exit_flow_example.json
  uses_codes_sql_table_example.json
  uses_codes_call_chain_example.json
  uses_codes_dynamic_sql_example.json
  uses_codes_intent_rerank_example.json
plugins/
  uses-codebase-plugin/
    .codex-plugin/plugin.json
    .mcp.json
    scripts/run_mcp_server.py
    skills/uses-codebase-search/SKILL.md
skills/
  uses-codebase-search/
    SKILL.md
src/uses_indexer/
  api.py
  answering.py
  embeddings.py
  __init__.py
  __main__.py
  cli.py
  indexer.py
  llm.py
  mcp_server.py
  models.py
  parser.py
  qa.py
tests/
  test_api.py
  test_answering.py
  test_mcp.py
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
- 语义块命中及其摘要
- 向量式召回命中
- 向量兼容状态 `vector_status`
- 覆盖当前证据的事务块 / SQL 块 / 失败处理块摘要
- 覆盖当前证据的异常处理块和退出跳转摘要
- 每个证据块对应的代码片段
- 相关调用、来路调用、表访问
- 一跳关联过程的摘要
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

生成最终回答：

```bash
python3 -m uses_indexer answer-codebase \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db \
  --question "证券代码获取的逻辑在哪里" \
  --evidence-limit 6 \
  --context-window 2 \
  --related-limit 3 \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_answer_example.json
```

当前行为：

- 如果配置了外部模型，会优先调用模型生成最终回答
- 如果没有配置外部模型，会回退到基于证据生成的 `draft_answer`
- 返回字段里会标明 `answer_source`

如果你还配置了外部 embedding：

- 建库会优先使用外部 embedding 生成 `chunk_vectors`
- 查询会优先使用相同 embedding 空间做块级向量召回
- 如果查询端和索引端 embedding 不兼容，会自动降级到 `FTS + LIKE + rerank`

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
- `POST /answer`

示例：

```bash
curl -s http://127.0.0.1:8000/health
```

```bash
curl -s http://127.0.0.1:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"证券代码获取的逻辑在哪里","evidence_limit":3}'
```

```bash
curl -s http://127.0.0.1:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"question":"证券代码获取的逻辑在哪里","evidence_limit":3}'
```

启动本地 stdio MCP server：

```bash
python3 -m uses_indexer serve-mcp \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db
```

可用 MCP 工具：

- `db_summary`
- `query_codebase`
- `assemble_evidence`
- `ask_codebase`
- `answer_codebase`

如果你想把它作为 Codex 的 repo-local 插件使用，仓库里已经包含：

- `plugins/uses-codebase-plugin/.codex-plugin/plugin.json`
- `plugins/uses-codebase-plugin/.mcp.json`
- `.agents/plugins/marketplace.json`

插件默认会启动：

```bash
python3 ./scripts/run_mcp_server.py
```

默认索引库是：

- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db`

如果需要切换索引库，可以传：

```bash
python3 ./scripts/run_mcp_server.py --db /absolute/path/to/your.db
```

当前检索默认是混合式的：

- `FTS`
- `chunk` 块级召回
- `vector_chunk` 本地哈希向量召回
- SQL fallback
- Python 重排

把 repo-local plugin 和技能安装到本机 Codex：

```bash
python3 -m uses_indexer install-codex-integration
```

这个命令会：

- 在 `~/plugins/uses-codebase-plugin` 创建指向仓库插件目录的符号链接
- 在 `~/.codex/skills/uses-codebase-search` 创建指向仓库技能目录的符号链接
- 在 `~/.agents/plugins/marketplace.json` 写入本地插件入口

如果本地已有同名目标，需要显式覆盖：

```bash
python3 -m uses_indexer install-codex-integration --force
```

## 外部模型配置

`answer-codebase` 和 `POST /answer` 支持一个 OpenAI-compatible 的聊天接口，使用这些环境变量：

- `USES_INDEXER_LLM_API_KEY`
- `USES_INDEXER_LLM_MODEL`
- `USES_INDEXER_LLM_BASE_URL`
- `USES_INDEXER_LLM_TEMPERATURE`
- `USES_INDEXER_LLM_MAX_TOKENS`

如果只设置了 `OPENAI_API_KEY`，仍然需要显式设置 `USES_INDEXER_LLM_MODEL`。

## 技能安装

仓库里已经包含技能定义：

- `skills/uses-codebase-search/SKILL.md`

我还已经把它安装到：

- `/Users/songzuoqiang/.codex/skills/uses-codebase-search/SKILL.md`

重启 Codex 后，这个技能就可以作为本地技能参与后续对话。技能会优先调用本地 MCP 工具，在 MCP 不可用时再回退到本地 `uses-indexer` API。

## 下一步

- 增加更稳定的块级 AST
- 补齐事务块、异常块、SQL 块的配对关系
- 增加更强语义的 embedding / 向量索引
- 增加更精细的表访问与过程关系
- 增加更丰富的模型适配器
- 增加更强的 MCP 能力和更细粒度的工具

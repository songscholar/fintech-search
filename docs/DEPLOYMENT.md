# Deployment Guide

## 目标

这份文档回答 3 个问题：

1. 这个项目最推荐怎么在本地部署
2. 怎么把它作为 HTTP 服务或 MCP 工具接到大模型
3. 真实 embedding、外部 LLM、Codex 插件分别应该怎么配置

当前项目主要支持单机本地部署，不依赖额外数据库或消息队列。

## 支持的部署形态

### 1. CLI 单机模式

适合：

- 本地建库
- 手工验证检索效果
- 做评测
- 先看结果再决定是否接服务

默认建议先用代码索引 `business_code_index.db`。如果需要同时检索代码和 metadata，再切到 `business_full_index.db`。

典型命令：

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m pip install -e .

python3 -m uses_indexer query-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 10
```

### 2. 本地 HTTP 服务模式

适合：

- 前端页面接入
- 本地脚本或工具调用
- 让其他大模型通过统一接口访问索引

启动命令：

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
PYTHONPATH=src python3 -m uses_indexer serve-api \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --host 127.0.0.1 \
  --port 8000
```

健康检查：

```bash
curl -s http://127.0.0.1:8000/health
```

核心接口：

- `GET /`
- `GET /ui`
- `GET /health`
- `GET /db-summary`
- `POST /query`
- `POST /evidence`
- `POST /ask`
- `POST /answer`

如果你只是想直接打开一版本地前端，不需要自己再写页面，启动后访问：

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/ui`

### 3. stdio MCP 模式

适合：

- 接入 Codex
- 接入支持 MCP 的 IDE / Agent / 桌面客户端
- 让对话式模型把本地代码库检索当成工具调用

启动命令：

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
PYTHONPATH=src python3 -m uses_indexer serve-mcp \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db
```

暴露工具：

- `db_summary`
- `query_codebase`
- `assemble_evidence`
- `ask_codebase`
- `answer_codebase`

## 推荐的本地部署路径

### 路径 1：直接使用现成索引库

这是当前最省事的方式。

现成完整索引库：

- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db`
- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_index.db` 仅作为子库回归索引保留

优点：

- 不需要重新建库
- 直接可用于查询、证据组装、问答、API、MCP

适合：

- 先看效果
- 做功能联调
- 演示给别人看

### 路径 2：自己重建本地 hash 索引

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m pip install -e .

python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index_summary.json
```

适合：

- 更新了源码目录
- 想重新生成最新索引
- 不依赖外部 embedding 服务

### 路径 3：重建真实 embedding 索引

```bash
export OPENAI_EMBEDDING_KEY="..."
export OPENAI_EMBEDDING_URL="https://oapi.aivue.cn/v1"
export OPENAI_EMBEDDING_NAME="text-embedding-3-large"
export OPENAI_EMBEDDING_BATCH_SIZE=8
export OPENAI_EMBEDDING_TIMEOUT=120
export OPENAI_EMBEDDING_CACHE_DB="/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_embedding_cache.db"

cd /Users/songzuoqiang/Documents/agent/condex/codes
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index_openai.db
```

如果中途中断：

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index_openai.db \
  --resume-vectors
```

当前建议：

- 始终配置 `OPENAI_EMBEDDING_CACHE_DB`
- batch size 优先用 `8` 或 `16`
- 全量建库不要当短命令跑，最好留出较长时间

## 回答层部署

如果你希望 `answer-codebase` 或 `POST /answer` 不只是返回本地 `draft_answer`，而是调用外部模型生成最终回答，还需要配置聊天模型环境变量。

如果你更习惯使用项目内 `.env`，可以先执行：

```bash
cp /Users/songzuoqiang/Documents/agent/condex/codes/.env.example \
  /Users/songzuoqiang/Documents/agent/condex/codes/.env
```

```bash
export USES_INDEXER_LLM_API_KEY="..."
export USES_INDEXER_LLM_MODEL="gpt-4.1-mini"
export USES_INDEXER_LLM_BASE_URL="https://api.openai.com/v1/chat/completions"
export USES_INDEXER_LLM_TEMPERATURE="0"
export USES_INDEXER_LLM_MAX_TOKENS="1200"
```

说明：

- 不配置这些变量时，系统仍可工作，但 `answer_source` 会是 `draft`
- 配置后，系统会先做本地检索与证据组装，再把证据发送给外部模型

## Codex 集成部署

如果你的目标是“让 Codex 把这个项目当成本地技能 / 工具自动调用”，推荐这样做：

### 1. 安装 skill 与 plugin

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m uses_indexer install-codex-integration
```

这一步会：

- 在 `~/plugins/uses-codebase-plugin` 建立插件符号链接
- 在 `~/.codex/skills/uses-codebase-search` 建立技能符号链接
- 在 `~/.agents/plugins/marketplace.json` 补齐本地 plugin 入口

### 2. 启动 MCP server

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 ./plugins/uses-codebase-plugin/scripts/run_mcp_server.py
```

如果要切库：

```bash
python3 ./plugins/uses-codebase-plugin/scripts/run_mcp_server.py \
  --db /absolute/path/to/your.db
```

### 3. 让对话模型走 MCP 工具

这时模型就可以通过：

- `query_codebase`
- `assemble_evidence`
- `ask_codebase`
- `answer_codebase`

来调用本地索引能力。

## 推荐部署清单

### 只看效果

1. `pip install -e .`
2. 直接使用现成的 `examples/business_code_index.db`
3. 跑 `query-index`
4. 跑 `answer-codebase`

### 做本地服务

1. `pip install -e .`
2. 确认索引库可用
3. 启动 `serve-api`
4. 用 `curl /health` 和 `curl /answer` 验证

### 做 Codex 工具化接入

1. `pip install -e .`
2. 执行 `install-codex-integration`
3. 启动 `serve-mcp` 或 plugin 自带脚本
4. 在 Codex 中验证能否调用 `answer_codebase`

## 常见问题

### 1. `db_path is required`

原因：

- 你调用了 API 或 MCP，但没有传 `db_path`
- 同时服务默认启动时也没有配置默认索引库

解决：

- 启动服务时明确加 `--db`
- 或请求里显式传 `db_path`

### 2. 为什么向量召回被禁用了

看返回里的 `vector_status`。

常见原因：

- 当前查询 embedding 和索引 embedding 不一致
- 当前库没有向量
- 你切换了模型但没有重新建库

### 3. 为什么回答看起来像摘要，不像大模型自然回答

原因：

- 当前没有配置外部聊天模型
- 系统回退到了本地 `draft_answer`

这不是错误，是设计上的保底策略。

### 4. 为什么真实 embedding 建库很慢

原因：

- 全量库块数很多
- 外部 embedding 接口在长文本和大 batch 下会变慢

建议：

- 先跑子集或中等规模验证
- 启用 cache
- 使用 `--resume-vectors`

## 相关阅读

- [ARCHITECTURE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/ARCHITECTURE.md)
- [INDEX_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/INDEX_SCHEMA.md)
- [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)
- [EVALUATION.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/EVALUATION.md)

# pre_log

## 2026-04-30 - 全局日志系统改造

### 背景

项目缺少生产化日志管理能力，前后端错误、API 调用链路、部署/启动停止、业务操作和数据库操作缺少统一落盘记录。

### 本轮改动

1. 新增集中日志模块
   - 新增 `src/uses_indexer/logging_system.py`
   - 日志默认写入项目根目录 `log/`
   - 按 `requests / errors / system / business / sql` 分类写 JSONL
   - 自动生成 `trace_id`
   - 自动脱敏密钥、Authorization、token、cookie、data_url、base64 大字段
   - 自动截断超长字符串和大数组/对象

2. HTTP/API 链路日志
   - `api.py` 为每次 JSON API 请求记录入参、出参摘要、状态码、耗时、客户端 IP、User-Agent
   - 响应头新增 `X-Trace-Id`
   - `ApiError` 与未捕获异常写入 `log/errors`
   - API 服务启动/停止写入 `log/system`

3. 前端错误上报
   - 新增 `POST /client-log`
   - 前端监听 `window.error` 和 `unhandledrejection`
   - 前端错误统一进入 `log/errors`

4. 业务与 SQL 摘要日志
   - 检索、证据组装、DB summary、建库、增量建库、向量补齐写业务/SQL 摘要
   - LLM 和 Agent 外呼记录 provider、model、耗时、usage 摘要
   - SQL 日志默认记录逻辑数据库操作摘要，不逐条打印所有 SQLite 语句，避免大库检索产生海量日志

5. 文档与目录
   - 新增 `docs/LOGGING.md`
   - README 增加日志文档入口
   - `.gitignore` 忽略 `log/*`，保留 `log/.gitkeep`

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/*.py`
- API 联调应检查：
  - `log/requests/YYYY-MM-DD.jsonl`
  - `log/errors/YYYY-MM-DD.jsonl`
  - `log/system/YYYY-MM-DD.jsonl`
  - `log/business/YYYY-MM-DD.jsonl`
  - `log/sql/YYYY-MM-DD.jsonl`

## 2026-05-01 - 智能助手三索引后端启动

### 背景

智能助手业务问答需要同时使用代码索引、metadata 元数据索引和表结构索引。此前 `serve-api` 只显式指定代码库，metadata/table 依赖自动发现，不利于生产部署和排查。

### 本轮改动

1. HTTP API 启动参数
   - `serve-api` 新增 `--metadata-db`
   - `serve-api` 新增 `--table-db`
   - `/health` 输出当前三类默认索引路径

2. 智能助手链路
   - `/agent/chat` 支持 `metadata_db_path` 和 `table_db_path`
   - `AgentGateway.chat()` 透传三类索引路径
   - LangChain agent 优先使用显式 metadata/table 路径，缺省时保留默认自动发现

3. 文档
   - 更新 `docs/system_files/DEPLOYMENT.md`
   - 更新 `docs/system_files/QUICKSTART.md`
   - 更新 `docs/system_files/WORKLOG.md`

### 当前推荐启动命令

```bash
PYTHONPATH=src python3 -m uses_indexer serve-api \
  --db examples/business_code_index.db \
  --metadata-db examples/business_metadata_index.db \
  --table-db examples/business_table_index.db \
  --host 127.0.0.1 \
  --port 8000
```

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/langchain_agent.py src/uses_indexer/agent_gateway.py src/uses_indexer/api.py src/uses_indexer/cli.py`
- `USES_INDEXER_ENV_FILE=/nonexistent PYTHONPATH=. pytest -q tests/test_api.py`

## 2026-05-01 - 智能助手模型 403 兜底修复

### 背景

前端智能助手请求失败：

```text
502: Intent classification failed: Error code: 403
Kimi For Coding is currently only available for Coding Agents...
```

根因是当前配置的模型不允许被普通 OpenAI-compatible HTTP 聊天接口调用，导致意图识别节点失败后直接抛出 502。

### 本轮改动

1. 意图识别兜底
   - `classify_retrieval_intent` 调用失败时不再中断请求。
   - 改用本地规则判断问题是否属于代码库/业务问题。
   - 本地判断结果写入 `context_bundle.intent.source = local_rule_fallback`。

2. LangChain 模型调用兜底
   - 如果 LangChain 依赖缺失或后续 LangChain 调模型仍失败，不再返回 502。
   - 后端改为执行本地索引检索，并返回检索摘要。
   - 响应中通过 `context_bundle.fallback` 和 `raw_response.fallback` 标记模型不可用。

3. 日志
   - 意图识别失败写入 `log/errors`，保留 provider、model、base_url 和兜底判断结果。

4. 检索词修复
   - 修复 `功能号333002` 这类中文紧贴数字时无法优先拆出 `333002` 的问题。
   - 本地兜底查询计划现在优先使用功能号数字，再使用整句补充检索。

5. 性能优化
   - 为纯数字功能号增加 `object_id_exact` 快速路径。
   - 直接查询 `procedures.object_id`，避免兜底场景进入完整大库召回。

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/agent_gateway.py src/uses_indexer/langchain_agent.py src/uses_indexer/api.py`
- `USES_INDEXER_ENV_FILE=/nonexistent PYTHONPATH=. pytest -q tests/test_api.py`，12 passed

## 2026-05-01 - Kimi Coding 调用链修复

### 背景

`.env` 当前使用：

```text
USES_INDEXER_AGENT_OPENAI_MODEL=kimi-for-coding
USES_INDEXER_AGENT_OPENAI_BASE_URL=https://api.kimi.com/coding/v1/chat/completions
```

该接口要求请求具备 Coding Agent 调用特征。`.env` 已配置 `USES_INDEXER_AGENT_OPENAI_USER_AGENT=claude-code/0.1.0`，但 LangChain `ChatOpenAI` 链路没有透传该 header，导致接口返回 403。

### 本轮改动

1. User-Agent 透传
   - LangChain `ChatOpenAI` 增加 `default_headers`。
   - 将 `AgentProviderConfig.user_agent` 透传给模型请求。

2. 模型调用策略
   - 撤销对 `kimi-for-coding` 的预跳过逻辑。
   - 恢复真实模型调用。
   - 如果模型仍不可用，再及时返回本地索引兜底结果并说明原因。

3. 意图识别修复
   - LLM 意图识别若误判明显的功能号/代码问题为无需检索，本地规则会覆盖为需要检索。

4. 检索工具性能
   - LangChain code tool 增加 `object_id_exact` 快速路径。
   - 即使模型传入整句，也先抽取功能号并直查 `procedures.object_id`。

### 验证

- `USES_INDEXER_ENV_FILE=/nonexistent PYTHONPATH=. pytest -q tests/test_api.py`，17 passed
- 真实接口验证：
  - 请求：`功能号333002包含哪些业务流程？`
  - Kimi 调用成功，不再 403。
  - LangChain 工具调用成功，调用 `search_code_index`。
  - 命中 `object_id_exact`。
  - 返回 `LS_SESEXT_NORMALORDER_ENTER / LS_证券周边_普通委托`。

## 2026-05-05 - LLM Service 统一改造

### 背景

项目有 3 套独立的 LLM HTTP 调用实现（`llm.py`、`agent_gateway.py`、`agent_loop.py`），各自拼 payload、发请求、解析响应，代码高度重复。需要统一封装为 `LlmService` 工具类，支持多 provider（Kimi / Xiaomi）切换。

### 本轮改动

1. `.env` 多 provider 配置
   - 新增 `KIMI_*` 和 `XIAOMI_*` 前缀式配置
   - `USES_INDEXER_LLM_PROVIDER` 控制默认 provider
   - 调用方可通过 `provider` 参数临时切换

2. `LlmService` 统一工具类（`src/uses_indexer/llm.py`）
   - `LlmService.from_env()` 按 provider 加载配置
   - `LlmService.chat()` 统一调用入口，支持 tools、response_format
   - 统一重试、超时、响应解析（content / tool_calls / usage）

3. 调用点迁移
   - `answering.py` — `CodebaseAnswerer` 改用 `LlmService`
   - `agent_loop.py` — 删除 `_perform_llm_request`，用 `LlmService`
   - `agent_gateway.py` — 删除 `_complete_openai_compatible` 等重复代码，用 `LlmService`
   - `langchain_agent.py` — 迁移到 `LlmService`，清理 config mutation hack

### 验证

- `python3 -c "from uses_indexer.llm import LlmService; s = LlmService.from_env(); print(s.list_providers())"`
- 前端智能助手对话链路正常

## 2026-05-05 - 前端 Markdown 渲染与聊天历史修复

### 背景

前端存在多个渲染问题：Mermaid 流程图背景不透明、聊天历史恢复后 Markdown 未解析（显示原始文本）、代码块缩进丢失。

### 本轮改动

1. Mermaid 流程图
   - 背景改为透明（CSS `.chat-message .mermaid-container`）
   - `preprocessMarkdown` 修复 LLM 输出的代码块格式（语言标识在独立行）

2. 聊天历史 Markdown 渲染修复
   - 根因：`app.js` 的 fallback `renderMarkdown` 同步返回纯文本，不等待动态 import 完成
   - 修复：改为 `await _mdModuleReady` 等待模块加载后再渲染
   - `markdown-renderer.js` 增加 `marked` 可用性检查和 try-catch 错误处理

3. Markdown 元素样式
   - `.chat-message` 新增 h1-h6、p、ul/ol、blockquote、table、a、hr 完整样式
   - 代码块 `white-space: pre` 保留缩进

### 验证

- 刷新页面后点击历史对话，Markdown 正常渲染
- Mermaid 流程图背景透明
- 代码块缩进正确

## 2026-05-05 - 业务文档模块

### 背景

前端已有"说明文档"模块（加载 `docs/system_files`），但缺少"业务文档"模块（应加载 `docs/business_files`）。后端 API 已支持 `?dir=business_files` 过滤参数。

### 本轮改动

1. `index.html`
   - 导航栏新增"业务文档"链接
   - 新增 `view-biz-docs` 列表视图和 `view-biz-doc-detail` 详情视图
   - DOM ID 加 `biz-` 前缀，复用 `.doc-*` CSS 类名

2. `app.js`
   - `initRefs` 新增 biz-docs DOM 引用
   - `setView` 新增 `biz-docs` 懒加载
   - 新增 `loadBizDocs`（API 带 `?dir=business_files`）、`renderBizDocsList`、`changeBizDocPage`、`onBizDocPageInput`、`renderBizDocDetail`、`backToBizDocs`

3. 无需改动
   - 后端（已有 `?dir=` 参数支持）
   - CSS（复用 `.doc-*` 类名）
   - 全局搜索（已自动包含 business_files 文档）

### 验证

- 点击导航栏"业务文档"，列表只显示 `docs/business_files/` 中的文件
- 点击条目，详情页正确渲染 Markdown
- 分页和返回列表功能正常

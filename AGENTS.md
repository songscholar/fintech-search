# AGENTS.md — uses-indexer

> 本文件面向 AI 编程助手。如果你第一次接触这个仓库，请先读本文，再按需要深入 `docs/` 目录。

---

## 项目概览

`uses-indexer` 是一个面向 USES/UFT DSL 代码库与 `metadata` 元数据目录的本地索引器与问答系统原型。

- **项目名称**：`uses-indexer`
- **版本**：`0.2.0`
- **Python 版本要求**：`>= 3.11`
- **核心目标**：把 XML 外壳 + CDATA DSL 代码体解析成结构化数据，写入 SQLite，提供混合检索、证据组装、问答包生成、HTTP API、MCP Server 和 Codex 插件接入。

端到端链路：

```
源码目录 -> 解析 -> SQLite 索引 -> 混合检索 -> 证据组装 -> 问答包 -> 最终回答 -> CLI/HTTP/MCP/Codex
```

当前不是编译器级精确语义还原，而是“面向大模型的本地代码知识后端”。

---

## 技术栈

| 层级 | 技术 |
|------|------|
| 语言 | Python 3.11+ |
| 构建系统 | `setuptools`（`pyproject.toml`） |
| 数据库 | SQLite + FTS5 |
| 向量召回 | 本地零依赖哈希向量（默认）或 OpenAI-compatible embedding（可选） |
| HTTP 服务 | 标准库 `http.server`（`ThreadingHTTPServer`） |
| MCP | 自研 stdio MCP server（不依赖外部 MCP SDK） |
| 前端 | 原生 HTML/CSS/JS（`src/uses_indexer/web/`） |
| 测试 | `pytest` |
| 外部模型 | OpenAI-compatible 聊天接口（可选） |

**零外部依赖原则**：默认安装不引入任何第三方 Python 包。所有可选能力（embedding、LLM 调用）通过环境变量配置，在缺失时自动降级。

---

## 目录结构

```
.
├── pyproject.toml              # 项目配置、setuptools 入口
├── .env.example                # 环境变量模板（LLM、Embedding、Agent Gateway）
├── .gitignore                  # 忽略 .db、__pycache__、*.egg-info 等
├── README.md                   # 面向人类用户的使用说明与能力清单
├── AGENTS.md                   # 本文件
│
├── src/uses_indexer/           # 核心源码包
│   ├── __init__.py             # 包公开 API
│   ├── __main__.py             # python3 -m uses_indexer 入口
│   ├── cli.py                  # CLI 命令编排（所有子命令注册在这里）
│   ├── parser.py               # 解析层：XML 外壳 + CDATA DSL 语句流
│   ├── metadata_parser.py      # 解析层：metadata 目录元数据条目
│   ├── table_parser.py         # 解析层：表结构文件
│   ├── indexer.py              # 索引层：SQLite 建库、查询、增量更新
│   ├── index_build.py          # 建库流程（全量/增量/向量补齐）
│   ├── index_write.py          # 写库细节（表创建、批量写入）
│   ├── table_indexer.py        # 表结构索引器
│   ├── retrieval.py            # 检索层：多路召回（FTS + 向量 + SQL fallback）
│   ├── rerank.py               # 重排层：意图感知重排、过程级聚合加权
│   ├── context_fetch.py        # 上下文获取：相关调用、来路调用、表访问
│   ├── evidence.py             # 证据组装：选择、裁剪、生成 llm_context
│   ├── qa.py                   # 问答包：system_prompt / user_prompt / draft_answer
│   ├── answering.py            # 回答层：调用外部模型或回退到 draft_answer
│   ├── llm.py                  # LLM 适配器：OpenAI-compatible 接口
│   ├── embeddings.py           # Embedding 层：本地哈希 + 外部接口 + 缓存 + 兼容校验
│   ├── api.py                  # HTTP API：/health /query /evidence /ask /answer /agent/*
│   ├── mcp_server.py           # stdio MCP server：5 个工具暴露
│   ├── agent_gateway.py        # 智能体网关：代理外部 Hermes/OpenClaw/OpenAI 服务
│   ├── evaluation.py           # 评测层：eval-retrieval、阈值检查
│   ├── debug_bundle.py         # 调试包：单题链路归档、回归面板、baseline 管理
│   ├── integration.py          # Codex skill/plugin 本地安装器
│   ├── semantic_recovery.py    # 语义规则唯一事实来源（调用语义、消息发布语义）
│   ├── observability.py        # 结构化 trace 输出
│   ├── config.py               # .env 发现与加载
│   ├── constants.py            # 常量与意图关键词集合
│   ├── schema.py               # SQLite DDL（所有表、FTS、索引定义）
│   ├── models.py               # 核心数据类：ParsedUnit、CodeStatement 等
│   ├── response_schema.py      # API 响应结构定义
│   ├── strategy_config.py      # 回答策略配置
│   ├── index_catalog.py        # 默认索引库发现
│   ├── index_utils.py          # 索引通用工具
│   ├── db_summary.py           # 数据库摘要
│   ├── metadata_semantics.py   # 元数据语义处理
│   ├── metadata_store.py       # 元数据存储
│   ├── web/                    # 内置前端
│   │   ├── index.html
│   │   ├── styles.css
│   │   └── app.js
│
├── tests/                      # 测试目录
│   ├── test_parser.py
│   ├── test_indexer.py
│   ├── test_api.py
│   ├── test_answering.py
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_embeddings.py
│   ├── test_evaluation.py
│   ├── test_qa.py
│   ├── test_mcp.py
│   ├── test_integration.py
│   ├── test_semantic_rules.py
│   └── test_table_indexer.py
│
├── docs/                       # 详细文档（中文）
│   ├── API.md                  # HTTP API 接口说明
│   ├── business_files/         # 业务文档
│   └── system_files/           # 系统说明文档
│       ├── ARCHITECTURE.md     # 架构总览、模块职责、设计取舍
│       ├── CALL_SEMANTICS.md   # LS/LF/AF 调用语义规则
│       ├── CHANGELOG.md        # 更新日志
│       ├── DEPLOYMENT.md       # 本地部署、HTTP/MCP/Codex 接入
│       ├── DEVELOPER_GUIDE.md  # 开发者指南、模块边界、推荐开发路径
│       ├── DEVELOPMENT_NOTES.md# 开发笔记
│       ├── EVALUATION.md       # 评测框架、A/B 对比、debug bundle 面板
│       ├── FRONTEND_DESIGN.md  # 前端页面设计说明
│       ├── FRONTEND_TECHNICAL.md # 前端与 API 对接方式
│       ├── INDEX_BOUNDARIES.md # 代码索引 / 元数据索引 / 全量索引边界
│       ├── INDEX_SCHEMA.md     # SQLite 表结构详细说明
│       ├── METADATA_INDEXING.md # 元数据索引说明
│       ├── NEWCOMER_GUIDE.md   # 新手指南、默认索引、常用命令
│       ├── OVERVIEW.md         # 项目概览
│       ├── QUICKSTART.md       # 快速开始
│       ├── RETRIEVAL_TUNING.md # 检索与重排调优指南
│       ├── SEMANTIC_RULES_EXTENSION.md # 扩展 DSL 语义规则
│       ├── TECH_SELECTION.md   # 技术选型
│       ├── TRACE_SCHEMA.md     # 结构化调试输出格式
│       ├── TROUBLESHOOTING.md  # 常见问题排障
│       ├── USAGE.md            # 日常提问方式、结果解读
│       └── WORKLOG.md          # 实施过程记录
│
├── eval/                       # 评测用例
│   ├── uses_codes_cases.json
│   └── uses_codes_effect_cases.json
│
├── examples/                   # 示例输出、摘要、报告（不纳入版本控制）
│   # .db 文件、.json 报告等均在此目录生成
│
├── plugins/
│   └── uses-codebase-plugin/   # Codex repo-local 插件
│       ├── .codex-plugin/plugin.json
│       ├── .mcp.json
│       └── scripts/run_mcp_server.py
│
├── skills/
│   └── uses-codebase-search/   # Codex 技能定义
│       └── SKILL.md
│
└── .agents/
    └── plugins/marketplace.json # 本地插件市场入口
```

---

## 安装与构建

```bash
# 安装为可编辑包（零外部依赖）
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m pip install -e .

# 验证安装
python3 -m uses_indexer --help
```

项目没有 `Makefile`、`setup.py` 或 `requirements.txt`。依赖通过 `pyproject.toml` 管理，当前 `dependencies = []`，即零外部依赖。

---

## 常用命令

### 建库
```bash
# 全量建库（本地哈希向量，默认）
python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code \
  --db examples/business_code_index.db \
  --output examples/business_code_index_summary.json

# 增量建库
python3 -m uses_indexer build-index ... --incremental

# 只补齐缺失向量
python3 -m uses_indexer build-index ... --resume-vectors

# 跳过向量阶段（后续再补）
python3 -m uses_indexer build-index ... --skip-vectors
```

### 查询与问答
```bash
# 简单查询
python3 -m uses_indexer query-index --db <db> --query "证券代码获取" --limit 10

# 组装证据
python3 -m uses_indexer assemble-evidence --db <db> --query "..." --limit 6

# 生成问答包
python3 -m uses_indexer ask-codebase --db <db> --question "..."

# 最终回答
python3 -m uses_indexer answer-codebase --db <db> --question "..."
```

### 评测
```bash
# 检索评测
PYTHONPATH=src python3 -m uses_indexer eval-retrieval \
  --db examples/uses_codes_index.db \
  --cases eval/uses_codes_cases.json \
  --limit 10 \
  --top-k 1,3,5,10 \
  --output examples/uses_codes_eval_report.json

# 评测对比
python3 -m uses_indexer compare-eval \
  --before examples/uses_codes_eval_report_before.json \
  --after examples/uses_codes_eval_report_after.json
```

### 服务启动
```bash
# HTTP API
python3 -m uses_indexer serve-api --db <db> --host 127.0.0.1 --port 8000

# MCP Server
python3 -m uses_indexer serve-mcp --db <db>

# 安装 Codex 集成
python3 -m uses_indexer install-codex-integration
```

---

## 测试

```bash
# 全量测试
PYTHONPATH=. pytest -q

# 推荐子集（局部修改时）
PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_evaluation.py tests/test_semantic_rules.py

# 语法检查
python3 -m py_compile src/uses_indexer/*.py
```

测试策略：
- 单元测试覆盖解析、索引、检索、问答、API、MCP、配置、embedding、评测、语义规则、表结构索引。
- 评测用例放在 `eval/` 目录，与功能测试分离。
- 新能力开发时，建议同步补充：功能测试、质量评测、规则测试（`tests/test_semantic_rules.py`）。

---

## 代码风格与开发约定

### 1. 模块分层约束

新逻辑不要堆回 `indexer.py`。按职责放入对应模块：

| 职责 | 文件 |
|------|------|
| 建库流程 | `index_build.py` |
| 写库细节 | `index_write.py` |
| 检索逻辑 | `retrieval.py` |
| 重排逻辑 | `rerank.py` |
| 上下文获取 | `context_fetch.py` |
| 证据裁剪 | `evidence.py` |
| 语义规则 | `semantic_recovery.py` |

### 2. 语义规则单一事实来源

调用语义（`LS/LF/AF/RS` 前缀规则）和消息发布语义已统一在 `semantic_recovery.py`。扩展新调用类型、消息发布类型或 label formatter 时，优先改这里，不要在其他模块再写一套。

### 3. 调试输出结构化

不要临时拼自由格式 debug 字段。优先复用 `observability.py` 和 `docs/TRACE_SCHEMA.md` 定义的结构化 trace。

### 4. 数据模型

核心模型使用 `@dataclass(slots=True)`，位于 `models.py`：

- `ParsedUnit`：文件级解析结果
- `CodeStatement`：单条语句
- `HistoryEntry`：文件修改历史
- `ParameterDecl`：参数声明

### 5. 常量与配置

意图关键词、正则表达式、阈值常量统一放在 `constants.py`。环境变量配置通过 `config.py` 的 `bootstrap_env()` 加载 `.env` 文件。

### 6. 字符串处理

项目处理大量中文 DSL 代码，字符串编码统一使用 UTF-8。JSON 输出默认 `ensure_ascii=False`。

---

## 开发工作流规范

### 1. 修改必须同步记录

**任何代码或配置的实质性修改完成后，必须同步记录到日志。** 不记录等于没完成。

| 日志文件 | 记录内容 | 面向读者 |
|---------|---------|---------|
| `docs/system_files/CHANGELOG.md` | 改了什么（功能 / 修复 / 改进列表） | 外部用户、协作者 |
| `docs/system_files/WORKLOG.md` | 怎么改的（阶段背景、决策过程、验证结果、设计教训） | 未来维护者、接棒 agent |

记录时机：
- 新增功能、修复 bug、性能优化、接口变更 → 同步追加 CHANGELOG
- 涉及方案选型、踩坑、验证过程、回退决策 → 同步追加 WORKLOG
- 单轮会话内的多次迭代，可在会话末尾一次性整理写入，不要完全遗漏

### 2. 文档变更必须同步更新

如果修改涉及以下文档类型，必须同步更新对应文件：

| 文档类型 | 存放位置 | 说明 |
|---------|---------|------|
| 系统说明文档 | `docs/system_files/` | 架构、部署、开发指南、评测、调优等 |
| 业务文档 | `docs/business_files/` | 业务规则、业务逻辑说明、业务术语表等 |
| 知识文档 | `docs/business_files/` 或 `docs/system_files/` | 沉淀的 domain knowledge、排查手册 |
| API/接口文档 | `docs/API.md` | HTTP API 端点、请求/响应格式、调用示例 |

**约束**：禁止只改代码不改文档。如果文档需要大篇幅重写，至少先追加一条"待完善"标记，说明当前状态。

### 3. 提交前必须本地 commit

每轮有意义的改动完成后，**必须先 `git add` + `git commit` 提交到本地**，再执行推送或其他操作。

- 不要在工作区留下大量未提交的零散改动
- 提交信息应清晰描述改动的目的和范围
- 如果工作区同时存在本次改动和历史遗留未提交文件，优先只提交本次相关改动；清理历史遗留变动应单独一轮处理
- 提交前检查：`.env` 是否含敏感信息、临时产物是否被误加入

### 4. 禁止提交的敏感信息

- `.env` 文件（含 API Key、密码等）——即使已在 git 跟踪中，新增敏感值时也应避免提交
- 运行期产物：CLI 输出 `.json`、诊断脚本、临时 `.db`、`.fuse_hidden*` 等
- 个人报告：如 `333002_business_logic_report.md` 这类单题分析产物

正确做法：
- 敏感配置通过 `.env.example` 模板同步，真实值留在本地 `.env`
- 临时产物写入 `examples/` 但不加入 git；如需保存，按日期建立子目录如 `examples/2026-05-01/`

---

## 输出规范

### 1. CLI 默认输出目录

所有会产生文件输出的 CLI 命令，如果未显式指定 `--output`，默认写入项目根目录下的 `examples/`：

- `query-index` → `examples/query_index_YYYYMMDD_HHMMSS.json`
- `eval-retrieval` → `examples/eval_retrieval_YYYYMMDD_HHMMSS.json`
- `answer-codebase` → `examples/answer_codebase_YYYYMMDD_HHMMSS.json`
- `debug-bundle` → `examples/debug_bundle_YYYYMMDD_HHMMSS.json`
- `db-summary` → `examples/db_summary_YYYYMMDD_HHMMSS.json`
- 其他评测、对比、回归面板命令同理

### 2. AI 助手执行约束

**禁止**在项目根目录直接创建以下类型的临时文件：

- `.json`（查询结果、评测报告、调试包）
- `.py`（临时诊断脚本、测试脚本）
- `.db`（索引库、缓存库）
- `.sh`（临时 shell 脚本）
- `.md`（临时日志、报告）

**正确做法**：

- 执行 CLI 时**总是显式指定 `--output`**：
  ```bash
  python3 -m uses_indexer query-index \
    --db examples/business_code_index_openai.db \
    --query "证券代码获取" \
    --output examples/query_result.json
  ```
- 临时诊断脚本放到 `examples/scripts/` 或 `examples/tmp/` 下
- 索引库和缓存库统一放到 `examples/` 下
- 如果 `examples/` 下文件过多，可以按日期建立子目录，如 `examples/2026-04-29/`

### 3. 已有目录约定

| 目录 | 用途 |
|------|------|
| `examples/` | CLI 输出、索引库、缓存、报告、摘要 |
| `examples/scripts/` | 临时诊断/测试脚本 |
| `examples/tmp/` | 一次性临时文件 |
| `src/uses_indexer/web/` | 内置前端资源 |
| `tests/` | pytest 测试文件 |
| `docs/` | 项目文档 |
| `eval/` | 固定评测用例 |

项目根目录（`/`）**只保留**源代码、配置和文档，不保存运行期产物。

---

## 关键配置

### 环境变量

复制 `.env.example` 到 `.env` 后按需填写：

```bash
cp .env.example .env
```

核心配置组：

- **LLM 回答**：`USES_INDEXER_LLM_API_KEY`、`USES_INDEXER_LLM_MODEL`、`USES_INDEXER_LLM_BASE_URL`
- **Embedding**：`USES_INDEXER_EMBEDDING_API_KEY`、`USES_INDEXER_EMBEDDING_MODEL`、`USES_INDEXER_EMBEDDING_BASE_URL`、`USES_INDEXER_EMBEDDING_CACHE_DB`
- **Agent Gateway**：`USES_INDEXER_AGENT_OPENAI_*`、`USES_INDEXER_AGENT_HERMES_*`、`USES_INDEXER_AGENT_OPENCLAW_*`

兼容别名（OpenAI embedding 专用）：`OPENAI_EMBEDDING_KEY`、`OPENAI_EMBEDDING_URL`、`OPENAI_EMBEDDING_NAME` 等。

### 默认索引库

服务启动时按以下优先级自动发现索引库：

1. `examples/business_code_index.db`（推荐，完整代码目录，不含 metadata）
2. `examples/business_full_index.db`（代码 + metadata 混合）
3. `examples/uses_codes_index.db`（子库，用于回归评测）

---

## 安全注意事项

1. **密钥管理**：API Key 只通过环境变量或 `.env` 注入，不要写进仓库文件。`.gitignore` 已忽略 `.env`。
2. **SQL 注入防护**：所有 SQLite 查询使用参数化绑定，不要拼接用户输入到 SQL 字符串。
3. **路径安全**：CLI 和 API 接收的路径参数应验证是否在预期目录内，避免路径遍历。
4. **HTTP 服务**：`serve-api` 使用标准库 `http.server`，当前面向本地开发，不建议直接暴露到公网。
5. **MCP Server**：stdio MCP 在当前进程内运行，注意避免阻塞 I/O。
6. **Embedding 缓存**：缓存数据库（`*_EMBEDDING_CACHE_DB`）只保存文本 hash 和向量 JSON，不保存原始代码文本。

---

## 部署方式

当前项目支持 4 种运行形态，共用同一套核心模块：

1. **CLI 单机模式**：本地建库、手工验证、评测。
2. **本地 HTTP 服务**：`serve-api`，前端通过 `http://127.0.0.1:8000/ui` 访问。
3. **stdio MCP 模式**：`serve-mcp`，接入 Codex 或支持 MCP 的 IDE/Agent。
4. **对话式工具接入**：通过 `install-codex-integration` 安装 skill 和 plugin。

Agent Gateway 设计：前端不直接连外部模型，而是走后端代理，好处是不暴露模型地址和鉴权，且能把本地检索上下文先组装好再交给外部智能体。

---

## 文档阅读顺序

如果你是第一次接触这个仓库：

1. `docs/NEWCOMER_GUIDE.md` — 认清默认索引、跑通 3 个常用命令
2. `docs/USAGE.md` — 学会怎么提问、怎么看返回结果
3. `docs/ARCHITECTURE.md` — 理解端到端调用链和各模块职责
4. `docs/DEVELOPER_GUIDE.md` — 模块边界、开发约束、推荐开发路径
5. `docs/INDEX_SCHEMA.md` — SQLite 里到底存了什么
6. `docs/DEPLOYMENT.md` — 怎么本地部署、怎么接 HTTP/MCP/Codex
7. `docs/EVALUATION.md` — 评测怎么跑、怎么做 A/B 对比和回归面板

---

## 版本与变更

- 当前版本：`0.2.0`
- 版本定义在 `pyproject.toml`
- 变更历史见 `docs/system_files/CHANGELOG.md` 或 `docs/system_files/WORKLOG.md`

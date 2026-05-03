# 更新日志

## 2026-05-01

### 新功能

- **新增 `/agent/analyze` 深度分析端点**
  - 专用于功能号业务逻辑深度解读，返回结构化分析报告。
  - 直接复用 `query_index(limit=2000, expand_downstream=True)` 的原始检索结果，不做中间加工。
  - 将前 3 个原始 hit（含 `procedure_profile`、`downstream_evidence`、`matched_text` 等完整字段）直接交给 LLM 自由整理。

- **智能助手前端自动路由**
  - `web/app.js` 的 `sendChat()` 在业务问答模式下自动检测 5–6 位纯数字或"功能号"关键词。
  - 命中后自动路由到 `/agent/analyze`，直接展示 LLM 整理后的业务逻辑报告。

### 改进

- **简化 `run_deep_analysis` 实现**
  - 废弃自组 `_build_evidence_for_agent`、`_format_evidence_for_llm`、六章模板 Prompt 以及 `_slim_*` / `_merge_*` 等中间加工逻辑。
  - 改为直接调用 `indexer.query_index`，将原始 JSON hits 交给 LLM，信息更完整，避免人为过滤导致丢失关键上下文。
  - 兼容 "1"+oid 映射（如 `333014` → `1333014`），解决功能号自然提问因 FTS 分词稀释而查不到的问题。

- **`evidence.py` 补充 `downstream_evidence`**
  - `assemble_evidence` 对 `hit_type == "procedure"` 的候选调用 `_expand_downstream_for_hit(conn, context_fetch, ...)`。
  - 输出字段与 `/query` API 对齐，包含 depth=3、max=9 的下游调用链展开及代码摘录。

- **超时配置提升**
  - `.env` 增加 `USES_INDEXER_AGENT_OPENAI_TIMEOUT=180` 和 `USES_INDEXER_LLM_TIMEOUT=180`。
  - `llm.py` 的 `OpenAICompatibleLlm.from_env()` 读取该值，解决 `/answer` 60 秒超时问题。

- **kimi-for-coding `reasoning_content` 兼容**
  - `agent_gateway.py` 和 `llm.py` 的 `_extract_content()` 增加对 `message.reasoning_content` 的提取 fallback。
  - 兼容 kimi-for-coding 返回空 `content` 但带 `reasoning_content` 的场景。

- **Agent Loop 二次提炼修复**
  - `api.py` 的 `_execute_analyze_tool` 在返回 report 前增加前缀指令，要求 LLM 直接完整呈现业务分析报告，不要进行额外摘要或压缩。
  - 解决 `/agent/run` 走 Agent Loop 时，报告被第二轮 LLM 压缩导致输入输出参数、表访问等细节丢失的问题。

- **文档目录重组**
  - 原 `docs/` 根目录文件分类移至 `docs/system_files/` 和 `docs/business_files/`。
  - 新增 `docs/API.md`，汇总当前 HTTP API 端点、请求/响应格式和调用示例。

### 验证

- **333104 报告质量修复**
  - 之前：输出参数空、调用链仅一层、无表信息。
  - 之后：LLM 基于原始 `procedure_profile` + `downstream_evidence` 还原出 4 层完整链路、下游 12 个输出字段、3 个读表、配置开关控制逻辑。

- **333002 验证通过**
  - LLM 基于原始 `matched_text` 还原出完整委托属性重置规则矩阵（3416/3574/3674 开关、各类证券类别映射）。

- **333014 映射兼容**
  - 支持 "1"+oid 映射，`333014` 能正确对应到 `1333014` 并命中 `LF_ESTTRADECTRL_PREOPENING_TRADE_HANDLE`。

## 2026-04-23

### 修复

- 修复功能号自然问题的主候选排序：`333002功能有哪些业务逻辑` 现在会优先命中 `LS_SESEXT_NORMALORDER_ENTER / object_id=333002`。
- 修复回答层 location 类问题的主候选判定，避免重复命中的次级检查块通过聚合分反超主服务。
- 补齐 `/favicon.ico` 响应，减少前端联调时的浏览器 404 噪音。

### 验证

- 完成前端当前实际使用接口联调：`/health`、`/db-summary`、`/query`、`/evidence`、`/ask`、`/answer`、`/debug-bundle`、`/agent/providers`、`/agent/chat`。
- 浏览器验证 `整套分析`、页面导航、结果页签和智能体设置弹窗均可正常使用。

## 2025-04-15

### 新功能

- **多跳调用链支持**
  - 从固定的 2 跳扩展为支持最多 10 跳调用链
  - 使用 BFS 算法进行多级遍历
  - 不同跳数有不同的权重（1-3跳强信号，4-6跳中等信号，7-10跳弱信号）
  - 追踪 outgoing（调用他人）和 incoming（被调用）两个方向的调用链

### 重排权重

| 跳数 | 权重 |
|-----|------|
| 1 | 3.0 |
| 2 | 1.5 |
| 3 | 1.0 |
| 4 | 0.6 |
| 5 | 0.4 |
| 6 | 0.25 |
| 7 | 0.15 |
| 8 | 0.1 |
| 9 | 0.05 |
| 10 | 0.02 |

### 代码改动

- `_procedure_call_neighbors()`: 支持 `max_depth` 参数，默认 10
- 重排逻辑：按跳数分配不同权重
- 证据组装：包含 `hop_depth` 和 `direction` 信息

---

## 历史版本

### v1.0 (初始版本)

- 支持 UFT/USES DSL 代码解析
- SQLite 索引存储
- FTS 全文检索
- 本地哈希向量 + OpenAI 向量双模式
- 混合检索 + 意图感知重排
- MCP / HTTP / CLI 多接口
- 元数据索引
- 消息中心主题发布追踪
- 完整的评测框架

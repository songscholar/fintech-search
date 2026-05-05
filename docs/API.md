# API 文档

## 端点列表

| 方法 | 端点 | 说明 |
|------|------|------|
| POST | `/query` | 检索代码索引 |
| POST | `/evidence` | 组装证据 |
| POST | `/ask` | 生成 QA 包 |
| POST | `/answer` | 生成最终回答 |
| POST | `/agent/chat` | Agent 对话 |
| **POST** | **`/agent/analyze`** | **深度分析（新增）** |
| GET | `/agent/providers` | 列出可用 Agent 提供商 |

---

## POST /agent/analyze

### 功能
执行 6 步深度调查流程，返回 LLM 生成的结构化 Markdown 业务分析报告。

适合场景：功能号精确分析、业务流程还原、调用链梳理。前端可直接渲染 `report` 字段。

### 请求体

```json
{
  "db_path": "indexes/business_code_index.db",
  "question": "333104功能的业务逻辑有哪些",
  "provider": "openai-compatible",
  "provider_override": {
    "base_url": "https://api.kimi.com/coding/v1/chat/completions",
    "model": "kimi-for-coding",
    "api_key": "sk-..."
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `db_path` | string | 是 | SQLite 索引库路径 |
| `question` | string | 是 | 分析问题（建议包含功能号） |
| `provider` | string | 否 | Agent 提供商名称 |
| `provider_override` | object | 否 | 临时覆盖提供商配置 |

### 响应体

```json
{
  "response_kind": "agent_deep_analyze",
  "question": "333104功能的业务逻辑有哪些",
  "report": "## 一、功能定义\n| 属性 | 内容 |\n|------|------|\n| 过程名 | LS_SESEXT_STOCKINFO_REQ |\n| 中文名 | LS_证券周边_客户证券持仓查询 |\n| 功能号 | 333104 |\n...",
  "elapsed_ms": 80709
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `response_kind` | string | 固定值 `agent_deep_analyze` |
| `question` | string | 原始问题 |
| `report` | string | LLM 生成的 Markdown 格式业务分析报告（前端可直接渲染） |
| `elapsed_ms` | int | 总耗时（毫秒） |

`report` 内容按以下六章组织：
1. **功能定义** — 属性表格（过程名、中文名、功能号、文件路径、类型、上游调用方）
2. **核心业务流程** — 总体概述 + 编号流程步骤（含条件分支树形图）
3. **关键输入参数** — Markdown 表格（参数名、说明、类型）
4. **关键输出参数** — Markdown 表格
5. **设计要点** — 2-5 条核心设计模式、业务规则、版本变更影响
6. **相关下游功能** — Markdown 表格（下游过程名、调用场景、调用方式）

### 6 步调查流程（后端执行，不暴露给前端）

| 步骤 | 动作 | 说明 |
|------|------|------|
| 1 | 确认索引库存在 | 检查数据库路径和大小 |
| 2 | 全文检索定位 | `query_index(limit=20, expand_downstream=True)` |
| 3 | 精确查找功能定义 | SQL 查询 `procedures.object_id = ?` |
| 4 | 解析源代码 | `parser.parse_path()` 提取修改历史、参数列表 |
| 5 | 查找上游调用关系 | SQL 查询 `edges.target_name = ?` |
| 6 | 查找下游调用关系 | SQL 查询 `edges.procedure_id = ?` |

最后一步：把 6 步原始证据组装成 prompt，调用 LLM 生成结构化报告。

### 与 `/agent/chat` 的区别

| | `/agent/chat` | `/agent/analyze` |
|---|---|---|
| 工作模式 | LangChain Agent 自动决策 | 固定 6 步流水线 |
| 返回内容 | 纯文本答案 | 结构化 Markdown 报告（6 章固定格式） |
| 适合场景 | 开放式问题 | 功能号精确分析、业务流程还原 |
| 前端渲染 | 直接展示文本 | 可用 Markdown 渲染器直接渲染 |
| 证据深度 | 依赖 Agent 决策 | 强制执行：检索→SQL→parse→edges |

### 性能参考

| 阶段 | 耗时 |
|------|------|
| 6 步数据收集 | ~1-2s |
| LLM 报告生成 | ~60-90s |
| **总耗时** | **~80s** |

> LLM 超时默认设置为 180s，以容纳长 prompt 推理。

---

## POST /query

### 变更：新增 `expand_downstream` 参数

```json
{
  "db_path": "indexes/business_code_index.db",
  "query": "333001",
  "limit": 10,
  "expand_downstream": true
}
```

- `expand_downstream` 默认 `true`
- 开启后，对 top 3 个 procedure hit 递归展开下游调用链（depth=3, max_downstream=9）
- 每个 hit 增加 `downstream_evidence` 和 `downstream_count` 字段

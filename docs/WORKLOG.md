# Worklog

## 2026-04-09

### 阶段 1：项目初始化

- 创建项目目录结构
- 明确项目目标：先做 DSL 解析层，再做索引层
- 结合完整代码目录 `uses_codes` 的真实结构确认了第一版范围

### 阶段 2：当前优先级

- 优先实现 XML + CDATA DSL 解析器
- 优先沉淀文档，而不是最后再补说明
- 优先支持最核心的结构：
  - 文件元数据
  - 参数
  - 历史记录
  - DSL 动作
  - 过程调用
  - 基础控制流

### 阶段 3：第一版解析器完成并验证

- 增加 CLI：
  - `parse-file`
  - `scan-dir`
- 增加单元测试，当前已通过
- 对完整目录 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 做全量扫描
- 当前扫描结果：
  - 文件数 `2564`
  - `Function` `1858`
  - `Service` `703`
  - `FactorService` `3`
- 当前语句抽取结果：
  - `action` `18140`
  - `call` `8085`
  - `control` `21326`
  - `assignment` `16406`
  - `comment` `33196`

### 阶段 4：本轮补强

- 增加对 `break / continue` 的控制流识别
- 增加对 `++@var / --@var` 的写入识别
- 增加对 `hs_strcpy / sprintf / hs_snprintf / substr` 等常见输出参数写入识别

### 阶段 5：SQLite 索引层

- 新增 `SQLiteIndexer`
- 增加表结构：
  - `files`
  - `procedures`
  - `histories`
  - `params`
  - `statements`
  - `actions`
  - `variable_refs`
  - `edges`
- 对完整目录 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 完成一版真实建库
- 当前数据库统计：
  - `files` `2564`
  - `procedures` `2564`
  - `histories` `7380`
  - `params` `70004`
  - `statements` `159148`
  - `actions` `26225`
  - `variable_refs` `214948`
  - `edges` `61249`

### 阶段 6：基础查询能力

- CLI 增加：
  - `build-index`
  - `db-summary`
  - `query-index`
- 支持按过程名、中文名、动作名、动作目标、变量名、语句原文进行基础检索
- 增加索引层测试并通过

### 阶段 7：FTS 检索与证据组装

- 在 SQLite 中增加：
  - `procedures_fts`
  - `statements_fts`
  - `actions_fts`
  - `edges_fts`
- `query-index` 升级为：
  - FTS 召回
  - SQL fallback
  - Python 重排
- 新增 `assemble-evidence`
- 增加 `llm_context` 组装能力，使检索结果可以直接喂给问答模型
- 补充索引层测试，覆盖：
  - FTS 建库
  - 混合检索
  - 证据上下文组装

### 阶段 8：问答包层

- 新增 `CodebaseQA`
- 新增 `ask-codebase` CLI
- 统一输出：
  - `prompt_package`
  - `draft_answer`
  - `supporting_locations`
- 当前问答层不直接依赖外部模型 API，而是先把可复用的问答输入和本地草稿答案整理好

### 阶段 9：本地 HTTP API

- 新增 `CodebaseApi`
- 新增 `serve-api` CLI
- 暴露接口：
  - `GET /health`
  - `GET /db-summary`
  - `POST /query`
  - `POST /evidence`
  - `POST /ask`
- API 层保持零额外依赖，直接基于标准库 `ThreadingHTTPServer`
- 补充 HTTP 层测试，确保服务可以真正起起来并返回 JSON

### 阶段 10：最终回答层与技能化

- 新增 `OpenAICompatibleLlm`
- 新增 `CodebaseAnswerer`
- 新增 CLI：
  - `answer-codebase`
- 新增 API：
  - `POST /answer`
- 当前支持：
  - 配置外部模型时调用模型生成最终回答
  - 未配置模型时回退到 `draft_answer`
- 新增仓库内技能定义：
  - `skills/uses-codebase-search/SKILL.md`
- 已安装到本机：
  - `/Users/songzuoqiang/.codex/skills/uses-codebase-search/SKILL.md`

### 后续计划

- 增加块级结构恢复
- 增加向量索引
- 增加更精确的表访问与关系抽取
- 增加更丰富的模型适配器
- 增加 MCP 集成封装

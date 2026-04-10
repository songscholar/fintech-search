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

### 阶段 11：MCP 与插件集成

- 新增 `CodebaseMcpServer`
- 新增 CLI：
  - `serve-mcp`
- 当前 MCP server 通过 stdio 暴露工具：
  - `db_summary`
  - `query_codebase`
  - `assemble_evidence`
  - `ask_codebase`
  - `answer_codebase`
- 新增 repo-local 插件：
  - `plugins/uses-codebase-plugin/.codex-plugin/plugin.json`
  - `plugins/uses-codebase-plugin/.mcp.json`
  - `plugins/uses-codebase-plugin/scripts/run_mcp_server.py`
  - `plugins/uses-codebase-plugin/skills/uses-codebase-search/SKILL.md`
- 新增 repo-local marketplace：
  - `.agents/plugins/marketplace.json`
- 更新仓库技能定义，使其优先使用 MCP，HTTP 作为 fallback
- 补充 MCP 层测试，覆盖：
  - `initialize`
  - `tools/list`
  - `tools/call`
  - stdio 输出格式

### 阶段 12：本地安装器

- 新增 `CodexIntegrationInstaller`
- 新增 CLI：
  - `install-codex-integration`
- 当前安装器会以符号链接方式安装：
  - `~/plugins/uses-codebase-plugin`
  - `~/.codex/skills/uses-codebase-search`
- 当前安装器还会维护：
  - `~/.agents/plugins/marketplace.json`
- 补充安装层测试，覆盖：
  - 首次安装
  - 重复安装幂等

### 阶段 13：检索质量增强

- 新增 `chunks` 和 `chunks_fts`
- 当前会按控制流边界和语句密度切出语义块
- `query-index` 现在会直接召回块级命中
- `assemble-evidence` 对块命中会直接使用块级上下文
- `assemble-evidence` 会额外补充一跳相关过程的摘要
- 重排层增加：
  - `chunk` 命中加权
  - 多来源命中加权

### 阶段 14：本地向量召回

- 新增 `LocalHashedEmbedder`
- 新增 `chunk_vectors`
- 建库时会为每个 `chunk` 生成本地哈希向量
- `query-index` 当前会把 `vector_chunk` 结果与 `FTS`、`LIKE` 一起混合重排
- 当前目标是补足“不完全同词但语义接近”的召回

### 阶段 15：外部 embedding 接入与兼容保护

- 新增 `OpenAICompatibleEmbedder`
- 新增 `create_embedder_from_env`
- 当前 embedding 层支持：
  - 默认走本地 `LocalHashedEmbedder`
  - 配置环境变量后切到 OpenAI-compatible embedding 接口
- 建库时会把 `embedding_provider / embedding_model / embedding_dimension` 写入 SQLite 元数据
- 查询时会先校验当前 embedding 配置与索引库是否处于同一向量空间
- 如果不兼容，会自动禁用向量召回，并在结果中输出 `vector_status`
- 如果向量请求失败，会自动回退到 `FTS + LIKE + rerank`
- `_insert_chunks` 改成按文件内语义块批量生成向量，减少外部 embedding 请求次数
- 补充测试，覆盖：
  - 默认本地 embedding
  - 环境变量切换到外部 embedding
  - 外部 embedding 分批请求
  - 向量空间不匹配时的安全降级
- 查询 embedding 请求失败时的安全回退

### 阶段 16：深层结构块恢复

- 新增 `blocks`
- 新增 `block_edges`
- 新增 `blocks_fts`
- 当前已恢复的结构块包括：
  - `transaction`
  - `sql_query`
  - `sql_execute`
  - `failure_handler`
  - `record_loop`
  - `record_pool_loop`
  - `component_loop`
- 结构块恢复基于已解析的扁平语句流，不额外引入第二套解析器
- `query-index` 增加块级命中
- `assemble-evidence` 会补充覆盖当前证据的恢复块
- `llm_context` 会显式携带恢复块摘要和块级关系
- 补充测试，覆盖：
  - 块表建库
  - 块级全文索引
  - 失败处理块召回
  - 证据中的覆盖块摘要

### 阶段 17：异常路径与退出标签恢复

- 新增结构块：
  - `exception_handler`
  - `when_others_handler`
  - `goto_exit`
  - `goto_jump`
  - `exit_label`
- 新增关系边：
  - `jumps_to_label`
  - `jumps_to_exit`
  - `defines_label`
- `related_context` 现在会补充控制流摘要
- `llm_context` 现在会显式输出 `Control flow`
- 补充测试，覆盖：
  - `svr_end` 查询
  - `goto / label` 关系边
  - 失败处理问句下的 `EXCEPTION / WHEN_OTHERS` 恢复

### 阶段 18：SQL 表访问抽取与两跳调用链

- `通用SQL执行`、`查询SQL语句开始` 现在会从 SQL 文本中抽取真实表名
- 当前支持从 `select / update / insert / delete / merge` 中恢复 `reads_table / writes_table`
- 查询重排新增两跳调用链 bonus
- `related_context` 新增：
  - `two_hop_outgoing`
  - `two_hop_incoming`
- `llm_context` 新增：
  - `Two-hop outgoing chain`
  - `Two-hop incoming chain`
- 调用链恢复增加 `name / chinese_name` 别名归一，解决真实仓库里“定义名”和“调用名”不一致的问题
- 补充测试，覆盖：
  - SQL 表访问抽取
  - 两跳调用链证据
  - 两跳调用链重排

### 阶段 19：动态 SQL 恢复

- 建库阶段新增轻量字符串提示追踪
- 当前支持从这些模式恢复 SQL 文本：
  - `@sql_str = "..."`
  - `hs_strcpy(@sql_str, "...")`
  - `sprintf(@sql_str, "...%s...", @table_name)`
  - `hs_snprintf(@sql_str_tmp, ..., "%s ...", @sql_str_tmp, "...")`
- `通用SQL执行[@sql_str][]` 这类语句现在会优先尝试展开最近一次字符串构造结果
- 如果展开成功，会继续按标准 SQL 规则抽取 `reads_table / writes_table`
- 在真实仓库中已验证到 `AF_DATASEINIT_SECONDLOADUSESTABLE` 这类 `delete from %s` 模式能恢复出可用表访问证据
- 新增样例：
  - `examples/uses_codes_dynamic_sql_example.json`
- 补充测试，覆盖：
  - 动态 SQL 建库不回归
  - 动态 SQL 表名检索

### 阶段 20：意图感知重排

- 查询阶段新增轻量意图分析
- 当前识别：
  - 表访问 / SQL 问题
  - 表写入 / 表读取问题
  - 变量赋值 / 参数问题
  - 调用链 / 被调用问题
  - 失败处理 / 异常路径问题
  - 过程 / 服务 / 函数定位问题
- 重排阶段会根据意图调整候选证据权重：
  - 表写入问题优先抬高 SQL 块、表访问边、写表动作
  - 变量赋值问题优先抬高 `assignment` 语句和变量写入命中
  - 被调用问题优先抬高调用方上下文
  - 失败处理问题优先抬高失败块、异常块、`WHEN_OTHERS` 相关证据
- 对非调用链问题会降低调用链 bonus，避免调用关系把局部证据挤下去
- 新增样例：
  - `examples/uses_codes_intent_rerank_example.json`
- 补充测试，覆盖：
  - 变量赋值意图
  - 表写入意图
  - 被调用意图
  - 失败处理意图

### 阶段 21：检索评测闭环

- 新增 `RetrievalEvaluator`
- 新增 CLI：
  - `eval-retrieval`
- 新增评测用例文件：
  - `eval/uses_codes_cases.json`
- 新增评测报告样例：
  - `examples/uses_codes_eval_report.json`
- 当前评测用例覆盖：
  - 动态 SQL 表写入
  - 错误码报错路径
  - 表读取
  - 过程调用引用
  - SQL 变量执行
- 当前报告指标包括：
  - `pass@k`
  - `expectation_recall@k`
  - `mean_first_relevant_rank`
  - 每个期望项的命中详情
  - 每个问题的 top hits
- 当前 5 条 baseline case 的样例结果：
  - `pass@1 = 1.0`
  - `pass@3 = 1.0`
  - `pass@5 = 1.0`
  - `pass@10 = 1.0`
  - `expectation_recall@10 = 0.9`
- 新增文档：
  - `docs/EVALUATION.md`
- 补充测试，覆盖：
  - 对象形式和数组形式的用例文件
  - 多类 expected 匹配
  - 汇总指标计算

### 阶段 22：评测报告 A/B 对比

- 新增评测报告对比函数：
  - `compare_eval_reports`
- 新增 CLI：
  - `compare-eval`
- 当前支持比较：
  - `pass@k`
  - `expectation_recall@k`
  - `mean_first_relevant_rank`
  - `matched_cases`
  - case 级 top hit 和首个相关排名
- case 级变化分类包括：
  - `improved`
  - `regressed`
  - `unchanged`
  - `added`
  - `removed`
- 新增样例：
  - `examples/uses_codes_eval_compare.json`
- 补充测试，覆盖：
  - 相同报告自比较
  - 首个相关排名后移时标记为 regression

### 阶段 23：OpenAI 兼容 Embedding 实测接入

- 扩展 `OpenAICompatibleEmbedder` 的环境变量兼容层，支持：
  - `OPENAI_EMBEDDING_KEY`
  - `OPENAI_EMBEDDING_URL`
  - `OPENAI_EMBEDDING_NAME`
  - `OPENAI_EMBEDDING_MODEL`
  - `OPENAI_EMBEDDING_BATCH_SIZE`
  - `OPENAI_EMBEDDING_DIMENSIONS`
  - `OPENAI_EMBEDDING_TIMEOUT`
- `OPENAI_EMBEDDING_URL` 支持填到 `/v1`，程序会自动规范化为 `/v1/embeddings`
- 外部 embedding 请求超时时间现在可以通过环境变量调整，避免大仓建库时被慢响应长期卡住
- 对 `https://oapi.aivue.cn/v1` + `text-embedding-3-large` 做了 smoke test：
  - batch size `1`、`4`、`16` 均返回 `3072` 维向量
  - 完整建库建议先使用 `OPENAI_EMBEDDING_BATCH_SIZE=16`
- 新增本地 hash 评测基准：
  - `examples/uses_codes_eval_report_local_hash.json`
- 新增不含密钥的真实 embedding 探测记录：
  - `examples/uses_codes_embedding_smoke.json`
- 补充测试，覆盖：
  - OpenAI embedding 别名配置
  - 别名维度、批量大小和超时参数
  - 非法超时参数报错

### 阶段 24：真实 Embedding 端到端评测

- 使用评测用例覆盖子集完成端到端测试：
  - 子集根目录：`/tmp/uses_codes_eval_subset`
  - 子集文件数：`4`
  - 子集语义块数：`193`
  - 真实 embedding 向量数：`193`
- 新增子集索引摘要：
  - `examples/uses_codes_index_subset_local_hash_summary.json`
  - `examples/uses_codes_index_real_embedding_subset_summary.json`
- 新增子集评测报告：
  - `examples/uses_codes_eval_report_subset_local_hash.json`
  - `examples/uses_codes_eval_report_real_embedding_subset.json`
  - `examples/uses_codes_eval_compare_real_embedding_subset.json`
- 新增端到端测试汇总：
  - `examples/uses_codes_embedding_e2e_report.json`
- 本轮评测结论：
  - 本地 hash 子集和真实 embedding 子集的 `pass@10` 都是 `1.0`
  - 真实 embedding 子集的 `matched_cases` 为 `5`
  - `expectation_recall@3` 和 `expectation_recall@5` 相对本地 hash 子集各下降 `0.1`
  - case 级变化为 `unchanged = 5`
- 全量成本评估：
  - 全量索引当前有 `28748` 个语义块
  - 当前按文件内 chunk 分批，batch size `16` 估算约 `3620` 次外部 embedding 请求
  - 代表性 16 条真实语义块请求耗时约 `13.45` 秒
  - 在加入全局批处理、断点续建或 embedding cache 前，不建议直接做全量真实 embedding 短测试

### 阶段 25：外部 Embedding 本地缓存

- 新增 `SQLiteEmbeddingCache`
- `OpenAICompatibleEmbedder` 现在支持可选本地 SQLite 缓存：
  - `USES_INDEXER_EMBEDDING_CACHE_DB`
  - `OPENAI_EMBEDDING_CACHE_DB`
- 缓存 key 由以下内容共同决定：
  - provider
  - model
  - base URL
  - dimensions
  - text SHA-256
- 缓存只保存文本 hash 和向量 JSON，不保存原始代码文本
- 命中缓存时不会调用外部 embedding 接口
- 未命中时按原 batch size 调用外部接口，并在请求成功后立即写入缓存
- 这样即使全量真实 embedding 建库中途中断，已完成的向量也能在下一次运行时复用
- 补充测试，覆盖：
  - `OPENAI_EMBEDDING_CACHE_DB` 环境变量读取
  - SQLite cache 跨 embedder 实例复用
  - 命中缓存时不重复请求外部接口

### 阶段 26：全局向量批处理与断点续建

- 调整建库流程：
  - 先解析并写入 `files / procedures / statements / chunks`
  - 再统一扫描缺失 `chunk_vectors` 的 chunk
  - 按全局 batch size 调用当前 embedder
  - 每完成一个向量 batch 就写入 `chunk_vectors` 并提交事务
- `_insert_chunks` 现在只负责写入 chunk 和 `chunks_fts`，不再逐文件请求 embedding
- 新增 `resume_chunk_vectors`
- `build-index` 新增参数：
  - `--resume-vectors`
- 续建模式会：
  - 校验命令传入的 source root 是否和索引库 metadata 一致
  - 校验当前 embedding provider / model / dimension 是否和索引库兼容
  - 自动跳过已有 `chunk_vectors`
  - 只为缺失向量的 chunk 发起 embedding 请求
- 建库结果新增 `vector_stats`，记录：
  - batch size
  - 续建前缺失向量数
  - 本轮插入向量数
  - batch 数
  - 续建后缺失向量数
- 补充测试，覆盖：
  - 全局批处理不再按文件逐个请求 embedding
  - 向量 batch 失败前已完成的 batch 会落库
  - `--resume-vectors` 只补齐缺失向量并跳过已有向量

### 阶段 27：真实 Embedding 中等规模续建验证

- 使用 6 个中等复杂文件做真实 embedding 测试：
  - 子集根目录：`/tmp/uses_codes_embedding_medium_subset`
  - 文件数：`6`
  - 语义块数：`475`
- 首次构建启用：
  - `OPENAI_EMBEDDING_BATCH_SIZE=16`
  - `OPENAI_EMBEDDING_TIMEOUT=90`
  - `OPENAI_EMBEDDING_CACHE_DB=examples/uses_codes_embedding_cache_medium.db`
- 首次构建在 `256` 条向量已落库后遇到接口读取超时
- 修复 `OpenAICompatibleEmbedder`：
  - 将底层 `TimeoutError` 包装为 `EmbeddingRequestError`
- 续建使用：
  - `--resume-vectors`
  - `OPENAI_EMBEDDING_BATCH_SIZE=8`
  - `OPENAI_EMBEDDING_TIMEOUT=120`
- 续建结果：
  - `missing_before = 219`
  - `inserted = 219`
  - `batches = 28`
  - `missing_after = 0`
  - 最终 `chunk_vectors = 475`
- 再次执行 no-op resume：
  - `missing_before = 0`
  - `inserted = 0`
  - `batches = 0`
- 新增报告：
  - `examples/uses_codes_embedding_medium_benchmark.json`
  - `examples/uses_codes_index_real_embedding_medium_summary.json`
- 结论：
  - 全局批处理、每批提交、cache 和 `--resume-vectors` 已能覆盖真实接口中途超时场景
  - 全量建库建议优先使用 batch size `8` 或 `16` 并开启 embedding cache

### 阶段 28：真实 Embedding 融合调权

- 问题背景：
  - 真实 embedding 子集评测中，`stock-code-get-callers` 的局部精确证据被语义相近但不含目标调用的 `vector_chunk` 推后
  - 该 case 表现为首个相关命中在 rank `3`，`expectation_recall@3` 和 `expectation_recall@5` 相对本地 hash 子集各下降 `0.1`
- 调整策略：
  - 扩展中文查询切分词，识别 `哪些流程调用证券代码获取` 这类调用链问题
  - 从查询中抽取 `证券代码获取` 这类 `focus_terms`，并排除 `查询 / 执行 / 报错` 这类通用操作意图词
  - 对 `matched_text` 直接包含焦点词的候选加权
  - 对只在上下文中包含焦点词的候选给较弱加权
  - 对调用链问题中缺少焦点词的 `vector_chunk` 增加惩罚
  - 调用链多跳重排只给包含焦点词的候选追加结构化关系奖励，避免泛相关块借关系分数继续上浮
  - 调用链 intent 加权要求显式过程焦点，或焦点词加 `call_flow / call_block / calls_procedure` 信号同时存在
- 新增回归测试：
  - `test_query_index_keeps_exact_call_focus_above_vector_only_context`
  - 验证 `哪些流程调用证券代码获取` 中，命中精确焦点词的证据排在 `vector_focus_mismatch` 候选之前
- 重新运行真实 embedding 子集评测：
  - `pass@1/pass@3/pass@5/pass@10 = 1.0`
  - `expectation_recall@1/@3/@5/@10 = 1.0`
  - `mean_first_relevant_rank = 1.0`
  - `stock-code-get-callers` 从首个相关命中 rank `3` 提升到 rank `1`
  - case 级变化为 `improved = 1`、`regressed = 0`、`unchanged = 4`
- 更新报告：
  - `examples/uses_codes_eval_report_real_embedding_subset.json`
  - `examples/uses_codes_eval_compare_real_embedding_subset.json`
  - `examples/uses_codes_embedding_e2e_report.json`

### 后续计划

- 扩充评测集到 30 到 50 条真实业务问题
- 继续增强块级结构恢复
- 增加更深的事务块 / SQL 块 / 异常块恢复
- 增加更精细的 goto / label 路径恢复
- 增强复杂动态 SQL 场景下的表访问恢复
- 增加更精确的表访问与关系抽取
- 增加更丰富的模型适配器
- 增加更强的 MCP 能力和更多可组合工具

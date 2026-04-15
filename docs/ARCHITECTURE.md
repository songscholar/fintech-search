# Architecture

## 目标

这个项目面向 `/Users/songzuoqiang/Documents/agent/code` 这样的完整 UFT/USES DSL 代码根目录，也兼容 `uses_codes` 这类单独子目录。

当前输入源不再只有业务 DSL 文件，还包括各核心 `metadata` 目录下的标准字段、常量、错误号、宏、主题域、缓存表、组件、字典等元数据文件。

第一阶段目标不是“直接问答”，而是先建立一个可靠的解析层，让后续索引和问答建立在结构化数据上。

## 当前阶段范围

当前版本已经做到：

- 识别文件类型：`LF / LS / AF / RS`
- 解析 XML 元信息
- 解析 `CDATA` 中的 DSL 代码体
- 解析 `metadata` 目录中的元数据文件与条目级对象
- 产出统一的 JSON 结构
- 把解析结果落入 SQLite
- 提供 SQLite FTS
- 提供混合检索、重排和证据组装
- 提供语义块切分与块级 FTS
- 提供本地哈希向量与向量式召回
- 提供 OpenAI-compatible embedding 接口接入
- 提供索引端与查询端的向量空间兼容校验
- 提供事务块 / SQL 块 / 失败处理块 / 循环块恢复
- 提供异常块和退出标签恢复
- 提供 SQL 表访问抽取
- 提供动态 SQL 字符串恢复
- 提供基于过程前缀的调用语义分类：
  - `LS -> AF`
  - `LS -> LF`
  - `LF -> LF`
  - `LF -> AF`
  - 视为本地函数调用
  - `LS -> LS`
  - `LF -> LS`
  - `AF -> LS`
  - 视为系统间 RPC 调用
- 提供消息中心主题发布语义分类：
  - `[同步消息发布][topic_name = ...]`
  - `[消息发布][topic_name = ...]`
  - 视为消息中心跨核心发布
- 提供两跳调用链扩展与重排
- 提供意图感知重排
- 提供块级关系摘要
- 提供本地 HTTP API
- 提供最终回答层
- 提供 stdio MCP server
- 提供 repo-local Codex 插件封装
- 提供检索评测闭环

当前版本还没有做到：

- 完整编译器级 AST
- 精确块嵌套恢复
- 深层事务块 / SQL 块 / 异常块恢复
- 更精确的跨过程关系图

## 一图总览

```mermaid
flowchart LR
    SRC["USES/UFT 源码目录 + metadata 元数据目录"]
    PARSER["Parser 解析 XML 与 CDATA DSL / metadata 条目"]
    IR["结构化中间表示 ParsedUnit"]
    INDEXER["Indexer 建库与关系恢复"]
    DB[("SQLite 索引库")]
    EMB["Embedding 层 local-hash 或 OpenAI-compatible"]
    RETRIEVE["query-index 混合检索与重排"]
    EVIDENCE["assemble-evidence 证据组装"]
    QA["ask-codebase 问答包"]
    ANSWER["answer-codebase 最终回答"]
    HTTP["HTTP API"]
    MCP["stdio MCP server"]
    CODEX["Codex skill 与 plugin"]
    EVAL["评测层 eval-retrieval compare-eval"]

    SRC --> PARSER --> IR --> INDEXER --> DB
    EMB --> INDEXER
    DB --> RETRIEVE --> EVIDENCE --> QA --> ANSWER
    EMB --> RETRIEVE
    DB --> EVAL
    RETRIEVE --> EVAL
    RETRIEVE --> HTTP
    EVIDENCE --> HTTP
    QA --> HTTP
    ANSWER --> HTTP
    RETRIEVE --> MCP
    EVIDENCE --> MCP
    QA --> MCP
    ANSWER --> MCP
    MCP --> CODEX
```

这个图表达的不是“未来设想”，而是当前仓库已经落地的结构：

- 左侧是源码输入与解析建库链路
- 中间是 SQLite 索引、embedding 与混合检索核心
- 右侧是问答输出、HTTP 服务、MCP 与 Codex 接入层
- 下方是独立的评测闭环，用于验证每次检索调优是否真的变好

## 端到端问答链路

```mermaid
sequenceDiagram
    participant U as User
    participant C as CLI HTTP MCP
    participant A as CodebaseAnswerer
    participant Q as CodebaseQA
    participant I as SQLiteIndexer
    participant D as SQLite DB
    participant L as External LLM Optional

    U->>C: 提问
    C->>A: answer-codebase 或 POST /answer
    A->>Q: ask
    Q->>I: assemble-evidence
    I->>D: FTS LIKE chunk vector 查询
    D-->>I: 候选结果
    I-->>Q: evidence 与 llm_context
    Q-->>A: prompt_package 与 draft_answer
    alt 配置了外部模型
        A->>L: 发送 prompt 与证据
        L-->>A: 最终回答
    else 未配置外部模型
        A-->>A: 使用 draft_answer
    end
    A-->>C: final_answer
    C-->>U: 返回 grounded answer
```

这条链路说明当前系统的核心设计取舍：

- 外部模型不是直接看仓库，而是只看索引层筛选出来的证据
- `draft_answer` 始终存在，所以即使没有外部模型也能完成一次可解释回答
- CLI、HTTP API、MCP 只是不同入口，底层复用的是同一套索引与问答逻辑

## 运行形态

当前项目支持 4 种运行形态：

- 离线建库：`build-index`、`db-summary`、`eval-retrieval`
- 本地查询：`query-index`、`assemble-evidence`、`ask-codebase`
- 本地服务：`serve-api`
- 对话式工具接入：`serve-mcp`、Codex skill、repo-local plugin

这 4 种形态共用一套核心模块，没有额外的“第二套服务实现”。

## 模块职责与源码映射

| 层级 | 主要职责 | 对应文件 |
| --- | --- | --- |
| 解析层 | 解析 XML 外壳、CDATA DSL、语句流、参数与元信息 | `src/uses_indexer/parser.py` |
| 索引层 | 建库、写入 SQLite、恢复关系、切块、块恢复、向量入库 | `src/uses_indexer/indexer.py` |
| Embedding 层 | 本地 hash 向量、外部 embedding、缓存与兼容校验 | `src/uses_indexer/embeddings.py` |
| 问答包层 | 生成 `system_prompt`、`user_prompt`、`draft_answer` | `src/uses_indexer/qa.py` |
| 回答层 | 调用外部模型或回退到 `draft_answer` | `src/uses_indexer/answering.py`, `src/uses_indexer/llm.py` |
| HTTP 层 | 暴露 `/query /evidence /ask /answer` | `src/uses_indexer/api.py` |
| MCP 层 | 暴露 `query_codebase / assemble_evidence / answer_codebase` 等工具 | `src/uses_indexer/mcp_server.py` |
| CLI 层 | 命令行入口与参数编排 | `src/uses_indexer/cli.py` |
| 评测层 | 检索评测与 A/B 对比 | `src/uses_indexer/evaluation.py` |
| 集成层 | 安装 Codex skill 与 plugin | `src/uses_indexer/integration.py`, `plugins/uses-codebase-plugin/`, `skills/uses-codebase-search/` |

调用语义规则详见：

- `docs/CALL_SEMANTICS.md`

## 功能边界

当前项目最适合扮演的角色是“面向大模型的本地代码知识后端”，而不是完整 IDE 或编译器。

它当前已经做好的事情：

- 把稳定 DSL 仓库转成可检索、可追踪、可评测的结构化索引
- 把自然语言问题转换成带证据的回答输入
- 让外部大模型通过 API 或 MCP 调用本地索引能力

它暂时不追求的事情：

- 100% 精确的编译器级语义还原
- 完整控制流图和完整跨过程图数据库
- 直接替代 IDE 的所有导航和重构能力

## 代码库观察结论

基于完整代码目录的抽样和统计，这个仓库有几个重要特点：

- 当前全量索引已经覆盖 `21148` 个 DSL 文件、`201030` 个语义块和 `40887` 个结构块

- 文件格式高度统一，属于稳定 DSL
- XML 壳固定，逻辑集中在 `CDATA`
- 业务层和 atom 层都使用同一套 DSL，只是厚薄不同
- DSL 与 C/C++ 风格原始语句混用
- 需要支持标签、跳转、SQL、异常块、事务块

## 文件模型

每个文件会先被解析成一个 `ParsedUnit`：

- `path`
- `unit_kind`
  - `Function`
  - `Service`
  - `FactorService`
- `prefix`
  - `LF`
  - `LS`
  - `AF`
  - `RS`
- `name`
- `chinese_name`
- `object_id`
- `attributes`
- `histories`
- `parameters`
- `statements`

## 语句模型

第一版不会强行恢复完整语法树，而是先产出“结构化扁平语句流”。

主要语句类型：

- `comment`
- `label`
- `brace`
- `action`
- `call`
- `control`
- `goto`
- `assignment`
- `raw`

其中：

- `action` 表示 `[获取记录]`、`[通用SQL执行]` 这类 DSL 动作
- `call` 表示 `[LF_xxx]`、`[AF_xxx]`、`[LS_xxx]`、`[RS_xxx]` 这类过程调用
- `control` 表示 `if / else if / else / while / switch / break / continue`

## 为什么先做扁平语句流

这样做有三个好处：

1. 实现快，能快速覆盖全仓库
2. 即使局部语法特殊，也能保留原文不丢信息
3. 后续可以在现有语句流基础上继续恢复块关系，而不需要推翻重做

## 当前 SQLite 索引

当前 SQLite 库已经包含这些表：

- `files`
- `procedures`
- `histories`
- `params`
- `statements`
- `actions`
- `variable_refs`
- `edges`
- `chunks`
- `chunk_vectors`
- `blocks`
- `block_edges`
- `procedures_fts`
- `statements_fts`
- `actions_fts`
- `edges_fts`
- `chunks_fts`
- `blocks_fts`

其中：

- `statements` 保存结构化语句流
- `actions` 是从语句流里投影出的 DSL 动作与过程调用
- `variable_refs` 保存变量读写
- `edges` 保存过程调用、表访问、变量写入等关系
- SQL 相关边既可能来自静态 SQL，也可能来自 `sprintf/hs_snprintf/hs_strcpy` 逐步构造后的动态 SQL
- `chunks` 把过程按语义块切开，降低单语句检索过碎的问题
- `chunk_vectors` 为每个语义块保存一份向量，默认使用本地哈希向量，也可以切到外部 embedding
- `blocks` 把事务、SQL、失败处理、循环这类更稳定的业务结构恢复成可检索对象
- `block_edges` 把块内部的过程调用、表访问、动作目标、控制流跳转聚合成块级关系摘要

当前已经落下的重点关系：

- `LS -> LF`
- `LF / LS / AF / RS -> procedure`
- `procedure -> table`
- `procedure -> variable`
- `procedure -> action`
- `procedure -> component`

## 当前查询方式

当前查询能力已经形成一条轻量检索管线，入口包括：

- `build-index`
- `db-summary`
- `query-index`
- `assemble-evidence`
- `ask-codebase`
- `serve-api`
- `answer-codebase`

`query-index` 当前会按下面的顺序工作：

1. 用 `FTS5` 查：
   - 结构块
   - 语义块
   - 过程
   - 动作
   - 语句
   - 关系边
2. 用本地向量查：
   - 语义块向量
   - 对近义问题或不完全同词问题做补充召回
   - 查询前先校验当前 embedding 是否和索引库一致
   - 若不一致则自动跳过向量召回，避免混用不同向量空间
3. 用普通 SQL `LIKE` 做 fallback：
   - 过程名 / 中文名 / 文件路径
   - 动作名 / 动作目标
   - 变量名
   - 原始语句文本
   - 关系边目标
4. 在 Python 里按命中源、词覆盖率、精确匹配、过程名命中做重排
5. 对块命中优先返回块级上下文，并补一跳关系过程摘要
6. 对证据所在范围补充覆盖它的恢复块，让 LLM 知道当前语句属于哪个事务 / SQL / 失败路径
7. 对候选过程应用两跳调用链重排，让调用链上的相关过程更容易一起进入证据
8. 对 `@sql_str / @table_name / @where_str` 这类字符串变量追踪最近一次稳定赋值，尽量把动态 SQL 还原成可抽表名的文本
9. 对问题做轻量意图识别，区分表访问、变量赋值、调用链、失败路径、过程定位等不同检索目标

这里额外有一个仓库特性要处理：

- 过程定义通常使用文件 stem，例如 `AF_DATASEINIT_LOADUSESTABLE`
- 调用语句里经常使用 `chineseName`，例如 `AF_系统参数公用_系统配置信息获取`

所以当前调用链恢复会同时解析 `name / chinese_name` 两套别名，再把它们归一到同一个过程实体上。

SQL 恢复这边也有一个仓库特性要处理：

- 很多过程不是直接把 SQL 写进 `[通用SQL执行]`
- 而是先对 `@sql_str`、`@sql_str_tmp`、`@table_name` 做多次赋值
- 再通过 `sprintf / hs_snprintf / hs_strcpy` 拼接成最终 SQL

所以当前建库阶段会维护一份轻量的字符串提示表，尽量恢复最近一次可解析的 SQL 片段，再抽取 `reads_table / writes_table`。

意图感知重排不会替代全文检索和向量召回，而是在候选结果已经召回后做加权。例如：

- 问“某表在哪里更新”时，优先抬高 SQL 块、表访问边、写表动作
- 问“某变量在哪里赋值”时，优先抬高 assignment 语句和变量写入命中
- 问“某过程被谁调用”时，优先抬高调用方上下文和调用链证据
- 问“失败/异常在哪里处理”时，优先抬高 failure / exception / when_others 结构块

`assemble-evidence` 会在重排结果之上继续做：

- 取命中语句附近的上下文窗口
- 对块命中直接使用语义块上下文
- 合并成过程级证据块
- 补充相关调用、来路调用、表访问、动作
- 补充一跳相关过程的摘要
- 生成可直接给 LLM 的 `llm_context`

所以当前这层已经不是“单纯搜一下”，而是一个可供问答系统直接消费的检索前置层。

## Embedding 层设计

当前 embedding 层采用“双模式”：

1. 默认模式
   - 使用本地 `LocalHashedEmbedder`
   - 零额外依赖
   - 适合本地快速验证
2. 增强模式
   - 使用 OpenAI-compatible embedding 接口
   - 通过环境变量配置
   - 可选启用 SQLite embedding cache，避免重复请求相同文本的向量
   - 适合提升自然语言到业务流程的语义召回

索引构建时会把 `provider / model / dimension` 写入 `metadata`。
查询时会读取这组元数据，和当前 embedder 做兼容性比对；只有两边处于同一向量空间时，才会真正开启 `vector_chunk` 召回。

外部 embedding 缓存的 key 会绑定 `provider / model / base_url / dimensions / text_sha256`，所以切换模型、端点或维度时不会误用旧向量。缓存只保存文本 hash 和向量 JSON，不保存原始代码文本。

建库流程现在分成两段：先解析并写入 `files / procedures / statements / chunks`，再全局扫描缺失 `chunk_vectors` 的 chunk 做批量 embedding。每个向量 batch 都会独立提交事务；如果中途失败，可以用 `build-index --resume-vectors` 复用已有结构索引，只补齐缺失向量。

`ask-codebase` 则再向前走一步：

- 调用 `assemble-evidence`
- 构造统一的 `system_prompt`
- 构造面向 LLM 的 `user_prompt`
- 生成一个本地 `draft_answer`

这意味着当前仓库已经具备“检索层 + 问答包层”，后续重点从“能回答”转向“能被外部模型稳定调用”。

`serve-api` 则把这两层暴露成一个本地 HTTP 服务：

- `GET /health`
- `GET /db-summary`
- `POST /query`
- `POST /evidence`
- `POST /ask`
- `POST /answer`

这个 API 层目前使用标准库实现，目标是：

- 本地零额外依赖即可启动
- 便于前端、IDE 插件或 MCP 服务复用
- 先稳定协议，再考虑换到更完整的 Web 框架

## 当前回答层

当前项目已经增加一个可选的“外部模型调用层”：

- `answer-codebase`
- `POST /answer`

其工作方式是：

1. 先走 `ask-codebase`，构造证据、提示词和 `draft_answer`
2. 如果配置了 OpenAI-compatible 接口，则调用外部模型生成最终答案
3. 如果未配置模型，则回退到本地 `draft_answer`

所以当前仓库已经具备：

- 检索层
- 证据组装层
- 问答包层
- 最终回答层
- HTTP 服务层
- MCP 工具层
- 插件层

## 技能层

仓库同时包含一个可安装的 Codex 技能：

- `skills/uses-codebase-search/SKILL.md`

这个技能的作用不是直接实现检索，而是把“何时调用本地索引服务、优先用哪个接口、如何引用证据”固化成一个可复用工作流。

## MCP 与插件层

当前项目已经在现有索引和问答层外面再包了一层零依赖 MCP server。

它直接复用：

- `SQLiteIndexer`
- `CodebaseQA`
- `CodebaseAnswerer`

并暴露成 5 个标准工具：

- `db_summary`
- `query_codebase`
- `assemble_evidence`
- `ask_codebase`
- `answer_codebase`

这里的设计取舍是：

1. 先做 `stdio`，而不是额外引入 MCP SDK
2. 先把现有能力原样包装成工具，而不是另起一套服务逻辑
3. 先提供 repo-local plugin，方便在本仓库内一起演进和版本化

这样做的好处是：

- 依赖少
- 部署简单
- HTTP 和 MCP 共用同一套业务逻辑
- 后续要换成更完整的 SDK，也不会影响现有检索层和回答层

## 评测层

当前项目新增了 `RetrievalEvaluator`，用于在固定问题集上评估检索层质量。

它复用现有的 `SQLiteIndexer.query_index`，不会绕开真实检索链路。评测时每个 case 会声明问题和期望命中的过程、路径、文本、表名或行号区间，然后输出：

- `pass@k`
- `expectation_recall@k`
- 首个相关命中的排名
- 每个期望项对应的命中详情
- 每个问题的 top hits

这一步的目标是把“检索规则调优”变成可回归验证的工程过程。后续接入真实 embedding 或继续增强结构关系时，可以用同一份 `eval/uses_codes_cases.json` 对比效果变化。

当前也提供 `compare-eval` 离线对比能力。它不访问数据库，只比较两份评测报告，输出汇总指标 delta 和 case 级 `improved / regressed / unchanged / added / removed`。这样后续在本地 hash embedding、真实 embedding、不同重排策略之间切换时，可以快速判断改动收益和回归点。

## 检索质量增强

这一轮检索增强主要覆盖了 4 个维度：

1. 切分：
   - 不再只依赖单语句窗口，而是按控制流边界和语句密度生成 `chunk`
2. 索引：
   - 新增 `chunks` 与 `chunks_fts`
3. 关系：
   - 在证据组装里加入一跳相关过程摘要
4. 重排：
   - 对块命中和多来源命中增加权重

这一步先把“文件切块、结构化索引、关系扩展、重排”四件事真正接起来，再在其上叠加向量召回。

在此基础上，当前版本又加了一层零依赖的本地哈希向量召回：

- 不依赖外部 embedding 服务
- 对中文短语会提取 n-gram 特征
- 对英文/标识符会提取 token 和子串特征
- 主要目标是补足“同义但不完全同词”的召回

## 本地安装层

为了让 repo-local plugin 更容易真正接入 Codex，本项目还补了一个本地安装器：

- `install-codex-integration`

它负责三件事：

1. 把 repo-local plugin 以符号链接方式挂到 `~/plugins/uses-codebase-plugin`
2. 把仓库技能以符号链接方式挂到 `~/.codex/skills/uses-codebase-search`
3. 在 `~/.agents/plugins/marketplace.json` 里补齐本地 marketplace 入口

这里选择“符号链接”而不是“复制目录”，原因是：

- 插件启动脚本需要保留 repo-local 相对路径关系
- 后续仓库更新后，本地集成不需要再次复制整份文件
- 更适合当前这个快速演进中的原型项目

## 下一阶段索引方向

当当前索引层稳定后，下一阶段会继续增加：

- `blocks`
- `chunks`
- `fts_statements`
- `fts_actions`
- 更精确的 `db_access`

重点增强方向：

- 精确恢复 `if / while / transaction / exception` 层级
- 增加更强语义的 embedding / 向量索引
- 增加更细粒度的上下文块切分
- 增加更丰富的模型适配器
- 增加更强的 MCP 能力，例如资源、提示词模板和更细粒度的工具

## 文档策略

这个项目采用“边做边记”的方式：

- `README.md` 记录当前可用能力和使用方式
- `docs/ARCHITECTURE.md` 记录架构和设计取舍
- `docs/WORKLOG.md` 记录实施过程

说明文档不是最后补，而是和实现同步推进。

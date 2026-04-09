# Architecture

## 目标

这个项目面向 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 这样的 UFT/USES DSL 代码库。

第一阶段目标不是“直接问答”，而是先建立一个可靠的解析层，让后续索引和问答建立在结构化数据上。

## 当前阶段范围

当前版本已经做到：

- 识别文件类型：`LF / LS / AF / RS`
- 解析 XML 元信息
- 解析 `CDATA` 中的 DSL 代码体
- 产出统一的 JSON 结构
- 把解析结果落入 SQLite
- 提供 SQLite FTS
- 提供混合检索、重排和证据组装
- 提供语义块切分与块级 FTS
- 提供本地哈希向量与向量式召回
- 提供 OpenAI-compatible embedding 接口接入
- 提供索引端与查询端的向量空间兼容校验
- 提供事务块 / SQL 块 / 失败处理块 / 循环块恢复
- 提供块级关系摘要
- 提供本地 HTTP API
- 提供最终回答层
- 提供 stdio MCP server
- 提供 repo-local Codex 插件封装

当前版本还没有做到：

- 完整编译器级 AST
- 精确块嵌套恢复
- 深层事务块 / SQL 块 / 异常块恢复
- 更精确的跨过程关系图

## 代码库观察结论

基于完整代码目录的抽样和统计，这个仓库有几个重要特点：

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
- `chunks` 把过程按语义块切开，降低单语句检索过碎的问题
- `chunk_vectors` 为每个语义块保存一份向量，默认使用本地哈希向量，也可以切到外部 embedding
- `blocks` 把事务、SQL、失败处理、循环这类更稳定的业务结构恢复成可检索对象
- `block_edges` 把块内部的过程调用、表访问、动作目标聚合成块级关系摘要

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
   - 适合提升自然语言到业务流程的语义召回

索引构建时会把 `provider / model / dimension` 写入 `metadata`。
查询时会读取这组元数据，和当前 embedder 做兼容性比对；只有两边处于同一向量空间时，才会真正开启 `vector_chunk` 召回。

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

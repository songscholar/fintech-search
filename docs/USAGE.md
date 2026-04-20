# Usage Guide

## 目标

这份文档回答的是“平时应该怎么用这个项目”。

重点不是解释内部实现，而是告诉你：

- 什么场景用哪个入口
- 问题应该怎么提
- 返回结果应该怎么看
- 什么时候要继续深挖

项目支持四种索引类型：

## 四种索引类型

### 1. 全量索引（all）
- 包含所有文件（代码文件 + 元数据文件）
- 适用于综合检索场景
- 推荐文件名：`business_full_index.db`

### 2. 代码索引（code）
- 仅包含代码文件（.uftfunction、.uftservice、.uftatomfunction、.uftfactorservice、.extinterface）
- 适用于代码逻辑检索，避免元数据干扰
- 推荐文件名：`business_code_index.db`
- 这是默认代码检索库

### 3. 元数据索引（metadata）
- 仅包含元数据文件（metadata 目录下的文件）
- 适用于元数据检索，避免代码干扰
- 推荐文件名：`business_metadata_index.db`

### 4. 表结构索引
- 包含表结构信息（.uftstructure 文件）
- 适用于表结构、字段、索引、表空间等检索
- 推荐文件名：`business_table_index.db`

## 索引构建指南

### 使用便捷脚本 build_indexes.py（推荐）

项目提供了便捷脚本 `build_indexes.py`，支持多种构建模式，特别适合批量构建索引。

#### 构建模式说明

| 模式 | 说明 | 构建的索引 |
|------|------|-----------|
| `code` | 仅构建代码索引 | 代码索引 |
| `metadata` | 仅构建元数据索引 | 元数据索引 |
| `table` | 仅构建表结构索引 | 表结构索引 |
| `three` | 一次构建三个专用索引 | 代码索引、元数据索引、表结构索引 |
| `full` | 仅构建全量索引 | 全量索引（包含代码+元数据） |
| `all` | 构建所有四个索引 | 代码索引、元数据索引、全量索引、表结构索引 |

#### 推荐使用场景

**场景 1：分别构建单个索引**

当你只需要更新某个特定索引时使用：

```bash
# 仅重新构建代码索引
python3 build_indexes.py --mode code

# 仅重新构建元数据索引
python3 build_indexes.py --mode metadata

# 仅重新构建表结构索引
python3 build_indexes.py --mode table
```

**场景 2：一次构建三个专用索引（最常用）**

推荐日常使用这个模式，它会依次构建代码、元数据、表结构三个专用索引：

```bash
python3 build_indexes.py --mode three
```

脚本特性：
- 自动删除旧的索引文件
- 实时监控 WAL 文件大小变化
- 完整的异常处理，某个索引构建失败不会影响其他索引
- 详细的进度和统计信息输出

**场景 3：构建全量索引**

当你需要一个包含所有信息的综合索引时使用：

```bash
python3 build_indexes.py --mode full
```

**场景 4：构建所有四个索引**

当你需要完整的索引集合时使用：

```bash
python3 build_indexes.py --mode all
```

#### 脚本输出说明

运行脚本时，你会看到：

1. **进度标识**：`[1/3]`、`[2/3]` 等表示当前正在构建第几个索引
2. **WAL 监控**：实时显示 `.db-wal` 文件大小变化（这是正常的，构建完成后会自动合并）
3. **统计信息**：每个索引构建完成后显示文件数、过程数、表数量等统计
4. **完成提示**：显示所有构建的索引文件位置

### 使用 CLI 命令逐个构建

如果需要更精细的控制，可以使用 CLI 命令逐个构建索引。详见 [QUICKSTART.md](QUICKSTART.md) 中的详细说明。

当前推荐默认代码检索库是：

- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db`

如果你要同时查代码和 metadata，请显式切到：

- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_full_index.db`

如果你只查 metadata，请使用：

- `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_metadata_index.db`

`examples/uses_codes_index.db` 继续保留，但主要用于较小范围的回归测试和调试。

## 先选入口

如果你只想知道“应该用哪个命令”，直接看这张表：

| 目标 | 推荐入口 | 说明 |
| --- | --- | --- |
| 快速看命中结果 | `query-index` | 最接近搜索 |
| 给大模型准备证据 | `assemble-evidence` | 返回 `llm_context` |
| 生成问答包 | `ask-codebase` | 返回 prompt 和 `draft_answer` |
| 直接要最终回答 | `answer-codebase` | 有 LLM 就调 LLM，没有就回退到 `draft_answer` |
| 给其他程序调用 | HTTP API | 适合前端、脚本、服务 |
| 给 Agent / Codex 调用 | MCP | 适合对话式工具调用 |

## 日常最常用的 5 个命令

### 1. 搜命中

```bash
python3 -m uses_indexer query-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 10
```

适合：

- 看候选过程有哪些
- 看重排是否合理
- 快速定位文件和过程

### 2. 组装证据

```bash
python3 -m uses_indexer assemble-evidence \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 3 \
  --context-window 2 \
  --related-limit 3
```

适合：

- 看模型最终会拿到哪些证据
- 检查上下文是不是够完整
- 分析为什么答案会偏

### 3. 生成问答包

```bash
python3 -m uses_indexer ask-codebase \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --question "哪些流程调用证券代码获取"
```

适合：

- 检查 `system_prompt` 和 `user_prompt`
- 看本地 `draft_answer`
- 调试 LLM 接入前的输入质量

### 4. 直接回答

```bash
python3 -m uses_indexer answer-codebase \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --question "哪些流程调用证券代码获取"
```

适合：

- 直接拿结果
- 验证当前整条链路能否闭环

### 5. 表结构查询

```bash
python3 -m uses_indexer query-table-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_table_index.db \
  --query "客户" \
  --limit 5
```

适合：

- 查找表结构信息
- 查看表字段和索引
- 检索表空间配置

## 问题怎么提效果更好

### 推荐问法

- “`AF_xxx` 被谁调用”
- “`@sql_str1` 在哪里执行”
- “`uses_entrust` 在哪里查询”
- “`ERR_xxx` 在哪里报错”
- “`证券代码获取` 的逻辑在哪里”
- “`手工打包头` 宏定义在哪里”
- “`CNST_MC_UFT_OPTSYNC` 对应什么主题”
- “`upbs_arg` 缓存表定义在哪里”

### 更好的表达方式

优先带上这些信息：

- 明确的过程名
- 明确的变量名
- 明确的表名
- 明确的错误码
- 明确的业务术语

例如：

- 好：`AF_DATASEINIT_SECONDLOADUSESTABLE 中 @sql_str1 在哪里执行`
- 一般：`sql_str1 怎么跑的`

### 不太好的问法

- 太泛：`这个功能怎么实现`
- 太短：`证券`
- 太口语且没有上下文：`这个报错是哪来的`

这类问题不是不能答，而是更容易把召回范围放大。

## 常见场景怎么用

### 场景 1：找过程调用方

问题：

- `哪些流程调用证券代码获取`
- `AF_DEEP 被谁调用`

推荐入口：

- 先用 `query-index`
- 再用 `assemble-evidence`

重点看：

- `intent_call_chain`
- `call_chain_one_hop`
- `call_chain_two_hop`
- `incoming_callers`
- `本地函数调用 / 系统间RPC调用` 标签

如果 related context 里出现：

- `AF_xxx(本地函数调用 LS->AF)`，表示同核心内函数调用
- `LS_xxx(系统间RPC调用 LF->LS)`，表示更应该按跨系统 RPC 调用理解

### 场景 1.5：找谁往 MC 发布某个主题

问题：

- `谁发布 CNST_MC_UFT_PUBSYNC`
- `哪个流程往 MC 发布 CNST_MC_UFT_OPTSYNC`

重点看：

- `edge_type=publishes_mc_topic`
- `target_kind=mc_topic`
- `消息中心主题发布`
- `同步发布 / 异步发布`

### 场景 2：找变量赋值或执行点

问题：

- `@deep_flag 在哪里赋值`
- `@sql_str1 在哪里执行`

重点看：

- `variable_focus`
- `match_source=assignment`
- `intent_sql_action`
- `intent_procedure_context`

### 场景 3：找表读写

问题：

- `uses_entrust 在哪里查询`
- `reload_fundacct 在哪里被删除`

重点看：

- `table_focus`
- `reads_table`
- `writes_table`
- `block_type=sql_execute` 或 SQL 相关 block

### 场景 4：找失败处理

问题：

- `ERR_SECU_QRY_ENTRUST_FAIL 在哪里报错`
- `查询失败在哪里处理`

重点看：

- `failure_flow_match`
- `intent_failure_block`
- `failure_handler`
- `exception_handler`
- `when_others_handler`

### 场景 5：给大模型直接回答

推荐直接用：

- `answer-codebase`
- 或 `POST /answer`

如果想先检查证据是否靠谱，再决定要不要交给外部模型，就先看 `assemble-evidence`。

### 场景 6：表结构查询

问题：

- `客户基本信息表的结构是什么`
- `uact_client 表有哪些字段`
- `哪些表使用了 HS_UFT_DATA 表空间`

推荐入口：

- `query-table-index`

重点看：

- 表名、中文名、对象号
- 表字段列表
- 表索引信息
- 表空间配置（数据库表空间、索引表空间、历史表空间等）

## 返回结果怎么看

### `query-index` 返回里最重要的字段

- `hit_type`
  - 命中的对象类型，例如 `chunk / block / statement / action / edge`
- `retrieval_source`
  - 命中来源，例如 `fts_chunk / vector_chunk / like_block`
- `match_source`
  - 命中的具体字段，例如 `chunk_summary / action_fts / block_summary`
- `reasons`
  - 为什么它排到前面
- `vector_status`
  - 向量召回是否真的参与了这次查询

你可以这样理解：

- `hit_type` 看“命中了什么”
- `retrieval_source` 看“它是怎么被找出来的”
- `reasons` 看“它为什么排得这么高”

### `assemble-evidence` 返回里最重要的字段

- `excerpt`
  - 证据附近的真实代码片段
- `context_statements`
  - 上下文语句窗口
- `recovered_blocks`
  - 当前命中位于什么结构块里
- `related_context`
  - 相关调用、来路调用、表访问、控制流
- `llm_context`
  - 可直接交给模型的文本证据包

### `answer-codebase` 返回里最重要的字段

- `draft_answer`
  - 本地基于证据生成的保底回答
- `supporting_locations`
  - 支撑回答的文件和行号
- `uncertainties`
  - 当前证据不足或多候选冲突点
- `answer_source`
  - `draft` 或 `llm`

## API 的常用用法

先启动：

```bash
PYTHONPATH=src python3 -m uses_indexer serve-api \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --host 127.0.0.1 \
  --port 8000
```

### 查候选

```bash
curl -s http://127.0.0.1:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"query":"哪些流程调用证券代码获取","limit":5}'
```

### 查证据

```bash
curl -s http://127.0.0.1:8000/evidence \
  -H 'Content-Type: application/json' \
  -d '{"query":"哪些流程调用证券代码获取","limit":3,"context_window":2,"related_limit":3}'
```

### 直接回答

```bash
curl -s http://127.0.0.1:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"question":"哪些流程调用证券代码获取","evidence_limit":3}'
```

## MCP / Codex 场景怎么理解

如果你把它接进 Codex 或其他支持 MCP 的 Agent，推荐思路是：

- 当问题很明确时，直接走 `answer_codebase`
- 当问题范围较大、你担心误答时，先走 `assemble_evidence`
- 当你只想让模型帮你“找位置”而不是“下结论”时，走 `query_codebase`

也就是说：

- `query_codebase` 更像搜索
- `assemble_evidence` 更像可解释证据层
- `answer_codebase` 更像面向用户的最终输出层

## 结果不理想时怎么排查

### 1. 先看 `query-index`

不要一上来只看最终回答。先看：

- 目标过程有没有进前几名
- `reasons` 是否符合你的预期
- `vector_status` 是否启用

### 2. 再看 `assemble-evidence`

确认：

- 证据片段够不够直接
- 上下文是否缺失
- 是否恢复出了正确的事务块 / SQL 块 / 失败块

### 3. 最后再看 `answer-codebase`

如果检索和证据都对，但答案不自然，通常是回答层问题。
如果检索本身就偏了，那应该优先调索引、切块、关系或重排。

## 推荐使用顺序

如果你是第一次真正用它，建议这样走：

1. `query-index`
2. `assemble-evidence`
3. `answer-codebase`
4. 如果要系统化调优，再用 `eval-retrieval`

这样你会很快建立一种感觉：

- 命中对不对
- 证据够不够
- 最终回答是不是可信

## 相关阅读

- [README.md](/Users/songzuoqiang/Documents/agent/condex/codes/README.md)
- [ARCHITECTURE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/ARCHITECTURE.md)
- [DEPLOYMENT.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEPLOYMENT.md)
- [EVALUATION.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/EVALUATION.md)

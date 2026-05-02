# 开发者指南

这份文档回答的是：如果你要继续开发这个项目，应该从哪里下手。

重点不是列出所有源码文件，而是先建立“模块边界感”。

## 当前推荐的心智模型

当前项目可以按 5 层理解：

1. 解析层
2. 建库写入层
3. 检索与重排层
4. 证据与回答层
5. 接入层

## 模块入口

### 1. 解析层

- [parser.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/parser.py)
- [metadata_parser.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/metadata_parser.py)
- [table_parser.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/table_parser.py)

职责：

- 解析 XML 外壳
- 解析 CDATA DSL 语句流
- 解析 metadata 条目
- 解析表结构文件

### 2. 建库写入层

- [index_build.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/index_build.py)
- [index_write.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/index_write.py)
- [table_indexer.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/table_indexer.py)

职责：

- 建表
- 全量建库
- 增量建库
- 过程/语句/边/块/chunk 写入

### 3. 检索与重排层

- [retrieval.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/retrieval.py)
- [rerank.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/rerank.py)
- [context_fetch.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/context_fetch.py)

职责：

- 多路召回
- rerank
- 相关过程与上下文查询

### 4. 证据与回答层

- [evidence.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/evidence.py)
- [qa.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/qa.py)
- [answering.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/answering.py)
- [llm.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/llm.py)
- [answer_strategy.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/answer_strategy.py)

职责：

- 证据选择
- prompt package
- draft answer
- 外部 LLM 回答策略

### 5. 接入层

- [cli.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/cli.py)
- [api.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/api.py)
- [mcp_server.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/mcp_server.py)

职责：

- CLI 编排
- HTTP API
- MCP 工具暴露

## 现在最应该遵守的开发约束

### 1. 新能力优先放到分层模块

不要再把新逻辑堆回 `indexer.py`。

推荐原则：

- 建库流程改 `index_build.py`
- 写库细节改 `index_write.py`
- 检索改 `retrieval.py`
- rerank 改 `rerank.py`
- 上下文获取改 `context_fetch.py`
- 证据裁剪改 `evidence.py`
- 统一语义规则改 `semantic_recovery.py`

### 2. 语义规则只保留一个事实来源

调用语义和消息发布语义已经统一到：

- [semantic_recovery.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/semantic_recovery.py)

如果后面要扩：

- 新调用类型
- 新消息发布类型
- 新 label formatter

优先改这里，而不是在 `indexer.py` 或 `context_fetch.py` 再写一套。

### 3. 调试输出优先走结构化 trace

不要再给 debug 临时拼新的自由格式字段。

优先复用：

- [observability.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/observability.py)
- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)

### 4. 评测优先补在已有入口

已经有：

- [evaluation.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/evaluation.py)
- [tests/test_evaluation.py](/Users/songzuoqiang/Documents/agent/condex/codes/tests/test_evaluation.py)
- [tests/test_semantic_rules.py](/Users/songzuoqiang/Documents/agent/condex/codes/tests/test_semantic_rules.py)

所以后面加新能力时，建议同步补：

- 功能测试
- 质量评测
- 规则测试

## 推荐开发路径

如果你要继续优化这个项目，建议按下面顺序：

1. 先看 [ARCHITECTURE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/ARCHITECTURE.md)
2. 再看 [INDEX_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/INDEX_SCHEMA.md)
3. 再读本文件
4. 最后进入对应模块改代码

## 常用验证命令

```bash
python3 -m py_compile src/uses_indexer/*.py
PYTHONPATH=. pytest -q
```

如果你只改了局部模块，建议优先跑对应子集：

```bash
PYTHONPATH=. pytest -q tests/test_indexer.py tests/test_evaluation.py tests/test_semantic_rules.py
```

# Trace Schema

`uses_indexer` 的调试输出现在统一使用 versioned trace envelope，适用于：

- CLI `query-index --debug`
- CLI `assemble-evidence --debug`
- HTTP API `/query` 与 `/evidence` 的 `debug=true`
- MCP `query_codebase` 与 `assemble_evidence` 的 `debug=true`
- 增量建库返回中的 `incremental_trace`

## 顶层字段

所有结构化 trace 都遵循同一组顶层字段：

```json
{
  "schema": "uses_indexer.debug.<kind>",
  "version": "1.0",
  "metadata": {
    "trace_id": "uuid",
    "producer": "uses_indexer",
    "schema": "uses_indexer.debug.<kind>",
    "version": "1.0",
    "generated_at": "2026-04-20T08:00:00+00:00"
  },
  "trace": {
    "stage": "<stage>"
  }
}
```

## Retrieval Trace

`schema = uses_indexer.debug.retrieval`

主要字段：

- `query_analysis`: 问题意图分析结果
- `retrieval_contributions`: 各召回通道的候选贡献
- `rerank_preview`: rerank 后的前若干候选及打分拆解
- `trace.stage = retrieval`
- `trace.sources`: FTS / vector / like 三路召回候选
- `trace.rerank`: rerank 后的候选统计与预览

适用场景：

- 为什么这个问题命中了这些候选
- rerank 前后分数如何变化
- 调用链或 SQL 意图有没有被识别到

## Evidence Trace

`schema = uses_indexer.debug.evidence`

主要字段：

- `retrieval`: 内嵌 retrieval trace
- `evidence_pruning`: 证据裁剪事件
- `trace.stage = evidence`
- `trace.selection`: 最终入选证据、裁剪数量、裁剪原因

适用场景：

- 为什么候选很多，但最终证据只有这几块
- 某段上下文为什么被判定为重复或超限

## Incremental Build Trace

`schema = uses_indexer.debug.incremental_build`

主要字段：

- `trace.stage = incremental_build`
- `trace.file_scan`: 当前文件数与历史索引状态文件数
- `trace.changes`: `added / changed / removed / reindexed`
- `trace.vector_stats`: 本次向量补齐统计

适用场景：

- 这次增量建库到底动了哪些文件
- 为什么会触发重建
- 本次是否补了新的向量

## 兼容性说明

- `schema` 与 `version` 是稳定识别键
- 后续新增字段时，优先保持向后兼容
- 消费端应以 `schema` 和 `version` 做分支处理，而不是依赖字段顺序

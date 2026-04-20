# 排障指南

这份文档回答的是：当结果不对、建库异常、或者调试信息看不懂时，应该怎么排。

## 一张总表

| 问题现象 | 先看哪里 |
| --- | --- |
| 搜不到结果 | `query-index --debug` |
| 候选很多但答案不对 | `assemble-evidence --debug` |
| 增量建库行为异常 | `incremental_trace` |
| 结果像是 metadata 干扰了代码检索 | 当前使用的索引库类型 |
| LLM 回答变差 | `ask-codebase` 的 prompt package 和 evidence |
| 改了语义规则后行为异常 | `tests/test_semantic_rules.py` |

## 1. 检索不对怎么排

先跑：

```bash
python3 -m uses_indexer query-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --query "你的问题" \
  --limit 10 \
  --debug
```

重点看：

- `query_analysis`
- `retrieval_contributions`
- `rerank_preview`

常见判断：

- 如果三路召回都没候选，优先怀疑问题提法或索引库选错
- 如果召回有候选，但 rerank 靠后，优先看 query intent 是否识别错
- 如果候选本来就不相关，优先看切块或边恢复

## 2. 证据不对怎么排

再跑：

```bash
python3 -m uses_indexer assemble-evidence \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --query "你的问题" \
  --limit 5 \
  --debug
```

重点看：

- `evidence`
- `evidence_pruning`
- 内嵌的 `retrieval`

常见判断：

- 如果候选对，但 evidence 少，优先看裁剪原因
- 如果 evidence 都来自同一过程，可能命中了 `procedure_evidence_cap`
- 如果上下文重复，通常会看到 `duplicate_context`

## 3. 增量建库不对怎么排

重点看增量返回中的：

- `incremental_impact`
- `incremental_trace`

现在已经可以看到：

- 哪些文件被识别为 `added / changed / removed`
- 本次影响了哪些 procedure / unit
- 是否触发了补向量或重建

如果你发现“改了文件但没更新结果”，先确认：

1. 改动文件是否在当前索引类型范围内
2. `incremental_impact.affected_units` 里有没有它
3. 当前查询是不是还在用旧库

## 4. LLM 层异常怎么排

如果 `answer-codebase` 返回不理想，建议按这条链路拆开看：

1. `query-index`
2. `assemble-evidence`
3. `ask-codebase`
4. `answer-codebase`

判断原则：

- `query-index` 不对：问题在检索层
- `assemble-evidence` 不对：问题在证据层
- `ask-codebase` 的 `draft_answer` 已经不对：问题多半不在 LLM
- 只有 `answer-codebase` 变差：再看 provider、prompt、timeout、fallback

## 5. 索引库选错怎么排

常见误区是把下面几个库混掉：

- `business_code_index.db`：默认代码检索库
- `business_full_index.db`：代码 + metadata
- `business_metadata_index.db`：只查元数据
- `business_table_index.db`：只查表结构

如果你看到：

- 命中很多 metadata，但你问的是代码逻辑

优先确认你是不是用了 `business_full_index.db`。

边界说明见：

- [INDEX_BOUNDARIES.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/INDEX_BOUNDARIES.md)

## 6. 推荐最小排障顺序

出现问题时，建议总是按这个顺序：

1. 确认当前索引库类型
2. 跑 `query-index --debug`
3. 跑 `assemble-evidence --debug`
4. 必要时看 `ask-codebase`
5. 必要时看 `incremental_trace`

## 7. 相关文档

- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)
- [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)
- [DEVELOPER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEVELOPER_GUIDE.md)

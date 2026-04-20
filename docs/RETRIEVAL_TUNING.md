# 检索调优指南

这份文档回答的是：如果检索质量不理想，应该按什么顺序调。

## 一条基本原则

先分清是下面哪一层出了问题：

1. 没召回到
2. 召回到了但 rerank 靠后
3. 候选对了但 evidence 裁掉了
4. evidence 对了但回答策略组织得不好

不要一上来就怪 LLM。

## 推荐调优顺序

### 1. 先看 `query-index --debug`

重点看：

- `query_analysis`
- `retrieval_contributions`
- `rerank_preview`

如果问题在这里，就优先调：

- 分词 / focus term
- query intent
- rerank bonus
- 调用链扩展

### 2. 再看 `assemble-evidence --debug`

重点看：

- `evidence_pruning`
- `trace.selection`
- `related_context`

如果问题在这里，就优先调：

- `procedure_evidence_cap`
- 去重策略
- related_limit
- context_window

### 3. 最后看 `eval-retrieval`

建议每次改完都跑：

```bash
PYTHONPATH=. python3 -m uses_indexer eval-retrieval \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db \
  --cases /Users/songzuoqiang/Documents/agent/condex/codes/eval/uses_codes_cases.json
```

重点看：

- `pass_at_k`
- `expectation_recall_at_k`
- `evidence_coverage`
- `top_hit_expectation_coverage`
- `top_three_expectation_coverage`

## 常见调优点

### 1. query intent

相关实现：

- [rerank.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/rerank.py)

适合调整：

- 表访问类问题
- 变量赋值类问题
- 失败路径类问题
- 调用链类问题

如果你发现：

- 候选里有正确结果，但老排不到前面

通常优先看这里。

### 2. semantic chunk / block 恢复

相关实现：

- [semantic_recovery.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/semantic_recovery.py)

适合调整：

- SQL 块恢复
- 失败处理块恢复
- 动态 SQL 恢复
- chunk summary 质量

如果你发现：

- 命中内容太碎
- evidence 不连贯

通常优先看这里。

### 3. related context

相关实现：

- [context_fetch.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/context_fetch.py)
- [evidence.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/evidence.py)

适合调整：

- related tables
- related procedures
- incoming / outgoing calls
- metadata relations

如果你发现：

- 主证据命中了，但缺少回答所需的上下游信息

通常优先看这里。

## 建议的调优纪律

每次只动一类规则，然后至少做 3 件事：

1. 跑局部测试
2. 跑 `eval-retrieval`
3. 用 `compare-eval` 对比前后报告

如果没有评测收益，就不要因为“代码看起来更聪明”而保留。

## 相关文档

- [EVALUATION.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/EVALUATION.md)
- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)
- [TROUBLESHOOTING.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TROUBLESHOOTING.md)

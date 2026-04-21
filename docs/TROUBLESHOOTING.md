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

如果你想把一次问题完整打包下来，方便离线复盘，可以直接运行：

```bash
PYTHONPATH=. python3 -m uses_indexer debug-bundle \
  --db ./examples/business_code_index.db \
  --question "证券代码获取的逻辑在哪里" \
  --archive-dir ./examples/debug_bundle_archive \
  --output ./examples/debug_bundle.json
```

这个 bundle 会同时包含：

- `query`
- `evidence`
- `answer`

如果传了 `--archive-dir`，还会额外落盘：

- `bundle.json`
- `bundle_summary.json`
- `query.json`
- `evidence.json`
- `answer.json`

这样更适合：

- 把单次问题诊断包发给其他同事
- 做线上问题留档
- 对比同一问题在不同版本中的 query/evidence/answer 变化

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

如果问题比较顽固，建议第 3 步和第 4 步之间直接补一遍 `debug-bundle --archive-dir`，把这次问题的整条链路先固化下来，再继续分析。

## 7. 两次版本怎么自动对比

如果你已经保存了两次 `debug-bundle` 输出，最省事的方式就是直接跑：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundles \
  --before ./examples/debug_bundle_archive_before \
  --after ./examples/debug_bundle_archive_after \
  --output ./examples/debug_bundle_compare.json
```

`--before` 和 `--after` 既可以传：

- `bundle.json`
- 也可以直接传 `--archive-dir` 生成出来的目录

返回结果会重点告诉你：

- `summary.query_hit_count`
- `summary.candidate_count`
- `summary.evidence_count`
- `summary.query_type`
- `summary.answer_source`
- `summary.final_answer_changed`
- `query.top_hit_changed`
- `evidence.top_evidence_changed`
- `answer.before_final_answer_excerpt / after_final_answer_excerpt`

### 什么时候最适合用 compare-debug-bundles

这几个场景最有价值：

1. 改了检索或 rerank 规则，想确认“同一个问题到底变好了还是变坏了”
2. 改了 evidence pruning，想看 top evidence 有没有偏掉
3. 改了 answer policy，想看回答来源是不是从 `draft` 变成了 `llm`，或者最终答案是否明显变了
4. 线上问题复盘时，想对比“故障版本”和“修复版本”的整条链路差异

### 怎么读这个对比结果

可以按这个顺序看：

1. 先看 `warnings`
   - 如果有 `question_changed` 或 `db_path_changed`，先确认是不是在拿两个不同问题或不同库做比较
2. 再看 `summary.query_type`
   - 如果 query type 变了，很多后续差异其实是“问题理解变了”带来的
3. 再看 `summary.query_hit_count / candidate_count / evidence_count`
   - 这是最粗粒度的召回和证据量变化
4. 再看 `query.top_hit_changed` 和 `evidence.top_evidence_changed`
   - 这是最接近“用户主观感受”的变化
5. 最后看 `answer.before_final_answer_excerpt / after_final_answer_excerpt`
   - 用来快速判断回答文案是不是只是润色变化，还是结论本身变了

### 一些经验判断

- `candidate_count` 上升，但 `top_hit_changed` 变差：通常是召回更宽了，但排序没跟上
- `query` 看起来差不多，`evidence.top_evidence_changed` 变差：通常是证据裁剪或上下文扩展出了偏差
- `query/evidence` 都没明显变化，但 `final_answer_changed` 很大：优先看 answer policy、prompt 或 LLM provider
- `query_type_changed`：优先先解决 query understanding，不要急着调 rerank

## 8. 相关文档

- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)
- [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)
- [DEVELOPER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEVELOPER_GUIDE.md)

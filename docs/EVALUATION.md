# Retrieval Evaluation

## 目标

评测层用于回答一个很具体的问题：每次修改检索、切块、索引或重排逻辑后，结果到底有没有变好。

第一版评测只覆盖检索证据，不评判最终 LLM 文案质量。原因是最终回答会受到模型、温度、提示词等因素影响，而检索证据是当前项目最需要先稳定的基础层。

## 用例文件

默认用例文件：

- `eval/uses_codes_cases.json`
- `eval/uses_codes_effect_cases.json`

格式示例：

```json
{
  "cases": [
    {
      "id": "dynamic-sql-reload-fundacct-delete",
      "question": "reload_fundacct 在哪里被删除",
      "tags": ["table_write", "dynamic_sql"],
      "expected": {
        "procedures": ["AF_DATASEINIT_SECONDLOADUSESTABLE"],
        "texts": ["reload_fundacct"],
        "paths": ["AF_DATASEINIT_SECONDLOADUSESTABLE.uftatomfunction"]
      }
    }
  ]
}
```

`expected` 当前支持：

- `procedures`：期望命中的过程名，大小写不敏感，按包含关系匹配。
- `paths`：期望命中的路径片段，适合限定具体文件。
- `texts`：期望命中的文本片段，会在 `matched_text / match_source / reasons` 中查找。
- `tables`：和 `texts` 一样处理，语义上用于表达表名期望。
- `line_ranges`：期望命中的行号区间。

`line_ranges` 示例：

```json
{
  "line_ranges": [
    {
      "path_contains": "AF_DEEP.uftatomfunction",
      "start": 8,
      "end": 10
    }
  ]
}
```

## 运行命令

```bash
PYTHONPATH=src python3 -m uses_indexer eval-retrieval \
  --db examples/uses_codes_index.db \
  --cases eval/uses_codes_cases.json \
  --limit 10 \
  --top-k 1,3,5,10 \
  --output examples/uses_codes_eval_report.json
```

如果你希望评测直接作为质量门槛，还可以加 threshold：

```bash
PYTHONPATH=src python3 -m uses_indexer eval-retrieval \
  --db examples/uses_codes_index.db \
  --cases eval/uses_codes_effect_cases.json \
  --limit 10 \
  --top-k 1,3,5,10 \
  --min-pass-at-k 5=0.9 \
  --min-tag-pass-at-k call_chain:5=1.0 \
  --min-query-type-pass-at-k callers:5=1.0 \
  --min-evidence-coverage 0.8 \
  --fail-on-thresholds
```

其中：

- `--min-pass-at-k 5=0.9`：全局 `pass@5` 至少为 `0.9`
- `--min-tag-pass-at-k call_chain:5=1.0`：`call_chain` 标签问题的 `pass@5` 必须为 `1.0`
- `--min-query-type-pass-at-k callers:5=1.0`：`callers` 类型问题的 `pass@5` 必须为 `1.0`

这样可以把“总体没退化，但某一类真实问题明显退化”的情况单独拦下来。

## 报告字段

报告会输出：

- `case_count`：用例数量。
- `summary.pass_at_k`：至少有一个期望项在 top-k 命中时，该 case 计为通过。
- `summary.expectation_recall_at_k`：每个 case 的期望项召回比例，再对所有 case 求平均。
- `summary.mean_first_relevant_rank`：首个相关命中的平均排名。
- `summary.by_query_type`：按 query type 聚合的质量统计。
- `summary.avg_relation_hit_count`：平均每个 case 有多少命中来自 relation retrieval。
- `summary.avg_feature_rerank_hit_count`：平均每个 case 有多少命中携带 feature-based rerank 信号。
- `cases[].expectations`：每个期望项是否命中，以及命中的 hit。
- `cases[].top_hits`：每个问题的前若干检索结果，方便人工审查。
- `cases[].query_type`：问题类型分类结果。
- `thresholds`：如果提供 threshold 参数，会返回逐项通过/失败检查。

典型 threshold metric 形态：

- `pass_at_k.5`
- `by_tag.call_chain.pass_at_k.5`
- `by_query_type.callers.pass_at_k.5`

## 对比报告

如果已经有两份评测报告，可以直接离线比较：

```bash
PYTHONPATH=src python3 -m uses_indexer compare-eval \
  --before examples/uses_codes_eval_report_local_hash.json \
  --after examples/uses_codes_eval_report_real_embedding.json \
  --output examples/uses_codes_eval_compare.json
```

对比报告会输出：

- `summary_delta.pass_at_k`
- `summary_delta.expectation_recall_at_k`
- `summary_delta.mean_first_relevant_rank`
- `case_change_counts`
- `cases[].change`
- `cases[].before`
- `cases[].after`

`cases[].change` 当前可能是：

- `improved`
- `regressed`
- `unchanged`
- `added`
- `removed`

判断规则优先看最大 top-k 下是否从未命中变为命中或反过来；其次看期望项召回率；最后看首个相关命中的排名是否提前或后移。

## 分项守门建议

如果你准备把 `eval-retrieval` 接到 CI，建议不要只配一个总门槛。更稳妥的做法是：

- 配一个全局 `--min-pass-at-k`
- 再给你最关心的标签配 `--min-tag-pass-at-k`
- 再给最容易回退的问题类型配 `--min-query-type-pass-at-k`

例如：

- `call_chain`
- `failure`
- `table_write`
- `callers`
- `variable_write`

这样后面即使整体平均值看起来还可以，也能更早发现某一类业务问法已经开始回退。

## 用 debug bundle 做 case 级复盘

`eval-retrieval` 更适合看“整体趋势”，但如果你想复盘某一个具体问题，建议配合 `debug-bundle` 和 `compare-debug-bundles` 一起用。

推荐流程：

1. 在改动前跑一次：

```bash
PYTHONPATH=. python3 -m uses_indexer debug-bundle \
  --db examples/business_code_index.db \
  --question "AF_DEEP 被谁调用" \
  --archive-dir examples/debug_callers_before
```

2. 在改动后再跑一次：

```bash
PYTHONPATH=. python3 -m uses_indexer debug-bundle \
  --db examples/business_code_index.db \
  --question "AF_DEEP 被谁调用" \
  --archive-dir examples/debug_callers_after
```

3. 最后直接比较：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundles \
  --before examples/debug_callers_before \
  --after examples/debug_callers_after \
  --markdown-output examples/debug_callers_compare.md
```

这样你就能把“总体指标变化”和“单题链路变化”连起来看：

- `eval-retrieval` 负责告诉你“整体有没有退化”
- `compare-debug-bundles` 负责告诉你“到底是哪一段链路变了”

推荐的查看顺序是：

1. 先看 `debug_callers_compare.md`
2. 再根据里面的 `focus_area` 去看 JSON 明细

这样通常会比直接翻整份 `debug_bundle_compare.json` 更快。

## 批量问题面板

如果你要在一次较大的改动后做“发布前回归”，建议直接跑批量面板，而不是只盯一个问题：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panel \
  --before-db examples/business_code_index_before.db \
  --after-db examples/business_code_index_after.db \
  --cases eval/uses_codes_effect_cases.json \
  --max-verdict-count possible_regression=0 \
  --fail-on-thresholds \
  --markdown-output examples/debug_bundle_panel.md \
  --output examples/debug_bundle_panel.json
```

这个面板的定位是：

- `eval-retrieval` 看整体指标
- `compare-debug-bundle-panel` 看一组典型问题的链路级变化

推荐组合方式：

1. 先跑 `eval-retrieval`
2. 如果整体指标有变化，再跑 `compare-debug-bundle-panel`
3. 从 panel 里的 `high priority cases` 开始逐题看 `comparison.md`

如果你想把它接到 CI，最推荐的方式是：

1. `eval-retrieval` 负责整体检索质量门槛
2. `compare-debug-bundle-panel` 负责典型问题链路门槛

两者一起用时，你能同时拦住：

- 整体指标退化
- 典型关键问题退化

如果你要做更长期的趋势跟踪，还可以把每次 panel 保存成 archive，然后比较两次 panel：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panels \
  --before examples/debug_bundle_panel_baseline \
  --after examples/debug_bundle_panel_current \
  --markdown-output examples/debug_bundle_panel_compare.md \
  --output examples/debug_bundle_panel_compare.json
```

这样可以把“这次回归和上一次基线相比，整体 case 结构到底怎么变了”也一起量化出来。

## 当前基准

当前初始评测集有 5 个 case，覆盖：

- 动态 SQL 表写入
- 错误码报错路径
- 表读取
- 过程调用引用
- SQL 变量执行

当前样例报告：

- `examples/uses_codes_eval_report.json`
- `examples/uses_codes_eval_report_local_hash.json`
- `examples/uses_codes_eval_compare.json`

当前样例结果：

- `pass@1 = 1.0`
- `pass@3 = 1.0`
- `pass@5 = 1.0`
- `pass@10 = 1.0`
- `expectation_recall@10 = 0.9`

## 真实 Embedding 对比流程

如果要对比本地 hash embedding 和真实语义 embedding，建议固定同一份 `eval/uses_codes_cases.json`，分别构建两个 SQLite 索引库：

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --db examples/uses_codes_index.db
```

```bash
export OPENAI_EMBEDDING_KEY="..."
export OPENAI_EMBEDDING_URL="https://oapi.aivue.cn/v1"
export OPENAI_EMBEDDING_NAME="text-embedding-3-large"
export OPENAI_EMBEDDING_BATCH_SIZE=16
export OPENAI_EMBEDDING_TIMEOUT=60
export OPENAI_EMBEDDING_CACHE_DB="examples/uses_codes_embedding_cache.db"

PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --db examples/uses_codes_index_openai.db
```

如果真实 embedding 建库中断，可以续建缺失向量：

```bash
PYTHONPATH=src python3 -m uses_indexer build-index \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --db examples/uses_codes_index_openai.db \
  --resume-vectors
```

然后分别运行 `eval-retrieval`，再用 `compare-eval` 生成对比报告。`examples/uses_codes_eval_report_local_hash.json` 是当前本地 hash 索引的基准报告，真实 embedding 的报告建议输出为 `examples/uses_codes_eval_report_real_embedding.json`。

注意事项：

- 密钥只通过环境变量注入，不要写进仓库文件。
- `OPENAI_EMBEDDING_URL` 可以填到 `/v1`，程序会自动补成 `/v1/embeddings`。
- `OPENAI_EMBEDDING_CACHE_DB` 是可选的本地 SQLite 缓存；开启后，相同模型、地址、维度和文本 hash 的 embedding 会复用缓存。
- `--resume-vectors` 会复用已有索引库，只扫描缺失 `chunk_vectors` 的 chunk，并自动跳过已有向量。
- 当前对 `https://oapi.aivue.cn/v1` 的 smoke test 中，batch size `1`、`4`、`16` 均可返回 `3072` 维向量；完整大仓建库建议先从 `OPENAI_EMBEDDING_BATCH_SIZE=16` 开始。
- `examples/uses_codes_index_openai.db` 和 `examples/uses_codes_embedding_cache.db` 属于本地构建产物，体积较大并且可能包含外部 embedding 结果，不纳入版本控制。

## 当前真实 Embedding 端到端结果

本轮先使用评测用例覆盖子集做端到端测试，子集包含 4 个核心过程文件、193 个语义块。这样可以验证真实 embedding 的建库、查询向量、评测和对比报告链路，同时避免全量建库在当前接口延迟下长时间卡住。

输出文件：

- `examples/uses_codes_embedding_e2e_report.json`
- `examples/uses_codes_index_subset_local_hash_summary.json`
- `examples/uses_codes_index_real_embedding_subset_summary.json`
- `examples/uses_codes_eval_report_subset_local_hash.json`
- `examples/uses_codes_eval_report_real_embedding_subset.json`
- `examples/uses_codes_eval_compare_real_embedding_subset.json`

子集对比结论：

- 本地 hash 子集和真实 embedding 子集的 `pass@10` 都是 `1.0`
- 真实 embedding 子集的 `matched_cases` 仍为 `5`
- 早期真实 embedding 子集曾出现 `expectation_recall@3` 和 `expectation_recall@5` 各下降 `0.1` 的问题，根因是向量候选把不含局部精确焦点词的泛相关 chunk 推到了前面
- 当前已加入 focus-aware 融合调权：调用链问题会抽取 `证券代码获取` 这类焦点词，并排除 `查询 / 执行 / 报错` 这类通用操作意图词，优先提升命中焦点词的 FTS / 结构化关系 / chunk-block 证据，并降低缺少焦点词的 `vector_chunk` 排名
- 调权后真实 embedding 子集的 `pass@1/pass@3/pass@5/pass@10` 均为 `1.0`
- 调权后真实 embedding 子集的 `expectation_recall@1/@3/@5/@10` 均为 `1.0`
- `stock-code-get-callers` 从首个相关命中 rank `3` 提升到 rank `1`
- case 级变化为 `improved = 1`、`regressed = 0`、`unchanged = 4`

全量建库风险：

- 全量索引当前有 `28748` 个语义块、`2553` 个含 chunk 的文件
- 旧实现按文件内 chunk 分批，batch size `16` 曾估算约 `3620` 次请求
- 当前实现已经改成全局批量补齐缺失向量，并支持 `--resume-vectors`
- 代表性 16 条真实语义块请求耗时约 `13.45` 秒；在继续调优 batch size 和接口稳定性前，仍不建议把全量真实 embedding 建库当作普通短测试

## 当前中等规模 Embedding 测试

本轮又使用 6 个中等复杂文件做真实 embedding 测试，共 `475` 个语义块。首次构建在 `256` 条向量落库后遇到接口读取超时；随后使用 `--resume-vectors`、batch size `8`、timeout `120` 秒继续补齐剩余向量。

输出文件：

- `examples/uses_codes_embedding_medium_benchmark.json`
- `examples/uses_codes_index_real_embedding_medium_summary.json`

结论：

- `chunk_vectors` 最终补齐到 `475 / 475`
- 续建阶段 `missing_before = 219`、`inserted = 219`、`missing_after = 0`
- 续建后再次执行 no-op resume，结果为 `missing_before = 0`、`inserted = 0`、`batches = 0`
- 这验证了全局批处理、每批提交、cache 和 `--resume-vectors` 能处理真实接口中途超时的场景
- 当前接口在较大 batch 或较长输入上仍可能超时，全量建库建议优先使用 batch size `8` 或 `16`，并始终开启 embedding cache

## 后续扩展

- 增加更多真实业务问题，优先扩到 30 到 50 条。
- 增加“找定义”和“找调用处”的区分字段。
- 增加 answer 层评测，检查最终回答是否引用了正确证据。
- 接入真实 embedding 后，用同一份 case 对比本地 hash embedding 与真实 embedding 的差异。

# Retrieval Evaluation

## 目标

评测层用于回答一个很具体的问题：每次修改检索、切块、索引或重排逻辑后，结果到底有没有变好。

第一版评测只覆盖检索证据，不评判最终 LLM 文案质量。原因是最终回答会受到模型、温度、提示词等因素影响，而检索证据是当前项目最需要先稳定的基础层。

## 用例文件

默认用例文件：

- `eval/uses_codes_cases.json`

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

## 报告字段

报告会输出：

- `case_count`：用例数量。
- `summary.pass_at_k`：至少有一个期望项在 top-k 命中时，该 case 计为通过。
- `summary.expectation_recall_at_k`：每个 case 的期望项召回比例，再对所有 case 求平均。
- `summary.mean_first_relevant_rank`：首个相关命中的平均排名。
- `cases[].expectations`：每个期望项是否命中，以及命中的 hit。
- `cases[].top_hits`：每个问题的前若干检索结果，方便人工审查。

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
- `expectation_recall@3` 和 `expectation_recall@5` 相对本地 hash 子集各下降 `0.1`
- case 级变化为 `unchanged = 5`，没有新增 `improved` 或 `regressed`

全量建库风险：

- 全量索引当前有 `28748` 个语义块、`2553` 个含 chunk 的文件
- 旧实现按文件内 chunk 分批，batch size `16` 曾估算约 `3620` 次请求
- 当前实现已经改成全局批量补齐缺失向量，并支持 `--resume-vectors`
- 代表性 16 条真实语义块请求耗时约 `13.45` 秒；在继续调优 batch size 和接口稳定性前，仍不建议把全量真实 embedding 建库当作普通短测试

## 后续扩展

- 增加更多真实业务问题，优先扩到 30 到 50 条。
- 增加“找定义”和“找调用处”的区分字段。
- 增加 answer 层评测，检查最终回答是否引用了正确证据。
- 接入真实 embedding 后，用同一份 case 对比本地 hash embedding 与真实 embedding 的差异。

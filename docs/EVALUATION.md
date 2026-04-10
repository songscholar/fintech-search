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

## 当前基准

当前初始评测集有 5 个 case，覆盖：

- 动态 SQL 表写入
- 错误码报错路径
- 表读取
- 过程调用引用
- SQL 变量执行

当前样例报告：

- `examples/uses_codes_eval_report.json`

当前样例结果：

- `pass@1 = 1.0`
- `pass@3 = 1.0`
- `pass@5 = 1.0`
- `pass@10 = 1.0`
- `expectation_recall@10 = 0.9`

## 后续扩展

- 增加更多真实业务问题，优先扩到 30 到 50 条。
- 增加“找定义”和“找调用处”的区分字段。
- 增加 answer 层评测，检查最终回答是否引用了正确证据。
- 接入真实 embedding 后，用同一份 case 对比本地 hash embedding 与真实 embedding 的差异。

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
  --markdown-output ./examples/debug_bundle_compare.md \
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

如果你传了 `--markdown-output`，还会额外生成一份更适合人直接看的 reviewer 摘要，里面会有：

- `verdict`
- `priority`
- `focus_area`
- `findings`
- `suggested next steps`

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

如果你先看 markdown reviewer 摘要，可以按这三个字段快速分流：

- `verdict`
  - `stable`：基本没有重要行为变化
  - `behavior_changed`：行为变了，但不一定是坏事
  - `possible_regression`：命中数或证据数下降，值得优先排查
  - `query_drift`：问题理解变了，先查 query understanding
  - `invalid_comparison`：两次输入不具备可比性
- `priority`
  - `high`：建议立刻看
  - `medium`：有变化，但未必是回退
  - `low`：基本稳定
- `focus_area`
  - `query_understanding`
  - `retrieval`
  - `evidence`
  - `answering`
  - `stable`

一个实用习惯是：

1. 先看 markdown reviewer 摘要
2. 再看 JSON 里的 `summary`
3. 最后只在需要时下钻到 `before_top_hits / after_top_hits` 和 `before_top_evidence / after_top_evidence`

### 一些经验判断

- `candidate_count` 上升，但 `top_hit_changed` 变差：通常是召回更宽了，但排序没跟上
- `query` 看起来差不多，`evidence.top_evidence_changed` 变差：通常是证据裁剪或上下文扩展出了偏差
- `query/evidence` 都没明显变化，但 `final_answer_changed` 很大：优先看 answer policy、prompt 或 LLM provider
- `query_type_changed`：优先先解决 query understanding，不要急着调 rerank
- `verdict=possible_regression` 且 `focus_area=retrieval`：先看 top hit 是否被更宽泛但更弱的候选替换
- `verdict=behavior_changed` 且 `focus_area=evidence`：先看 evidence pruning 和 context expansion

## 8. 一组固定问题怎么批量复盘

如果你不想逐题手工跑 `debug-bundle`，可以直接用批量回归面板：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panel \
  --before-db ./examples/business_code_index_before.db \
  --after-db ./examples/business_code_index_after.db \
  --cases ./eval/uses_codes_effect_cases.json \
  --max-changed-cases 0 \
  --max-verdict-count possible_regression=0 \
  --max-focus-area-count retrieval=1 \
  --fail-on-thresholds \
  --archive-dir ./examples/debug_bundle_panel \
  --markdown-output ./examples/debug_bundle_panel.md \
  --output ./examples/debug_bundle_panel.json
```

这个命令会做三件事：

1. 对 `cases` 里的每个问题分别跑 before/after 两套 `debug-bundle`
2. 逐题生成 comparison
3. 最后汇总成一个总览 panel

如果你传了 threshold 参数，panel 结果里还会带：

- `thresholds.status`
- `thresholds.failed_count`
- `thresholds.checks`

并且在带 `--fail-on-thresholds` 时，CLI 会返回非零退出码。

### cases 文件怎么准备

它直接复用评测用例格式，所以最简单的方式就是沿用你已有的：

- `eval/uses_codes_cases.json`
- `eval/uses_codes_effect_cases.json`

最少只需要有 `question`，例如：

```json
{
  "cases": [
    {
      "id": "stock-code-callers",
      "question": "证券代码获取被谁调用",
      "tags": ["call_chain", "callers"]
    }
  ]
}
```

### panel 输出里最值得先看什么

先看 markdown 总览里的：

- `changed cases`
- `verdict counts`
- `priority counts`
- `focus areas`
- `high priority cases`

这几个字段能帮你快速判断：

- 这次改动是不是影响了很多问题
- 影响主要集中在 retrieval / evidence / answering 哪一层
- 哪几个 case 最值得优先人工复盘

### panel threshold 怎么配

最常用的是这几类：

- `--max-changed-cases`
  - 限制这次总共有多少题发生了明显行为变化
- `--max-high-priority-cases`
  - 限制高优先级问题数量
- `--max-verdict-count possible_regression=0`
  - 禁止出现 `possible_regression`
- `--max-focus-area-count retrieval=1`
  - 限制回退主要集中在某一层时的数量

一个比较实用的保守配置例子是：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panel \
  --before-db ./examples/business_code_index_before.db \
  --after-db ./examples/business_code_index_after.db \
  --cases ./eval/uses_codes_effect_cases.json \
  --max-changed-cases 2 \
  --max-high-priority-cases 0 \
  --max-verdict-count possible_regression=0 \
  --max-focus-area-count retrieval=1 \
  --fail-on-thresholds
```

这个配置的含义是：

- 允许少量行为变化
- 不允许高优先级问题
- 不允许明确回退
- retrieval 层的问题最多只允许 1 个

### archive-dir 会产出什么

如果传了 `--archive-dir`，每个 case 都会生成一套目录，里面包括：

- `before/`
- `after/`
- `comparison.json`
- `comparison.md`

所以它特别适合：

- 做一次版本发布前的回归审阅
- 把高优先级 case 发给同事一起看
- 留一份“这次改动到底影响了哪些典型问题”的证据包
- 在 CI 里作为发布前守门

### 如果你是通过 API / MCP 调用

现在这套 panel 能力不只在 CLI 可用：

- HTTP API:
  - `POST /compare-debug-bundle-panel`
- MCP tool:
  - `compare_debug_bundle_panel`

这样如果你是在上层 Agent、服务端任务或前端控制台里做回归，也可以直接复用同一套 panel 结构和 threshold 结果，而不用自己再拼装一层。

### 怎么和历史基线 panel 做比较

如果你已经保存过一份 panel archive，后面可以直接拿它和当前 panel 做比较：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panels \
  --before ./examples/debug_bundle_panel_baseline \
  --after ./examples/debug_bundle_panel_current \
  --markdown-output ./examples/debug_bundle_panel_compare.md \
  --output ./examples/debug_bundle_panel_compare.json
```

这里的 `--before / --after` 既可以传：

- panel archive 目录
- 也可以直接传 `panel.json`

返回结果会重点告诉你：

- `changed_case_count` 的变化
- `stable_case_count` 的变化
- `verdict_counts_delta`
- `priority_counts_delta`
- `focus_area_counts_delta`
- `high_priority_cases` 的前后差异

一个实用的持续回归流程是：

1. 先生成当前版本的 panel archive
2. 用 `compare-debug-bundle-panels` 和上一次基线 archive 做比较
3. 如果 panel-level 对比明显变差，再下钻到单题 `comparison.md`

### 怎么管理固定 baseline

如果你不想每次都记住某个历史 archive 的完整路径，可以把它保存成命名 baseline。

先保存：

```bash
PYTHONPATH=. python3 -m uses_indexer save-debug-bundle-panel-baseline \
  --panel ./examples/debug_bundle_panel_current \
  --name "release-candidate" \
  --baseline-dir ./examples/panel_baselines \
  --output ./examples/release_candidate_baseline.json
```

再查看当前有哪些 baseline：

```bash
PYTHONPATH=. python3 -m uses_indexer list-debug-bundle-panel-baselines \
  --baseline-dir ./examples/panel_baselines
```

最后把当前 panel 和固定 baseline 做比较：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panel-baseline \
  --panel ./examples/debug_bundle_panel_current \
  --name "release-candidate" \
  --baseline-dir ./examples/panel_baselines \
  --markdown-output ./examples/release_candidate_compare.md \
  --output ./examples/release_candidate_compare.json
```

这套命名 baseline 的好处是：

- 不需要人工维护“这次应该拿哪个 archive 目录做 before”
- 同名 baseline 可以直接覆盖，适合“当前状态就是新的标准答案”
- 很适合 release review、固定 smoke case 和长期回归

如果你准备长期维护一批 baseline，建议保存时就附带备注和标签：

```bash
PYTHONPATH=. python3 -m uses_indexer save-debug-bundle-panel-baseline \
  --panel ./examples/debug_bundle_panel_current \
  --name "release-candidate" \
  --baseline-dir ./examples/panel_baselines \
  --note "2026-04-21 发布候选版本" \
  --tag release \
  --tag smoke
```

这样后面列举时就能直接筛：

```bash
PYTHONPATH=. python3 -m uses_indexer list-debug-bundle-panel-baselines \
  --baseline-dir ./examples/panel_baselines \
  --tag release
```

如果你想看某个 baseline 的完整元数据，而不是只看列表摘要：

```bash
PYTHONPATH=. python3 -m uses_indexer show-debug-bundle-panel-baseline \
  --name "release-candidate" \
  --baseline-dir ./examples/panel_baselines
```

如果你只想和“最近一份 release baseline”比较，而不想手写 baseline 名称，可以直接用：

```bash
PYTHONPATH=. python3 -m uses_indexer compare-debug-bundle-panel-latest-baseline \
  --panel ./examples/debug_bundle_panel_current \
  --baseline-dir ./examples/panel_baselines \
  --tag release \
  --markdown-output ./examples/release_candidate_latest_compare.md
```

最后，如果某个 baseline 已经过时，也可以直接删掉：

```bash
PYTHONPATH=. python3 -m uses_indexer delete-debug-bundle-panel-baseline \
  --name "release-candidate" \
  --baseline-dir ./examples/panel_baselines
```

如果你想看一组 baseline 的长期走势，而不是只做两两比较，可以直接看 trend：

```bash
PYTHONPATH=. python3 -m uses_indexer show-debug-bundle-panel-baseline-trend \
  --baseline-dir ./examples/panel_baselines \
  --tag release \
  --markdown-output ./examples/release_baseline_trend.md \
  --output ./examples/release_baseline_trend.json
```

这个结果适合回答三类问题：

- 最近几次 release baseline 的 `changed_case_count` 是上升还是下降
- `possible_regression_count` 是不是在慢慢累积
- 当前这一类 baseline 的总体趋势是变稳了还是变差了

建议先看 markdown，再在需要时下钻 JSON：

- `Timeline`
  - 看每次 baseline 的 `changed / possible_regression`
- `Transitions`
  - 看相邻两次 baseline 的变化量
- `Overall delta`
  - 看从最早一份到最新一份的累计变化

### baseline 管理也开放到了 API / MCP

现在除了 CLI，还可以直接通过服务接口做这些事：

- HTTP API
  - `POST /compare-debug-bundle-panels`
  - `GET /list-debug-bundle-panel-baselines`
  - `GET /show-debug-bundle-panel-baseline-trend`
  - `GET /show-debug-bundle-panel-baseline`
  - `POST /save-debug-bundle-panel-baseline`
  - `POST /compare-debug-bundle-panel-baseline`
  - `POST /compare-debug-bundle-panel-latest-baseline`
  - `POST /delete-debug-bundle-panel-baseline`
- MCP tool
  - `compare_debug_bundle_panels`
  - `list_debug_bundle_panel_baselines`
  - `show_debug_bundle_panel_baseline_trend`
  - `show_debug_bundle_panel_baseline`
  - `save_debug_bundle_panel_baseline`
  - `compare_debug_bundle_panel_baseline`
  - `compare_debug_bundle_panel_latest_baseline`
  - `delete_debug_bundle_panel_baseline`

## 9. 相关文档

- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)
- [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)
- [DEVELOPER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEVELOPER_GUIDE.md)

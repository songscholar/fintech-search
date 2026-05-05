# 索引构建变慢问题复盘

## 问题现象

在代码索引内容变厚之后，重新构建 `business_code_index.db` 的速度明显变慢。

表现包括：

- 旧构建运行数小时仍未完成。
- Python 进程 CPU 持续接近满载，不像死锁。
- `indexes/business_code_index.db-wal` 持续增长到 GB 级。
- 主库 `indexes/business_code_index.db` 长时间只有很小体积。
- 另一个 SQLite 连接查询时，`files / procedures / chunks / procedure_features` 等核心表仍接近 0。
- 用户体感从“半小时左右构建完成”变成“看起来要跑好几个小时”。

## 问题分析

排查时没有立即停止旧构建，而是先用只读方式观察：

- 通过 `ps` 确认构建进程仍在运行。
- 通过 `ls -lh indexes/business_code_index.db*` 观察主库和 WAL 文件大小。
- 通过 SQLite 只读查询核心表行数，确认主库尚未提交可见数据。
- 对照 `index_build.py` 发现全量构建虽然已经做了阶段级提交，但 `index_files` 阶段内部仍是一个巨大的事务。

进一步分析后，主要耗时和风险集中在两个阶段：

- `index_files`：解析 2 万多个源码文件，写入 files、procedures、statements、edges、chunks、blocks、FTS 等大量数据。
- `refresh_procedure_features`：对每个过程汇总调用、表访问、变量、topic、metadata 等结构化画像。

当 `index_files` 被包在一个超大事务里时，构建看似一直在写 WAL，但主库迟迟不可见，失败后也很难判断真实进度。

## 问题原因

根因不是单一 SQL 慢查询，而是几个因素叠加：

- 构建内容变厚后，每个文件写入的数据量显著增加。
- `index_files` 阶段仍然采用超大事务，必须等整个阶段结束后才提交。
- WAL 在大事务期间持续增长，主库在 checkpoint 前不可见。
- 构建进度缺少文件批次级别的可观测性。
- 之前优化了 `refresh_procedure_features` 的分批提交，但没有把同样的策略下沉到文件索引阶段。

这导致用户看到的是“进程在跑、WAL 在涨、主库没变化”，很容易被误判为构建卡死。

## 解决方法

本次修复分成三层。

### 1. 文件索引阶段分批提交

修改 `src/uses_indexer/index_build.py`：

- `_store_index_metadata()` 后立即 `commit`。
- `_index_files()` 新增 `batch_size` 参数。
- 全量构建默认每 `500` 个文件提交一次。
- 最后一批不足 `500` 的文件也会提交。
- 开启 progress 时输出 `index_files_batch_committed`。

修复后构建日志会出现：

```text
[build-index] index_files_batch_committed {"processed": 500, "total": 23798}
```

### 2. 过程画像阶段分批提交

`refresh_all_procedure_features()` 保持批量刷新：

- 默认每 `500` 个过程一批。
- 每批独立事务提交。
- 输出 `refresh_procedure_features_batch`。

### 3. 向量阶段保持可恢复

向量阶段继续使用批量补齐逻辑：

- `populate_missing_chunk_vectors()` 按 embedder batch size 分批插入。
- 支持 `--skip-vectors` 先建结构索引。
- 支持 `--resume-vectors` 后补向量。

## 修复效果

重建代码索引后，构建过程可以看到真实进度：

- 文件索引阶段按 `500` 文件提交。
- 过程画像阶段按 `500` 过程提交。
- 主库不再长时间保持 4KB。
- WAL 不再无界增长到无法判断状态。
- 构建失败时也可以看到已经提交到哪个批次。

一次完整重建结果：

- 文件数：`23895`
- chunk 数：`201368`
- 向量数：`201368`
- procedure_features：`23895`

## 举一反三

以后遇到大库构建变慢，不能只看“进程还在跑”，要同时看三个维度：

- CPU 是否活跃。
- WAL 是否变化。
- 主库核心表是否持续可见增长。

对于任何大批量构建任务，默认应遵循：

- 不要把几十万行写入放在一个超大事务里。
- 每个长阶段都要有可观测的阶段事件。
- 批量提交大小应该是可配置的。
- 构建 summary 应记录每个阶段耗时。
- 失败恢复能力要尽量提前设计。

后续可继续增强：

- 把 `batch_size=500` 提升为 CLI 参数或环境变量。
- 在 summary 中记录每个批次的耗时统计。
- 增加慢阶段报警，例如某阶段超过阈值时输出诊断建议。
- 对 `refresh_procedure_features` 做更细粒度的 SQL explain 或 profile。

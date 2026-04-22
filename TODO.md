# TODO

## Release Workflow / Baseline

- [ ] 增加 `release workflow trend`
  目标：按 `tag / baseline_name / status` 聚合同一类 release workflow 的时间线，直接看 `blocked -> ready_to_promote -> promoted` 的长期变化。

- [ ] 增加 `latest release workflow`
  目标：支持直接读取“最近一次 release workflow”，避免每次都手动传 archive 路径。

- [ ] 增加 `release workflow baseline`
  目标：像 panel baseline 一样，为 release workflow 建立命名基线，支持固定发布动作模板的长期比对。

- [ ] 增加 `release workflow diff drill-down`
  目标：在 workflow compare 结果里补更细的差异下钻，例如直接展示 gate checks 哪几项变了、latest comparison 里哪一段 evidence / answer 发生了关键变化。

- [ ] 增加 `release workflow archive index`
  目标：对 workflow archives 建索引，支持按 `tag / status / verdict / date` 快速筛选和列举。

- [ ] 增加 `release workflow retention/cleanup`
  目标：支持 archive 的保留策略、按标签归档、清理过旧 workflow，避免根目录或归档目录持续膨胀。

## Quality Gates

- [ ] 增加 `scoped promotion policies`
  目标：支持按 `release / smoke / nightly` 定义不同 gate 规则，而不是所有 promote 都共用一套阈值。

- [ ] 增加 `policy presets`
  目标：内置几组常见 gate/promotion preset，例如 `strict_release`、`smoke_fast_path`、`nightly_observe_only`。

- [ ] 增加 `gate failure explanations`
  目标：让 gate 失败时不只是返回 failed checks，还能自动给出更人类可读的“为什么这次不能 promote”的总结。

## Reporting / Review

- [ ] 增加 `review pack export`
  目标：把 panel compare、release workflow、promotion gate、latest comparison 统一导出成一个 reviewer pack，方便评审或留档。

- [ ] 增加 `markdown summary index`
  目标：为历史 markdown summaries 生成目录页，支持快速浏览最近几次评测、workflow、baseline 对比结果。

- [ ] 增加 `change log stitching`
  目标：把 `pro_log`、workflow archives、baseline promotions 串起来，形成“本次发布质量动作时间线”。

## Automation / Ops

- [ ] 增加 `workflow automation`
  目标：让固定问题集的 compare/gate/promote 可以由定时任务或 heartbeat 自动执行。

- [ ] 增加 `post-run notifications`
  目标：在 workflow `blocked`、`possible_regression`、`promoted` 时自动产出更适合通知/IM 的摘要。

- [ ] 增加 `CI-friendly workflow exit codes`
  目标：让 release workflow 在不同失败类型下返回稳定退出码，方便接入 CI/CD。

## Documentation

- [ ] 补一份 `RELEASE_WORKFLOW_GUIDE.md`
  目标：把 panel、baseline、trend、promotion gate、release workflow、archives、comparisons 串成一份完整操作指南。

- [ ] 补一份 `QUALITY_PLAYBOOK.md`
  目标：总结“什么时候该 compare、什么时候该 promote、什么时候只做 observe”的实践规则。

## Cleanup / Consistency

- [ ] 统一 `archive / baseline / workflow` 三类产物的 summary schema
  目标：减少字段漂移，方便后面做统一索引和统一列表页。

- [ ] 统一 `CLI / API / MCP` 在 debug/workflow 相关命令上的输出约定
  目标：避免后面继续演进时三个入口的字段慢慢漂移。

- [ ] 增加端到端回归测试
  目标：从 `panel compare -> gate -> promote -> workflow archive -> compare workflow` 串成一条完整回归链路。

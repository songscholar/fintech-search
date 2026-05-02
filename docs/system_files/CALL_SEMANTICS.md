# Call Semantics

## 目标

这份文档记录 USES/UFT 代码中的过程调用与跨核心通信语义规则，避免把所有 `[LF_xxx] / [AF_xxx] / [LS_xxx]` 或消息发布动作都当成同一种“普通调用”。

在这个项目里，这些规则会同时用于：

- `calls_procedure` 边的语义分类
- `publishes_mc_topic` 边的消息发布语义分类
- `db-summary` 中的调用类型统计
- `assemble-evidence` 与 `answer-codebase` 的调用链证据说明

## 当前规则

### 1. 本地函数调用

以下组合视为同一核心内的本地函数调用：

- `LS -> AF`
- `LS -> LF`
- `LF -> LF`
- `LF -> AF`

当前分类标签：

- `call_kind = local_function_call`
- `call_label = 本地函数调用`

### 2. 系统间 RPC 调用

以下组合视为跨系统 / 跨核心的 RPC 调用：

- `LS -> LS`
- `LF -> LS`
- `AF -> LS`
- `LS -> EI`
- `LF -> EI`
- `AF -> EI`
- `RS -> EI`

这类调用常见于不同代码核心之间，例如：

- `uses_codes`
- `usms_codes`
- `ucrt_codes`
- `ucbp_codes`

它们可以分别部署，因此调用 `LS` 目标过程时，经常应该理解成系统间服务调用，而不是单纯的本地过程跳转。

当前分类标签：

- `call_kind = rpc_call`
- `call_label = 系统间RPC调用`

### 3. 消息中心主题发布

以下动作属于一类特殊的跨核心消息调用语义：

- `[同步消息发布][topic_name = ...][...]`
- `[消息发布][topic_name = ...][...]`

这类动作表示：

- 当前过程把消息发布到 `MC` 消息中心
- 由订阅该 `topic_name` 的其他核心异步消费
- 在架构语义上，它更像“跨核心事件驱动调用”，也可以看作一种特殊的异步 RPC 分发

当前分类标签：

- `edge_type = publishes_mc_topic`
- `message_kind = mc_topic_publish`
- `message_label = 消息中心主题发布`
- `communication_kind = cross_core_message_publish`
- `communication_label = 跨核心消息发布`

发布方式进一步区分：

- `[同步消息发布]`
  - `publish_mode = sync`
  - `publish_mode_label = 同步发布`
- `[消息发布]`
  - `publish_mode = async`
  - `publish_mode_label = 异步发布`

主题名会从 `topic_name` 参数中提取，例如：

- `CNST_MC_UFT_PUBSYNC`
- `CNST_MC_UFT_OPTSYNC`

### 4. 未归类调用

如果当前前缀组合不在上述规则内，系统会先保守地标为：

- `call_kind = unknown_call_kind`
- `call_label = 未归类调用`

这表示：

- 当前索引器没有足够规则把它归到“本地函数调用”或“RPC 调用”
- 后续可以继续扩展新的调用前缀语义

## 当前实现位置

当前规则已经落到代码里：

- 调用边写入时分类：
  - `/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/indexer.py`
- 消息中心主题边写入时分类：
  - `/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/indexer.py`
- 调用链 related context 展示时分类：
  - `/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/indexer.py`
- `db-summary` 调用类型统计：
  - `/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/indexer.py`

## 当前输出方式

### `calls_procedure` 边的 `detail_json`

当前调用边会记录：

- `source_prefix`
- `target_prefix`
- `call_rule`
- `call_kind`
- `call_label`

例如：

```json
{
  "source_prefix": "LS",
  "target_prefix": "AF",
  "call_rule": "LS->AF",
  "call_kind": "local_function_call",
  "call_label": "本地函数调用"
}
```

### `db-summary`

现在会额外输出：

- `call_kind_counts`
- `call_rule_counts`
- `mc_publish_mode_counts`
- `mc_topic_counts`

这样可以快速知道一个索引库里：

- 本地函数调用有多少
- RPC 调用有多少
- 哪种前缀组合最多
- 哪些 MC topic 被发布过
- 同步发布和异步发布各有多少

### `assemble-evidence` / `answer-codebase`

证据上下文里的相关调用现在会带上调用语义标签，例如：

- `AF_LOCAL(本地函数调用 LS->AF)`
- `LS_REMOTE(系统间RPC调用 LF->LS)`
- `CNST_MC_UFT_OPTSYNC(消息中心主题发布 异步发布)`

## 边界说明

当前规则是基于你们代码规范里的“显式前缀语义”实现的，不是运行时网络抓包，也不是部署拓扑探测。

因此它当前更适合表达：

- 调用在架构语义上更像本地函数
- 调用在架构语义上更像 RPC
- 某个过程是否向 MC 发布了某个跨核心 topic

它暂时不表达：

- 实际部署地址
- 真实网络协议
- 超时、重试、熔断等运行时 RPC 行为

## 后续可继续增强的方向

- 按代码核心目录给过程补充 `service_domain`
- 增加同名 `LS` 过程的跨目录消歧
- 在调用图里区分“显式本地调用”、“显式 RPC 调用”、“未归类调用”
- 增加“谁消费某个 MC topic”的订阅侧规则
- 在问答中支持直接解释“这段为什么属于 RPC 调用”

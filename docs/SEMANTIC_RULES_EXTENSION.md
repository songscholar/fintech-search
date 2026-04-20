# DSL 语义规则扩展指南

这份文档回答的是：如果你要继续给 USES/UFT DSL 增加新的语义规则，应该改哪里。

## 现在的原则

语义规则的“单一事实来源”优先放在：

- [semantic_recovery.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/semantic_recovery.py)

不要再把同一套规则分别塞进：

- `indexer.py`
- `context_fetch.py`
- `evidence.py`

这些模块应该消费规则，而不是重新定义规则。

## 当前已经统一的规则类型

### 1. 调用语义

例如：

- `LS -> AF`
- `LS -> LF`
- `LF -> LF`
- `LF -> AF`
- `LS -> LS`
- `LF -> LS`
- `AF -> LS`

相关入口：

- `LOCAL_CALL_RULES`
- `RPC_CALL_RULES`
- `classify_call_semantics`
- `coerce_call_semantics`

### 2. 消息发布语义

例如：

- `同步消息发布`
- `消息发布`

相关入口：

- `MC_PUBLISH_ACTIONS`
- `classify_mc_publish`
- `format_mc_topic_label`

## 扩一条新规则时的推荐步骤

### 1. 先改 `semantic_recovery.py`

如果是新规则类型，优先加：

- 规则常量
- classify helper
- formatter
- registry 项

### 2. 再改消费方

常见消费方：

- [index_write.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/index_write.py)
- [context_fetch.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/context_fetch.py)
- [evidence.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/evidence.py)

### 3. 最后补测试

优先补：

- [tests/test_semantic_rules.py](/Users/songzuoqiang/Documents/agent/condex/codes/tests/test_semantic_rules.py)

如果规则会影响结果链路，再补：

- `tests/test_indexer.py`
- `tests/test_evaluation.py`

## 推荐的测试层次

### 1. 规则测试

验证：

- classify helper 是否按预期输出
- registry 是否暴露规则
- formatter 是否稳定

### 2. 索引测试

验证：

- 边是否写入
- detail_json 是否带上新语义字段
- summarize_db 是否正确聚合

### 3. 证据测试

验证：

- llm_context 是否出现预期标签
- related context 是否能读出新语义

## 一个实用原则

如果新规则只是“让解释更好看”，那它应该主要影响：

- `detail_json`
- formatter
- related context

如果新规则会改变召回或排序，那它还应该继续影响：

- edge 写入
- chunk / block summary
- rerank

## 相关文档

- [CALL_SEMANTICS.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/CALL_SEMANTICS.md)
- [DEVELOPER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEVELOPER_GUIDE.md)

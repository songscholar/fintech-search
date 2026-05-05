# 新手指南

这份文档回答的是第一次接触这个仓库时，最短路径应该怎么走。

目标不是一次看完所有设计细节，而是先把 3 件事跑通：

1. 知道默认该用哪个索引库
2. 知道最常用的 3 个命令
3. 知道回答不对时下一步该看哪里

## 第一步：先认清默认索引

平时默认用：

- `indexes/business_code_index.db`

它表示：

- 覆盖完整代码根目录范围
- 只包含 DSL / UFT 代码文件
- 不混入 `metadata`

如果你要同时查代码和元数据，再切到：

- `indexes/business_full_index.db`

如果你只查元数据，请用：

- `indexes/business_metadata_index.db`

如果你只做小范围回归调试，可以继续用：

- `indexes/uses_codes_index.db`

更完整的边界说明见：

- [INDEX_BOUNDARIES.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/INDEX_BOUNDARIES.md)

## 第二步：先跑最常用的 3 个命令

### 1. 先看命中

```bash
python3 -m uses_indexer query-index \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/indexes/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 10
```

适合：

- 快速定位过程
- 看候选是否合理
- 判断是不是检索阶段就跑偏了

### 2. 再看证据

```bash
python3 -m uses_indexer assemble-evidence \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/indexes/business_code_index.db \
  --query "哪些流程调用证券代码获取" \
  --limit 3
```

适合：

- 看最终送给模型的证据块
- 判断上下文够不够
- 分析为什么答案不完整

### 3. 最后直接回答

```bash
python3 -m uses_indexer answer-codebase \
  --db /Users/songzuoqiang/Documents/agent/condex/codes/indexes/business_code_index.db \
  --question "哪些流程调用证券代码获取"
```

适合：

- 直接拿结果
- 验证整条链路是否闭环

## 第三步：问题提法怎么更稳

更容易答好的问题通常更具体：

- “哪些流程调用 `AF_SYSARGPUB_STKCODE_GET`”
- “`uses_fund_real` 在哪里更新”
- “查询失败在哪里处理”
- “`@sql_str` 在哪里赋值并执行”

相对更弱的问题：

- “这个功能怎么实现”
- “这个模块的逻辑”
- “代码在哪”

建议优先带上：

- 过程名
- 表名
- 变量名
- 错误码
- 你想看的角度：调用链 / 表访问 / 变量赋值 / 失败路径

## 第四步：答得不对先看哪里

按这个顺序排查最省时间：

1. 先跑 `query-index`
2. 再跑 `assemble-evidence`
3. 如果要看为什么命中这些结果，打开 `--debug`

推荐看这些文档：

- [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)：平时怎么提问、怎么选入口
- [TRACE_SCHEMA.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TRACE_SCHEMA.md)：怎么看结构化调试输出
- [TROUBLESHOOTING.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/TROUBLESHOOTING.md)：常见排障路径

## 第五步：建议阅读顺序

如果你是第一次接触这个仓库，推荐按这个顺序读：

1. [NEWCOMER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/NEWCOMER_GUIDE.md)
2. [USAGE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/USAGE.md)
3. [ARCHITECTURE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/ARCHITECTURE.md)
4. [DEVELOPER_GUIDE.md](/Users/songzuoqiang/Documents/agent/condex/codes/docs/DEVELOPER_GUIDE.md)

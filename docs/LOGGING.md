# 日志系统

`uses-indexer` 的运行日志统一写入项目根目录 `log/`。日志使用 JSON Lines，便于 `tail`、`jq`、日志采集器或后续 ELK/Loki/OpenTelemetry 适配。

## 目录结构

```text
log/
├── requests/   # HTTP/API 链路日志：入参、出参摘要、状态码、耗时、trace_id
├── errors/     # 后端异常与前端上报异常：错误类型、堆栈、上下文
├── system/     # 系统日志：服务启动/停止、建库启动、向量补齐启动等
├── business/   # 业务日志：查询、证据组装、问答、Agent、LLM、建库完成等
└── sql/        # 数据库操作摘要：检索、证据、DB summary、建库/增量等逻辑 SQL 事件
```

文件按日期拆分，例如：

```text
log/requests/2026-04-30.jsonl
log/errors/2026-04-30.jsonl
```

## 记录范围

- HTTP 请求链路：`method`、`path`、状态码、耗时、客户端信息、请求体、响应摘要、`trace_id`
- 报错日志：`ApiError`、未捕获后端异常、LLM/Agent/检索/证据/建库失败、前端 `error` 与 `unhandledrejection`
- 系统日志：API 服务启动/停止、全量建库、增量建库、向量补齐启动
- 业务日志：代码检索、证据组装、问答、Agent 聊天、LLM 调用、debug bundle、建库完成
- SQL 日志：默认记录逻辑数据库操作摘要，不逐条打印底层 SQLite SQL，避免大库检索产生海量日志

## 脱敏与截断

日志模块会自动处理：

- `api_key`、`Authorization`、`token`、`secret`、`password`、`cookie` 等字段脱敏
- `data_url`、疑似 base64 大字符串、二进制内容截断
- 超长字符串和超大数组/对象截断

默认限制：

- `USES_INDEXER_LOG_MAX_STRING=4000`
- `USES_INDEXER_LOG_MAX_ITEMS=80`

## 配置

```bash
# 关闭日志
export USES_INDEXER_LOG_ENABLED=0

# 改写日志目录
export USES_INDEXER_LOG_DIR=/path/to/log

# 调整截断阈值
export USES_INDEXER_LOG_MAX_STRING=8000
export USES_INDEXER_LOG_MAX_ITEMS=120
```

默认开启日志，默认目录是项目根目录 `log/`。

## 查看示例

```bash
# 最近 API 链路
tail -f log/requests/$(date +%F).jsonl

# 查看错误
tail -f log/errors/$(date +%F).jsonl

# 按 trace_id 串联一次请求
rg "<trace_id>" log/
```

HTTP 响应头会返回 `X-Trace-Id`，可以用它在 `log/requests`、`log/errors`、`log/business`、`log/sql` 中串联一次调用。

## 设计说明

当前日志系统坚持零第三方依赖，使用标准库直接写 JSONL。生产环境如果需要集中采集，可以让采集器直接读取 `log/*/*.jsonl`，或后续在 `logging_system.py` 中增加 OpenTelemetry / Loki / ELK exporter。

# pre_log

## 2026-04-30 - 全局日志系统改造

### 背景

项目缺少生产化日志管理能力，前后端错误、API 调用链路、部署/启动停止、业务操作和数据库操作缺少统一落盘记录。

### 本轮改动

1. 新增集中日志模块
   - 新增 `src/uses_indexer/logging_system.py`
   - 日志默认写入项目根目录 `log/`
   - 按 `requests / errors / system / business / sql` 分类写 JSONL
   - 自动生成 `trace_id`
   - 自动脱敏密钥、Authorization、token、cookie、data_url、base64 大字段
   - 自动截断超长字符串和大数组/对象

2. HTTP/API 链路日志
   - `api.py` 为每次 JSON API 请求记录入参、出参摘要、状态码、耗时、客户端 IP、User-Agent
   - 响应头新增 `X-Trace-Id`
   - `ApiError` 与未捕获异常写入 `log/errors`
   - API 服务启动/停止写入 `log/system`

3. 前端错误上报
   - 新增 `POST /client-log`
   - 前端监听 `window.error` 和 `unhandledrejection`
   - 前端错误统一进入 `log/errors`

4. 业务与 SQL 摘要日志
   - 检索、证据组装、DB summary、建库、增量建库、向量补齐写业务/SQL 摘要
   - LLM 和 Agent 外呼记录 provider、model、耗时、usage 摘要
   - SQL 日志默认记录逻辑数据库操作摘要，不逐条打印所有 SQLite 语句，避免大库检索产生海量日志

5. 文档与目录
   - 新增 `docs/LOGGING.md`
   - README 增加日志文档入口
   - `.gitignore` 忽略 `log/*`，保留 `log/.gitkeep`

### 验证

- `PYTHONPATH=src python3 -m py_compile src/uses_indexer/*.py`
- API 联调应检查：
  - `log/requests/YYYY-MM-DD.jsonl`
  - `log/errors/YYYY-MM-DD.jsonl`
  - `log/system/YYYY-MM-DD.jsonl`
  - `log/business/YYYY-MM-DD.jsonl`
  - `log/sql/YYYY-MM-DD.jsonl`

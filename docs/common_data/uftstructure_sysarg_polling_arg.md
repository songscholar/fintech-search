# polling_arg - 轮询参数表

**表对象ID**: 307
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | time_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | polling_function | 否 |  |  |
| 4 | polling_kind | 否 |  |  |
| 5 | enable_status | 否 |  |  |
| 6 | polling_name | 否 |  |  |
| 7 | time_kind | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | polling_function | 否 |  |  |
| 10 | polling_kind | 否 |  |  |
| 11 | enable_status | 否 |  |  |
| 12 | polling_name | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_polling_arg | ART | 是 | time_kind, exchange_type, polling_function, polling_kind, time_kind, exchange_type, polling_function, polling_kind |
| idx_polling_arg | ART | 是 | time_kind, exchange_type, polling_function, polling_kind, time_kind, exchange_type, polling_function, polling_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_polling_arg | time_kind, exchange_type, polling_function, polling_kind, time_kind, exchange_type, polling_function, polling_kind |
| idx_polling_arg | time_kind, exchange_type, polling_function, polling_kind, time_kind, exchange_type, polling_function, polling_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-10 16:44:15 | 3.0.2.83 | 王润雪 | 改为落redo |
| 2024-05-27 15:53:28 | 3.0.2.9 | 张云焘 | 新增 |
| 2025-04-10 16:44:15 | 3.0.2.83 | 王润雪 | 改为落redo |
| 2024-05-27 15:53:28 | 3.0.2.9 | 张云焘 | 新增 |

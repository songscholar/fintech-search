# hstkcode_arg - H股全流通代码参数表

**表对象ID**: 5011
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | capital_amount | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | capital_amount | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hstkcode_arg | 默认 | 否 |  |
| idx_hstkcode_arg | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_hstkcode_arg | 默认 | 否 |  |
| idx_hstkcode_arg | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hstkcode_arg | exchange_type, stock_code, exchange_type, stock_code |
| idx_hstkcode_arg | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:21:55 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:16:09 | 3.0.2.84 | taocong45644 | 当前表hstkcode_arg，修改了索引idx_hstkcode_arg,索引字段修改为：(exchange_type... |
| 2025-02-19 13:32:13 | 3.0.6.36 | 李想 | 新增表 |
| 2026-03-05 17:21:55 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:16:09 | 3.0.2.84 | taocong45644 | 当前表hstkcode_arg，修改了索引idx_hstkcode_arg,索引字段修改为：(exchange_type... |
| 2025-02-19 13:32:13 | 3.0.6.36 | 李想 | 新增表 |

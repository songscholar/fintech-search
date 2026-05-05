# eb_stkcode - 转板代码信息表

**表对象ID**: 128
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | eb_stock_code | 否 |  |  |
| 3 | eb_exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | eb_date | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | position_str | 否 |  | eb_exchange_type(4)+eb_stock_code(8) |
| 11 | init_date | 否 |  |  |
| 12 | eb_stock_code | 否 |  |  |
| 13 | eb_exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | eb_date | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | position_str | 否 |  | eb_exchange_type(4)+eb_stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_eb_stkcode | 默认 | 否 |  |
| idx_eb_stkcode | ART | 是 | eb_exchange_type, eb_stock_code, eb_exchange_type, eb_stock_code |
| idx_eb_stkcode | 默认 | 否 |  |
| idx_eb_stkcode | ART | 是 | eb_exchange_type, eb_stock_code, eb_exchange_type, eb_stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_eb_stkcode | eb_exchange_type, eb_stock_code, eb_exchange_type, eb_stock_code |
| idx_eb_stkcode | eb_exchange_type, eb_stock_code, eb_exchange_type, eb_stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:38:45 | 3.0.2.103 | taocong45644 | 当前表eb_stkcode，修改了索引idx_eb_stkcode,索引字段修改为：(eb_exchange_type,... |
| 2025-02-18 16:30:14 | 3.0.6.58 | 李想 | 新增表 |
| 2025-12-01 14:38:45 | 3.0.2.103 | taocong45644 | 当前表eb_stkcode，修改了索引idx_eb_stkcode,索引字段修改为：(eb_exchange_type,... |
| 2025-02-18 16:30:14 | 3.0.6.58 | 李想 | 新增表 |

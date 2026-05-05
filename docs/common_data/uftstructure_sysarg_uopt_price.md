# uopt_price - 期权行情表

**表对象ID**: 9012
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | option_code | 否 |  |  |
| 4 | opt_last_price | 否 |  |  |
| 5 | business_balance | 否 |  |  |
| 6 | business_amount | 否 |  |  |
| 7 | close_flag | 否 |  |  |
| 8 | square_price | 否 |  |  |
| 9 | optexch_status | 否 |  |  |
| 10 | optauction_price | 否 |  |  |
| 11 | undrop_amount | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | option_code | 否 |  |  |
| 15 | opt_last_price | 否 |  |  |
| 16 | business_balance | 否 |  |  |
| 17 | business_amount | 否 |  |  |
| 18 | close_flag | 否 |  |  |
| 19 | square_price | 否 |  |  |
| 20 | optexch_status | 否 |  |  |
| 21 | optauction_price | 否 |  |  |
| 22 | undrop_amount | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_price | 默认 | 否 | init_date, init_date |
| idx_uopt_price | 默认 | 是 | exchange_type, option_code, exchange_type, option_code |
| idx_uopt_price | 默认 | 否 | init_date, init_date |
| idx_uopt_price | 默认 | 是 | exchange_type, option_code, exchange_type, option_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_price | exchange_type, option_code, exchange_type, option_code |
| idx_uopt_price | exchange_type, option_code, exchange_type, option_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 14:52:05 | V3.0.2.91 | 李奕轩 | uopt_price表存储介质改为DB+MDB，表空间改为uarg |
| 2025-07-28 16:12:41 | V3.0.2.90 | 吴笑东 | 物理表uopt_price，删除索引字段(索引idx_uopt_price:删除了索引字段：init_date);
 |
| 2024-08-20 15:05:08 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |
| 2025-09-16 14:52:05 | V3.0.2.91 | 李奕轩 | uopt_price表存储介质改为DB+MDB，表空间改为uarg |
| 2025-07-28 16:12:41 | V3.0.2.90 | 吴笑东 | 物理表uopt_price，删除索引字段(索引idx_uopt_price:删除了索引字段：init_date);
 |
| 2024-08-20 15:05:08 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |

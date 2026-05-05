# uopt_underly_code - 期权标的证券表

**表对象ID**: 9008
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_name | 否 |  |  |
| 5 | amount_per_hand | 否 |  |  |
| 6 | valid_date | 否 |  |  |
| 7 | underly_status | 否 |  |  |
| 8 | update_type | 否 |  |  |
| 9 | hold_resopen_company | 否 |  |  |
| 10 | modify_date | 否 |  |  |
| 11 | last_price | 否 |  |  |
| 12 | closing_price | 否 |  |  |
| 13 | par_value | 否 |  |  |
| 14 | report_unit | 否 |  |  |
| 15 | store_unit | 否 |  |  |
| 16 | en_entrust_way | 否 |  |  |
| 17 | close_price | 否 |  |  |
| 18 | his_volatility | 否 |  |  |
| 19 | limit_value_up | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | stock_name | 否 |  |  |
| 27 | amount_per_hand | 否 |  |  |
| 28 | valid_date | 否 |  |  |
| 29 | underly_status | 否 |  |  |
| 30 | update_type | 否 |  |  |
| 31 | hold_resopen_company | 否 |  |  |
| 32 | modify_date | 否 |  |  |
| 33 | last_price | 否 |  |  |
| 34 | closing_price | 否 |  |  |
| 35 | par_value | 否 |  |  |
| 36 | report_unit | 否 |  |  |
| 37 | store_unit | 否 |  |  |
| 38 | en_entrust_way | 否 |  |  |
| 39 | close_price | 否 |  |  |
| 40 | his_volatility | 否 |  |  |
| 41 | limit_value_up | 否 |  |  |
| 42 | update_date | 否 |  |  |
| 43 | update_time | 否 |  |  |
| 44 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_underly_code | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_uopt_underly_code | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_underly_code | exchange_type, stock_code, exchange_type, stock_code |
| idx_uopt_underly_code | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-18 16:59:33 | V3.0.3.16 | 汪迎 | 物理表uopt_underly_code，添加了表字段(his_volatility);
物理表uopt_underl... |
| 2025-02-14 15:23:48 | V3.0.3.15 | 张明月 | 物理表uopt_underly_code，添加了表字段(close_price);
 |
| 2024-08-20 15:05:29 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |
| 2023-12-16 17:28:42 | 3.0.0.0 | wuxd |  |
| 2025-04-18 16:59:33 | V3.0.3.16 | 汪迎 | 物理表uopt_underly_code，添加了表字段(his_volatility);
物理表uopt_underl... |
| 2025-02-14 15:23:48 | V3.0.3.15 | 张明月 | 物理表uopt_underly_code，添加了表字段(close_price);
 |
| 2024-08-20 15:05:29 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |
| 2023-12-16 17:28:42 | 3.0.0.0 | wuxd |  |

# uopt_marginfloat_total_jour - 期权保证金浮动比例汇总流水表

**表对象ID**: 9027
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | partition_id | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | option_code | 否 |  |  |
| 11 | option_type | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | before_margin_ratio | 否 |  |  |
| 14 | after_margin_ratio | 否 |  |  |
| 15 | position_str | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | serial_no | 否 |  |  |
| 18 | curr_date | 否 |  |  |
| 19 | curr_time | 否 |  |  |
| 20 | partition_id | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | company_no | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | option_code | 否 |  |  |
| 26 | option_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | before_margin_ratio | 否 |  |  |
| 29 | after_margin_ratio | 否 |  |  |
| 30 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_marginfloat_total_jour | 默认 | 是 | client_id, position_str, client_id, position_str |
| idx_uopt_marginfloat_total_jour | 默认 | 是 | client_id, position_str, client_id, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_marginfloat_total_jour | client_id, position_str, client_id, position_str |
| idx_uopt_marginfloat_total_jour | client_id, position_str, client_id, position_str |

# uopt_loancompact_jour - 股票期权资券合约流水表

**表对象ID**: 9024
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | trace_id | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | loan_compact_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | real_action | 否 |  |  |
| 15 | business_flag | 否 |  |  |
| 16 | occur_balance | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | post_balance | 否 |  |  |
| 19 | post_amount | 否 |  |  |
| 20 | cancel_serial_no | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | modify_fields | 否 |  |  |
| 24 | init_date | 否 |  |  |
| 25 | trace_id | 否 |  |  |
| 26 | serial_no | 否 |  |  |
| 27 | curr_date | 否 |  |  |
| 28 | curr_time | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | loan_compact_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | money_type | 否 |  |  |
| 37 | real_action | 否 |  |  |
| 38 | business_flag | 否 |  |  |
| 39 | occur_balance | 否 |  |  |
| 40 | occur_amount | 否 |  |  |
| 41 | post_balance | 否 |  |  |
| 42 | post_amount | 否 |  |  |
| 43 | cancel_serial_no | 否 |  |  |
| 44 | position_str | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | modify_fields | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_loancompact_jour | 默认 | 否 | client_id, position_str, client_id, position_str |
| idx_uopt_loancompact_jour | 默认 | 否 | client_id, position_str, client_id, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_loancompact_jour | client_id, position_str, client_id, position_str |
| idx_uopt_loancompact_jour | client_id, position_str, client_id, position_str |

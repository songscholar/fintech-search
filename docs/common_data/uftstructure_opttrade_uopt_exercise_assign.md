# uopt_exercise_assign - 期权行权指派信息表

**表对象ID**: 9021
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | option_type | 否 |  |  |
| 8 | option_code | 否 |  |  |
| 9 | opthold_type | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | entrust_bs | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | business_type | 否 |  |  |
| 16 | hold_amount | 否 |  |  |
| 17 | exercise_price | 否 |  |  |
| 18 | exercise_amount | 否 |  |  |
| 19 | settle_amount | 否 |  |  |
| 20 | exercise_balance | 否 |  |  |
| 21 | settle_balance | 否 |  |  |
| 22 | sys_std_margin | 否 |  |  |
| 23 | exefrozen_balance | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | init_date | 否 |  |  |
| 27 | company_no | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | option_type | 否 |  |  |
| 33 | option_code | 否 |  |  |
| 34 | opthold_type | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | money_type | 否 |  |  |
| 38 | entrust_bs | 否 |  |  |
| 39 | seat_no | 否 |  |  |
| 40 | business_type | 否 |  |  |
| 41 | hold_amount | 否 |  |  |
| 42 | exercise_price | 否 |  |  |
| 43 | exercise_amount | 否 |  |  |
| 44 | settle_amount | 否 |  |  |
| 45 | exercise_balance | 否 |  |  |
| 46 | settle_balance | 否 |  |  |
| 47 | sys_std_margin | 否 |  |  |
| 48 | exefrozen_balance | 否 |  |  |
| 49 | date_clear | 否 |  |  |
| 50 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_exercise_assign | 默认 | 是 | client_id, stock_account, exchange_type, option_code, opthold_type, client_id, stock_account, exchange_type, option_code, opthold_type |
| idx_optexeassign_code | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |
| idx_uopt_exercise_assign | 默认 | 是 | client_id, stock_account, exchange_type, option_code, opthold_type, client_id, stock_account, exchange_type, option_code, opthold_type |
| idx_optexeassign_code | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_exercise_assign | client_id, stock_account, exchange_type, option_code, opthold_type, client_id, stock_account, exchange_type, option_code, opthold_type |
| idx_uopt_exercise_assign | client_id, stock_account, exchange_type, option_code, opthold_type, client_id, stock_account, exchange_type, option_code, opthold_type |

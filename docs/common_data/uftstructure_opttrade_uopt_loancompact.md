# uopt_loancompact - 股票期权资券合约表

**表对象ID**: 9017
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | begin_balance | 否 |  |  |
| 10 | current_balance | 否 |  |  |
| 11 | begin_amount | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | loan_compact_type | 否 |  |  |
| 14 | loan_compact_status | 否 |  |  |
| 15 | real_repaid_balance | 否 |  |  |
| 16 | real_repaid_amount | 否 |  |  |
| 17 | real_repaid_fine | 否 |  |  |
| 18 | real_repaid_fare | 否 |  |  |
| 19 | real_repaid_interest | 否 |  |  |
| 20 | repaid_compact_balance | 否 |  |  |
| 21 | repaid_compact_amount | 否 |  |  |
| 22 | repaid_compact_fine | 否 |  |  |
| 23 | repaid_compact_fare | 否 |  |  |
| 24 | repaid_compact_interest | 否 |  |  |
| 25 | opt_repaid_mod | 否 |  |  |
| 26 | integral_balance | 否 |  |  |
| 27 | fine_integral | 否 |  |  |
| 28 | interest_rate | 否 |  |  |
| 29 | fine_rate | 否 |  |  |
| 30 | settle_interest | 否 |  |  |
| 31 | settle_fine | 否 |  |  |
| 32 | fare | 否 |  |  |
| 33 | interest | 否 |  |  |
| 34 | fine | 否 |  |  |
| 35 | date_clear | 否 |  |  |
| 36 | position_str | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | init_date | 否 |  |  |
| 39 | client_id | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | stock_account | 否 |  |  |
| 43 | stock_code | 否 |  |  |
| 44 | stock_type | 否 |  |  |
| 45 | money_type | 否 |  |  |
| 46 | begin_balance | 否 |  |  |
| 47 | current_balance | 否 |  |  |
| 48 | begin_amount | 否 |  |  |
| 49 | current_amount | 否 |  |  |
| 50 | loan_compact_type | 否 |  |  |
| 51 | loan_compact_status | 否 |  |  |
| 52 | real_repaid_balance | 否 |  |  |
| 53 | real_repaid_amount | 否 |  |  |
| 54 | real_repaid_fine | 否 |  |  |
| 55 | real_repaid_fare | 否 |  |  |
| 56 | real_repaid_interest | 否 |  |  |
| 57 | repaid_compact_balance | 否 |  |  |
| 58 | repaid_compact_amount | 否 |  |  |
| 59 | repaid_compact_fine | 否 |  |  |
| 60 | repaid_compact_fare | 否 |  |  |
| 61 | repaid_compact_interest | 否 |  |  |
| 62 | opt_repaid_mod | 否 |  |  |
| 63 | integral_balance | 否 |  |  |
| 64 | fine_integral | 否 |  |  |
| 65 | interest_rate | 否 |  |  |
| 66 | fine_rate | 否 |  |  |
| 67 | settle_interest | 否 |  |  |
| 68 | settle_fine | 否 |  |  |
| 69 | fare | 否 |  |  |
| 70 | interest | 否 |  |  |
| 71 | fine | 否 |  |  |
| 72 | date_clear | 否 |  |  |
| 73 | position_str | 否 |  |  |
| 74 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_loancompact | 默认 | 是 | client_id, position_str, client_id, position_str |
| idx_uopt_loancompact | 默认 | 是 | client_id, position_str, client_id, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_loancompact | client_id, position_str, client_id, position_str |
| idx_uopt_loancompact | client_id, position_str, client_id, position_str |

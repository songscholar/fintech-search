# optexeassign - 行权指派导出表

**表对象ID**: 3203
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | company_no | 是 |  |  |
| 4 | client_id | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | stock_account | 是 |  |  |
| 8 | option_type | 是 |  |  |
| 9 | option_code | 是 |  |  |
| 10 | opthold_type | 是 |  |  |
| 11 | stock_code | 是 |  |  |
| 12 | stock_type | 是 |  |  |
| 13 | money_type | 是 |  |  |
| 14 | entrust_bs | 是 |  |  |
| 15 | seat_no | 是 |  |  |
| 16 | business_type | 是 |  |  |
| 17 | hold_amount | 是 |  |  |
| 18 | exercise_price | 是 |  |  |
| 19 | exercise_amount | 是 |  |  |
| 20 | settle_amount | 是 |  |  |
| 21 | exercise_balance | 是 |  |  |
| 22 | settle_balance | 是 |  |  |
| 23 | sys_std_margin | 是 |  |  |
| 24 | exefrozen_balance | 是 |  |  |
| 25 | remark | 是 |  |  |
| 26 | date_clear | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | init_date | 是 |  |  |
| 29 | branch_no | 是 |  |  |
| 30 | company_no | 是 |  |  |
| 31 | client_id | 是 |  |  |
| 32 | fund_account | 是 |  |  |
| 33 | exchange_type | 是 |  |  |
| 34 | stock_account | 是 |  |  |
| 35 | option_type | 是 |  |  |
| 36 | option_code | 是 |  |  |
| 37 | opthold_type | 是 |  |  |
| 38 | stock_code | 是 |  |  |
| 39 | stock_type | 是 |  |  |
| 40 | money_type | 是 |  |  |
| 41 | entrust_bs | 是 |  |  |
| 42 | seat_no | 是 |  |  |
| 43 | business_type | 是 |  |  |
| 44 | hold_amount | 是 |  |  |
| 45 | exercise_price | 是 |  |  |
| 46 | exercise_amount | 是 |  |  |
| 47 | settle_amount | 是 |  |  |
| 48 | exercise_balance | 是 |  |  |
| 49 | settle_balance | 是 |  |  |
| 50 | sys_std_margin | 是 |  |  |
| 51 | exefrozen_balance | 是 |  |  |
| 52 | remark | 是 |  |  |
| 53 | date_clear | 是 |  |  |
| 54 | position_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optexeassign | 默认 | 是 | client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date, client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date |
| idx_optexeassign | 默认 | 是 | client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date, client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optexeassign | client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date, client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date |
| idx_optexeassign | client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date, client_id, fund_account, stock_account, exchange_type, option_code, opthold_type, init_date |

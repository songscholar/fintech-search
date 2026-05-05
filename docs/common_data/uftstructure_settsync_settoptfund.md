# settoptfund - 清算期权资金表

**表对象ID**: 3225
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | money_type | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | current_balance | 是 |  |  |
| 6 | enable_balance | 是 |  |  |
| 7 | cash_balance | 是 |  |  |
| 8 | check_balance | 是 |  |  |
| 9 | frozen_balance | 是 |  |  |
| 10 | unfrozen_balance | 是 |  |  |
| 11 | correct_balance | 是 |  |  |
| 12 | real_balance | 是 |  |  |
| 13 | uncome_buy_balance | 是 |  |  |
| 14 | uncome_sell_balance | 是 |  |  |
| 15 | uncome_correct_balance | 是 |  |  |
| 16 | asset_prop | 是 |  |  |
| 17 | product_flag | 是 |  |  |
| 18 | node_id | 是 |  |  |
| 19 | bank_no | 是 |  |  |
| 20 | square_flag | 是 |  |  |
| 21 | real_status | 是 |  |  |
| 22 | begin_enable_balance | 是 |  |  |
| 23 | fund_account | 是 |  |  |
| 24 | money_type | 是 |  |  |
| 25 | client_id | 是 |  |  |
| 26 | branch_no | 是 |  |  |
| 27 | current_balance | 是 |  |  |
| 28 | enable_balance | 是 |  |  |
| 29 | cash_balance | 是 |  |  |
| 30 | check_balance | 是 |  |  |
| 31 | frozen_balance | 是 |  |  |
| 32 | unfrozen_balance | 是 |  |  |
| 33 | correct_balance | 是 |  |  |
| 34 | real_balance | 是 |  |  |
| 35 | uncome_buy_balance | 是 |  |  |
| 36 | uncome_sell_balance | 是 |  |  |
| 37 | uncome_correct_balance | 是 |  |  |
| 38 | asset_prop | 是 |  |  |
| 39 | product_flag | 是 |  |  |
| 40 | node_id | 是 |  |  |
| 41 | bank_no | 是 |  |  |
| 42 | square_flag | 是 |  |  |
| 43 | real_status | 是 |  |  |
| 44 | begin_enable_balance | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optsettfund | 默认 | 是 | fund_account, money_type, fund_account, money_type |
| idx_optsettfund | 默认 | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optsettfund | fund_account, money_type, fund_account, money_type |
| idx_optsettfund | fund_account, money_type, fund_account, money_type |

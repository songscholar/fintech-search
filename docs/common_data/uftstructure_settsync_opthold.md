# opthold - 期权清算持仓导出表

**表对象ID**: 3208
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | money_type | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | option_code | 是 |  |  |
| 10 | option_type | 是 |  |  |
| 11 | opthold_type | 是 |  |  |
| 12 | begin_amount | 是 |  |  |
| 13 | current_amount | 是 |  |  |
| 14 | uncome_open_amount | 是 |  |  |
| 15 | uncome_drop_amount | 是 |  |  |
| 16 | frozen_amount | 是 |  |  |
| 17 | unfrozen_amount | 是 |  |  |
| 18 | optcomb_used_amount | 是 |  |  |
| 19 | correct_amount | 是 |  |  |
| 20 | enable_amount | 是 |  |  |
| 21 | real_open_amount | 是 |  |  |
| 22 | real_drop_amount | 是 |  |  |
| 23 | real_buy_balance | 是 |  |  |
| 24 | real_sell_balance | 是 |  |  |
| 25 | entrust_drop_amount | 是 |  |  |
| 26 | sum_open_amount | 是 |  |  |
| 27 | sum_drop_amount | 是 |  |  |
| 28 | sum_buy_balance | 是 |  |  |
| 29 | sum_sell_balance | 是 |  |  |
| 30 | used_pur_quota | 是 |  |  |
| 31 | opt_cost_price | 是 |  |  |
| 32 | sum_buy_fare | 是 |  |  |
| 33 | sum_sell_fare | 是 |  |  |
| 34 | node_id | 是 |  |  |
| 35 | sysnode_version | 是 |  |  |
| 36 | post_current_amount | 是 |  |  |
| 37 | optcomb_used_amount_opt | 是 |  |  |
| 38 | exchange_type | 是 |  |  |
| 39 | money_type | 是 |  |  |
| 40 | branch_no | 是 |  |  |
| 41 | stock_account | 是 |  |  |
| 42 | client_id | 是 |  |  |
| 43 | fund_account | 是 |  |  |
| 44 | stock_code | 是 |  |  |
| 45 | stock_type | 是 |  |  |
| 46 | option_code | 是 |  |  |
| 47 | option_type | 是 |  |  |
| 48 | opthold_type | 是 |  |  |
| 49 | begin_amount | 是 |  |  |
| 50 | current_amount | 是 |  |  |
| 51 | uncome_open_amount | 是 |  |  |
| 52 | uncome_drop_amount | 是 |  |  |
| 53 | frozen_amount | 是 |  |  |
| 54 | unfrozen_amount | 是 |  |  |
| 55 | optcomb_used_amount | 是 |  |  |
| 56 | correct_amount | 是 |  |  |
| 57 | enable_amount | 是 |  |  |
| 58 | real_open_amount | 是 |  |  |
| 59 | real_drop_amount | 是 |  |  |
| 60 | real_buy_balance | 是 |  |  |
| 61 | real_sell_balance | 是 |  |  |
| 62 | entrust_drop_amount | 是 |  |  |
| 63 | sum_open_amount | 是 |  |  |
| 64 | sum_drop_amount | 是 |  |  |
| 65 | sum_buy_balance | 是 |  |  |
| 66 | sum_sell_balance | 是 |  |  |
| 67 | used_pur_quota | 是 |  |  |
| 68 | opt_cost_price | 是 |  |  |
| 69 | sum_buy_fare | 是 |  |  |
| 70 | sum_sell_fare | 是 |  |  |
| 71 | node_id | 是 |  |  |
| 72 | sysnode_version | 是 |  |  |
| 73 | post_current_amount | 是 |  |  |
| 74 | optcomb_used_amount_opt | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optsetthold | 默认 | 是 | exchange_type, stock_account, branch_no, option_code, opthold_type, exchange_type, stock_account, branch_no, option_code, opthold_type |
| idx_optsetthold | 默认 | 是 | exchange_type, stock_account, branch_no, option_code, opthold_type, exchange_type, stock_account, branch_no, option_code, opthold_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optsetthold | exchange_type, stock_account, branch_no, option_code, opthold_type, exchange_type, stock_account, branch_no, option_code, opthold_type |
| idx_optsetthold | exchange_type, stock_account, branch_no, option_code, opthold_type, exchange_type, stock_account, branch_no, option_code, opthold_type |

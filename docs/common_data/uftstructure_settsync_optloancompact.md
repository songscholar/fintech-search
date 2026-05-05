# optloancompact - 资券合约导出表

**表对象ID**: 3204
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | node_id | 是 |  |  |
| 2 | sysnode_version | 是 |  |  |
| 3 | init_date | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | asset_prop | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_type | 是 |  |  |
| 12 | money_type | 是 |  |  |
| 13 | begin_balance | 是 |  |  |
| 14 | current_balance | 是 |  |  |
| 15 | begin_amount | 是 |  |  |
| 16 | current_amount | 是 |  |  |
| 17 | loan_compact_type | 是 |  |  |
| 18 | loan_compact_status | 是 |  |  |
| 19 | real_repaid_balance | 是 |  |  |
| 20 | real_repaid_amount | 是 |  |  |
| 21 | real_repaid_fine | 是 |  |  |
| 22 | real_repaid_fare | 是 |  |  |
| 23 | real_repaid_interest | 是 |  |  |
| 24 | repaid_compact_balance | 是 |  |  |
| 25 | repaid_compact_amount | 是 |  |  |
| 26 | repaid_compact_fine | 是 |  |  |
| 27 | repaid_compact_fare | 是 |  |  |
| 28 | repaid_compact_interest | 是 |  |  |
| 29 | opt_repaid_mod | 是 |  |  |
| 30 | integral_balance | 是 |  |  |
| 31 | fine_integral | 是 |  |  |
| 32 | interest_rate | 是 |  |  |
| 33 | fine_rate | 是 |  |  |
| 34 | settle_interest | 是 |  |  |
| 35 | settle_fine | 是 |  |  |
| 36 | fare | 是 |  |  |
| 37 | interest | 是 |  |  |
| 38 | fine | 是 |  |  |
| 39 | date_clear | 是 |  |  |
| 40 | position_str | 是 |  |  |
| 41 | remark | 是 |  |  |
| 42 | node_id | 是 |  |  |
| 43 | sysnode_version | 是 |  |  |
| 44 | init_date | 是 |  |  |
| 45 | branch_no | 是 |  |  |
| 46 | client_id | 是 |  |  |
| 47 | fund_account | 是 |  |  |
| 48 | asset_prop | 是 |  |  |
| 49 | exchange_type | 是 |  |  |
| 50 | stock_account | 是 |  |  |
| 51 | stock_code | 是 |  |  |
| 52 | stock_type | 是 |  |  |
| 53 | money_type | 是 |  |  |
| 54 | begin_balance | 是 |  |  |
| 55 | current_balance | 是 |  |  |
| 56 | begin_amount | 是 |  |  |
| 57 | current_amount | 是 |  |  |
| 58 | loan_compact_type | 是 |  |  |
| 59 | loan_compact_status | 是 |  |  |
| 60 | real_repaid_balance | 是 |  |  |
| 61 | real_repaid_amount | 是 |  |  |
| 62 | real_repaid_fine | 是 |  |  |
| 63 | real_repaid_fare | 是 |  |  |
| 64 | real_repaid_interest | 是 |  |  |
| 65 | repaid_compact_balance | 是 |  |  |
| 66 | repaid_compact_amount | 是 |  |  |
| 67 | repaid_compact_fine | 是 |  |  |
| 68 | repaid_compact_fare | 是 |  |  |
| 69 | repaid_compact_interest | 是 |  |  |
| 70 | opt_repaid_mod | 是 |  |  |
| 71 | integral_balance | 是 |  |  |
| 72 | fine_integral | 是 |  |  |
| 73 | interest_rate | 是 |  |  |
| 74 | fine_rate | 是 |  |  |
| 75 | settle_interest | 是 |  |  |
| 76 | settle_fine | 是 |  |  |
| 77 | fare | 是 |  |  |
| 78 | interest | 是 |  |  |
| 79 | fine | 是 |  |  |
| 80 | date_clear | 是 |  |  |
| 81 | position_str | 是 |  |  |
| 82 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optloancompact | 默认 | 是 | position_str, position_str |
| idx_optloancompact | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optloancompact | position_str, position_str |
| idx_optloancompact | position_str, position_str |

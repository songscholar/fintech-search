# surstockjour_tosett - 余券流水表

**表对象ID**: 3079
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | operator_no | 是 |  |  |
| 6 | op_branch_no | 是 |  |  |
| 7 | op_entrust_way | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | branch_no | 是 |  |  |
| 10 | cashgroup_no | 是 |  |  |
| 11 | real_action | 是 |  |  |
| 12 | fund_account | 是 |  |  |
| 13 | client_id | 是 |  |  |
| 14 | exchange_type | 是 |  |  |
| 15 | stock_account | 是 |  |  |
| 16 | stock_code | 是 |  |  |
| 17 | stock_type | 是 |  |  |
| 18 | money_type | 是 |  |  |
| 19 | business_flag | 是 |  |  |
| 20 | occur_amount | 是 |  |  |
| 21 | post_amount | 是 |  |  |
| 22 | remark | 是 |  |  |
| 23 | cancel_serialno | 是 |  |  |
| 24 | position_str | 是 |  |  |
| 25 | surstock_end_balance | 是 |  |  |
| 26 | update_date | 是 |  |  |
| 27 | update_time | 是 |  |  |
| 28 | transaction_no | 是 |  |  |
| 29 | asset_prop | 是 |  |  |
| 30 | init_date | 是 |  |  |
| 31 | serial_no | 是 |  |  |
| 32 | curr_date | 是 |  |  |
| 33 | curr_time | 是 |  |  |
| 34 | operator_no | 是 |  |  |
| 35 | op_branch_no | 是 |  |  |
| 36 | op_entrust_way | 是 |  |  |
| 37 | op_station | 是 |  |  |
| 38 | branch_no | 是 |  |  |
| 39 | cashgroup_no | 是 |  |  |
| 40 | real_action | 是 |  |  |
| 41 | fund_account | 是 |  |  |
| 42 | client_id | 是 |  |  |
| 43 | exchange_type | 是 |  |  |
| 44 | stock_account | 是 |  |  |
| 45 | stock_code | 是 |  |  |
| 46 | stock_type | 是 |  |  |
| 47 | money_type | 是 |  |  |
| 48 | business_flag | 是 |  |  |
| 49 | occur_amount | 是 |  |  |
| 50 | post_amount | 是 |  |  |
| 51 | remark | 是 |  |  |
| 52 | cancel_serialno | 是 |  |  |
| 53 | position_str | 是 |  |  |
| 54 | surstock_end_balance | 是 |  |  |
| 55 | update_date | 是 |  |  |
| 56 | update_time | 是 |  |  |
| 57 | transaction_no | 是 |  |  |
| 58 | asset_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_surstockjour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_surstockjour_acct | 默认 | 是 | fund_account, fund_account |
| idx_surstockjour_id | 默认 | 是 | client_id, client_id |
| idx_surstockjour_pos | 默认 | 是 | position_str, position_str |
| idx_surstockjour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_surstockjour_acct | 默认 | 是 | fund_account, fund_account |
| idx_surstockjour_id | 默认 | 是 | client_id, client_id |
| idx_surstockjour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_surstockjour_pos | position_str, position_str |
| idx_surstockjour_pos | position_str, position_str |

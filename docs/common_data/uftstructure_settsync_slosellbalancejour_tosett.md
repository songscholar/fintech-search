# slosellbalancejour_tosett - 融券卖出所得流水表2

**表对象ID**: 3080
**所属模块**: settsync
**数据空间**: HS_UFT_DATA

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | operator_no | 是 |  |  |
| 4 | op_branch_no | 是 |  |  |
| 5 | op_entrust_way | 是 |  |  |
| 6 | op_station | 是 |  |  |
| 7 | branch_no | 是 |  |  |
| 8 | curr_time | 是 |  |  |
| 9 | curr_date | 是 |  |  |
| 10 | money_type | 是 |  |  |
| 11 | fund_account | 是 |  |  |
| 12 | client_id | 是 |  |  |
| 13 | business_flag | 是 |  |  |
| 14 | occur_balance | 是 |  |  |
| 15 | post_balance | 是 |  |  |
| 16 | real_action | 是 |  |  |
| 17 | position_str | 是 |  |  |
| 18 | occur_used_balance | 是 |  |  |
| 19 | post_used_balance | 是 |  |  |
| 20 | remark | 是 |  |  |
| 21 | occur_frozen_balance | 是 |  |  |
| 22 | post_frozen_balance | 是 |  |  |
| 23 | update_date | 是 |  |  |
| 24 | update_time | 是 |  |  |
| 25 | transaction_no | 是 |  |  |
| 26 | asset_prop | 是 |  |  |
| 27 | init_date | 是 |  |  |
| 28 | serial_no | 是 |  |  |
| 29 | operator_no | 是 |  |  |
| 30 | op_branch_no | 是 |  |  |
| 31 | op_entrust_way | 是 |  |  |
| 32 | op_station | 是 |  |  |
| 33 | branch_no | 是 |  |  |
| 34 | curr_time | 是 |  |  |
| 35 | curr_date | 是 |  |  |
| 36 | money_type | 是 |  |  |
| 37 | fund_account | 是 |  |  |
| 38 | client_id | 是 |  |  |
| 39 | business_flag | 是 |  |  |
| 40 | occur_balance | 是 |  |  |
| 41 | post_balance | 是 |  |  |
| 42 | real_action | 是 |  |  |
| 43 | position_str | 是 |  |  |
| 44 | occur_used_balance | 是 |  |  |
| 45 | post_used_balance | 是 |  |  |
| 46 | remark | 是 |  |  |
| 47 | occur_frozen_balance | 是 |  |  |
| 48 | post_frozen_balance | 是 |  |  |
| 49 | update_date | 是 |  |  |
| 50 | update_time | 是 |  |  |
| 51 | transaction_no | 是 |  |  |
| 52 | asset_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_slosellbalancejour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_slosellbalancejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_slosellbalancejour_id | 默认 | 是 | client_id, client_id |
| idx_slosellbalancejour_pos | 默认 | 是 | position_str, position_str |
| idx_slosellbalancejour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_slosellbalancejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_slosellbalancejour_id | 默认 | 是 | client_id, client_id |
| idx_slosellbalancejour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_slosellbalancejour_pos | position_str, position_str |
| idx_slosellbalancejour_pos | position_str, position_str |

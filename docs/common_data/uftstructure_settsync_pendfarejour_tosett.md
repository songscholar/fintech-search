# pendfarejour_tosett - 费用待扣收流水表

**表对象ID**: 3078
**所属模块**: settsync
**数据空间**: HS_UFT_DATA

## 字段列表（共 66 个）

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
| 10 | pendfare_id | 是 |  |  |
| 11 | fund_account | 是 |  |  |
| 12 | client_id | 是 |  |  |
| 13 | stock_account | 是 |  |  |
| 14 | exchange_type | 是 |  |  |
| 15 | stock_type | 是 |  |  |
| 16 | stock_code | 是 |  |  |
| 17 | compact_id | 是 |  |  |
| 18 | money_type | 是 |  |  |
| 19 | cashgroup_no | 是 |  |  |
| 20 | pendfare_type | 是 |  |  |
| 21 | occur_fare | 是 |  |  |
| 22 | post_fare | 是 |  |  |
| 23 | remark | 是 |  |  |
| 24 | position_str | 是 |  |  |
| 25 | real_action | 是 |  |  |
| 26 | prefer_balance | 是 |  |  |
| 27 | frozen_balance | 是 |  |  |
| 28 | cashcompact_id | 是 |  |  |
| 29 | fund_account_src | 是 |  |  |
| 30 | update_date | 是 |  |  |
| 31 | update_time | 是 |  |  |
| 32 | transaction_no | 是 |  |  |
| 33 | asset_prop | 是 |  |  |
| 34 | init_date | 是 |  |  |
| 35 | serial_no | 是 |  |  |
| 36 | curr_date | 是 |  |  |
| 37 | curr_time | 是 |  |  |
| 38 | operator_no | 是 |  |  |
| 39 | op_branch_no | 是 |  |  |
| 40 | op_entrust_way | 是 |  |  |
| 41 | op_station | 是 |  |  |
| 42 | branch_no | 是 |  |  |
| 43 | pendfare_id | 是 |  |  |
| 44 | fund_account | 是 |  |  |
| 45 | client_id | 是 |  |  |
| 46 | stock_account | 是 |  |  |
| 47 | exchange_type | 是 |  |  |
| 48 | stock_type | 是 |  |  |
| 49 | stock_code | 是 |  |  |
| 50 | compact_id | 是 |  |  |
| 51 | money_type | 是 |  |  |
| 52 | cashgroup_no | 是 |  |  |
| 53 | pendfare_type | 是 |  |  |
| 54 | occur_fare | 是 |  |  |
| 55 | post_fare | 是 |  |  |
| 56 | remark | 是 |  |  |
| 57 | position_str | 是 |  |  |
| 58 | real_action | 是 |  |  |
| 59 | prefer_balance | 是 |  |  |
| 60 | frozen_balance | 是 |  |  |
| 61 | cashcompact_id | 是 |  |  |
| 62 | fund_account_src | 是 |  |  |
| 63 | update_date | 是 |  |  |
| 64 | update_time | 是 |  |  |
| 65 | transaction_no | 是 |  |  |
| 66 | asset_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pendfarejour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_pendfarejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_pendfarejour_id | 默认 | 是 | client_id, client_id |
| idx_pendfarejour_pos | 默认 | 是 | position_str, position_str |
| idx_pendfarejour | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_pendfarejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_pendfarejour_id | 默认 | 是 | client_id, client_id |
| idx_pendfarejour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pendfarejour_pos | position_str, position_str |
| idx_pendfarejour_pos | position_str, position_str |

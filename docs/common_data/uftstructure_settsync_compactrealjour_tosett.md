# compactrealjour_tosett - 实时合约流水表

**表对象ID**: 3082
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 82 个）

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
| 10 | compact_id | 是 |  |  |
| 11 | fund_account | 是 |  |  |
| 12 | client_id | 是 |  |  |
| 13 | stock_account | 是 |  |  |
| 14 | exchange_type | 是 |  |  |
| 15 | stock_code | 是 |  |  |
| 16 | stock_type | 是 |  |  |
| 17 | money_type | 是 |  |  |
| 18 | compact_type | 是 |  |  |
| 19 | business_flag | 是 |  |  |
| 20 | occur_balance | 是 |  |  |
| 21 | post_balance | 是 |  |  |
| 22 | occur_amount | 是 |  |  |
| 23 | post_amount | 是 |  |  |
| 24 | occur_fare | 是 |  |  |
| 25 | post_fare | 是 |  |  |
| 26 | occur_interest | 是 |  |  |
| 27 | post_interest | 是 |  |  |
| 28 | occur_frozen_interest | 是 |  |  |
| 29 | post_frozen_interest | 是 |  |  |
| 30 | entrust_no | 是 |  |  |
| 31 | remark | 是 |  |  |
| 32 | cancel_serialno | 是 |  |  |
| 33 | position_str | 是 |  |  |
| 34 | occur_repaycost_balance | 是 |  |  |
| 35 | post_repaycost_balance | 是 |  |  |
| 36 | fund_account_src | 是 |  |  |
| 37 | prefer_balance | 是 |  |  |
| 38 | update_date | 是 |  |  |
| 39 | update_time | 是 |  |  |
| 40 | transaction_no | 是 |  |  |
| 41 | asset_prop | 是 |  |  |
| 42 | init_date | 是 |  |  |
| 43 | serial_no | 是 |  |  |
| 44 | curr_date | 是 |  |  |
| 45 | curr_time | 是 |  |  |
| 46 | operator_no | 是 |  |  |
| 47 | op_branch_no | 是 |  |  |
| 48 | op_entrust_way | 是 |  |  |
| 49 | op_station | 是 |  |  |
| 50 | branch_no | 是 |  |  |
| 51 | compact_id | 是 |  |  |
| 52 | fund_account | 是 |  |  |
| 53 | client_id | 是 |  |  |
| 54 | stock_account | 是 |  |  |
| 55 | exchange_type | 是 |  |  |
| 56 | stock_code | 是 |  |  |
| 57 | stock_type | 是 |  |  |
| 58 | money_type | 是 |  |  |
| 59 | compact_type | 是 |  |  |
| 60 | business_flag | 是 |  |  |
| 61 | occur_balance | 是 |  |  |
| 62 | post_balance | 是 |  |  |
| 63 | occur_amount | 是 |  |  |
| 64 | post_amount | 是 |  |  |
| 65 | occur_fare | 是 |  |  |
| 66 | post_fare | 是 |  |  |
| 67 | occur_interest | 是 |  |  |
| 68 | post_interest | 是 |  |  |
| 69 | occur_frozen_interest | 是 |  |  |
| 70 | post_frozen_interest | 是 |  |  |
| 71 | entrust_no | 是 |  |  |
| 72 | remark | 是 |  |  |
| 73 | cancel_serialno | 是 |  |  |
| 74 | position_str | 是 |  |  |
| 75 | occur_repaycost_balance | 是 |  |  |
| 76 | post_repaycost_balance | 是 |  |  |
| 77 | fund_account_src | 是 |  |  |
| 78 | prefer_balance | 是 |  |  |
| 79 | update_date | 是 |  |  |
| 80 | update_time | 是 |  |  |
| 81 | transaction_no | 是 |  |  |
| 82 | asset_prop | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_compactrealjour_pos | 默认 | 是 | position_str, position_str |
| idx_compactrealjour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_compactrealjour_pos | position_str, position_str |
| idx_compactrealjour_pos | position_str, position_str |

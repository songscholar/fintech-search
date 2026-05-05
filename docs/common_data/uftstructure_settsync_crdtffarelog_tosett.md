# crdtffarelog_tosett - 前台费用日志表

**表对象ID**: 3081
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | curr_date | 是 |  |  |
| 3 | curr_time | 是 |  |  |
| 4 | serial_no | 是 |  |  |
| 5 | business_flag | 是 |  |  |
| 6 | op_branch_no | 是 |  |  |
| 7 | operator_no | 是 |  |  |
| 8 | op_station | 是 |  |  |
| 9 | branch_no | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | client_id | 是 |  |  |
| 12 | square_flag | 是 |  |  |
| 13 | bank_no | 是 |  |  |
| 14 | money_type | 是 |  |  |
| 15 | exchange_type | 是 |  |  |
| 16 | stock_account | 是 |  |  |
| 17 | op_entrust_way | 是 |  |  |
| 18 | fare_type | 是 |  |  |
| 19 | fare | 是 |  |  |
| 20 | fare_count | 是 |  |  |
| 21 | fare_date | 是 |  |  |
| 22 | entrust_no | 是 |  |  |
| 23 | status | 是 |  |  |
| 24 | prev_status | 是 |  |  |
| 25 | cancel_serialno | 是 |  |  |
| 26 | position_str | 是 |  |  |
| 27 | update_date | 是 |  |  |
| 28 | update_time | 是 |  |  |
| 29 | transaction_no | 是 |  |  |
| 30 | asset_prop | 是 |  |  |
| 31 | init_date | 是 |  |  |
| 32 | curr_date | 是 |  |  |
| 33 | curr_time | 是 |  |  |
| 34 | serial_no | 是 |  |  |
| 35 | business_flag | 是 |  |  |
| 36 | op_branch_no | 是 |  |  |
| 37 | operator_no | 是 |  |  |
| 38 | op_station | 是 |  |  |
| 39 | branch_no | 是 |  |  |
| 40 | fund_account | 是 |  |  |
| 41 | client_id | 是 |  |  |
| 42 | square_flag | 是 |  |  |
| 43 | bank_no | 是 |  |  |
| 44 | money_type | 是 |  |  |
| 45 | exchange_type | 是 |  |  |
| 46 | stock_account | 是 |  |  |
| 47 | op_entrust_way | 是 |  |  |
| 48 | fare_type | 是 |  |  |
| 49 | fare | 是 |  |  |
| 50 | fare_count | 是 |  |  |
| 51 | fare_date | 是 |  |  |
| 52 | entrust_no | 是 |  |  |
| 53 | status | 是 |  |  |
| 54 | prev_status | 是 |  |  |
| 55 | cancel_serialno | 是 |  |  |
| 56 | position_str | 是 |  |  |
| 57 | update_date | 是 |  |  |
| 58 | update_time | 是 |  |  |
| 59 | transaction_no | 是 |  |  |
| 60 | asset_prop | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtffarelog | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_crdtffarelog_stk | 默认 | 是 | stock_account, branch_no, fare_type, business_flag, stock_account, branch_no, fare_type, business_flag |
| idx_crdtffarelog_id | 默认 | 是 | client_id, client_id |
| idx_crdtffarelog_acct | 默认 | 是 | fund_account, fund_account |
| idx_crdtffarelog_pos | 默认 | 是 | position_str, position_str |
| idx_crdtffarelog | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_crdtffarelog_stk | 默认 | 是 | stock_account, branch_no, fare_type, business_flag, stock_account, branch_no, fare_type, business_flag |
| idx_crdtffarelog_id | 默认 | 是 | client_id, client_id |
| idx_crdtffarelog_acct | 默认 | 是 | fund_account, fund_account |
| idx_crdtffarelog_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtffarelog_pos | position_str, position_str |
| idx_crdtffarelog_pos | position_str, position_str |

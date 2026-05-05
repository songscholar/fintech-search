# compactapply_tosett - 合约展期申请表2

**表对象ID**: 3077
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
| 5 | branch_no | 是 |  |  |
| 6 | compact_id | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | stock_code | 是 |  |  |
| 12 | cash_asset | 是 |  |  |
| 13 | market_value_begin | 是 |  |  |
| 14 | total_debit | 是 |  |  |
| 15 | per_assurescale_value | 是 |  |  |
| 16 | risk_remind_info | 是 |  |  |
| 17 | assist_info | 是 |  |  |
| 18 | compact_apply_status | 是 |  |  |
| 19 | date_clear | 是 |  |  |
| 20 | remark | 是 |  |  |
| 21 | position_str | 是 |  |  |
| 22 | autoaudit_fail_reason | 是 |  |  |
| 23 | op_station | 是 |  |  |
| 24 | real_compact_balance | 是 |  |  |
| 25 | real_compact_fare | 是 |  |  |
| 26 | per_assurescale_value_out | 是 |  |  |
| 27 | update_date | 是 |  |  |
| 28 | update_time | 是 |  |  |
| 29 | transaction_no | 是 |  |  |
| 30 | asset_prop | 是 |  |  |
| 31 | init_date | 是 |  |  |
| 32 | curr_date | 是 |  |  |
| 33 | curr_time | 是 |  |  |
| 34 | serial_no | 是 |  |  |
| 35 | branch_no | 是 |  |  |
| 36 | compact_id | 是 |  |  |
| 37 | client_id | 是 |  |  |
| 38 | fund_account | 是 |  |  |
| 39 | stock_account | 是 |  |  |
| 40 | exchange_type | 是 |  |  |
| 41 | stock_code | 是 |  |  |
| 42 | cash_asset | 是 |  |  |
| 43 | market_value_begin | 是 |  |  |
| 44 | total_debit | 是 |  |  |
| 45 | per_assurescale_value | 是 |  |  |
| 46 | risk_remind_info | 是 |  |  |
| 47 | assist_info | 是 |  |  |
| 48 | compact_apply_status | 是 |  |  |
| 49 | date_clear | 是 |  |  |
| 50 | remark | 是 |  |  |
| 51 | position_str | 是 |  |  |
| 52 | autoaudit_fail_reason | 是 |  |  |
| 53 | op_station | 是 |  |  |
| 54 | real_compact_balance | 是 |  |  |
| 55 | real_compact_fare | 是 |  |  |
| 56 | per_assurescale_value_out | 是 |  |  |
| 57 | update_date | 是 |  |  |
| 58 | update_time | 是 |  |  |
| 59 | transaction_no | 是 |  |  |
| 60 | asset_prop | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_compactapply | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_compactapply_pos | 默认 | 是 | position_str, position_str |
| idx_compactapply_acct | 默认 | 是 | fund_account, fund_account |
| idx_compactapply_stock | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_compactapply | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_compactapply_pos | 默认 | 是 | position_str, position_str |
| idx_compactapply_acct | 默认 | 是 | fund_account, fund_account |
| idx_compactapply_stock | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_compactapply_pos | position_str, position_str |
| idx_compactapply_pos | position_str, position_str |

# uft_compact_apply - UFT合约展期申请表

**表对象ID**: 7990
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | compact_id | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | cash_asset | 否 |  |  |
| 13 | market_value_begin | 否 |  |  |
| 14 | total_debit | 否 |  |  |
| 15 | per_assurescale_value | 否 |  |  |
| 16 | risk_remind_info | 否 |  |  |
| 17 | assist_info | 否 |  |  |
| 18 | compact_apply_status | 否 |  |  |
| 19 | date_clear | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | autoaudit_fail_reason | 否 |  |  |
| 23 | op_station | 否 |  |  |
| 24 | init_date | 否 |  |  |
| 25 | curr_date | 否 |  |  |
| 26 | curr_time | 否 |  |  |
| 27 | serial_no | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | compact_id | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | cash_asset | 否 |  |  |
| 36 | market_value_begin | 否 |  |  |
| 37 | total_debit | 否 |  |  |
| 38 | per_assurescale_value | 否 |  |  |
| 39 | risk_remind_info | 否 |  |  |
| 40 | assist_info | 否 |  |  |
| 41 | compact_apply_status | 否 |  |  |
| 42 | date_clear | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | position_str | 否 |  |  |
| 45 | autoaudit_fail_reason | 否 |  |  |
| 46 | op_station | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_compact_apply | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_uft_compact_apply_pos | ART | 是 | position_str, position_str |
| idx_uft_compact_apply_acct | ART | 是 | fund_account, fund_account |
| idx_uft_compact_apply_stock | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_uft_compact_apply | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_uft_compact_apply_pos | ART | 是 | position_str, position_str |
| idx_uft_compact_apply_acct | ART | 是 | fund_account, fund_account |
| idx_uft_compact_apply_stock | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_compact_apply | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_uft_compact_apply | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

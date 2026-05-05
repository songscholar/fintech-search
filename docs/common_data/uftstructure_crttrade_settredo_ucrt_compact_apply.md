# settredo_ucrt_compact_apply - 日终清算合约展期申请表

**表对象ID**: 7596
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | compact_id | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | cash_asset | 否 |  |  |
| 12 | total_debit | 否 |  |  |
| 13 | per_assurescale_value | 否 |  |  |
| 14 | compact_apply_status | 否 |  |  |
| 15 | date_clear | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | market_value_begin | 否 |  |  |
| 18 | autoaudit_fail_reason | 否 |  |  |
| 19 | op_station | 否 |  |  |
| 20 | real_compact_balance | 否 |  |  |
| 21 | real_compact_fare | 否 |  |  |
| 22 | per_assurescale_value_out | 否 |  |  |
| 23 | sett_dml_type | 否 |  |  |
| 24 | sett_batch_no | 否 |  |  |
| 25 | init_date | 否 |  |  |
| 26 | curr_date | 否 |  |  |
| 27 | curr_time | 否 |  |  |
| 28 | serial_no | 否 |  |  |
| 29 | compact_id | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | cash_asset | 否 |  |  |
| 36 | total_debit | 否 |  |  |
| 37 | per_assurescale_value | 否 |  |  |
| 38 | compact_apply_status | 否 |  |  |
| 39 | date_clear | 否 |  |  |
| 40 | remark | 否 |  |  |
| 41 | market_value_begin | 否 |  |  |
| 42 | autoaudit_fail_reason | 否 |  |  |
| 43 | op_station | 否 |  |  |
| 44 | real_compact_balance | 否 |  |  |
| 45 | real_compact_fare | 否 |  |  |
| 46 | per_assurescale_value_out | 否 |  |  |
| 47 | sett_dml_type | 否 |  |  |
| 48 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_compact_apply | ART | 是 | fund_account, init_date, serial_no, sett_batch_no, fund_account, init_date, serial_no, sett_batch_no |
| idx_strd_ucrt_compact_apply | ART | 是 | fund_account, init_date, serial_no, sett_batch_no, fund_account, init_date, serial_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_compact_apply | fund_account, init_date, serial_no, sett_batch_no, fund_account, init_date, serial_no, sett_batch_no |
| idx_strd_ucrt_compact_apply | fund_account, init_date, serial_no, sett_batch_no, fund_account, init_date, serial_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

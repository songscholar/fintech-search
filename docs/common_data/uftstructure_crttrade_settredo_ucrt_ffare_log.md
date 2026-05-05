# settredo_ucrt_ffare_log - 日终清算融资融券UFT前台费用日志表

**表对象ID**: 7597
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | bank_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | business_flag | 否 |  |  |
| 4 | cancel_serial_no | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_microtime | 否 |  |  |
| 7 | entrust_no | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | fare | 否 |  |  |
| 10 | fare_date | 否 |  |  |
| 11 | fare_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | op_branch_no | 否 |  |  |
| 16 | op_entrust_way | 否 |  |  |
| 17 | op_station | 否 |  |  |
| 18 | operator_no | 否 |  |  |
| 19 | prev_status | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | square_flag | 否 |  |  |
| 22 | status | 否 |  |  |
| 23 | stock_account | 否 |  |  |
| 24 | sett_dml_type | 否 |  |  |
| 25 | sett_batch_no | 否 |  |  |
| 26 | bank_no | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | business_flag | 否 |  |  |
| 29 | cancel_serial_no | 否 |  |  |
| 30 | curr_date | 否 |  |  |
| 31 | curr_microtime | 否 |  |  |
| 32 | entrust_no | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | fare | 否 |  |  |
| 35 | fare_date | 否 |  |  |
| 36 | fare_type | 否 |  |  |
| 37 | fund_account | 否 |  |  |
| 38 | init_date | 否 |  |  |
| 39 | money_type | 否 |  |  |
| 40 | op_branch_no | 否 |  |  |
| 41 | op_entrust_way | 否 |  |  |
| 42 | op_station | 否 |  |  |
| 43 | operator_no | 否 |  |  |
| 44 | prev_status | 否 |  |  |
| 45 | serial_no | 否 |  |  |
| 46 | square_flag | 否 |  |  |
| 47 | status | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | sett_dml_type | 否 |  |  |
| 50 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_ffare_log | ART | 是 | fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no, fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no |
| idx_strd_ucrt_ffare_log | ART | 是 | fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no, fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_ffare_log | fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no, fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no |
| idx_strd_ucrt_ffare_log | fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no, fund_account, entrust_no, init_date, serial_no, branch_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

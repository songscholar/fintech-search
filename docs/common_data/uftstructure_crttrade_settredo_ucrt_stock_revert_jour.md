# settredo_ucrt_stock_revert_jour - 日终清算融资融券股份反向操作流水表

**表对象ID**: 7587
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_time | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | op_branch_no | 否 |  |  |
| 11 | operator_no | 否 |  |  |
| 12 | op_station | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | occur_amount | 否 |  |  |
| 16 | treat_status | 否 |  |  |
| 17 | valid_date | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | client_group | 否 |  |  |
| 20 | room_code | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | cancel_serialno | 否 |  |  |
| 24 | frozen_reason | 否 |  |  |
| 25 | stock_code_long | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | sett_dml_type | 否 |  |  |
| 28 | sett_batch_no | 否 |  |  |
| 29 | init_date | 否 |  |  |
| 30 | serial_no | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | curr_date | 否 |  |  |
| 36 | curr_time | 否 |  |  |
| 37 | business_flag | 否 |  |  |
| 38 | op_branch_no | 否 |  |  |
| 39 | operator_no | 否 |  |  |
| 40 | op_station | 否 |  |  |
| 41 | fund_account | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | occur_amount | 否 |  |  |
| 44 | treat_status | 否 |  |  |
| 45 | valid_date | 否 |  |  |
| 46 | position_str | 否 |  |  |
| 47 | client_group | 否 |  |  |
| 48 | room_code | 否 |  |  |
| 49 | money_type | 否 |  |  |
| 50 | stock_type | 否 |  |  |
| 51 | cancel_serialno | 否 |  |  |
| 52 | frozen_reason | 否 |  |  |
| 53 | stock_code_long | 否 |  |  |
| 54 | remark | 否 |  |  |
| 55 | sett_dml_type | 否 |  |  |
| 56 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_crt_stockrevertjour | ART | 是 | serial_no, init_date, fund_account, sett_batch_no, serial_no, init_date, fund_account, sett_batch_no |
| idx_strd_crt_stockrevertjour | ART | 是 | serial_no, init_date, fund_account, sett_batch_no, serial_no, init_date, fund_account, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_crt_stockrevertjour | serial_no, init_date, fund_account, sett_batch_no, serial_no, init_date, fund_account, sett_batch_no |
| idx_strd_crt_stockrevertjour | serial_no, init_date, fund_account, sett_batch_no, serial_no, init_date, fund_account, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

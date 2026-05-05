# ucrt_ffare_log - 融资融券UFT前台费用日志表

**表对象ID**: 7542
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

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
| 24 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 25 | client_id | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | client_name | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | bank_no | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | business_flag | 否 |  |  |
| 39 | cancel_serial_no | 否 |  |  |
| 40 | curr_date | 否 |  |  |
| 41 | curr_microtime | 否 |  |  |
| 42 | entrust_no | 否 |  |  |
| 43 | exchange_type | 否 |  |  |
| 44 | fare | 否 |  |  |
| 45 | fare_date | 否 |  |  |
| 46 | fare_type | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | init_date | 否 |  |  |
| 49 | money_type | 否 |  |  |
| 50 | op_branch_no | 否 |  |  |
| 51 | op_entrust_way | 否 |  |  |
| 52 | op_station | 否 |  |  |
| 53 | operator_no | 否 |  |  |
| 54 | prev_status | 否 |  |  |
| 55 | serial_no | 否 |  |  |
| 56 | square_flag | 否 |  |  |
| 57 | status | 否 |  |  |
| 58 | stock_account | 否 |  |  |
| 59 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 60 | client_id | 否 | H |  |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | limit_flag | 否 | H |  |
| 64 | asset_prop | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_client_group | 否 | H |  |
| 67 | corp_risk_level | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | client_name | 否 | H |  |
| 70 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_ffare_log | 默认 | 否 | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |
| idx_ucrt_ffare_log | ART | 是 | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |
| uk_rpt_ucrtffarelog | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtffarelog_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_ffare_log | 默认 | 否 | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |
| idx_ucrt_ffare_log | ART | 是 | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |
| uk_rpt_ucrtffarelog | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtffarelog_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_ffare_log | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |
| idx_ucrt_ffare_log | fund_account, entrust_no, init_date, serial_no, branch_no, fund_account, entrust_no, init_date, serial_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-27 17:21:59 | 3.0.8.19 | 袁文龙 | 当前表ucrt_ffare_log，修改了索引idx_ucrt_ffare_log,索引字段修改为：(fund_acco... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2024-07-22 13:26:29 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-09-15 10:22:05 | V3.0.1.2 | 许琮擎 | 表索引重命名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-02-27 17:21:59 | 3.0.8.19 | 袁文龙 | 当前表ucrt_ffare_log，修改了索引idx_ucrt_ffare_log,索引字段修改为：(fund_acco... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2024-07-22 13:26:29 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-09-15 10:22:05 | V3.0.1.2 | 许琮擎 | 表索引重命名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

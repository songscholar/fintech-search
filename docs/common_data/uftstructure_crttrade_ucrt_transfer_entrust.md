# ucrt_transfer_entrust - 非交易过户委托表

**表对象ID**: 7540
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account_src | 否 |  |  |
| 6 | client_id_src | 否 |  |  |
| 7 | stock_account_src | 否 |  |  |
| 8 | seat_no_src | 否 |  |  |
| 9 | fund_account_dest | 否 |  |  |
| 10 | client_id_dest | 否 |  |  |
| 11 | stock_account_dest | 否 |  |  |
| 12 | seat_no_dest | 否 |  |  |
| 13 | withdraw_flag | 否 |  |  |
| 14 | frozen_serial_no | 否 |  |  |
| 15 | unfrozen_status | 否 |  |  |
| 16 | cost_price | 否 |  |  |
| 17 | return_serial_no | 否 |  |  |
| 18 | return_time | 否 |  |  |
| 19 | return_code | 否 |  |  |
| 20 | return_info | 否 |  |  |
| 21 | cancel_serial_no | 否 |  |  |
| 22 | position_str | 否 |  | curr_date(8)+partition_no(2)＋curr_microtime(12)+serial_no(8) |
| 23 | branch_no | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | risk_level | 否 | H |  |
| 29 | corp_client_group | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | client_name | 否 | H |  |
| 33 | client_prop | 否 | H |  |
| 34 | init_date | 否 |  |  |
| 35 | entrust_no | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | fund_account_src | 否 |  |  |
| 39 | client_id_src | 否 |  |  |
| 40 | stock_account_src | 否 |  |  |
| 41 | seat_no_src | 否 |  |  |
| 42 | fund_account_dest | 否 |  |  |
| 43 | client_id_dest | 否 |  |  |
| 44 | stock_account_dest | 否 |  |  |
| 45 | seat_no_dest | 否 |  |  |
| 46 | withdraw_flag | 否 |  |  |
| 47 | frozen_serial_no | 否 |  |  |
| 48 | unfrozen_status | 否 |  |  |
| 49 | cost_price | 否 |  |  |
| 50 | return_serial_no | 否 |  |  |
| 51 | return_time | 否 |  |  |
| 52 | return_code | 否 |  |  |
| 53 | return_info | 否 |  |  |
| 54 | cancel_serial_no | 否 |  |  |
| 55 | position_str | 否 |  | curr_date(8)+partition_no(2)＋curr_microtime(12)+serial_no(8) |
| 56 | branch_no | 否 | H |  |
| 57 | client_group | 否 | H |  |
| 58 | room_code | 否 | H |  |
| 59 | asset_prop | 否 | H |  |
| 60 | limit_flag | 否 | H |  |
| 61 | risk_level | 否 | H |  |
| 62 | corp_client_group | 否 | H |  |
| 63 | corp_risk_level | 否 | H |  |
| 64 | asset_level | 否 | H |  |
| 65 | client_name | 否 | H |  |
| 66 | client_prop | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_transfer_entrust | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_ucrt_transfer_entrust_status | ART | 是 | unfrozen_status, unfrozen_status |
| uk_rpt_ucrttransferentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_ucrt_transfer_entrust | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_ucrt_transfer_entrust_status | ART | 是 | unfrozen_status, unfrozen_status |
| uk_rpt_ucrttransferentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_transfer_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_ucrt_transfer_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-28 21:30 | 0.3.3.113 | 雷玄 | 新增 idx_ucrt_transfer_entrust_status 索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-28 21:30 | 0.3.3.113 | 雷玄 | 新增 idx_ucrt_transfer_entrust_status 索引 |

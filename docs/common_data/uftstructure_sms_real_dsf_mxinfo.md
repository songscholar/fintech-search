# real_dsf_mxinfo - 实时代收代付明细表

**表对象ID**: 2837
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 110 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | csdc_order_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | square_seat | 否 |  |  |
| 5 | csdc_seat_no | 否 |  |  |
| 6 | seat_no | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_code2 | 否 |  |  |
| 10 | clear_busi_type | 否 |  |  |
| 11 | order_id | 否 |  |  |
| 12 | other_id | 否 |  |  |
| 13 | csdc_execute_no | 否 |  |  |
| 14 | clear_serial_no | 否 |  |  |
| 15 | net_balance | 否 |  |  |
| 16 | balance_t | 否 |  |  |
| 17 | fare_sx | 否 |  |  |
| 18 | trade_date | 否 |  |  |
| 19 | begin_clear_date | 否 |  |  |
| 20 | csdc_send_date | 否 |  |  |
| 21 | csdc_real_status | 否 |  |  |
| 22 | csdc_by1 | 否 |  |  |
| 23 | csdc_by2 | 否 |  |  |
| 24 | csdc_by3_f | 否 |  |  |
| 25 | branch_no | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | match_status | 否 |  |  |
| 28 | deal_flag | 否 |  |  |
| 29 | position_str | 否 |  | lpad(@clear_serial_no, 16, '0') || lpad(@clear_busi_type, 4, |
| 30 | sub_balance | 否 |  |  |
| 31 | curr_time | 否 |  |  |
| 32 | asset_prop | 否 |  |  |
| 33 | set_seat_no | 否 |  |  |
| 34 | file_type | 否 |  |  |
| 35 | file_kind | 否 |  |  |
| 36 | settle_mark | 否 |  |  |
| 37 | supply_chk_balance | 否 |  |  |
| 38 | revert_serial_no | 否 |  |  |
| 39 | record_type | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | rtgs_settle_way | 否 |  |  |
| 42 | remark | 否 |  |  |
| 43 | client_id | 否 | H |  |
| 44 | client_name | 否 | H |  |
| 45 | corp_client_group | 否 | H |  |
| 46 | client_group | 否 | H |  |
| 47 | room_code | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | client_prop | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_risk_level | 否 | H |  |
| 53 | stock_name | 否 | H |  |
| 54 | stock_type | 否 | H |  |
| 55 | sub_stock_type | 否 | H |  |
| 56 | init_date | 否 |  |  |
| 57 | csdc_order_no | 否 |  |  |
| 58 | exchange_type | 否 |  |  |
| 59 | square_seat | 否 |  |  |
| 60 | csdc_seat_no | 否 |  |  |
| 61 | seat_no | 否 |  |  |
| 62 | stock_account | 否 |  |  |
| 63 | stock_code | 否 |  |  |
| 64 | stock_code2 | 否 |  |  |
| 65 | clear_busi_type | 否 |  |  |
| 66 | order_id | 否 |  |  |
| 67 | other_id | 否 |  |  |
| 68 | csdc_execute_no | 否 |  |  |
| 69 | clear_serial_no | 否 |  |  |
| 70 | net_balance | 否 |  |  |
| 71 | balance_t | 否 |  |  |
| 72 | fare_sx | 否 |  |  |
| 73 | trade_date | 否 |  |  |
| 74 | begin_clear_date | 否 |  |  |
| 75 | csdc_send_date | 否 |  |  |
| 76 | csdc_real_status | 否 |  |  |
| 77 | csdc_by1 | 否 |  |  |
| 78 | csdc_by2 | 否 |  |  |
| 79 | csdc_by3_f | 否 |  |  |
| 80 | branch_no | 否 |  |  |
| 81 | fund_account | 否 |  |  |
| 82 | match_status | 否 |  |  |
| 83 | deal_flag | 否 |  |  |
| 84 | position_str | 否 |  | lpad(@clear_serial_no, 16, '0') || lpad(@clear_busi_type, 4, |
| 85 | sub_balance | 否 |  |  |
| 86 | curr_time | 否 |  |  |
| 87 | asset_prop | 否 |  |  |
| 88 | set_seat_no | 否 |  |  |
| 89 | file_type | 否 |  |  |
| 90 | file_kind | 否 |  |  |
| 91 | settle_mark | 否 |  |  |
| 92 | supply_chk_balance | 否 |  |  |
| 93 | revert_serial_no | 否 |  |  |
| 94 | record_type | 否 |  |  |
| 95 | serial_no | 否 |  |  |
| 96 | rtgs_settle_way | 否 |  |  |
| 97 | remark | 否 |  |  |
| 98 | client_id | 否 | H |  |
| 99 | client_name | 否 | H |  |
| 100 | corp_client_group | 否 | H |  |
| 101 | client_group | 否 | H |  |
| 102 | room_code | 否 | H |  |
| 103 | limit_flag | 否 | H |  |
| 104 | client_prop | 否 | H |  |
| 105 | asset_level | 否 | H |  |
| 106 | risk_level | 否 | H |  |
| 107 | corp_risk_level | 否 | H |  |
| 108 | stock_name | 否 | H |  |
| 109 | stock_type | 否 | H |  |
| 110 | sub_stock_type | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_realdsfmxinfo_no | 默认 | 否 | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | 默认 | 否 | fund_account, clear_serial_no, fund_account, clear_serial_no |
| idx_realdsfmxinfo | 默认 | 是 | position_str, position_str |
| idx_realdsfmxinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | 默认 | 是 | fund_account, clear_serial_no, fund_account, clear_serial_no |
| idx_rpt_realdsfmxinfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_realdsfmxinfo_ac | ART | 是 | fund_account, fund_account |
| idx_realdsfmxinfo_no | 默认 | 否 | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | 默认 | 否 | fund_account, clear_serial_no, fund_account, clear_serial_no |
| idx_realdsfmxinfo | 默认 | 是 | position_str, position_str |
| idx_realdsfmxinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | 默认 | 是 | fund_account, clear_serial_no, fund_account, clear_serial_no |
| idx_rpt_realdsfmxinfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_realdsfmxinfo_ac | ART | 是 | fund_account, fund_account |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_realdsfmxinfo | position_str, position_str |
| idx_realdsfmxinfo_no | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | fund_account, clear_serial_no, fund_account, clear_serial_no |
| idx_realdsfmxinfo | position_str, position_str |
| idx_realdsfmxinfo_no | clear_serial_no, clear_serial_no |
| idx_realdsfmxinfo_stkcode | exchange_type, stock_code, exchange_type, stock_code |
| idx_realdsfmxinfo_acno | fund_account, clear_serial_no, fund_account, clear_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-06 16:50:48 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-07-21 17:34:14 | 3.0.6.88 | 常行 | 物理表real_dsf_mxinfo，增加索引(idx_realdsfmxinfo_no:[clear_serial_n... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2025-11-06 16:50:48 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-07-21 17:34:14 | 3.0.6.88 | 常行 | 物理表real_dsf_mxinfo，增加索引(idx_realdsfmxinfo_no:[clear_serial_n... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

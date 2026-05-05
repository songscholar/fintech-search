# afof_realtime - 基金盘后业务实时成交表

**表对象ID**: 5546
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 122 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | business_flag | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | entrust_amount | 否 |  |  |
| 14 | entrust_balance | 否 |  |  |
| 15 | return_time | 否 |  |  |
| 16 | discount | 否 |  |  |
| 17 | allot_no | 否 |  |  |
| 18 | search_serialno | 否 |  |  |
| 19 | ofdeal_status | 否 |  |  |
| 20 | agency_no | 否 |  |  |
| 21 | join_report_account | 否 |  |  |
| 22 | join_stock_account | 否 |  |  |
| 23 | join_seat_no | 否 |  |  |
| 24 | ta_serialno | 否 |  |  |
| 25 | return_code | 否 |  |  |
| 26 | return_info | 否 |  |  |
| 27 | id_kind | 否 |  |  |
| 28 | id_no | 否 |  |  |
| 29 | original_appno | 否 |  |  |
| 30 | original_serialno | 否 |  |  |
| 31 | trans_code | 否 |  |  |
| 32 | other_agno | 否 |  |  |
| 33 | other_netno | 否 |  |  |
| 34 | other_transaccount | 否 |  |  |
| 35 | other_stkacco | 否 |  |  |
| 36 | component_num | 否 |  |  |
| 37 | component_code_str | 否 |  |  |
| 38 | component_market_str | 否 |  |  |
| 39 | component_amount_str | 否 |  |  |
| 40 | component_balance_str | 否 |  |  |
| 41 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_time(9)+branch_no(5)+seria |
| 42 | hkdc_approve_amount | 否 |  |  |
| 43 | hkdc_oppose_amount | 否 |  |  |
| 44 | hkdc_waive_amount | 否 |  |  |
| 45 | entrust_no | 否 |  |  |
| 46 | hksz_business_type | 否 |  |  |
| 47 | csdc_sellfro_flag | 否 |  |  |
| 48 | branch_no | 否 |  |  |
| 49 | client_name | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | client_group | 否 | H |  |
| 52 | room_code | 否 | H |  |
| 53 | asset_prop | 否 | H |  |
| 54 | limit_flag | 否 | H |  |
| 55 | client_prop | 否 | H |  |
| 56 | asset_level | 否 | H |  |
| 57 | risk_level | 否 | H |  |
| 58 | corp_risk_level | 否 | H |  |
| 59 | stock_name | 否 | H |  |
| 60 | stock_type | 否 | H |  |
| 61 | sub_stock_type | 否 | H |  |
| 62 | init_date | 否 |  |  |
| 63 | serial_no | 否 |  |  |
| 64 | curr_date | 否 |  |  |
| 65 | curr_microtime | 否 |  |  |
| 66 | business_flag | 否 |  |  |
| 67 | fund_account | 否 |  |  |
| 68 | client_id | 否 |  |  |
| 69 | exchange_type | 否 |  |  |
| 70 | stock_account | 否 |  |  |
| 71 | stock_code | 否 |  |  |
| 72 | money_type | 否 |  |  |
| 73 | seat_no | 否 |  |  |
| 74 | entrust_amount | 否 |  |  |
| 75 | entrust_balance | 否 |  |  |
| 76 | return_time | 否 |  |  |
| 77 | discount | 否 |  |  |
| 78 | allot_no | 否 |  |  |
| 79 | search_serialno | 否 |  |  |
| 80 | ofdeal_status | 否 |  |  |
| 81 | agency_no | 否 |  |  |
| 82 | join_report_account | 否 |  |  |
| 83 | join_stock_account | 否 |  |  |
| 84 | join_seat_no | 否 |  |  |
| 85 | ta_serialno | 否 |  |  |
| 86 | return_code | 否 |  |  |
| 87 | return_info | 否 |  |  |
| 88 | id_kind | 否 |  |  |
| 89 | id_no | 否 |  |  |
| 90 | original_appno | 否 |  |  |
| 91 | original_serialno | 否 |  |  |
| 92 | trans_code | 否 |  |  |
| 93 | other_agno | 否 |  |  |
| 94 | other_netno | 否 |  |  |
| 95 | other_transaccount | 否 |  |  |
| 96 | other_stkacco | 否 |  |  |
| 97 | component_num | 否 |  |  |
| 98 | component_code_str | 否 |  |  |
| 99 | component_market_str | 否 |  |  |
| 100 | component_amount_str | 否 |  |  |
| 101 | component_balance_str | 否 |  |  |
| 102 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_time(9)+branch_no(5)+seria |
| 103 | hkdc_approve_amount | 否 |  |  |
| 104 | hkdc_oppose_amount | 否 |  |  |
| 105 | hkdc_waive_amount | 否 |  |  |
| 106 | entrust_no | 否 |  |  |
| 107 | hksz_business_type | 否 |  |  |
| 108 | csdc_sellfro_flag | 否 |  |  |
| 109 | branch_no | 否 |  |  |
| 110 | client_name | 否 | H |  |
| 111 | corp_client_group | 否 | H |  |
| 112 | client_group | 否 | H |  |
| 113 | room_code | 否 | H |  |
| 114 | asset_prop | 否 | H |  |
| 115 | limit_flag | 否 | H |  |
| 116 | client_prop | 否 | H |  |
| 117 | asset_level | 否 | H |  |
| 118 | risk_level | 否 | H |  |
| 119 | corp_risk_level | 否 | H |  |
| 120 | stock_name | 否 | H |  |
| 121 | stock_type | 否 | H |  |
| 122 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_realtime_pos | ART | 是 | position_str, position_str |
| idx_afof_realtime_fund_acct | 默认 | 否 | fund_account, fund_account |
| idx_afof_realtime_pos | 默认 | 否 | position_str, position_str |
| idx_afof_realtime | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_afof_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_afofrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_afofrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_afof_realtime_pos | ART | 是 | position_str, position_str |
| idx_afof_realtime_fund_acct | 默认 | 否 | fund_account, fund_account |
| idx_afof_realtime_pos | 默认 | 否 | position_str, position_str |
| idx_afof_realtime | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_afof_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_afofrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_afofrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_realtime_pos | position_str, position_str |
| idx_afof_realtime_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 15:33:38 | V3.0.2.106 | taocong45644 | 当前表afof_realtime，增加索引（ idx_afof_realtime_pos:[position_str]）... |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-01 20:00:56 | 3.0.2.64 | 张训华 | 调整唯一索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_afof_realtime_pos |
| 2024-12-27 14:28:13 | 3.0.2.33 | 李江霖 | 增加position_str的备注 |
| 2024-10-30 13:53:11 | 3.0.5.1053 | 雷玄 | 物理表afof_realtime，增加索引(idx_afof_realtime_fund_acct:[fund_acco... |
| 2024-08-02 13:15:43 | 3.0.2.32 | 戴英花 | 物理表afof_realtime，添加了表字段(branch_no);
 |
| 2024-07-02 17:10:13 | 3.0.2.27 | 张训华 | 新增表 |
| 2026-03-09 15:33:38 | V3.0.2.106 | taocong45644 | 当前表afof_realtime，增加索引（ idx_afof_realtime_pos:[position_str]）... |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-01 20:00:56 | 3.0.2.64 | 张训华 | 调整唯一索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_afof_realtime_pos |
| 2024-12-27 14:28:13 | 3.0.2.33 | 李江霖 | 增加position_str的备注 |
| 2024-10-30 13:53:11 | 3.0.5.1053 | 雷玄 | 物理表afof_realtime，增加索引(idx_afof_realtime_fund_acct:[fund_acco... |
| 2024-08-02 13:15:43 | 3.0.2.32 | 戴英花 | 物理表afof_realtime，添加了表字段(branch_no);
 |

> 共 16 条修改记录，仅显示最近15条

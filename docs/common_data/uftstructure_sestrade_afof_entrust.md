# afof_entrust - 基金盘后业务委托表

**表对象ID**: 5545
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 156 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | report_account | 否 |  |  |
| 16 | seat_no | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | entrust_amount | 否 |  |  |
| 20 | entrust_balance | 否 |  |  |
| 21 | allot_no | 否 |  |  |
| 22 | business_amount | 否 |  |  |
| 23 | business_balance | 否 |  |  |
| 24 | clear_balance | 否 |  |  |
| 25 | prev_balance | 否 |  |  |
| 26 | entrust_status | 否 |  |  |
| 27 | return_code | 否 |  |  |
| 28 | return_info | 否 |  |  |
| 29 | report_microtime | 否 |  |  |
| 30 | rpt_operator | 否 |  |  |
| 31 | discount | 否 |  |  |
| 32 | id_kind | 否 |  |  |
| 33 | id_no | 否 |  |  |
| 34 | agency_no | 否 |  |  |
| 35 | original_appno | 否 |  |  |
| 36 | original_serialno | 否 |  |  |
| 37 | join_stock_account | 否 |  |  |
| 38 | join_seat_no | 否 |  |  |
| 39 | join_report_account | 否 |  |  |
| 40 | trans_code | 否 |  |  |
| 41 | other_agno | 否 |  |  |
| 42 | other_netno | 否 |  |  |
| 43 | other_transaccount | 否 |  |  |
| 44 | other_stkacco | 否 |  |  |
| 45 | component_num | 否 |  |  |
| 46 | component_code_str | 否 |  |  |
| 47 | component_market_str | 否 |  |  |
| 48 | component_amount_str | 否 |  |  |
| 49 | component_balance_str | 否 |  |  |
| 50 | search_serialno | 否 |  |  |
| 51 | search_flag | 否 |  |  |
| 52 | send_count | 否 |  |  |
| 53 | fare | 否 |  |  |
| 54 | cancel_serial_no | 否 |  |  |
| 55 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_milltime(9)+branch_no(5)+s |
| 56 | hksz_business_type | 否 |  |  |
| 57 | entrust_type | 否 |  |  |
| 58 | csdc_sellfro_flag | 否 |  |  |
| 59 | ext_order_id | 否 |  |  |
| 60 | sub_stock_type | 否 |  |  |
| 61 | enable_polling | 否 |  |  |
| 62 | aecn_number | 否 |  |  |
| 63 | pending_number | 否 |  |  |
| 64 | orig_judifrozen_id | 否 |  |  |
| 65 | principal | 否 |  |  |
| 66 | dividend | 否 |  |  |
| 67 | client_name | 否 | H |  |
| 68 | corp_client_group | 否 | H |  |
| 69 | client_group | 否 | H |  |
| 70 | room_code | 否 | H |  |
| 71 | asset_prop | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | client_prop | 否 | H |  |
| 74 | asset_level | 否 | H |  |
| 75 | risk_level | 否 | H |  |
| 76 | corp_risk_level | 否 | H |  |
| 77 | stock_name | 否 | H |  |
| 78 | stock_type | 否 | H |  |
| 79 | init_date | 否 |  |  |
| 80 | entrust_no | 否 |  |  |
| 81 | curr_date | 否 |  |  |
| 82 | curr_microtime | 否 |  |  |
| 83 | op_branch_no | 否 |  |  |
| 84 | operator_no | 否 |  |  |
| 85 | op_entrust_way | 否 |  |  |
| 86 | op_station | 否 |  |  |
| 87 | business_flag | 否 |  |  |
| 88 | branch_no | 否 |  |  |
| 89 | fund_account | 否 |  |  |
| 90 | client_id | 否 |  |  |
| 91 | exchange_type | 否 |  |  |
| 92 | stock_account | 否 |  |  |
| 93 | report_account | 否 |  |  |
| 94 | seat_no | 否 |  |  |
| 95 | stock_code | 否 |  |  |
| 96 | money_type | 否 |  |  |
| 97 | entrust_amount | 否 |  |  |
| 98 | entrust_balance | 否 |  |  |
| 99 | allot_no | 否 |  |  |
| 100 | business_amount | 否 |  |  |
| 101 | business_balance | 否 |  |  |
| 102 | clear_balance | 否 |  |  |
| 103 | prev_balance | 否 |  |  |
| 104 | entrust_status | 否 |  |  |
| 105 | return_code | 否 |  |  |
| 106 | return_info | 否 |  |  |
| 107 | report_microtime | 否 |  |  |
| 108 | rpt_operator | 否 |  |  |
| 109 | discount | 否 |  |  |
| 110 | id_kind | 否 |  |  |
| 111 | id_no | 否 |  |  |
| 112 | agency_no | 否 |  |  |
| 113 | original_appno | 否 |  |  |
| 114 | original_serialno | 否 |  |  |
| 115 | join_stock_account | 否 |  |  |
| 116 | join_seat_no | 否 |  |  |
| 117 | join_report_account | 否 |  |  |
| 118 | trans_code | 否 |  |  |
| 119 | other_agno | 否 |  |  |
| 120 | other_netno | 否 |  |  |
| 121 | other_transaccount | 否 |  |  |
| 122 | other_stkacco | 否 |  |  |
| 123 | component_num | 否 |  |  |
| 124 | component_code_str | 否 |  |  |
| 125 | component_market_str | 否 |  |  |
| 126 | component_amount_str | 否 |  |  |
| 127 | component_balance_str | 否 |  |  |
| 128 | search_serialno | 否 |  |  |
| 129 | search_flag | 否 |  |  |
| 130 | send_count | 否 |  |  |
| 131 | fare | 否 |  |  |
| 132 | cancel_serial_no | 否 |  |  |
| 133 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_milltime(9)+branch_no(5)+s |
| 134 | hksz_business_type | 否 |  |  |
| 135 | entrust_type | 否 |  |  |
| 136 | csdc_sellfro_flag | 否 |  |  |
| 137 | ext_order_id | 否 |  |  |
| 138 | sub_stock_type | 否 |  |  |
| 139 | enable_polling | 否 |  |  |
| 140 | aecn_number | 否 |  |  |
| 141 | pending_number | 否 |  |  |
| 142 | orig_judifrozen_id | 否 |  |  |
| 143 | principal | 否 |  |  |
| 144 | dividend | 否 |  |  |
| 145 | client_name | 否 | H |  |
| 146 | corp_client_group | 否 | H |  |
| 147 | client_group | 否 | H |  |
| 148 | room_code | 否 | H |  |
| 149 | asset_prop | 否 | H |  |
| 150 | limit_flag | 否 | H |  |
| 151 | client_prop | 否 | H |  |
| 152 | asset_level | 否 | H |  |
| 153 | risk_level | 否 | H |  |
| 154 | corp_risk_level | 否 | H |  |
| 155 | stock_name | 否 | H |  |
| 156 | stock_type | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_entrust_pos | ART | 是 | position_str, position_str |
| idx_afof_entrust_pos | 默认 | 否 | position_str, position_str |
| idx_afof_entrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| idx_afof_entrust_allot | ART | 是 | allot_no, allot_no |
| idx_afof_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| idx_afof_entrust_pos | ART | 是 | position_str, position_str |
| uk_rpt_afofentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_afofentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_afof_entrust_pos | ART | 是 | position_str, position_str |
| idx_afof_entrust_pos | 默认 | 否 | position_str, position_str |
| idx_afof_entrust | ART | 是 | init_date, branch_no, entrust_no, init_date, branch_no, entrust_no |
| idx_afof_entrust_allot | ART | 是 | allot_no, allot_no |
| idx_afof_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| idx_afof_entrust_pos | ART | 是 | position_str, position_str |
| uk_rpt_afofentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_afofentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_entrust_pos | position_str, position_str |
| idx_afof_entrust_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 15:32:19 | V3.0.2.106 | taocong45644 | 当前表afof_entrust，增加索引（ idx_afof_entrust_pos:[position_str]）;... |
| 2026-01-21 16:00:52 | V3.0.8.33 | 刘大为 | 所有表afof_entrust，添加了表字段(aecn_number);
所有表afof_entrust，添加了表字段... |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-01 20:00:56 | 3.0.2.64 | 张训华 | 调整唯一索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_afof_entrust_pos |
| 2025-01-23 10:43:26 | 3.0.2.58 | 钟兆星 | 增加fund_account索引 |
| 2024-12-27 14:28:13 | 3.0.2.30 | 李江霖 | 增加position_str的备注 |
| 2024-07-25 13:14:00 | 3.0.2.29 | 王锦汇 | 物理表afof_entrust，添加了表字段(enable_polling);
 |
| 2024-07-25 10:50:43 | 3.0.2.29 | 王锦汇 | 物理表afof_entrust，添加了表字段(branch_no);
 |
| 2024-07-06 11:13:10 | 3.0.2.28 | 张训华 | cancel_serialno字段改成cancel_serial_no字段 |
| 2024-06-28 19:46:43 | 3.0.2.22 | 张训华 | 新增表,物理表增加索引 |
| 2026-03-09 15:32:19 | V3.0.2.106 | taocong45644 | 当前表afof_entrust，增加索引（ idx_afof_entrust_pos:[position_str]）;... |
| 2026-01-21 16:00:52 | V3.0.8.33 | 刘大为 | 所有表afof_entrust，添加了表字段(aecn_number);
所有表afof_entrust，添加了表字段... |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-01 20:00:56 | 3.0.2.64 | 张训华 | 调整唯一索引 |

> 共 22 条修改记录，仅显示最近15条

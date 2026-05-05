# cbs_entrust - 港股委托表

**表对象ID**: 5548
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 162 个）

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
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | report_account | 否 |  |  |
| 16 | seat_no | 否 |  |  |
| 17 | entrust_prop | 否 |  |  |
| 18 | entrust_type | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | entrust_amount | 否 |  |  |
| 21 | entrust_balance | 否 |  |  |
| 22 | prev_balance | 否 |  |  |
| 23 | entrust_status | 否 |  |  |
| 24 | report_microtime | 否 |  |  |
| 25 | report_no | 否 |  |  |
| 26 | record_no | 否 |  |  |
| 27 | store_unit | 否 |  |  |
| 28 | report_unit | 否 |  |  |
| 29 | report_bs | 否 |  |  |
| 30 | join_report_no | 否 |  |  |
| 31 | cbpcontract_id | 否 |  |  |
| 32 | prop_seat_no | 否 |  |  |
| 33 | business_id | 否 |  |  |
| 34 | stock_type | 否 |  |  |
| 35 | business_microtime | 否 |  |  |
| 36 | return_code | 否 |  |  |
| 37 | date_clear | 否 |  |  |
| 38 | cancel_serial_no | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | position_str | 否 |  | curr_date(8)+curr_time(9)+init_date(8)+entrust_no(10)+branch |
| 41 | entrust_price | 否 |  |  |
| 42 | relation_name | 否 |  |  |
| 43 | relation_tel | 否 |  |  |
| 44 | business_amount | 否 |  |  |
| 45 | business_balance | 否 |  |  |
| 46 | withdraw_amount | 否 |  |  |
| 47 | clear_balance | 否 |  |  |
| 48 | report_code | 否 |  |  |
| 49 | firm_id | 否 |  |  |
| 50 | fare_kind | 否 |  |  |
| 51 | room_code | 否 |  |  |
| 52 | cbpconfer_id | 否 |  |  |
| 53 | max_price_levels | 否 |  |  |
| 54 | trade_time_type | 否 |  |  |
| 55 | exchange_rate | 否 |  |  |
| 56 | entrust_reference | 否 |  |  |
| 57 | sub_stock_type | 否 |  |  |
| 58 | batch_no | 否 |  |  |
| 59 | return_info | 否 |  |  |
| 60 | extend_field | 否 |  |  |
| 61 | dispart_fare_str | 否 |  |  |
| 62 | dispart_svr_fare | 否 |  |  |
| 63 | order_id | 否 |  |  |
| 64 | orig_order_id | 否 |  |  |
| 65 | enable_polling | 否 |  |  |
| 66 | prop_branch_no | 否 |  |  |
| 67 | prop_stock_account | 否 |  |  |
| 68 | orig_business_id | 否 |  |  |
| 69 | back_balance | 否 |  |  |
| 70 | date_back | 否 |  |  |
| 71 | login_pbu | 否 |  |  |
| 72 | client_name | 否 | H |  |
| 73 | corp_client_group | 否 | H |  |
| 74 | client_group | 否 | H |  |
| 75 | asset_prop | 否 | H |  |
| 76 | limit_flag | 否 | H |  |
| 77 | client_prop | 否 | H |  |
| 78 | asset_level | 否 | H |  |
| 79 | risk_level | 否 | H |  |
| 80 | corp_risk_level | 否 | H |  |
| 81 | stock_name | 否 | H |  |
| 82 | init_date | 否 |  |  |
| 83 | entrust_no | 否 |  |  |
| 84 | curr_date | 否 |  |  |
| 85 | curr_microtime | 否 |  |  |
| 86 | op_branch_no | 否 |  |  |
| 87 | operator_no | 否 |  |  |
| 88 | op_entrust_way | 否 |  |  |
| 89 | op_station | 否 |  |  |
| 90 | branch_no | 否 |  |  |
| 91 | fund_account | 否 |  |  |
| 92 | client_id | 否 |  |  |
| 93 | exchange_type | 否 |  |  |
| 94 | stock_code | 否 |  |  |
| 95 | stock_account | 否 |  |  |
| 96 | report_account | 否 |  |  |
| 97 | seat_no | 否 |  |  |
| 98 | entrust_prop | 否 |  |  |
| 99 | entrust_type | 否 |  |  |
| 100 | entrust_bs | 否 |  |  |
| 101 | entrust_amount | 否 |  |  |
| 102 | entrust_balance | 否 |  |  |
| 103 | prev_balance | 否 |  |  |
| 104 | entrust_status | 否 |  |  |
| 105 | report_microtime | 否 |  |  |
| 106 | report_no | 否 |  |  |
| 107 | record_no | 否 |  |  |
| 108 | store_unit | 否 |  |  |
| 109 | report_unit | 否 |  |  |
| 110 | report_bs | 否 |  |  |
| 111 | join_report_no | 否 |  |  |
| 112 | cbpcontract_id | 否 |  |  |
| 113 | prop_seat_no | 否 |  |  |
| 114 | business_id | 否 |  |  |
| 115 | stock_type | 否 |  |  |
| 116 | business_microtime | 否 |  |  |
| 117 | return_code | 否 |  |  |
| 118 | date_clear | 否 |  |  |
| 119 | cancel_serial_no | 否 |  |  |
| 120 | remark | 否 |  |  |
| 121 | position_str | 否 |  | curr_date(8)+curr_time(9)+init_date(8)+entrust_no(10)+branch |
| 122 | entrust_price | 否 |  |  |
| 123 | relation_name | 否 |  |  |
| 124 | relation_tel | 否 |  |  |
| 125 | business_amount | 否 |  |  |
| 126 | business_balance | 否 |  |  |
| 127 | withdraw_amount | 否 |  |  |
| 128 | clear_balance | 否 |  |  |
| 129 | report_code | 否 |  |  |
| 130 | firm_id | 否 |  |  |
| 131 | fare_kind | 否 |  |  |
| 132 | room_code | 否 |  |  |
| 133 | cbpconfer_id | 否 |  |  |
| 134 | max_price_levels | 否 |  |  |
| 135 | trade_time_type | 否 |  |  |
| 136 | exchange_rate | 否 |  |  |
| 137 | entrust_reference | 否 |  |  |
| 138 | sub_stock_type | 否 |  |  |
| 139 | batch_no | 否 |  |  |
| 140 | return_info | 否 |  |  |
| 141 | extend_field | 否 |  |  |
| 142 | dispart_fare_str | 否 |  |  |
| 143 | dispart_svr_fare | 否 |  |  |
| 144 | order_id | 否 |  |  |
| 145 | orig_order_id | 否 |  |  |
| 146 | enable_polling | 否 |  |  |
| 147 | prop_branch_no | 否 |  |  |
| 148 | prop_stock_account | 否 |  |  |
| 149 | orig_business_id | 否 |  |  |
| 150 | back_balance | 否 |  |  |
| 151 | date_back | 否 |  |  |
| 152 | login_pbu | 否 |  |  |
| 153 | client_name | 否 | H |  |
| 154 | corp_client_group | 否 | H |  |
| 155 | client_group | 否 | H |  |
| 156 | asset_prop | 否 | H |  |
| 157 | limit_flag | 否 | H |  |
| 158 | client_prop | 否 | H |  |
| 159 | asset_level | 否 | H |  |
| 160 | risk_level | 否 | H |  |
| 161 | corp_risk_level | 否 | H |  |
| 162 | stock_name | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbs_entrust | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_cbs_entrust_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_cbs_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| idx_cbs_entrust_id | ART | 是 | client_id, client_id |
| idx_cbs_entrust_status | ART | 是 | entrust_status, entrust_status |
| idx_cbs_entrust_stk | ART | 是 | stock_account, stock_account |
| uk_rpt_cbsentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_cbsentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_cbs_entrust | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_cbs_entrust_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_cbs_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| idx_cbs_entrust_id | ART | 是 | client_id, client_id |
| idx_cbs_entrust_status | ART | 是 | entrust_status, entrust_status |
| idx_cbs_entrust_stk | ART | 是 | stock_account, stock_account |
| uk_rpt_cbsentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_cbsentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbs_entrust | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_cbs_entrust | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:02:09 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:16:33 | 3.0.2.71 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-18 17:09:50 | 3.0.6.1004 | 范文浩 | 调整索引顺序，idx_cbs_entrust_acct新增索引字段position_str |
| 2025-06-06 13:31:01 | 3.0.2.70 | 董乾坤 | 物理表cbs_entrust，添加了表字段(login_pbu);
 |
| 2025-01-23 17:33:30 | 3.0.2.59 | 钟兆星 | 删除idx_cbs_entrust_pos索引(position_str) |
| 2024-12-27 14:28:13 | 3.0.2.56 | 李江霖 | 增加position_str的备注 |
| 2025-01-06 14:11:57 | 3.0.2.55 | 雷玄 | 物理表cbs_entrust，添加了表字段(prop_branch_no);
物理表cbs_entrust，添加了表字... |
| 2024-07-25 14:03:01 | 3.0.2.30 | 乐闽庭 | 内存表增加索引idx_cbs_entrust_polling |
| 2024-07-24 13:53:32 | 3.0.2.30 | 乐闽庭 | 物理表cbs_entrust，添加了表字段(curr_microtime);
物理表cbs_entrust，添加了表字... |
| 2024-07-24 13:52:03 | 3.0.2.30 | 乐闽庭 | 物理表cbs_entrust，删除了表字段(curr_time);
物理表cbs_entrust，删除了表字段(bac... |
| 2024-06-27 11:28:29 | 3.0.2.22 | 董乾坤 | 新增 |
| 2026-03-09 14:02:09 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:16:33 | 3.0.2.71 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |

> 共 24 条修改记录，仅显示最近15条

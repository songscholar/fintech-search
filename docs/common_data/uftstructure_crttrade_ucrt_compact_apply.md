# ucrt_compact_apply - 合约展期申请表

**表对象ID**: 7526
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

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
| 12 | market_value | 否 |  |  |
| 13 | total_debit | 否 |  |  |
| 14 | per_assurescale_value | 否 |  |  |
| 15 | compact_apply_status | 否 |  |  |
| 16 | compact_postpone_term | 否 |  |  |
| 17 | autoaudit_flag | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | market_value_begin | 否 |  |  |
| 21 | autoaudit_fail_reason | 否 |  |  |
| 22 | op_station | 否 |  |  |
| 23 | real_compact_balance | 否 |  |  |
| 24 | real_compact_fare | 否 |  |  |
| 25 | per_assurescale_value_out | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 27 | risk_remind_info | 是 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | stock_name | 否 | H |  |
| 30 | sub_stock_type | 否 | H |  |
| 31 | stock_type | 否 | H |  |
| 32 | client_group | 否 | H |  |
| 33 | room_code | 否 | H |  |
| 34 | asset_prop | 否 | H |  |
| 35 | limit_flag | 否 | H |  |
| 36 | risk_level | 否 | H |  |
| 37 | corp_client_group | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |
| 39 | asset_level | 否 | H |  |
| 40 | client_name | 否 | H |  |
| 41 | client_prop | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | curr_time | 否 |  |  |
| 45 | serial_no | 否 |  |  |
| 46 | compact_id | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | fund_account | 否 |  |  |
| 49 | stock_account | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | cash_asset | 否 |  |  |
| 53 | market_value | 否 |  |  |
| 54 | total_debit | 否 |  |  |
| 55 | per_assurescale_value | 否 |  |  |
| 56 | compact_apply_status | 否 |  |  |
| 57 | compact_postpone_term | 否 |  |  |
| 58 | autoaudit_flag | 否 |  |  |
| 59 | date_clear | 否 |  |  |
| 60 | remark | 否 |  |  |
| 61 | market_value_begin | 否 |  |  |
| 62 | autoaudit_fail_reason | 否 |  |  |
| 63 | op_station | 否 |  |  |
| 64 | real_compact_balance | 否 |  |  |
| 65 | real_compact_fare | 否 |  |  |
| 66 | per_assurescale_value_out | 否 |  |  |
| 67 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 68 | risk_remind_info | 是 |  |  |
| 69 | branch_no | 否 |  |  |
| 70 | stock_name | 否 | H |  |
| 71 | sub_stock_type | 否 | H |  |
| 72 | stock_type | 否 | H |  |
| 73 | client_group | 否 | H |  |
| 74 | room_code | 否 | H |  |
| 75 | asset_prop | 否 | H |  |
| 76 | limit_flag | 否 | H |  |
| 77 | risk_level | 否 | H |  |
| 78 | corp_client_group | 否 | H |  |
| 79 | corp_risk_level | 否 | H |  |
| 80 | asset_level | 否 | H |  |
| 81 | client_name | 否 | H |  |
| 82 | client_prop | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_apply_unique | 默认 | 否 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_ucrt_compact_apply | 默认 | 否 | stock_account, exchange_type, stock_account, exchange_type |
| idx_ucrt_compact_apply | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_ucrt_compact_apply | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_apply_compact_id | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_compact_apply_unique | ART | 是 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| uk_rpt_ucrtcompactapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtcompactapply_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_compact_apply_unique | 默认 | 否 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_ucrt_compact_apply | 默认 | 否 | stock_account, exchange_type, stock_account, exchange_type |
| idx_ucrt_compact_apply | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_ucrt_compact_apply | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_apply_compact_id | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_compact_apply_unique | ART | 是 | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| uk_rpt_ucrtcompactapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtcompactapply_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_apply | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_apply | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-04 13:35:22 | 3.0.6.1067 | 牟家乐 | 所有表ucrt_compact_apply，添加了表字段(risk_remind_info);
 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-21 14:37:52 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_compact_apply，添加了表字段(branch_no);
物理表ucrt_compact_ap... |
| 2023-10-26 11:12:34 | V3.0.1.12 | 沈勋 | 增加索引(idx_ucrt_compact_apply_unique:[init_date,serial_no,fund... |
| 2023-09-18 09:34:07 | V3.0.1.3 | 吴威 | 物理表ucrt_compact_apply，删除索引字段(索引idx_ucrt_compact_apply:删除了索引字... |
| 2023-09-18 09:33:38 | V3.0.1.3 | 吴威 | 物理表ucrt_compact_apply，增加索引字段(索引idx_ucrt_compact_apply:增加了索引字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-04 13:35:22 | 3.0.6.1067 | 牟家乐 | 所有表ucrt_compact_apply，添加了表字段(risk_remind_info);
 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-21 14:37:52 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_compact_apply，添加了表字段(branch_no);
物理表ucrt_compact_ap... |
| 2023-10-26 11:12:34 | V3.0.1.12 | 沈勋 | 增加索引(idx_ucrt_compact_apply_unique:[init_date,serial_no,fund... |
| 2023-09-18 09:34:07 | V3.0.1.3 | 吴威 | 物理表ucrt_compact_apply，删除索引字段(索引idx_ucrt_compact_apply:删除了索引字... |
| 2023-09-18 09:33:38 | V3.0.1.3 | 吴威 | 物理表ucrt_compact_apply，增加索引字段(索引idx_ucrt_compact_apply:增加了索引字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# ucrt_compact_real_jour - 合约实时流水表

**表对象ID**: 7518
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | compact_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | compact_type | 否 |  |  |
| 18 | business_flag | 否 |  |  |
| 19 | occur_balance | 否 |  |  |
| 20 | post_balance | 否 |  |  |
| 21 | occur_amount | 否 |  |  |
| 22 | post_amount | 否 |  |  |
| 23 | occur_fare | 否 |  |  |
| 24 | post_fare | 否 |  |  |
| 25 | occur_interest | 否 |  |  |
| 26 | post_interest | 否 |  |  |
| 27 | occur_frozen_interest | 否 |  |  |
| 28 | post_frozen_interest | 否 |  |  |
| 29 | entrust_no | 否 |  |  |
| 30 | remark | 否 |  |  |
| 31 | cancel_serial_no | 否 |  |  |
| 32 | occur_repaycost_balance | 否 |  |  |
| 33 | post_repaycost_balance | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 36 | client_group | 否 | H |  |
| 37 | room_code | 否 | H |  |
| 38 | asset_prop | 否 | H |  |
| 39 | limit_flag | 否 | H |  |
| 40 | risk_level | 否 | H |  |
| 41 | corp_client_group | 否 | H |  |
| 42 | corp_risk_level | 否 | H |  |
| 43 | asset_level | 否 | H |  |
| 44 | client_name | 否 | H |  |
| 45 | stock_name | 否 | H |  |
| 46 | client_prop | 否 | H |  |
| 47 | sub_stock_type | 否 | H |  |
| 48 | init_date | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | curr_date | 否 |  |  |
| 51 | curr_microtime | 否 |  |  |
| 52 | operator_no | 否 |  |  |
| 53 | op_branch_no | 否 |  |  |
| 54 | op_entrust_way | 否 |  |  |
| 55 | op_station | 否 |  |  |
| 56 | compact_id | 否 |  |  |
| 57 | fund_account | 否 |  |  |
| 58 | client_id | 否 |  |  |
| 59 | stock_account | 否 |  |  |
| 60 | exchange_type | 否 |  |  |
| 61 | stock_code | 否 |  |  |
| 62 | stock_type | 否 |  |  |
| 63 | money_type | 否 |  |  |
| 64 | compact_type | 否 |  |  |
| 65 | business_flag | 否 |  |  |
| 66 | occur_balance | 否 |  |  |
| 67 | post_balance | 否 |  |  |
| 68 | occur_amount | 否 |  |  |
| 69 | post_amount | 否 |  |  |
| 70 | occur_fare | 否 |  |  |
| 71 | post_fare | 否 |  |  |
| 72 | occur_interest | 否 |  |  |
| 73 | post_interest | 否 |  |  |
| 74 | occur_frozen_interest | 否 |  |  |
| 75 | post_frozen_interest | 否 |  |  |
| 76 | entrust_no | 否 |  |  |
| 77 | remark | 否 |  |  |
| 78 | cancel_serial_no | 否 |  |  |
| 79 | occur_repaycost_balance | 否 |  |  |
| 80 | post_repaycost_balance | 否 |  |  |
| 81 | branch_no | 否 |  |  |
| 82 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 83 | client_group | 否 | H |  |
| 84 | room_code | 否 | H |  |
| 85 | asset_prop | 否 | H |  |
| 86 | limit_flag | 否 | H |  |
| 87 | risk_level | 否 | H |  |
| 88 | corp_client_group | 否 | H |  |
| 89 | corp_risk_level | 否 | H |  |
| 90 | asset_level | 否 | H |  |
| 91 | client_name | 否 | H |  |
| 92 | stock_name | 否 | H |  |
| 93 | client_prop | 否 | H |  |
| 94 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_real_jour_no | ART | 是 | fund_account, compact_id, init_date, serial_no, fund_account, compact_id, init_date, serial_no |
| idx_ucrt_compact_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtcompactrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_compact_real_jour_no | ART | 是 | fund_account, compact_id, init_date, serial_no, fund_account, compact_id, init_date, serial_no |
| idx_ucrt_compact_real_jour | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ucrtcompactrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtcompactrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_compact_real_jour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-21 14:23:02 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_compact_real_jour，添加了表字段(branch_no);
物理表ucrt_compac... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-21 14:23:02 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_compact_real_jour，添加了表字段(branch_no);
物理表ucrt_compac... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

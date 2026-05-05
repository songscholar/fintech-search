# cbs_realtime - 港股成交表

**表对象ID**: 5562
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 88 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | entrust_prop | 否 |  |  |
| 13 | entrust_price | 否 |  |  |
| 14 | entrust_amount | 否 |  |  |
| 15 | entrust_balance | 否 |  |  |
| 16 | business_balance | 否 |  |  |
| 17 | business_amount | 否 |  |  |
| 18 | business_price | 否 |  |  |
| 19 | business_microtime | 否 |  |  |
| 20 | seat_no | 否 |  |  |
| 21 | entrust_no | 否 |  |  |
| 22 | business_id | 否 |  |  |
| 23 | prop_seat_no | 否 |  |  |
| 24 | cancel_serial_no | 否 |  |  |
| 25 | return_code | 否 |  |  |
| 26 | return_info | 否 |  |  |
| 27 | real_type | 否 |  |  |
| 28 | real_status | 否 |  |  |
| 29 | remark | 否 |  |  |
| 30 | position_str | 否 |  | curr_date(8)+curr_milltime(9)+branch_no(5)+serial_no(10) |
| 31 | clear_balance | 否 |  |  |
| 32 | client_name | 否 | H |  |
| 33 | corp_client_group | 否 | H |  |
| 34 | client_group | 否 | H |  |
| 35 | room_code | 否 | H |  |
| 36 | asset_prop | 否 | H |  |
| 37 | limit_flag | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | asset_level | 否 | H |  |
| 40 | risk_level | 否 | H |  |
| 41 | corp_risk_level | 否 | H |  |
| 42 | stock_type | 否 | H |  |
| 43 | stock_name | 否 | H |  |
| 44 | sub_stock_type | 否 | H |  |
| 45 | init_date | 否 |  |  |
| 46 | serial_no | 否 |  |  |
| 47 | curr_date | 否 |  |  |
| 48 | curr_microtime | 否 |  |  |
| 49 | branch_no | 否 |  |  |
| 50 | fund_account | 否 |  |  |
| 51 | client_id | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | stock_account | 否 |  |  |
| 54 | stock_code | 否 |  |  |
| 55 | entrust_bs | 否 |  |  |
| 56 | entrust_prop | 否 |  |  |
| 57 | entrust_price | 否 |  |  |
| 58 | entrust_amount | 否 |  |  |
| 59 | entrust_balance | 否 |  |  |
| 60 | business_balance | 否 |  |  |
| 61 | business_amount | 否 |  |  |
| 62 | business_price | 否 |  |  |
| 63 | business_microtime | 否 |  |  |
| 64 | seat_no | 否 |  |  |
| 65 | entrust_no | 否 |  |  |
| 66 | business_id | 否 |  |  |
| 67 | prop_seat_no | 否 |  |  |
| 68 | cancel_serial_no | 否 |  |  |
| 69 | return_code | 否 |  |  |
| 70 | return_info | 否 |  |  |
| 71 | real_type | 否 |  |  |
| 72 | real_status | 否 |  |  |
| 73 | remark | 否 |  |  |
| 74 | position_str | 否 |  | curr_date(8)+curr_milltime(9)+branch_no(5)+serial_no(10) |
| 75 | clear_balance | 否 |  |  |
| 76 | client_name | 否 | H |  |
| 77 | corp_client_group | 否 | H |  |
| 78 | client_group | 否 | H |  |
| 79 | room_code | 否 | H |  |
| 80 | asset_prop | 否 | H |  |
| 81 | limit_flag | 否 | H |  |
| 82 | client_prop | 否 | H |  |
| 83 | asset_level | 否 | H |  |
| 84 | risk_level | 否 | H |  |
| 85 | corp_risk_level | 否 | H |  |
| 86 | stock_type | 否 | H |  |
| 87 | stock_name | 否 | H |  |
| 88 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cbs_realtime | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_cbs_realtime_busid | ART | 是 | business_id, entrust_no, branch_no, business_id, entrust_no, branch_no |
| idx_cbs_realtime_acct | ART | 是 | fund_account, fund_account |
| idx_cbs_realtime_id | ART | 是 | client_id, client_id |
| idx_cbs_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_cbsrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_cbsrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_cbs_realtime | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_cbs_realtime_busid | ART | 是 | business_id, entrust_no, branch_no, business_id, entrust_no, branch_no |
| idx_cbs_realtime_acct | ART | 是 | fund_account, fund_account |
| idx_cbs_realtime_id | ART | 是 | client_id, client_id |
| idx_cbs_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_cbsrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_cbsrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cbs_realtime | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_cbs_realtime | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:11:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:17:51 | 3.0.2.31 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.31 | 李江霖 | 增加position_str的备注 |
| 2024-07-24 15:21:32 | 3.0.2.30 | 乐闽庭 | 新增表 |
| 2026-03-09 14:11:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:17:51 | 3.0.2.31 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.31 | 李江霖 | 增加position_str的备注 |
| 2024-07-24 15:21:32 | 3.0.2.30 | 乐闽庭 | 新增表 |

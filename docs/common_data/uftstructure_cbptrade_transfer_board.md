# transfer_board - 份额转让信息表

**表对象ID**: 2543
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | entrust_price | 否 |  |  |
| 14 | entrust_amount | 否 |  |  |
| 15 | confirm_amount | 否 |  |  |
| 16 | recall_amount | 否 |  |  |
| 17 | pre_frozen_balance | 否 |  |  |
| 18 | confirm_balance | 否 |  |  |
| 19 | recall_balance | 否 |  |  |
| 20 | transfer_status | 否 |  |  |
| 21 | relation_name | 否 |  |  |
| 22 | relation_tel | 否 |  |  |
| 23 | report_id | 否 |  |  |
| 24 | transfer_prop | 否 |  |  |
| 25 | message_notes | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | op_station | 否 |  |  |
| 28 | op_entrust_way | 否 |  |  |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | client_group | 否 | H |  |
| 32 | room_code | 否 | H |  |
| 33 | asset_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |
| 39 | stock_name | 否 | H |  |
| 40 | stock_type | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | serial_no | 否 |  |  |
| 44 | curr_date | 否 |  |  |
| 45 | curr_time | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | branch_no | 否 |  |  |
| 49 | exchange_type | 否 |  |  |
| 50 | stock_account | 否 |  |  |
| 51 | seat_no | 否 |  |  |
| 52 | entrust_bs | 否 |  |  |
| 53 | stock_code | 否 |  |  |
| 54 | entrust_price | 否 |  |  |
| 55 | entrust_amount | 否 |  |  |
| 56 | confirm_amount | 否 |  |  |
| 57 | recall_amount | 否 |  |  |
| 58 | pre_frozen_balance | 否 |  |  |
| 59 | confirm_balance | 否 |  |  |
| 60 | recall_balance | 否 |  |  |
| 61 | transfer_status | 否 |  |  |
| 62 | relation_name | 否 |  |  |
| 63 | relation_tel | 否 |  |  |
| 64 | report_id | 否 |  |  |
| 65 | transfer_prop | 否 |  |  |
| 66 | message_notes | 否 |  |  |
| 67 | position_str | 否 |  |  |
| 68 | op_station | 否 |  |  |
| 69 | op_entrust_way | 否 |  |  |
| 70 | client_name | 否 | H |  |
| 71 | corp_client_group | 否 | H |  |
| 72 | client_group | 否 | H |  |
| 73 | room_code | 否 | H |  |
| 74 | asset_prop | 否 | H |  |
| 75 | limit_flag | 否 | H |  |
| 76 | client_prop | 否 | H |  |
| 77 | asset_level | 否 | H |  |
| 78 | risk_level | 否 | H |  |
| 79 | corp_risk_level | 否 | H |  |
| 80 | stock_name | 否 | H |  |
| 81 | stock_type | 否 | H |  |
| 82 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_transfer_board | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_transfer_board_report | ART | 是 | report_id, transfer_prop, report_id, transfer_prop |
| uk_rpt_transferboard | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_transferboard_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_transfer_board | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_transfer_board_report | ART | 是 | report_id, transfer_prop, report_id, transfer_prop |
| uk_rpt_transferboard | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_transferboard_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_transfer_board | serial_no, init_date, serial_no, init_date |
| idx_transfer_board | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:26:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-09 14:49:10 | V3.0.2.19 | 董乾坤 | 新增 |
| 2026-03-04 16:26:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-09 14:49:10 | V3.0.2.19 | 董乾坤 | 新增 |

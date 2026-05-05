# uref_trade_query - 转融通交易联机查询表

**表对象ID**: 6109
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_milltime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | report_no | 否 |  |  |
| 6 | orig_report_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | entrust_balance | 否 |  |  |
| 14 | ref_term | 否 |  |  |
| 15 | refbase_rate | 否 |  |  |
| 16 | report_amount | 否 |  |  |
| 17 | orig_refbusi_code | 否 |  |  |
| 18 | refbusi_code | 否 |  |  |
| 19 | oppo_stkaccount | 否 |  |  |
| 20 | oppo_seatno | 否 |  |  |
| 21 | cbpconfer_id | 否 |  |  |
| 22 | csfc_compact_id | 否 |  |  |
| 23 | oppcsfc_compact_id | 否 |  |  |
| 24 | csfc_report_status | 否 |  |  |
| 25 | deal_time | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | stock_name | 否 | H |  |
| 28 | stock_type | 否 | H |  |
| 29 | sub_stock_type | 否 | H |  |
| 30 | client_group | 否 | H |  |
| 31 | room_code | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | client_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | branch_no | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | curr_date | 否 |  |  |
| 38 | curr_milltime | 否 |  |  |
| 39 | serial_no | 否 |  |  |
| 40 | report_no | 否 |  |  |
| 41 | orig_report_no | 否 |  |  |
| 42 | fund_account | 否 |  |  |
| 43 | exchange_type | 否 |  |  |
| 44 | money_type | 否 |  |  |
| 45 | stock_account | 否 |  |  |
| 46 | seat_no | 否 |  |  |
| 47 | stock_code | 否 |  |  |
| 48 | entrust_balance | 否 |  |  |
| 49 | ref_term | 否 |  |  |
| 50 | refbase_rate | 否 |  |  |
| 51 | report_amount | 否 |  |  |
| 52 | orig_refbusi_code | 否 |  |  |
| 53 | refbusi_code | 否 |  |  |
| 54 | oppo_stkaccount | 否 |  |  |
| 55 | oppo_seatno | 否 |  |  |
| 56 | cbpconfer_id | 否 |  |  |
| 57 | csfc_compact_id | 否 |  |  |
| 58 | oppcsfc_compact_id | 否 |  |  |
| 59 | csfc_report_status | 否 |  |  |
| 60 | deal_time | 否 |  |  |
| 61 | position_str | 否 |  |  |
| 62 | stock_name | 否 | H |  |
| 63 | stock_type | 否 | H |  |
| 64 | sub_stock_type | 否 | H |  |
| 65 | client_group | 否 | H |  |
| 66 | room_code | 否 | H |  |
| 67 | asset_prop | 否 | H |  |
| 68 | client_prop | 否 | H |  |
| 69 | limit_flag | 否 | H |  |
| 70 | branch_no | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reftradeqry | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reftradeqry_pos | ART | 是 | position_str, position_str |
| idx_reftradeqry | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reftradeqry_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_reftradeqry | serial_no, init_date, serial_no, init_date |
| uk_rpt_ureftradequery | init_date, position_str, init_date, position_str |
| idx_reftradeqry | serial_no, init_date, serial_no, init_date |
| uk_rpt_ureftradequery | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

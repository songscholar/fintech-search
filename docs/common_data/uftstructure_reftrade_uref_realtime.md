# uref_realtime - 转融通出借成交表

**表对象ID**: 6104
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_milltime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | report_no | 否 |  |  |
| 6 | entrust_no | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | refbusi_code | 否 |  |  |
| 15 | cbpconfer_id | 否 |  |  |
| 16 | cbp_business_id | 否 |  |  |
| 17 | business_amount | 否 |  |  |
| 18 | business_time | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | client_name | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | client_prop | 否 | H |  |
| 25 | limit_flag | 否 | H |  |
| 26 | stock_name | 否 | H |  |
| 27 | stock_type | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | corp_client_group | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | curr_date | 否 |  |  |
| 35 | curr_milltime | 否 |  |  |
| 36 | serial_no | 否 |  |  |
| 37 | report_no | 否 |  |  |
| 38 | entrust_no | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | fund_account | 否 |  |  |
| 42 | exchange_type | 否 |  |  |
| 43 | seat_no | 否 |  |  |
| 44 | stock_account | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | refbusi_code | 否 |  |  |
| 47 | cbpconfer_id | 否 |  |  |
| 48 | cbp_business_id | 否 |  |  |
| 49 | business_amount | 否 |  |  |
| 50 | business_time | 否 |  |  |
| 51 | position_str | 否 |  |  |
| 52 | client_name | 否 | H |  |
| 53 | client_group | 否 | H |  |
| 54 | room_code | 否 | H |  |
| 55 | asset_prop | 否 | H |  |
| 56 | client_prop | 否 | H |  |
| 57 | limit_flag | 否 | H |  |
| 58 | stock_name | 否 | H |  |
| 59 | stock_type | 否 | H |  |
| 60 | sub_stock_type | 否 | H |  |
| 61 | corp_client_group | 否 | H |  |
| 62 | asset_level | 否 | H |  |
| 63 | risk_level | 否 | H |  |
| 64 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refrealtime | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refrealtime_reportno | ART | 是 | report_no, cbp_business_id, report_no, cbp_business_id |
| idx_refrealtime_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_refrealtime_id | ART | 是 | client_id, client_id |
| idx_refrealtime_pos | ART | 是 | position_str, position_str |
| idx_refrealtime | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_refrealtime_reportno | ART | 是 | report_no, cbp_business_id, report_no, cbp_business_id |
| idx_refrealtime_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_refrealtime_id | ART | 是 | client_id, client_id |
| idx_refrealtime_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refrealtime | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefrealtime | init_date, position_str, init_date, position_str |
| idx_rpt_urefrealtime_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefrealtime_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefrealtime_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_refrealtime | serial_no, init_date, serial_no, init_date |
| uk_rpt_urefrealtime | init_date, position_str, init_date, position_str |
| idx_rpt_urefrealtime_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefrealtime_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefrealtime_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:37:35 | V3.0.2.6 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_realtime，添加了表字段(corp_client_group);
... |
| 2025-11-24 11:24:58 | V3.0.2.5 | 廖宏玮 | 调整内存表索引 |
| 2025-10-16 10:41:18 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:37:35 | V3.0.2.6 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_realtime，添加了表字段(corp_client_group);
... |
| 2025-11-24 11:24:58 | V3.0.2.5 | 廖宏玮 | 调整内存表索引 |
| 2025-10-16 10:41:18 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

# uqms_ass_equity - 头寸担保证券权益信息表

**表对象ID**: 1007
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | equity_type | 否 |  |  |
| 18 | current_amount | 否 |  |  |
| 19 | recoup_amount | 否 |  |  |
| 20 | recoup_balance | 否 |  |  |
| 21 | register_date | 否 |  |  |
| 22 | divid_date | 否 |  |  |
| 23 | deal_status | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | stock_name | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | serial_no | 否 |  |  |
| 39 | curr_date | 否 |  |  |
| 40 | curr_time | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | op_branch_no | 否 |  |  |
| 43 | op_entrust_way | 否 |  |  |
| 44 | op_station | 否 |  |  |
| 45 | branch_no | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | exchange_type | 否 |  |  |
| 50 | stock_code | 否 |  |  |
| 51 | stock_type | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | equity_type | 否 |  |  |
| 54 | current_amount | 否 |  |  |
| 55 | recoup_amount | 否 |  |  |
| 56 | recoup_balance | 否 |  |  |
| 57 | register_date | 否 |  |  |
| 58 | divid_date | 否 |  |  |
| 59 | deal_status | 否 |  |  |
| 60 | date_clear | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 63 | client_group | 否 | H |  |
| 64 | room_code | 否 | H |  |
| 65 | asset_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | risk_level | 否 | H |  |
| 68 | corp_client_group | 否 | H |  |
| 69 | corp_risk_level | 否 | H |  |
| 70 | asset_level | 否 | H |  |
| 71 | client_name | 否 | H |  |
| 72 | stock_name | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_ass_equity_pos | ART | 是 | position_str, position_str |
| idx_uqms_ass_equity_acct | ART | 是 | fund_account, fund_account |
| idx_uqms_ass_equity_id | ART | 是 | client_id, client_id |
| uk_rpt_uqms_ass_equity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| uk_rpt_uqms_ass_equity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uqms_ass_equity_pos | ART | 是 | position_str, position_str |
| idx_uqms_ass_equity_acct | ART | 是 | fund_account, fund_account |
| idx_uqms_ass_equity_id | ART | 是 | client_id, client_id |
| uk_rpt_uqms_ass_equity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| uk_rpt_uqms_ass_equity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_ass_equity_pos | position_str, position_str |
| idx_uqms_ass_equity_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:54:18 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 15:03:25 | V3.0.6.26 | 洪略 | 修正资源维护错误的问题 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-07 08:59:23 | 3.0.2.24 | 洪略 | 增加历史表 |
| 2026-03-05 16:54:18 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 15:03:25 | V3.0.6.26 | 洪略 | 修正资源维护错误的问题 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-07 08:59:23 | 3.0.2.24 | 洪略 | 增加历史表 |

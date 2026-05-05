# arp_equity_jour - 约定购回权益流水表

**表对象ID**: 2536
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
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | business_flag | 否 |  |  |
| 11 | contract_id | 否 |  |  |
| 12 | arp_equity_type | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | occur_amount | 否 |  |  |
| 21 | post_amount | 否 |  |  |
| 22 | occur_balance | 否 |  |  |
| 23 | post_balance | 否 |  |  |
| 24 | entrust_date | 否 |  |  |
| 25 | entrust_no | 否 |  |  |
| 26 | cancel_serialno | 否 |  |  |
| 27 | report_id | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 30 | client_name | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | client_group | 否 | H |  |
| 33 | room_code | 否 | H |  |
| 34 | asset_prop | 否 | H |  |
| 35 | limit_flag | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | risk_level | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | stock_name | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | serial_no | 否 |  |  |
| 44 | curr_date | 否 |  |  |
| 45 | curr_time | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | operator_no | 否 |  |  |
| 48 | op_entrust_way | 否 |  |  |
| 49 | op_station | 否 |  |  |
| 50 | branch_no | 否 |  |  |
| 51 | business_flag | 否 |  |  |
| 52 | contract_id | 否 |  |  |
| 53 | arp_equity_type | 否 |  |  |
| 54 | fund_account | 否 |  |  |
| 55 | client_id | 否 |  |  |
| 56 | stock_account | 否 |  |  |
| 57 | exchange_type | 否 |  |  |
| 58 | stock_code | 否 |  |  |
| 59 | stock_type | 否 |  |  |
| 60 | money_type | 否 |  |  |
| 61 | occur_amount | 否 |  |  |
| 62 | post_amount | 否 |  |  |
| 63 | occur_balance | 否 |  |  |
| 64 | post_balance | 否 |  |  |
| 65 | entrust_date | 否 |  |  |
| 66 | entrust_no | 否 |  |  |
| 67 | cancel_serialno | 否 |  |  |
| 68 | report_id | 否 |  |  |
| 69 | remark | 否 |  |  |
| 70 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 71 | client_name | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | client_group | 否 | H |  |
| 74 | room_code | 否 | H |  |
| 75 | asset_prop | 否 | H |  |
| 76 | limit_flag | 否 | H |  |
| 77 | client_prop | 否 | H |  |
| 78 | asset_level | 否 | H |  |
| 79 | risk_level | 否 | H |  |
| 80 | corp_risk_level | 否 | H |  |
| 81 | stock_name | 否 | H |  |
| 82 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpequityjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpequityjour_cont | ART | 是 | contract_id, contract_id |
| idx_arpequityjour_acct | ART | 是 | fund_account, fund_account |
| idx_arpequityjour_id | ART | 是 | client_id, client_id |
| idx_arpequityjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpequityjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpequityjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_arpequityjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpequityjour_cont | ART | 是 | contract_id, contract_id |
| idx_arpequityjour_acct | ART | 是 | fund_account, fund_account |
| idx_arpequityjour_id | ART | 是 | client_id, client_id |
| idx_arpequityjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpequityjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpequityjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpequityjour | serial_no, init_date, serial_no, init_date |
| idx_arpequityjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:22:56 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2026-03-04 16:22:56 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |

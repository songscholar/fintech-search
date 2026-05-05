# hstock_quota_jour - H股全流通额度信息流水表

**表对象ID**: 5722
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 92 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | id_no | 否 |  |  |
| 14 | holder_name_long | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | stock_code2 | 否 |  |  |
| 18 | stock_name | 否 |  |  |
| 19 | bank_account | 否 |  |  |
| 20 | full_bank_name | 否 |  |  |
| 21 | company_name | 否 |  |  |
| 22 | facility_quota | 否 |  |  |
| 23 | used_quota | 否 |  |  |
| 24 | occur_quota | 否 |  |  |
| 25 | random_code | 否 |  |  |
| 26 | official_document | 否 |  |  |
| 27 | hold_rate_h | 否 |  |  |
| 28 | modify_date | 否 |  |  |
| 29 | op_flag | 否 |  |  |
| 30 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 31 | remark | 否 |  |  |
| 32 | pay_bank_no_long | 否 |  |  |
| 33 | frozen_quota | 否 |  |  |
| 34 | client_id | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | corp_client_group | 否 | H |  |
| 37 | client_group | 否 | H |  |
| 38 | room_code | 否 | H |  |
| 39 | asset_prop | 否 | H |  |
| 40 | limit_flag | 否 | H |  |
| 41 | client_prop | 否 | H |  |
| 42 | asset_level | 否 | H |  |
| 43 | risk_level | 否 | H |  |
| 44 | corp_risk_level | 否 | H |  |
| 45 | stock_type | 否 | H |  |
| 46 | sub_stock_type | 否 | H |  |
| 47 | init_date | 否 |  |  |
| 48 | serial_no | 否 |  |  |
| 49 | curr_date | 否 |  |  |
| 50 | curr_time | 否 |  |  |
| 51 | op_branch_no | 否 |  |  |
| 52 | operator_no | 否 |  |  |
| 53 | op_station | 否 |  |  |
| 54 | op_entrust_way | 否 |  |  |
| 55 | branch_no | 否 |  |  |
| 56 | fund_account | 否 |  |  |
| 57 | stock_account | 否 |  |  |
| 58 | organ_flag | 否 |  |  |
| 59 | id_no | 否 |  |  |
| 60 | holder_name_long | 否 |  |  |
| 61 | exchange_type | 否 |  |  |
| 62 | stock_code | 否 |  |  |
| 63 | stock_code2 | 否 |  |  |
| 64 | stock_name | 否 |  |  |
| 65 | bank_account | 否 |  |  |
| 66 | full_bank_name | 否 |  |  |
| 67 | company_name | 否 |  |  |
| 68 | facility_quota | 否 |  |  |
| 69 | used_quota | 否 |  |  |
| 70 | occur_quota | 否 |  |  |
| 71 | random_code | 否 |  |  |
| 72 | official_document | 否 |  |  |
| 73 | hold_rate_h | 否 |  |  |
| 74 | modify_date | 否 |  |  |
| 75 | op_flag | 否 |  |  |
| 76 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 77 | remark | 否 |  |  |
| 78 | pay_bank_no_long | 否 |  |  |
| 79 | frozen_quota | 否 |  |  |
| 80 | client_id | 否 | H |  |
| 81 | client_name | 否 | H |  |
| 82 | corp_client_group | 否 | H |  |
| 83 | client_group | 否 | H |  |
| 84 | room_code | 否 | H |  |
| 85 | asset_prop | 否 | H |  |
| 86 | limit_flag | 否 | H |  |
| 87 | client_prop | 否 | H |  |
| 88 | asset_level | 否 | H |  |
| 89 | risk_level | 否 | H |  |
| 90 | corp_risk_level | 否 | H |  |
| 91 | stock_type | 否 | H |  |
| 92 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hstock_quota_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_hstock_quota_jour_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_hstockquotajour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_hstockquotajour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_hstock_quota_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_hstock_quota_jour_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_hstockquotajour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_hstockquotajour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hstock_quota_jour | init_date, serial_no, init_date, serial_no |
| idx_hstock_quota_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:36:58 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2026-03-09 14:36:58 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |

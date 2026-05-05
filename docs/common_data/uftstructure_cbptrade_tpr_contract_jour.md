# tpr_contract_jour - 三方回购合约流水表

**表对象ID**: 2349
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 98 个）

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
| 9 | business_flag | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | contract_id | 否 |  |  |
| 16 | tpr_source_type | 否 |  |  |
| 17 | prop_fund_acco | 否 |  |  |
| 18 | prop_stock_account | 否 |  |  |
| 19 | prop_seat_no | 否 |  |  |
| 20 | entrust_date | 否 |  |  |
| 21 | entrust_balance | 否 |  |  |
| 22 | expire_year_rate | 否 |  |  |
| 23 | back_balance | 否 |  |  |
| 24 | date_back | 否 |  |  |
| 25 | real_year_rate | 否 |  |  |
| 26 | real_back_balance | 否 |  |  |
| 27 | real_date_back | 否 |  |  |
| 28 | fruits | 否 |  |  |
| 29 | current_assure_value | 否 |  |  |
| 30 | report_id | 否 |  |  |
| 31 | szdc_business_no | 否 |  |  |
| 32 | tpr_contract_status | 否 |  |  |
| 33 | date_clear | 否 |  |  |
| 34 | remark | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 36 | en_basket_id | 否 |  |  |
| 37 | exch_out_fruits | 否 |  |  |
| 38 | occur_fruits | 否 |  |  |
| 39 | income_treatmode | 否 |  |  |
| 40 | client_name | 否 | H |  |
| 41 | corp_client_group | 否 | H |  |
| 42 | client_group | 否 | H |  |
| 43 | room_code | 否 | H |  |
| 44 | asset_prop | 否 | H |  |
| 45 | limit_flag | 否 | H |  |
| 46 | client_prop | 否 | H |  |
| 47 | asset_level | 否 | H |  |
| 48 | risk_level | 否 | H |  |
| 49 | corp_risk_level | 否 | H |  |
| 50 | init_date | 否 |  |  |
| 51 | serial_no | 否 |  |  |
| 52 | curr_date | 否 |  |  |
| 53 | curr_time | 否 |  |  |
| 54 | op_branch_no | 否 |  |  |
| 55 | operator_no | 否 |  |  |
| 56 | op_entrust_way | 否 |  |  |
| 57 | op_station | 否 |  |  |
| 58 | business_flag | 否 |  |  |
| 59 | branch_no | 否 |  |  |
| 60 | fund_account | 否 |  |  |
| 61 | client_id | 否 |  |  |
| 62 | stock_account | 否 |  |  |
| 63 | exchange_type | 否 |  |  |
| 64 | contract_id | 否 |  |  |
| 65 | tpr_source_type | 否 |  |  |
| 66 | prop_fund_acco | 否 |  |  |
| 67 | prop_stock_account | 否 |  |  |
| 68 | prop_seat_no | 否 |  |  |
| 69 | entrust_date | 否 |  |  |
| 70 | entrust_balance | 否 |  |  |
| 71 | expire_year_rate | 否 |  |  |
| 72 | back_balance | 否 |  |  |
| 73 | date_back | 否 |  |  |
| 74 | real_year_rate | 否 |  |  |
| 75 | real_back_balance | 否 |  |  |
| 76 | real_date_back | 否 |  |  |
| 77 | fruits | 否 |  |  |
| 78 | current_assure_value | 否 |  |  |
| 79 | report_id | 否 |  |  |
| 80 | szdc_business_no | 否 |  |  |
| 81 | tpr_contract_status | 否 |  |  |
| 82 | date_clear | 否 |  |  |
| 83 | remark | 否 |  |  |
| 84 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 85 | en_basket_id | 否 |  |  |
| 86 | exch_out_fruits | 否 |  |  |
| 87 | occur_fruits | 否 |  |  |
| 88 | income_treatmode | 否 |  |  |
| 89 | client_name | 否 | H |  |
| 90 | corp_client_group | 否 | H |  |
| 91 | client_group | 否 | H |  |
| 92 | room_code | 否 | H |  |
| 93 | asset_prop | 否 | H |  |
| 94 | limit_flag | 否 | H |  |
| 95 | client_prop | 否 | H |  |
| 96 | asset_level | 否 | H |  |
| 97 | risk_level | 否 | H |  |
| 98 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprcontractjour_id | 默认 | 否 |  |
| idx_tprcontractjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_tprcontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_tprcontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprcontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprcontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_tprcontractjour_id | 默认 | 否 |  |
| idx_tprcontractjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_tprcontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_tprcontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprcontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprcontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprcontractjour_id | init_date, serial_no, init_date, serial_no |
| idx_tprcontractjour_id | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:36:43 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 15:56:28 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:36:43 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 15:56:28 | V3.0.2.1007 | 张明月 | 新增 |

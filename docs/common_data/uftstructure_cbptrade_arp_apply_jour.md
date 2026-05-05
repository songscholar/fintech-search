# arp_apply_jour - 约定购回申请流水表

**表对象ID**: 2509
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 120 个）

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
| 9 | business_flag | 否 |  |  |
| 10 | contract_id | 否 |  |  |
| 11 | join_contract_id | 否 |  |  |
| 12 | papercont_id | 否 |  |  |
| 13 | arp_apply_type | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | funder_no | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | expire_year_rate | 否 |  |  |
| 23 | entrust_amount | 否 |  |  |
| 24 | entrust_balance | 否 |  |  |
| 25 | back_principal | 否 |  |  |
| 26 | back_balance | 否 |  |  |
| 27 | date_back | 否 |  |  |
| 28 | entrust_date | 否 |  |  |
| 29 | entrust_no | 否 |  |  |
| 30 | ask_back_balance | 否 |  |  |
| 31 | ask_date_back | 否 |  |  |
| 32 | ask_year_rate | 否 |  |  |
| 33 | arp_apply_status | 否 |  |  |
| 34 | sign_date | 否 |  |  |
| 35 | sign_operator_no | 否 |  |  |
| 36 | fund_useage | 否 |  |  |
| 37 | audit_remark | 否 |  |  |
| 38 | rate_mode | 否 |  |  |
| 39 | assure_ratio | 否 |  |  |
| 40 | assure_price | 否 |  |  |
| 41 | stkused_flag | 否 |  |  |
| 42 | stkused_year_rate | 否 |  |  |
| 43 | margin_focus_ratio | 否 |  |  |
| 44 | margin_alert_ratio | 否 |  |  |
| 45 | margin_treat_ratio | 否 |  |  |
| 46 | date_clear | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | position_str | 否 |  | 定位串 init_date(8)+serial_no(10) |
| 49 | client_name | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | client_group | 否 | H |  |
| 52 | room_code | 否 | H |  |
| 53 | asset_prop | 否 | H |  |
| 54 | limit_flag | 否 | H |  |
| 55 | client_prop | 否 | H |  |
| 56 | asset_level | 否 | H |  |
| 57 | risk_level | 否 | H |  |
| 58 | corp_risk_level | 否 | H |  |
| 59 | stock_name | 否 | H |  |
| 60 | sub_stock_type | 否 | H |  |
| 61 | init_date | 否 |  |  |
| 62 | serial_no | 否 |  |  |
| 63 | curr_date | 否 |  |  |
| 64 | curr_time | 否 |  |  |
| 65 | op_branch_no | 否 |  |  |
| 66 | operator_no | 否 |  |  |
| 67 | op_station | 否 |  |  |
| 68 | op_entrust_way | 否 |  |  |
| 69 | business_flag | 否 |  |  |
| 70 | contract_id | 否 |  |  |
| 71 | join_contract_id | 否 |  |  |
| 72 | papercont_id | 否 |  |  |
| 73 | arp_apply_type | 否 |  |  |
| 74 | branch_no | 否 |  |  |
| 75 | fund_account | 否 |  |  |
| 76 | client_id | 否 |  |  |
| 77 | stock_account | 否 |  |  |
| 78 | exchange_type | 否 |  |  |
| 79 | funder_no | 否 |  |  |
| 80 | stock_code | 否 |  |  |
| 81 | stock_type | 否 |  |  |
| 82 | expire_year_rate | 否 |  |  |
| 83 | entrust_amount | 否 |  |  |
| 84 | entrust_balance | 否 |  |  |
| 85 | back_principal | 否 |  |  |
| 86 | back_balance | 否 |  |  |
| 87 | date_back | 否 |  |  |
| 88 | entrust_date | 否 |  |  |
| 89 | entrust_no | 否 |  |  |
| 90 | ask_back_balance | 否 |  |  |
| 91 | ask_date_back | 否 |  |  |
| 92 | ask_year_rate | 否 |  |  |
| 93 | arp_apply_status | 否 |  |  |
| 94 | sign_date | 否 |  |  |
| 95 | sign_operator_no | 否 |  |  |
| 96 | fund_useage | 否 |  |  |
| 97 | audit_remark | 否 |  |  |
| 98 | rate_mode | 否 |  |  |
| 99 | assure_ratio | 否 |  |  |
| 100 | assure_price | 否 |  |  |
| 101 | stkused_flag | 否 |  |  |
| 102 | stkused_year_rate | 否 |  |  |
| 103 | margin_focus_ratio | 否 |  |  |
| 104 | margin_alert_ratio | 否 |  |  |
| 105 | margin_treat_ratio | 否 |  |  |
| 106 | date_clear | 否 |  |  |
| 107 | remark | 否 |  |  |
| 108 | position_str | 否 |  | 定位串 init_date(8)+serial_no(10) |
| 109 | client_name | 否 | H |  |
| 110 | corp_client_group | 否 | H |  |
| 111 | client_group | 否 | H |  |
| 112 | room_code | 否 | H |  |
| 113 | asset_prop | 否 | H |  |
| 114 | limit_flag | 否 | H |  |
| 115 | client_prop | 否 | H |  |
| 116 | asset_level | 否 | H |  |
| 117 | risk_level | 否 | H |  |
| 118 | corp_risk_level | 否 | H |  |
| 119 | stock_name | 否 | H |  |
| 120 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpapplyjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_arpapplyjour_id | ART | 是 | client_id, client_id |
| idx_arpapplyjour_cid | ART | 是 | contract_id, contract_id |
| idx_arpapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_arpapplyjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_arpapplyjour_id | ART | 是 | client_id, client_id |
| idx_arpapplyjour_cid | ART | 是 | contract_id, contract_id |
| idx_arpapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_arpapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpapplyjour | serial_no, init_date, serial_no, init_date |
| idx_arpapplyjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:16:12 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-06 16:04:46 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 16:16:12 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-06 16:04:46 | V3.0.2.1009 | 黄积冲 | 新增表 |

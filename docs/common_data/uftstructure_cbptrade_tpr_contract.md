# tpr_contract - 三方回购合约表

**表对象ID**: 2355
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | contract_id | 否 |  |  |
| 8 | tpr_source_type | 否 |  |  |
| 9 | prop_fund_acco | 否 |  |  |
| 10 | prop_stock_account | 否 |  |  |
| 11 | prop_seat_no | 否 |  |  |
| 12 | entrust_date | 否 |  |  |
| 13 | entrust_balance | 否 |  |  |
| 14 | expire_year_rate | 否 |  |  |
| 15 | back_balance | 否 |  |  |
| 16 | date_back | 否 |  |  |
| 17 | real_year_rate | 否 |  |  |
| 18 | real_back_balance | 否 |  |  |
| 19 | real_date_back | 否 |  |  |
| 20 | fruits | 否 |  |  |
| 21 | current_assure_value | 否 |  |  |
| 22 | report_id | 否 |  |  |
| 23 | szdc_business_no | 否 |  |  |
| 24 | tpr_contract_status | 否 |  |  |
| 25 | date_clear | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 28 | en_basket_id | 否 |  |  |
| 29 | exch_out_fruits | 否 |  |  |
| 30 | income_treatmode | 否 |  |  |
| 31 | client_name | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | client_group | 否 | H |  |
| 34 | room_code | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | asset_level | 否 | H |  |
| 39 | risk_level | 否 | H |  |
| 40 | corp_risk_level | 否 | H |  |
| 41 | init_date | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | stock_account | 否 |  |  |
| 46 | exchange_type | 否 |  |  |
| 47 | contract_id | 否 |  |  |
| 48 | tpr_source_type | 否 |  |  |
| 49 | prop_fund_acco | 否 |  |  |
| 50 | prop_stock_account | 否 |  |  |
| 51 | prop_seat_no | 否 |  |  |
| 52 | entrust_date | 否 |  |  |
| 53 | entrust_balance | 否 |  |  |
| 54 | expire_year_rate | 否 |  |  |
| 55 | back_balance | 否 |  |  |
| 56 | date_back | 否 |  |  |
| 57 | real_year_rate | 否 |  |  |
| 58 | real_back_balance | 否 |  |  |
| 59 | real_date_back | 否 |  |  |
| 60 | fruits | 否 |  |  |
| 61 | current_assure_value | 否 |  |  |
| 62 | report_id | 否 |  |  |
| 63 | szdc_business_no | 否 |  |  |
| 64 | tpr_contract_status | 否 |  |  |
| 65 | date_clear | 否 |  |  |
| 66 | remark | 否 |  |  |
| 67 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 68 | en_basket_id | 否 |  |  |
| 69 | exch_out_fruits | 否 |  |  |
| 70 | income_treatmode | 否 |  |  |
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

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprcontract_id | 默认 | 否 |  |
| idx_tprcontract_id | ART | 是 | contract_id, contract_id |
| idx_tprcontract_acct | ART | 是 | fund_account, fund_account |
| idx_tprcontract_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_tprcontract_tolast | ART | 是 | date_clear, date_clear |
| idx_tprcontract_id | 默认 | 否 |  |
| idx_tprcontract_id | ART | 是 | contract_id, contract_id |
| idx_tprcontract_acct | ART | 是 | fund_account, fund_account |
| idx_tprcontract_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_tprcontract_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprcontract_id | contract_id, contract_id |
| idx_tprcontract_id | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:38:50 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-28 15:47:38 | 3.0.2.1 | 李江霖 | 修改position_str的备注，与代码保持一致 |
| 2024-09-23 17:10:38 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:38:50 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-28 15:47:38 | 3.0.2.1 | 李江霖 | 修改position_str的备注，与代码保持一致 |
| 2024-09-23 17:10:38 | V3.0.2.1007 | 张明月 | 新增 |

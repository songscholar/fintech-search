# tpr_contract_ext - 三方回购合约扩展表

**表对象ID**: 2347
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | contract_id | 否 |  |  |
| 7 | report_id | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | impawn_amount | 否 |  |  |
| 10 | exch_in_amount | 否 |  |  |
| 11 | exch_out_amount | 否 |  |  |
| 12 | client_id | 否 | H |  |
| 13 | client_name | 否 | H |  |
| 14 | corp_client_group | 否 | H |  |
| 15 | client_group | 否 | H |  |
| 16 | room_code | 否 | H |  |
| 17 | asset_prop | 否 | H |  |
| 18 | limit_flag | 否 | H |  |
| 19 | client_prop | 否 | H |  |
| 20 | asset_level | 否 | H |  |
| 21 | risk_level | 否 | H |  |
| 22 | corp_risk_level | 否 | H |  |
| 23 | stock_name | 否 | H |  |
| 24 | stock_type | 否 | H |  |
| 25 | sub_stock_type | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | stock_account | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | contract_id | 否 |  |  |
| 32 | report_id | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | impawn_amount | 否 |  |  |
| 35 | exch_in_amount | 否 |  |  |
| 36 | exch_out_amount | 否 |  |  |
| 37 | client_id | 否 | H |  |
| 38 | client_name | 否 | H |  |
| 39 | corp_client_group | 否 | H |  |
| 40 | client_group | 否 | H |  |
| 41 | room_code | 否 | H |  |
| 42 | asset_prop | 否 | H |  |
| 43 | limit_flag | 否 | H |  |
| 44 | client_prop | 否 | H |  |
| 45 | asset_level | 否 | H |  |
| 46 | risk_level | 否 | H |  |
| 47 | corp_risk_level | 否 | H |  |
| 48 | stock_name | 否 | H |  |
| 49 | stock_type | 否 | H |  |
| 50 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprcontractext_id | 默认 | 否 |  |
| idx_tprcontractext_id | ART | 是 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| uk_rpt_tprcontractext | ART | 是 | init_date, contract_id, exchange_type, stock_code, init_date, contract_id, exchange_type, stock_code |
| idx_tprcontractext_id | 默认 | 否 |  |
| idx_tprcontractext_id | ART | 是 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| uk_rpt_tprcontractext | ART | 是 | init_date, contract_id, exchange_type, stock_code, init_date, contract_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprcontractext_id | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| idx_tprcontractext_id | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:35:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 15:44:10 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:35:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 15:44:10 | V3.0.2.1007 | 张明月 | 新增 |

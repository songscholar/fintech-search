# stb_ipo_ask_result - 证券股转IPO询价结果表

**表对象ID**: 5753
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | business_id | 否 |  |  |
| 7 | contract_id | 否 |  |  |
| 8 | confirm_amount | 否 |  |  |
| 9 | business_price | 否 |  |  |
| 10 | business_date | 否 |  |  |
| 11 | business_time | 否 |  |  |
| 12 | withdraw_cause | 否 |  |  |
| 13 | returnbusin_kind | 否 |  |  |
| 14 | date_clear | 否 |  |  |
| 15 | business_amount2 | 否 |  |  |
| 16 | client_id | 否 | H |  |
| 17 | client_name | 否 | H |  |
| 18 | branch_no | 否 | H |  |
| 19 | corp_client_group | 否 | H |  |
| 20 | client_group | 否 | H |  |
| 21 | room_code | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | client_prop | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_risk_level | 否 | H |  |
| 27 | stock_name | 否 | H |  |
| 28 | stock_type | 否 | H |  |
| 29 | sub_stock_type | 否 | H |  |
| 30 | init_date | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | business_id | 否 |  |  |
| 36 | contract_id | 否 |  |  |
| 37 | confirm_amount | 否 |  |  |
| 38 | business_price | 否 |  |  |
| 39 | business_date | 否 |  |  |
| 40 | business_time | 否 |  |  |
| 41 | withdraw_cause | 否 |  |  |
| 42 | returnbusin_kind | 否 |  |  |
| 43 | date_clear | 否 |  |  |
| 44 | business_amount2 | 否 |  |  |
| 45 | client_id | 否 | H |  |
| 46 | client_name | 否 | H |  |
| 47 | branch_no | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |
| 51 | limit_flag | 否 | H |  |
| 52 | client_prop | 否 | H |  |
| 53 | asset_level | 否 | H |  |
| 54 | risk_level | 否 | H |  |
| 55 | corp_risk_level | 否 | H |  |
| 56 | stock_name | 否 | H |  |
| 57 | stock_type | 否 | H |  |
| 58 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_ipo_ask_result | ART | 是 | fund_account, exchange_type, stock_account, stock_code, returnbusin_kind, fund_account, exchange_type, stock_account, stock_code, returnbusin_kind |
| idx_stbipoaskresult | ART | 是 | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| uk_rpt_stbipoaskresult | ART | 是 | init_date, fund_account, exchange_type, stock_account, stock_code, contract_id, init_date, fund_account, exchange_type, stock_account, stock_code, contract_id |
| idx_rpt_stbipoaskresult_tolast | ART | 是 | date_clear, date_clear |
| idx_stb_ipo_ask_result | ART | 是 | fund_account, exchange_type, stock_account, stock_code, returnbusin_kind, fund_account, exchange_type, stock_account, stock_code, returnbusin_kind |
| idx_stbipoaskresult | ART | 是 | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| uk_rpt_stbipoaskresult | ART | 是 | init_date, fund_account, exchange_type, stock_account, stock_code, contract_id, init_date, fund_account, exchange_type, stock_account, stock_code, contract_id |
| idx_rpt_stbipoaskresult_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_ipo_ask_result | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |
| idx_stb_ipo_ask_result | fund_account, exchange_type, stock_account, stock_code, init_date, contract_id, fund_account, exchange_type, stock_account, stock_code, init_date, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:40:46 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-27 11:22:36 | 3.0.2.61 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-17 11:00:37 | 3.0.2.20 | yusz | 物理表stb_ipo_ask_result，删除了表字段(branch_no);
 |
| 2026-03-09 14:40:46 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-02-27 11:22:36 | 3.0.2.61 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-17 11:00:37 | 3.0.2.20 | yusz | 物理表stb_ipo_ask_result，删除了表字段(branch_no);
 |

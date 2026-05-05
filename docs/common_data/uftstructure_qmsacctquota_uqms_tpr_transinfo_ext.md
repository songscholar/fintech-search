# uqms_tpr_transinfo_ext - 额度管理转发申报信息扩展表

**表对象ID**: 1622
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exec_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | basket_id | 否 |  |  |
| 8 | basket_name | 否 |  |  |
| 9 | discount_rate | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | impawn_amount | 否 |  |  |
| 12 | impawn_bs | 否 |  |  |
| 13 | stock_property | 否 |  |  |
| 14 | stock_parvalue | 否 |  |  |
| 15 | client_id | 否 | H |  |
| 16 | client_name | 否 | H |  |
| 17 | corp_client_group | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | stock_name | 否 | H |  |
| 27 | stock_type | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | branch_no | 否 |  |  |
| 31 | exec_id | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | basket_id | 否 |  |  |
| 36 | basket_name | 否 |  |  |
| 37 | discount_rate | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | impawn_amount | 否 |  |  |
| 40 | impawn_bs | 否 |  |  |
| 41 | stock_property | 否 |  |  |
| 42 | stock_parvalue | 否 |  |  |
| 43 | client_id | 否 | H |  |
| 44 | client_name | 否 | H |  |
| 45 | corp_client_group | 否 | H |  |
| 46 | client_group | 否 | H |  |
| 47 | room_code | 否 | H |  |
| 48 | asset_prop | 否 | H |  |
| 49 | limit_flag | 否 | H |  |
| 50 | client_prop | 否 | H |  |
| 51 | asset_level | 否 | H |  |
| 52 | risk_level | 否 | H |  |
| 53 | corp_risk_level | 否 | H |  |
| 54 | stock_name | 否 | H |  |
| 55 | stock_type | 否 | H |  |
| 56 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_tprtransinfoext_id | ART | 是 | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |
| uk_rpt_uqmstprtransinfoext | ART | 是 | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |
| idx_uqms_tprtransinfoext_id | ART | 是 | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |
| uk_rpt_uqmstprtransinfoext | ART | 是 | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_tprtransinfoext_id | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |
| idx_uqms_tprtransinfoext_id | init_date, exec_id, exchange_type, stock_code, stock_property, init_date, exec_id, exchange_type, stock_code, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:48:05 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 16:54:30 | 3.0.6.13 | 周富安 | 新增 |
| 2026-03-05 16:48:05 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 16:54:30 | 3.0.6.13 | 周富安 | 新增 |

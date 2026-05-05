# brp_contract_ext - 债券质押协议回购合约扩展表

**表对象ID**: 2357
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | join_position_str | 否 |  |  |
| 7 | orig_report_id | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | impawn_amount | 否 |  |  |
| 10 | exch_in_amount | 否 |  |  |
| 11 | exch_out_amount | 否 |  |  |
| 12 | use_date | 否 |  |  |
| 13 | stock_property | 否 |  |  |
| 14 | client_id | 否 | H |  |
| 15 | client_name | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | client_group | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | client_prop | 否 | H |  |
| 22 | asset_level | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | stock_name | 否 | H |  |
| 26 | stock_type | 否 | H |  |
| 27 | sub_stock_type | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | join_position_str | 否 |  |  |
| 34 | orig_report_id | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | impawn_amount | 否 |  |  |
| 37 | exch_in_amount | 否 |  |  |
| 38 | exch_out_amount | 否 |  |  |
| 39 | use_date | 否 |  |  |
| 40 | stock_property | 否 |  |  |
| 41 | client_id | 否 | H |  |
| 42 | client_name | 否 | H |  |
| 43 | corp_client_group | 否 | H |  |
| 44 | client_group | 否 | H |  |
| 45 | room_code | 否 | H |  |
| 46 | asset_prop | 否 | H |  |
| 47 | limit_flag | 否 | H |  |
| 48 | client_prop | 否 | H |  |
| 49 | asset_level | 否 | H |  |
| 50 | risk_level | 否 | H |  |
| 51 | corp_risk_level | 否 | H |  |
| 52 | stock_name | 否 | H |  |
| 53 | stock_type | 否 | H |  |
| 54 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_brpcontractext_id | 默认 | 否 |  |
| idx_brpcontractext_id | ART | 是 | join_position_str, exchange_type, stock_code, stock_property, join_position_str, exchange_type, stock_code, stock_property |
| idx_brpcontractext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_brpcontractext | ART | 是 | init_date, join_position_str, exchange_type, stock_code, stock_property, init_date, join_position_str, exchange_type, stock_code, stock_property |
| idx_brpcontractext_id | 默认 | 否 |  |
| idx_brpcontractext_id | ART | 是 | join_position_str, exchange_type, stock_code, stock_property, join_position_str, exchange_type, stock_code, stock_property |
| idx_brpcontractext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_brpcontractext | ART | 是 | init_date, join_position_str, exchange_type, stock_code, stock_property, init_date, join_position_str, exchange_type, stock_code, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_brpcontractext_id | join_position_str, exchange_type, stock_code, stock_property, join_position_str, exchange_type, stock_code, stock_property |
| idx_brpcontractext_id | join_position_str, exchange_type, stock_code, stock_property, join_position_str, exchange_type, stock_code, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:40:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 17:20:50 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:40:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-09-23 17:20:50 | V3.0.2.1007 | 张明月 | 新增 |

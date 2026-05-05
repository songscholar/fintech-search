# blp_contractext - 债券借贷合约扩展表

**表对象ID**: 2541
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | cbpcontract_id | 否 |  |  |
| 9 | impawn_amount | 否 |  |  |
| 10 | exch_in_amount | 否 |  |  |
| 11 | exch_out_amount | 否 |  |  |
| 12 | fruits | 否 |  |  |
| 13 | exch_out_fruits | 否 |  |  |
| 14 | use_date | 否 |  |  |
| 15 | stock_property | 否 |  |  |
| 16 | client_id | 否 | H |  |
| 17 | client_name | 否 | H |  |
| 18 | corp_client_group | 否 | H |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | asset_prop | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | client_prop | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_risk_level | 否 | H |  |
| 27 | stock_name | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | branch_no | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | cbpcontract_id | 否 |  |  |
| 37 | impawn_amount | 否 |  |  |
| 38 | exch_in_amount | 否 |  |  |
| 39 | exch_out_amount | 否 |  |  |
| 40 | fruits | 否 |  |  |
| 41 | exch_out_fruits | 否 |  |  |
| 42 | use_date | 否 |  |  |
| 43 | stock_property | 否 |  |  |
| 44 | client_id | 否 | H |  |
| 45 | client_name | 否 | H |  |
| 46 | corp_client_group | 否 | H |  |
| 47 | client_group | 否 | H |  |
| 48 | room_code | 否 | H |  |
| 49 | asset_prop | 否 | H |  |
| 50 | limit_flag | 否 | H |  |
| 51 | client_prop | 否 | H |  |
| 52 | asset_level | 否 | H |  |
| 53 | risk_level | 否 | H |  |
| 54 | corp_risk_level | 否 | H |  |
| 55 | stock_name | 否 | H |  |
| 56 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_blp_contractext_cid | 默认 | 否 |  |
| idx_blp_contractext_acct | 默认 | 否 |  |
| idx_blp_contractext_cid | 默认 | 否 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_blp_contractext_cid | ART | 是 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_blp_contractext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_blpcontractext | ART | 是 | init_date, cbpcontract_id, exchange_type, stock_code, stock_property, init_date, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_rpt_blpcontractext_acct | ART | 是 | fund_account, fund_account |
| idx_blp_contractext_cid | 默认 | 否 |  |
| idx_blp_contractext_acct | 默认 | 否 |  |
| idx_blp_contractext_cid | 默认 | 否 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_blp_contractext_cid | ART | 是 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_blp_contractext_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_blpcontractext | ART | 是 | init_date, cbpcontract_id, exchange_type, stock_code, stock_property, init_date, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_rpt_blpcontractext_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_blp_contractext_cid | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_blp_contractext_cid | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:25:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:45:27 | 3.0.2.75 | taocong45644 | 当前表blp_contractext，修改了索引idx_blp_contractext_cid,索引字段修改为：(cbp... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |
| 2026-03-04 16:25:27 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:45:27 | 3.0.2.75 | taocong45644 | 当前表blp_contractext，修改了索引idx_blp_contractext_cid,索引字段修改为：(cbp... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |

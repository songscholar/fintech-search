# impawn_stock - 质押国债表

**表对象ID**: 5561
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | pre_out_amount | 否 |  |  |
| 7 | pre_in_amount | 否 |  |  |
| 8 | store_amount | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_account(20)+stock_co |
| 10 | tohis_date | 否 | H |  |
| 11 | branch_no | 否 | H |  |
| 12 | client_name | 否 | H |  |
| 13 | corp_client_group | 否 | H |  |
| 14 | client_group | 否 | H |  |
| 15 | room_code | 否 | H |  |
| 16 | asset_prop | 否 | H |  |
| 17 | limit_flag | 否 | H |  |
| 18 | client_prop | 否 | H |  |
| 19 | asset_level | 否 | H |  |
| 20 | risk_level | 否 | H |  |
| 21 | corp_risk_level | 否 | H |  |
| 22 | stock_name | 否 | H |  |
| 23 | stock_type | 否 | H |  |
| 24 | sub_stock_type | 否 | H |  |
| 25 | client_id | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_account | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | pre_out_amount | 否 |  |  |
| 31 | pre_in_amount | 否 |  |  |
| 32 | store_amount | 否 |  |  |
| 33 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_account(20)+stock_co |
| 34 | tohis_date | 否 | H |  |
| 35 | branch_no | 否 | H |  |
| 36 | client_name | 否 | H |  |
| 37 | corp_client_group | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | asset_prop | 否 | H |  |
| 41 | limit_flag | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | asset_level | 否 | H |  |
| 44 | risk_level | 否 | H |  |
| 45 | corp_risk_level | 否 | H |  |
| 46 | stock_name | 否 | H |  |
| 47 | stock_type | 否 | H |  |
| 48 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_rpt_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, tohis_date, fund_account, exchange_type, stock_account, stock_code, tohis_date |
| idx_rpt_impawn_stock_pos | ART | 是 | position_str, tohis_date, position_str, tohis_date |
| idx_rpt_impawn_stock_cid | ART | 是 | client_id, tohis_date, client_id, tohis_date |
| idx_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_rpt_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, tohis_date, fund_account, exchange_type, stock_account, stock_code, tohis_date |
| idx_rpt_impawn_stock_pos | ART | 是 | position_str, tohis_date, position_str, tohis_date |
| idx_rpt_impawn_stock_cid | ART | 是 | client_id, tohis_date, client_id, tohis_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_impawn_stock | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_impawn_stock | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:11:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:34 | V3.0.8.15 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-29 12:12:21 | 3.0.2.31 | 洪略 | 补齐历史表的索引idx_impawn_stock_cid资源 |
| 2025-11-25 09:49:11 | 3.0.2.30 | 洪略 | 补齐资源同时当前表增加position_str字段 |
| 2024-07-19 10:20:33 | 3.0.2.29 | 张云焘 | 删除branch_no |
| 2026-03-09 14:11:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:34 | V3.0.8.15 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-29 12:12:21 | 3.0.2.31 | 洪略 | 补齐历史表的索引idx_impawn_stock_cid资源 |
| 2025-11-25 09:49:11 | 3.0.2.30 | 洪略 | 补齐资源同时当前表增加position_str字段 |
| 2024-07-19 10:20:33 | 3.0.2.29 | 张云焘 | 删除branch_no |

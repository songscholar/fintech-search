# srp_assure - 股票质押担保物表

**表对象ID**: 2623
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | impawn_asset_type | 否 |  |  |
| 6 | contract_id | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | seat_no | 否 |  |  |
| 10 | stock_property | 否 |  |  |
| 11 | stock_describe | 否 |  |  |
| 12 | impawn_id | 否 |  |  |
| 13 | report_id | 否 |  |  |
| 14 | current_amount | 否 |  |  |
| 15 | enable_amount | 否 |  |  |
| 16 | current_balance | 否 |  |  |
| 17 | enable_balance | 否 |  |  |
| 18 | enable_sell | 否 |  |  |
| 19 | settle_flag | 否 |  |  |
| 20 | position_str | 否 |  | contract_id(18)+stock_account(20)+stock_code(6)+exchange_typ |
| 21 | tohis_date | 否 | H |  |
| 22 | client_name | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | asset_level | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_risk_level | 否 | H |  |
| 32 | stock_name | 否 | H |  |
| 33 | stock_type | 否 | H |  |
| 34 | sub_stock_type | 否 | H |  |
| 35 | fund_account | 否 |  |  |
| 36 | client_id | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | stock_account | 否 |  |  |
| 39 | impawn_asset_type | 否 |  |  |
| 40 | contract_id | 否 |  |  |
| 41 | stock_code | 否 |  |  |
| 42 | exchange_type | 否 |  |  |
| 43 | seat_no | 否 |  |  |
| 44 | stock_property | 否 |  |  |
| 45 | stock_describe | 否 |  |  |
| 46 | impawn_id | 否 |  |  |
| 47 | report_id | 否 |  |  |
| 48 | current_amount | 否 |  |  |
| 49 | enable_amount | 否 |  |  |
| 50 | current_balance | 否 |  |  |
| 51 | enable_balance | 否 |  |  |
| 52 | enable_sell | 否 |  |  |
| 53 | settle_flag | 否 |  |  |
| 54 | position_str | 否 |  | contract_id(18)+stock_account(20)+stock_code(6)+exchange_typ |
| 55 | tohis_date | 否 | H |  |
| 56 | client_name | 否 | H |  |
| 57 | corp_client_group | 否 | H |  |
| 58 | client_group | 否 | H |  |
| 59 | room_code | 否 | H |  |
| 60 | asset_prop | 否 | H |  |
| 61 | limit_flag | 否 | H |  |
| 62 | client_prop | 否 | H |  |
| 63 | asset_level | 否 | H |  |
| 64 | risk_level | 否 | H |  |
| 65 | corp_risk_level | 否 | H |  |
| 66 | stock_name | 否 | H |  |
| 67 | stock_type | 否 | H |  |
| 68 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpassure | ART | 是 | position_str, position_str |
| idx_srpassure_con | ART | 是 | contract_id, contract_id |
| idx_srpassure_fund | ART | 是 | fund_account, fund_account |
| uk_rpt_srpassure | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_srpassure_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |
| idx_srpassure | ART | 是 | position_str, position_str |
| idx_srpassure_con | ART | 是 | contract_id, contract_id |
| idx_srpassure_fund | ART | 是 | fund_account, fund_account |
| uk_rpt_srpassure | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_srpassure_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpassure | position_str, position_str |
| idx_srpassure | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:53:45 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.2 | 李江霖 | 修改position_str的备注，与代码保持一致 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:40 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:53:45 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.2 | 李江霖 | 修改position_str的备注，与代码保持一致 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:40 | 3.0.3.1 | wuxd | 新增 |

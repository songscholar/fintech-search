# srp_assure_jour - 股票质押担保物流水表

**表对象ID**: 2624
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | business_flag | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | srp_operate_type | 否 |  |  |
| 7 | cancel_serialno | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | impawn_asset_type | 否 |  |  |
| 13 | contract_id | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | seat_no | 否 |  |  |
| 17 | stock_property | 否 |  |  |
| 18 | stock_describe | 否 |  |  |
| 19 | post_amount | 否 |  |  |
| 20 | occur_amount | 否 |  |  |
| 21 | post_balance | 否 |  |  |
| 22 | occur_balance | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | stock_name | 否 | H |  |
| 36 | stock_type | 否 | H |  |
| 37 | sub_stock_type | 否 | H |  |
| 38 | init_date | 否 |  |  |
| 39 | serial_no | 否 |  |  |
| 40 | business_flag | 否 |  |  |
| 41 | curr_date | 否 |  |  |
| 42 | curr_time | 否 |  |  |
| 43 | srp_operate_type | 否 |  |  |
| 44 | cancel_serialno | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | branch_no | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | impawn_asset_type | 否 |  |  |
| 50 | contract_id | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | seat_no | 否 |  |  |
| 54 | stock_property | 否 |  |  |
| 55 | stock_describe | 否 |  |  |
| 56 | post_amount | 否 |  |  |
| 57 | occur_amount | 否 |  |  |
| 58 | post_balance | 否 |  |  |
| 59 | occur_balance | 否 |  |  |
| 60 | remark | 否 |  |  |
| 61 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 62 | client_name | 否 | H |  |
| 63 | corp_client_group | 否 | H |  |
| 64 | client_group | 否 | H |  |
| 65 | room_code | 否 | H |  |
| 66 | asset_prop | 否 | H |  |
| 67 | limit_flag | 否 | H |  |
| 68 | client_prop | 否 | H |  |
| 69 | asset_level | 否 | H |  |
| 70 | risk_level | 否 | H |  |
| 71 | corp_risk_level | 否 | H |  |
| 72 | stock_name | 否 | H |  |
| 73 | stock_type | 否 | H |  |
| 74 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpassurejour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_srpassurejour_con | ART | 是 | contract_id, contract_id |
| uk_rpt_srpassurejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpassurejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_srpassurejour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_srpassurejour_con | ART | 是 | contract_id, contract_id |
| uk_rpt_srpassurejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpassurejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpassurejour | init_date, serial_no, init_date, serial_no |
| idx_srpassurejour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:54:09 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:33 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:54:09 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:33 | 3.0.3.1 | wuxd | 新增 |

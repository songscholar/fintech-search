# finexe_out_impawn - 融资行权场外质押明细表

**表对象ID**: 2626
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | impawn_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | out_impawn_type | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_type | 否 |  |  |
| 12 | impawn_amount | 否 |  |  |
| 13 | out_assure_value | 否 |  |  |
| 14 | out_impawn_status | 否 |  |  |
| 15 | assure_ratio | 否 |  |  |
| 16 | csdc_impawn_id | 否 |  |  |
| 17 | end_date | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | position_str | 否 |  | init_date(8)+serial_no(8) |
| 21 | client_name | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | client_group | 否 | H |  |
| 24 | room_code | 否 | H |  |
| 25 | asset_prop | 否 | H |  |
| 26 | limit_flag | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | stock_name | 否 | H |  |
| 32 | sub_stock_type | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | impawn_id | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | out_impawn_type | 否 |  |  |
| 40 | exchange_type | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | stock_type | 否 |  |  |
| 44 | impawn_amount | 否 |  |  |
| 45 | out_assure_value | 否 |  |  |
| 46 | out_impawn_status | 否 |  |  |
| 47 | assure_ratio | 否 |  |  |
| 48 | csdc_impawn_id | 否 |  |  |
| 49 | end_date | 否 |  |  |
| 50 | date_clear | 否 |  |  |
| 51 | remark | 否 |  |  |
| 52 | position_str | 否 |  | init_date(8)+serial_no(8) |
| 53 | client_name | 否 | H |  |
| 54 | corp_client_group | 否 | H |  |
| 55 | client_group | 否 | H |  |
| 56 | room_code | 否 | H |  |
| 57 | asset_prop | 否 | H |  |
| 58 | limit_flag | 否 | H |  |
| 59 | client_prop | 否 | H |  |
| 60 | asset_level | 否 | H |  |
| 61 | risk_level | 否 | H |  |
| 62 | corp_risk_level | 否 | H |  |
| 63 | stock_name | 否 | H |  |
| 64 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finoutimpawn | ART | 是 | impawn_id, impawn_id |
| idx_finoutimpawn_acct | ART | 是 | fund_account, fund_account |
| idx_finoutimpawn_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeoutimpawn | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeoutimpawn_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_finoutimpawn | ART | 是 | impawn_id, impawn_id |
| idx_finoutimpawn_acct | ART | 是 | fund_account, fund_account |
| idx_finoutimpawn_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeoutimpawn | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeoutimpawn_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finoutimpawn | impawn_id, impawn_id |
| idx_finoutimpawn | impawn_id, impawn_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:55:12 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:18 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:55:12 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:18 | 3.0.3.1 | wuxd | 新增 |

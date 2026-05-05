# bad_fine_interest - 融资行权坏账罚息表

**表对象ID**: 2625
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | bad_fine_balance | 否 |  |  |
| 6 | repaid_bad_fine_balance | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | client_name | 否 | H |  |
| 9 | corp_client_group | 否 | H |  |
| 10 | client_group | 否 | H |  |
| 11 | room_code | 否 | H |  |
| 12 | asset_prop | 否 | H |  |
| 13 | limit_flag | 否 | H |  |
| 14 | client_prop | 否 | H |  |
| 15 | asset_level | 否 | H |  |
| 16 | risk_level | 否 | H |  |
| 17 | corp_risk_level | 否 | H |  |
| 18 | init_date | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | bad_fine_balance | 否 |  |  |
| 23 | repaid_bad_fine_balance | 否 |  |  |
| 24 | date_clear | 否 |  |  |
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

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_badfineinterest | ART | 是 | client_id, fund_account, client_id, fund_account |
| uk_rpt_badfineinterest | ART | 是 | init_date, client_id, fund_account, init_date, client_id, fund_account |
| idx_rpt_badfineinterest_tolast | ART | 是 | date_clear, date_clear |
| idx_badfineinterest | ART | 是 | client_id, fund_account, client_id, fund_account |
| uk_rpt_badfineinterest | ART | 是 | init_date, client_id, fund_account, init_date, client_id, fund_account |
| idx_rpt_badfineinterest_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_badfineinterest | client_id, fund_account, client_id, fund_account |
| idx_badfineinterest | client_id, fund_account, client_id, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:54:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:26 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:54:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:26 | 3.0.3.1 | wuxd | 新增 |

# bad_fine_interest_jour - 融资行权坏账罚息流水表

**表对象ID**: 2633
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | occur_balance | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 9 | client_name | 否 | H |  |
| 10 | corp_client_group | 否 | H |  |
| 11 | client_group | 否 | H |  |
| 12 | room_code | 否 | H |  |
| 13 | asset_prop | 否 | H |  |
| 14 | limit_flag | 否 | H |  |
| 15 | client_prop | 否 | H |  |
| 16 | asset_level | 否 | H |  |
| 17 | risk_level | 否 | H |  |
| 18 | corp_risk_level | 否 | H |  |
| 19 | init_date | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | occur_balance | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 27 | client_name | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | client_prop | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | risk_level | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_badfineinterestjour | ART | 是 | position_str, position_str |
| idx_badfineinterestjour_a | ART | 是 | fund_account, fund_account |
| uk_rpt_badfineinterestjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_badfineinterestjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_badfineinterestjour | ART | 是 | position_str, position_str |
| idx_badfineinterestjour_a | ART | 是 | fund_account, fund_account |
| uk_rpt_badfineinterestjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_badfineinterestjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_badfineinterestjour | position_str, position_str |
| idx_badfineinterestjour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:57:33 | V3.0.2.79 | T202601134655 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:19 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:57:33 | V3.0.2.79 | T202601134655 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:19 | 3.0.3.1 | wuxd | 新增 |

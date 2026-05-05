# srp_adv_reg - 股票质押预约借款登记表

**表对象ID**: 2629
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | funder_no | 否 |  |  |
| 6 | entrust_date | 否 |  |  |
| 7 | fin_balance | 否 |  |  |
| 8 | entrust_balance | 否 |  |  |
| 9 | srp_kind | 否 |  |  |
| 10 | deal_status | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | position_str | 否 |  | entrust_date(8)+funder_no(10)+srp_kind(2)+fund_account(18)+s |
| 13 | adv_frozen_balance | 否 |  |  |
| 14 | adv_frozen_ratio | 否 |  |  |
| 15 | real_balance | 否 |  |  |
| 16 | serial_no | 否 |  |  |
| 17 | client_name | 否 | H |  |
| 18 | corp_client_group | 否 | H |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | funder_no | 否 |  |  |
| 31 | entrust_date | 否 |  |  |
| 32 | fin_balance | 否 |  |  |
| 33 | entrust_balance | 否 |  |  |
| 34 | srp_kind | 否 |  |  |
| 35 | deal_status | 否 |  |  |
| 36 | date_clear | 否 |  |  |
| 37 | position_str | 否 |  | entrust_date(8)+funder_no(10)+srp_kind(2)+fund_account(18)+s |
| 38 | adv_frozen_balance | 否 |  |  |
| 39 | adv_frozen_ratio | 否 |  |  |
| 40 | real_balance | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | client_name | 否 | H |  |
| 43 | corp_client_group | 否 | H |  |
| 44 | client_group | 否 | H |  |
| 45 | room_code | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | client_prop | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpadvreg | ART | 是 | position_str, position_str |
| idx_srpadvreg_acct | ART | 是 | fund_account, fund_account |
| idx_srpadvreg_id | ART | 是 | client_id, client_id |
| uk_rpt_srpadvreg | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpadvreg_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpadvreg_tolast | ART | 是 | date_clear, date_clear |
| idx_srpadvreg | ART | 是 | position_str, position_str |
| idx_srpadvreg_acct | ART | 是 | fund_account, fund_account |
| idx_srpadvreg_id | ART | 是 | client_id, client_id |
| uk_rpt_srpadvreg | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpadvreg_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpadvreg_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpadvreg | position_str, position_str |
| idx_srpadvreg | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:56:22 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:54 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:56:22 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:54 | 3.0.3.1 | wuxd | 新增 |

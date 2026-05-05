# srp_fpre_clear - 股票质押融出方预入账表

**表对象ID**: 2611
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | funder_no | 否 |  |  |
| 10 | funder_name | 否 |  |  |
| 11 | contract_id | 否 |  |  |
| 12 | clear_balance | 否 |  |  |
| 13 | business_flag | 否 |  |  |
| 14 | deal_flag | 否 |  |  |
| 15 | date_clear | 否 |  |  |
| 16 | position_str | 否 |  | init_date(8)+serial_no(10) |
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
| 27 | init_date | 否 |  |  |
| 28 | serial_no | 否 |  |  |
| 29 | curr_date | 否 |  |  |
| 30 | curr_time | 否 |  |  |
| 31 | branch_no | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | funder_no | 否 |  |  |
| 36 | funder_name | 否 |  |  |
| 37 | contract_id | 否 |  |  |
| 38 | clear_balance | 否 |  |  |
| 39 | business_flag | 否 |  |  |
| 40 | deal_flag | 否 |  |  |
| 41 | date_clear | 否 |  |  |
| 42 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 43 | client_name | 否 | H |  |
| 44 | corp_client_group | 否 | H |  |
| 45 | client_group | 否 | H |  |
| 46 | room_code | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | client_prop | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_risk_level | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpfpreclear | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpfpreclear_con | ART | 是 | contract_id, contract_id |
| idx_srpfpreclear_id | ART | 是 | client_id, client_id |
| idx_srpfpreclear_acct | ART | 是 | fund_account, fund_account |
| idx_srpfpreclear_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpfpreclear | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpfpreclear_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_srpfpreclear | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpfpreclear_con | ART | 是 | contract_id, contract_id |
| idx_srpfpreclear_id | ART | 是 | client_id, client_id |
| idx_srpfpreclear_acct | ART | 是 | fund_account, fund_account |
| idx_srpfpreclear_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpfpreclear | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpfpreclear_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpfpreclear_pos | position_str, position_str |
| idx_srpfpreclear_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:48:22 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:50 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:48:22 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:50 | 3.0.3.1 | wuxd | 新增 |

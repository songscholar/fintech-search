# finexe_dictate - 融资行权指令信息表

**表对象ID**: 2631
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | op_branch_no | 否 |  |  |
| 4 | operator_no | 否 |  |  |
| 5 | op_entrust_way | 否 |  |  |
| 6 | op_station | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | dictate_applicant | 否 |  |  |
| 11 | apply_date | 否 |  |  |
| 12 | apply_time | 否 |  |  |
| 13 | dictate_closer | 否 |  |  |
| 14 | close_date | 否 |  |  |
| 15 | close_time | 否 |  |  |
| 16 | finexe_dictate_type | 否 |  |  |
| 17 | finexe_dictate_status | 否 |  |  |
| 18 | limit_days | 否 |  |  |
| 19 | date_clear | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  | init_date(8)+serial_no(10)+fund_account(18) |
| 22 | transaction_no | 否 |  |  |
| 23 | client_name | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_prop | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | op_branch_no | 否 |  |  |
| 36 | operator_no | 否 |  |  |
| 37 | op_entrust_way | 否 |  |  |
| 38 | op_station | 否 |  |  |
| 39 | fund_account | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | dictate_applicant | 否 |  |  |
| 43 | apply_date | 否 |  |  |
| 44 | apply_time | 否 |  |  |
| 45 | dictate_closer | 否 |  |  |
| 46 | close_date | 否 |  |  |
| 47 | close_time | 否 |  |  |
| 48 | finexe_dictate_type | 否 |  |  |
| 49 | finexe_dictate_status | 否 |  |  |
| 50 | limit_days | 否 |  |  |
| 51 | date_clear | 否 |  |  |
| 52 | remark | 否 |  |  |
| 53 | position_str | 否 |  | init_date(8)+serial_no(10)+fund_account(18) |
| 54 | transaction_no | 否 |  |  |
| 55 | client_name | 否 | H |  |
| 56 | corp_client_group | 否 | H |  |
| 57 | client_group | 否 | H |  |
| 58 | room_code | 否 | H |  |
| 59 | asset_prop | 否 | H |  |
| 60 | limit_flag | 否 | H |  |
| 61 | client_prop | 否 | H |  |
| 62 | asset_level | 否 | H |  |
| 63 | risk_level | 否 | H |  |
| 64 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexedictate | ART | 是 | position_str, position_str |
| idx_finexedictate_id | ART | 是 | client_id, client_id |
| idx_finexedictate_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_finexedictate | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexedictate_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_finexedictate_tolast | ART | 是 | date_clear, date_clear |
| idx_finexedictate | ART | 是 | position_str, position_str |
| idx_finexedictate_id | ART | 是 | client_id, client_id |
| idx_finexedictate_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_finexedictate | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexedictate_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_finexedictate_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexedictate | position_str, position_str |
| idx_finexedictate | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:57:09 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:35 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:57:09 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:35 | 3.0.3.1 | wuxd | 新增 |

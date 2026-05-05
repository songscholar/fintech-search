# arp_crquota_jour - 约定购回授信流水表

**表对象ID**: 2605
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 78 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | business_flag | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | arp_credit_quota | 否 |  |  |
| 15 | arp_credit_rate | 否 |  |  |
| 16 | break_times | 否 |  |  |
| 17 | risk_rate | 否 |  |  |
| 18 | cbpacct_type | 否 |  |  |
| 19 | en_cbpbusi_type | 否 |  |  |
| 20 | allow_break_times | 否 |  |  |
| 21 | curr_break_times | 否 |  |  |
| 22 | blacklist_flag | 否 |  |  |
| 23 | black_times | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 26 | remark | 否 |  |  |
| 27 | self_credit_quota | 否 |  |  |
| 28 | papercont_id | 否 |  |  |
| 29 | valid_date | 否 |  |  |
| 30 | client_name | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | client_group | 否 | H |  |
| 33 | room_code | 否 | H |  |
| 34 | asset_prop | 否 | H |  |
| 35 | limit_flag | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | risk_level | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | init_date | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | curr_date | 否 |  |  |
| 43 | curr_time | 否 |  |  |
| 44 | op_branch_no | 否 |  |  |
| 45 | operator_no | 否 |  |  |
| 46 | op_station | 否 |  |  |
| 47 | op_entrust_way | 否 |  |  |
| 48 | branch_no | 否 |  |  |
| 49 | business_flag | 否 |  |  |
| 50 | fund_account | 否 |  |  |
| 51 | client_id | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | arp_credit_quota | 否 |  |  |
| 54 | arp_credit_rate | 否 |  |  |
| 55 | break_times | 否 |  |  |
| 56 | risk_rate | 否 |  |  |
| 57 | cbpacct_type | 否 |  |  |
| 58 | en_cbpbusi_type | 否 |  |  |
| 59 | allow_break_times | 否 |  |  |
| 60 | curr_break_times | 否 |  |  |
| 61 | blacklist_flag | 否 |  |  |
| 62 | black_times | 否 |  |  |
| 63 | date_clear | 否 |  |  |
| 64 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 65 | remark | 否 |  |  |
| 66 | self_credit_quota | 否 |  |  |
| 67 | papercont_id | 否 |  |  |
| 68 | valid_date | 否 |  |  |
| 69 | client_name | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | client_group | 否 | H |  |
| 72 | room_code | 否 | H |  |
| 73 | asset_prop | 否 | H |  |
| 74 | limit_flag | 否 | H |  |
| 75 | client_prop | 否 | H |  |
| 76 | asset_level | 否 | H |  |
| 77 | risk_level | 否 | H |  |
| 78 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpcrquotajour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_arpcrquotajour_acct | ART | 是 | fund_account, fund_account |
| idx_arpcrquotajour_cbpbusi | ART | 是 | en_cbpbusi_type, en_cbpbusi_type |
| uk_rpt_arpcrquotajour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpcrquotajour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_arpcrquotajour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_arpcrquotajour_acct | ART | 是 | fund_account, fund_account |
| idx_arpcrquotajour_cbpbusi | ART | 是 | en_cbpbusi_type, en_cbpbusi_type |
| uk_rpt_arpcrquotajour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpcrquotajour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpcrquotajour | init_date, serial_no, init_date, serial_no |
| idx_arpcrquotajour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:45:28 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-26 17:00:32 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:11 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:45:28 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-08-26 17:00:32 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:11 | 3.0.3.1 | wuxd | 新增 |

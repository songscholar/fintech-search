# arp_acct_arg_jour - 约定购回客户综合设置流水表

**表对象ID**: 2533
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | op_entrust_way | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | en_entrust_way | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | position_str | 否 |  | 定位串 init_date(8)+serial_no(10) |
| 16 | client_name | 否 | H |  |
| 17 | corp_client_group | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | serial_no | 否 |  |  |
| 28 | curr_date | 否 |  |  |
| 29 | curr_time | 否 |  |  |
| 30 | op_branch_no | 否 |  |  |
| 31 | op_entrust_way | 否 |  |  |
| 32 | op_station | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | money_type | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | client_id | 否 |  |  |
| 37 | en_entrust_way | 否 |  |  |
| 38 | date_clear | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | position_str | 否 |  | 定位串 init_date(8)+serial_no(10) |
| 41 | client_name | 否 | H |  |
| 42 | corp_client_group | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | client_prop | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpacctargjour_pos | ART | 是 | position_str, position_str |
| idx_arpacctargjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpacctargjour_acct | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_arpacctargjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpacctargjour_cid  | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_arpacctargjour_tolast | ART | 是 | date_clear, date_clear |
| idx_arpacctargjour_pos | ART | 是 | position_str, position_str |
| idx_arpacctargjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_arpacctargjour_acct | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_arpacctargjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_arpacctargjour_cid  | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_arpacctargjour_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpacctargjour_pos | position_str, position_str |
| idx_arpacctargjour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:21:34 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-11-19 13:41:24 | V3.0.2.1 | 洪略 | 补充资源 |
| 2024-12-06 16:04:18 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 16:21:34 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-11-19 13:41:24 | V3.0.2.1 | 洪略 | 补充资源 |
| 2024-12-06 16:04:18 | V3.0.2.1009 | 黄积冲 | 新增表 |

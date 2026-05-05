# fund_x_jour - 其他资金流水表

**表对象ID**: 5970
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_time | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | op_branch_no | 否 |  |  |
| 11 | operator_no | 否 |  |  |
| 12 | op_station | 否 |  |  |
| 13 | op_entrust_way | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | bank_no | 否 |  |  |
| 16 | occur_balance | 否 |  |  |
| 17 | post_balance | 否 |  |  |
| 18 | join_date | 否 |  |  |
| 19 | join_serial_no | 否 |  |  |
| 20 | check_string | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | real_status | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | risk_level | 否 | H |  |
| 29 | corp_client_group | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | client_name | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | money_type | 否 |  |  |
| 38 | exchange_type | 否 |  |  |
| 39 | curr_date | 否 |  |  |
| 40 | curr_time | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | op_branch_no | 否 |  |  |
| 43 | operator_no | 否 |  |  |
| 44 | op_station | 否 |  |  |
| 45 | op_entrust_way | 否 |  |  |
| 46 | branch_no | 否 |  |  |
| 47 | bank_no | 否 |  |  |
| 48 | occur_balance | 否 |  |  |
| 49 | post_balance | 否 |  |  |
| 50 | join_date | 否 |  |  |
| 51 | join_serial_no | 否 |  |  |
| 52 | check_string | 否 |  |  |
| 53 | remark | 否 |  |  |
| 54 | real_status | 否 |  |  |
| 55 | position_str | 否 |  |  |
| 56 | client_group | 否 | H |  |
| 57 | room_code | 否 | H |  |
| 58 | asset_prop | 否 | H |  |
| 59 | limit_flag | 否 | H |  |
| 60 | risk_level | 否 | H |  |
| 61 | corp_client_group | 否 | H |  |
| 62 | corp_risk_level | 否 | H |  |
| 63 | asset_level | 否 | H |  |
| 64 | client_name | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fundxjour | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_fundxjour_pos | ART | 是 | position_str, position_str |
| idx_fundxjour_id | ART | 是 | client_id, client_id |
| idx_fundxjour_acct | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_rpt_fundxjour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_fundxjour_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_rpt_fundxjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_fundxjour | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_fundxjour_pos | ART | 是 | position_str, position_str |
| idx_fundxjour_id | ART | 是 | client_id, client_id |
| idx_fundxjour_acct | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_rpt_fundxjour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_fundxjour_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_rpt_fundxjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundxjour | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_fundxjour | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:32:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-06 15:45:12 | 3.0.2.64 | 洪略 |  |
| 2025-03-22 17:46:57 | V3.0.2.2001 | 高志强 | 新增 |
| 2024-11-29 16:58:02 | 3.0.2.51 | 范文浩 | 物理表fund_x_jour，添加了表字段(init_date);
物理表fund_x_jour，添加了表字段(ser... |
| 2026-03-04 16:32:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-06 15:45:12 | 3.0.2.64 | 洪略 |  |
| 2025-03-22 17:46:57 | V3.0.2.2001 | 高志强 | 新增 |
| 2024-11-29 16:58:02 | 3.0.2.51 | 范文浩 | 物理表fund_x_jour，添加了表字段(init_date);
物理表fund_x_jour，添加了表字段(ser... |

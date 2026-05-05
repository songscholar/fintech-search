# brp_contract_ext_jour - 债券质押协议回购合约扩展流水表

**表对象ID**: 2345
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | operator_no | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | op_station | 否 |  |  |
| 10 | business_flag | 否 |  |  |
| 11 | join_position_str | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | orig_report_id | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 20 | stock_property | 否 |  |  |
| 21 | client_id | 否 | H |  |
| 22 | client_name | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | asset_level | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_risk_level | 否 | H |  |
| 32 | init_date | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | curr_date | 否 |  |  |
| 36 | curr_time | 否 |  |  |
| 37 | op_branch_no | 否 |  |  |
| 38 | operator_no | 否 |  |  |
| 39 | op_entrust_way | 否 |  |  |
| 40 | op_station | 否 |  |  |
| 41 | business_flag | 否 |  |  |
| 42 | join_position_str | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | stock_account | 否 |  |  |
| 45 | exchange_type | 否 |  |  |
| 46 | orig_report_id | 否 |  |  |
| 47 | stock_code | 否 |  |  |
| 48 | occur_amount | 否 |  |  |
| 49 | remark | 否 |  |  |
| 50 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 51 | stock_property | 否 |  |  |
| 52 | client_id | 否 | H |  |
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

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_brpconextjour_id | 默认 | 否 |  |
| idx_brpconextjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_brpconextjour_pos | ART | 是 | position_str, position_str |
| idx_brpconextjour_con | ART | 是 | join_position_str, join_position_str |
| idx_brpconextjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_brpcontractextjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_brpcontractextjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_brpconextjour_id | 默认 | 否 |  |
| idx_brpconextjour_id | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_brpconextjour_pos | ART | 是 | position_str, position_str |
| idx_brpconextjour_con | ART | 是 | join_position_str, join_position_str |
| idx_brpconextjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_brpcontractextjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_brpcontractextjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_brpconextjour_id | init_date, serial_no, init_date, serial_no |
| idx_brpconextjour_id | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:34:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 15:20:18 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:34:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 15:20:18 | V3.0.2.1007 | 张明月 | 新增 |

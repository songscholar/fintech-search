# uqms_fund_revert_jour - 资金反向操作流水

**表对象ID**: 1005
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_microtime | 否 |  |  |
| 7 | business_flag | 否 |  |  |
| 8 | op_branch_no | 否 |  |  |
| 9 | operator_no | 否 |  |  |
| 10 | op_station | 否 |  |  |
| 11 | occur_balance | 否 |  |  |
| 12 | post_balance | 否 |  |  |
| 13 | treat_status | 否 |  |  |
| 14 | valid_date | 否 |  |  |
| 15 | frozen_reason | 否 |  |  |
| 16 | join_serial_no | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | asset_prop | 否 | H |  |
| 22 | limit_flag | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | client_name | 否 | H |  |
| 28 | client_id | 否 | H |  |
| 29 | branch_no | 否 | H |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | money_type | 否 |  |  |
| 34 | curr_date | 否 |  |  |
| 35 | curr_microtime | 否 |  |  |
| 36 | business_flag | 否 |  |  |
| 37 | op_branch_no | 否 |  |  |
| 38 | operator_no | 否 |  |  |
| 39 | op_station | 否 |  |  |
| 40 | occur_balance | 否 |  |  |
| 41 | post_balance | 否 |  |  |
| 42 | treat_status | 否 |  |  |
| 43 | valid_date | 否 |  |  |
| 44 | frozen_reason | 否 |  |  |
| 45 | join_serial_no | 否 |  |  |
| 46 | remark | 否 |  |  |
| 47 | position_str | 否 |  |  |
| 48 | client_group | 否 | H |  |
| 49 | room_code | 否 | H |  |
| 50 | asset_prop | 否 | H |  |
| 51 | limit_flag | 否 | H |  |
| 52 | risk_level | 否 | H |  |
| 53 | corp_client_group | 否 | H |  |
| 54 | corp_risk_level | 否 | H |  |
| 55 | asset_level | 否 | H |  |
| 56 | client_name | 否 | H |  |
| 57 | client_id | 否 | H |  |
| 58 | branch_no | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_fund_revert_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_uqmsfundrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsfundrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uqmstfundrevertjour_tolast | ART | 是 | valid_date, valid_date |
| uk_uqms_fund_revert_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_uqmsfundrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsfundrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uqmstfundrevertjour_tolast | ART | 是 | valid_date, valid_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_fund_revert_jour | init_date, serial_no, init_date, serial_no |
| idx_uqms_fund_revert_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:53:30 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-05 19:25:42 | 3.0.6.24 | 洪略 | 增加历史表 |
| 2025-09-19 09:35:24 | 3.0.2.10 | huangzh | 所有表uqms_fund_revert_jour，删除了表字段（cashgroup_no）；
所有表uqms_fund... |
| 2025-06-20 11:06:23 | 3.0.2.9 | huangzh | 物理表uqms_fund_revert_jour，添加了表字段(position_str);
物理表uqms_fund... |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:53:30 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-05 19:25:42 | 3.0.6.24 | 洪略 | 增加历史表 |
| 2025-09-19 09:35:24 | 3.0.2.10 | huangzh | 所有表uqms_fund_revert_jour，删除了表字段（cashgroup_no）；
所有表uqms_fund... |
| 2025-06-20 11:06:23 | 3.0.2.9 | huangzh | 物理表uqms_fund_revert_jour，添加了表字段(position_str);
物理表uqms_fund... |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

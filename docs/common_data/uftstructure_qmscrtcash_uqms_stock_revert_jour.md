# uqms_stock_revert_jour - 股份反向操作流水

**表对象ID**: 1006
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

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
| 11 | occur_amount | 否 |  |  |
| 12 | treat_status | 否 |  |  |
| 13 | valid_date | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | frozen_reason | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | risk_level | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | corp_risk_level | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | client_name | 否 | H |  |
| 26 | client_prop | 否 | H |  |
| 27 | sub_stock_type | 否 | H |  |
| 28 | stock_name | 否 | H |  |
| 29 | branch_no | 否 | H |  |
| 30 | client_id | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | serial_no | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | money_type | 否 |  |  |
| 35 | curr_date | 否 |  |  |
| 36 | curr_microtime | 否 |  |  |
| 37 | business_flag | 否 |  |  |
| 38 | op_branch_no | 否 |  |  |
| 39 | operator_no | 否 |  |  |
| 40 | op_station | 否 |  |  |
| 41 | occur_amount | 否 |  |  |
| 42 | treat_status | 否 |  |  |
| 43 | valid_date | 否 |  |  |
| 44 | stock_type | 否 |  |  |
| 45 | frozen_reason | 否 |  |  |
| 46 | stock_code | 否 |  |  |
| 47 | exchange_type | 否 |  |  |
| 48 | position_str | 否 |  |  |
| 49 | asset_prop | 否 | H |  |
| 50 | limit_flag | 否 | H |  |
| 51 | risk_level | 否 | H |  |
| 52 | corp_client_group | 否 | H |  |
| 53 | corp_risk_level | 否 | H |  |
| 54 | asset_level | 否 | H |  |
| 55 | client_name | 否 | H |  |
| 56 | client_prop | 否 | H |  |
| 57 | sub_stock_type | 否 | H |  |
| 58 | stock_name | 否 | H |  |
| 59 | branch_no | 否 | H |  |
| 60 | client_id | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_stock_revert_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_uqmsstockrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsstockrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uqmsstockrevertjour_tolast | ART | 是 | valid_date, valid_date |
| uk_uqms_stock_revert_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_uqmsstockrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uqmsstockrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uqmsstockrevertjour_tolast | ART | 是 | valid_date, valid_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_stock_revert_jour | init_date, serial_no, init_date, serial_no |
| idx_uqms_stock_revert_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:53:53 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-06 18:00:05 | 3.0.2.24 | 洪略 | 增加历史表 |
| 2025-09-19 09:36:03 | 3.0.2.10 | huangzh | 所有表uqms_stock_revert_jour，删除了表字段（cashgroup_no）；
所有表uqms_sto... |
| 2025-06-19 10:17:35 | 3.0.2.8 | huangzh | 物理表uqms_stock_revert_jour，添加了表字段(stock_code);
物理表uqms_stock... |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:53:53 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-11-06 18:00:05 | 3.0.2.24 | 洪略 | 增加历史表 |
| 2025-09-19 09:36:03 | 3.0.2.10 | huangzh | 所有表uqms_stock_revert_jour，删除了表字段（cashgroup_no）；
所有表uqms_sto... |
| 2025-06-19 10:17:35 | 3.0.2.8 | huangzh | 物理表uqms_stock_revert_jour，添加了表字段(stock_code);
物理表uqms_stock... |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

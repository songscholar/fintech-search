# uqms_cash_fund_jour - 头寸资金流水表

**表对象ID**: 1002
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | cashgroup_no | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | occur_balance | 否 |  |  |
| 13 | post_balance | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | join_serial_no | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | real_action | 否 |  |  |
| 18 | position_str | 否 |  | init_date(8)+serial_no(8) |
| 19 | init_date | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | curr_date | 否 |  |  |
| 22 | curr_microtime | 否 |  |  |
| 23 | operator_no | 否 |  |  |
| 24 | op_branch_no | 否 |  |  |
| 25 | op_entrust_way | 否 |  |  |
| 26 | op_station | 否 |  |  |
| 27 | cashgroup_no | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | business_flag | 否 |  |  |
| 30 | occur_balance | 否 |  |  |
| 31 | post_balance | 否 |  |  |
| 32 | cancel_serial_no | 否 |  |  |
| 33 | join_serial_no | 否 |  |  |
| 34 | remark | 否 |  |  |
| 35 | real_action | 否 |  |  |
| 36 | position_str | 否 |  | init_date(8)+serial_no(8) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_cash_fund_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_fund_jour_cancelno | ART | 是 | cashgroup_no, money_type, cancel_serial_no, cashgroup_no, money_type, cancel_serial_no |
| uk_rpt_uqmscashfundjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_uqmscashfundjour_no | ART | 是 | init_date, cashgroup_no, init_date, cashgroup_no |
| uk_uqms_cash_fund_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_fund_jour_cancelno | ART | 是 | cashgroup_no, money_type, cancel_serial_no, cashgroup_no, money_type, cancel_serial_no |
| uk_rpt_uqmscashfundjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_uqmscashfundjour_no | ART | 是 | init_date, cashgroup_no, init_date, cashgroup_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_cash_fund_jour | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_fund_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:52:14 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 09:13:54 | V3.0.6.27 | 洪略 | 补充分区信息 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-16 17:18:24 | 3.0.6.8 | 周兆军 | 所有表uqms_cash_fund_jour，添加了表字段(position_str);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-21 17:48:01 | 0.3.3.140 | 程猛 | 增加字段real_action |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:52:14 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 09:13:54 | V3.0.6.27 | 洪略 | 补充分区信息 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-16 17:18:24 | 3.0.6.8 | 周兆军 | 所有表uqms_cash_fund_jour，添加了表字段(position_str);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-21 17:48:01 | 0.3.3.140 | 程猛 | 增加字段real_action |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

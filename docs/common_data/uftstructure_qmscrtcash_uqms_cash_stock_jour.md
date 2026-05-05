# uqms_cash_stock_jour - 头寸股份流水表

**表对象ID**: 1004
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 46 个）

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
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | business_flag | 否 |  |  |
| 14 | occur_amount | 否 |  |  |
| 15 | post_amount | 否 |  |  |
| 16 | cancel_serial_no | 否 |  |  |
| 17 | join_serial_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | real_action | 否 |  |  |
| 20 | real_buy_used_amount | 否 |  |  |
| 21 | position_str | 否 |  | init_date(8)+serial_no(8) |
| 22 | stock_name | 否 | H |  |
| 23 | sub_stock_type | 否 | H |  |
| 24 | init_date | 否 |  |  |
| 25 | serial_no | 否 |  |  |
| 26 | curr_date | 否 |  |  |
| 27 | curr_microtime | 否 |  |  |
| 28 | operator_no | 否 |  |  |
| 29 | op_branch_no | 否 |  |  |
| 30 | op_entrust_way | 否 |  |  |
| 31 | op_station | 否 |  |  |
| 32 | cashgroup_no | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | business_flag | 否 |  |  |
| 37 | occur_amount | 否 |  |  |
| 38 | post_amount | 否 |  |  |
| 39 | cancel_serial_no | 否 |  |  |
| 40 | join_serial_no | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | real_action | 否 |  |  |
| 43 | real_buy_used_amount | 否 |  |  |
| 44 | position_str | 否 |  | init_date(8)+serial_no(8) |
| 45 | stock_name | 否 | H |  |
| 46 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_cash_stock_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_stock_jour_cancel | ART | 是 | cashgroup_no, exchange_type, stock_code, cancel_serial_no, cashgroup_no, exchange_type, stock_code, cancel_serial_no |
| uk_rpt_uqmscashstockjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_uqmscashstockjour_no | ART | 是 | init_date, cashgroup_no, stock_code, exchange_type, init_date, cashgroup_no, stock_code, exchange_type |
| uk_uqms_cash_stock_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_stock_jour_cancel | ART | 是 | cashgroup_no, exchange_type, stock_code, cancel_serial_no, cashgroup_no, exchange_type, stock_code, cancel_serial_no |
| uk_rpt_uqmscashstockjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_uqmscashstockjour_no | ART | 是 | init_date, cashgroup_no, stock_code, exchange_type, init_date, cashgroup_no, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_cash_stock_jour | init_date, serial_no, init_date, serial_no |
| idx_uqms_cash_stock_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:53:08 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 09:15:17 | V3.0.6.27 | 洪略 | 补充分区信息 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-16 17:18:24 | 3.0.6.8 | 周兆军 | 所有表uqms_cash_fund_jour，添加了表字段(position_str);
 |
| 2025-08-06 11:05:22 | 3.0.6.23 | 黄佳平 | 索引ART优化 |
| 2025-06-23 16:55:05 | 3.0.2.8 | 王润雪 | 物理表uqms_cash_stock_jour，添加了表字段(real_buy_used_amount) |
| 2025-06-19 09:46:45 | 3.0.6.20 | 牟家乐 | 物理表uqms_cash_stock_jour，添加了表字段(real_buy_used_amount);
 |
| 2023-08-21 17:51:29 | 0.3.3.140 | 程猛 | 增加字段real_action |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:53:08 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 09:15:17 | V3.0.6.27 | 洪略 | 补充分区信息 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-16 17:18:24 | 3.0.6.8 | 周兆军 | 所有表uqms_cash_fund_jour，添加了表字段(position_str);
 |
| 2025-08-06 11:05:22 | 3.0.6.23 | 黄佳平 | 索引ART优化 |
| 2025-06-23 16:55:05 | 3.0.2.8 | 王润雪 | 物理表uqms_cash_stock_jour，添加了表字段(real_buy_used_amount) |

> 共 18 条修改记录，仅显示最近15条

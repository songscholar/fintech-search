# uopt_fundreal_jour - 期权资金变动表

**表对象ID**: 9603
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | trace_id | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | occur_balance | 否 |  |  |
| 10 | post_balance | 否 |  |  |
| 11 | real_action | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | real_serialno | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | position_str | 否 |  |  |
| 16 | fund_real_jour_kind | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | modify_fields | 否 |  |  |
| 19 | init_date | 否 |  |  |
| 20 | serial_no | 否 |  |  |
| 21 | trace_id | 否 |  |  |
| 22 | curr_date | 否 |  |  |
| 23 | curr_time | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | occur_balance | 否 |  |  |
| 28 | post_balance | 否 |  |  |
| 29 | real_action | 否 |  |  |
| 30 | business_flag | 否 |  |  |
| 31 | real_serialno | 否 |  |  |
| 32 | cancel_serial_no | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | fund_real_jour_kind | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | modify_fields | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fundrealjour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_fundrealjour_serial | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_fundrealjour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_fundrealjour_serial_temp | 默认 | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |
| idx_uopt_fundrealjour_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_fundrealjour_serial | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_fundrealjour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_fundrealjour_serial_temp | 默认 | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fundrealjour_serial | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |
| idx_uopt_fundrealjour_serial | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-13 16:03:32 | V3.0.2.17 | 张明月 | 所有表uopt_fundreal_jour，添加了表字段(fund_real_jour_kind);
 |
| 2025-07-25 16:54:26 | V3.0.2.1 | 汪迎 | 物理表uopt_fundreal_jour，添加了表字段(position_str);
,物理表uopt_fundre... |
| 2025-11-13 16:03:32 | V3.0.2.17 | 张明月 | 所有表uopt_fundreal_jour，添加了表字段(fund_real_jour_kind);
 |
| 2025-07-25 16:54:26 | V3.0.2.1 | 汪迎 | 物理表uopt_fundreal_jour，添加了表字段(position_str);
,物理表uopt_fundre... |

# uarg_useroper_log - 用户操作日志表

**表对象ID**: 107
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | function_id | 否 |  |  |
| 11 | operator_action | 否 |  |  |
| 12 | receipt_flag | 否 |  |  |
| 13 | oper_code | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | trade_account | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | occur_balance | 否 |  |  |
| 20 | join_date | 否 |  |  |
| 21 | join_serial_no | 否 |  |  |
| 22 | op_remark | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | audit_flag | 否 |  |  |
| 25 | audit_operator_no | 否 |  |  |
| 26 | audit_date | 否 |  |  |
| 27 | audit_time | 否 |  |  |
| 28 | menu_id | 否 |  |  |
| 29 | asset_prop | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | curr_date | 否 |  |  |
| 33 | curr_time | 否 |  |  |
| 34 | op_branch_no | 否 |  |  |
| 35 | operator_no | 否 |  |  |
| 36 | op_station | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | business_flag | 否 |  |  |
| 39 | function_id | 否 |  |  |
| 40 | operator_action | 否 |  |  |
| 41 | receipt_flag | 否 |  |  |
| 42 | oper_code | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | trade_account | 否 |  |  |
| 46 | occur_amount | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | occur_balance | 否 |  |  |
| 49 | join_date | 否 |  |  |
| 50 | join_serial_no | 否 |  |  |
| 51 | op_remark | 否 |  |  |
| 52 | position_str | 否 |  |  |
| 53 | audit_flag | 否 |  |  |
| 54 | audit_operator_no | 否 |  |  |
| 55 | audit_date | 否 |  |  |
| 56 | audit_time | 否 |  |  |
| 57 | menu_id | 否 |  |  |
| 58 | asset_prop | 否 |  |  |

## 索引（共 20 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_useroperlog | 默认 | 否 |  |
| idx_useroperlog_oper | 默认 | 否 |  |
| idx_useroperlog_page | 默认 | 否 |  |
| idx_useroperlog_bran | 默认 | 否 |  |
| idx_useroperlog_id | 默认 | 否 |  |
| idx_useroperlog | ART | 是 | position_str, position_str |
| idx_useroperlog_oper | ART | 是 | operator_no, operator_no |
| idx_rpt_useroperlog_page | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_useroperlog_bran | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_useroperlog_id | ART | 是 | init_date, operator_no, position_str, init_date, operator_no, position_str |
| idx_useroperlog | 默认 | 否 |  |
| idx_useroperlog_oper | 默认 | 否 |  |
| idx_useroperlog_page | 默认 | 否 |  |
| idx_useroperlog_bran | 默认 | 否 |  |
| idx_useroperlog_id | 默认 | 否 |  |
| idx_useroperlog | ART | 是 | position_str, position_str |
| idx_useroperlog_oper | ART | 是 | operator_no, operator_no |
| idx_rpt_useroperlog_page | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_useroperlog_bran | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_useroperlog_id | ART | 是 | init_date, operator_no, position_str, init_date, operator_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_useroperlog | position_str, position_str |
| idx_useroperlog | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:21:59 | 3.0.2.103 | taocong45644 | 当前表uarg_useroper_log，修改了索引idx_useroperlog,索引字段修改为：(position_... |
| 2025-11-06 17:02:51 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-02-20 19:01:55 | 3.0.6.117 | 李想 | 新增 |
| 2025-12-01 15:21:59 | 3.0.2.103 | taocong45644 | 当前表uarg_useroper_log，修改了索引idx_useroperlog,索引字段修改为：(position_... |
| 2025-11-06 17:02:51 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-02-20 19:01:55 | 3.0.6.117 | 李想 | 新增 |

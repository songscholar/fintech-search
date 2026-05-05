# assunderly_loginfo - 担保标的行情转入日志表

**表对象ID**: 7090
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | loginfo_type | 否 |  |  |
| 7 | operator_no | 否 |  |  |
| 8 | op_branch_no | 否 |  |  |
| 9 | operation_flag | 否 |  |  |
| 10 | serial_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 13 | init_date | 否 |  |  |
| 14 | curr_date | 否 |  |  |
| 15 | curr_time | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | loginfo_type | 否 |  |  |
| 19 | operator_no | 否 |  |  |
| 20 | op_branch_no | 否 |  |  |
| 21 | operation_flag | 否 |  |  |
| 22 | serial_no | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assunderly_loginfo | ART | 是 | position_str, position_str |
| idx_assunderly_loginfo_type | ART | 是 | loginfo_type, loginfo_type |
| uk_rpt_assunderlyloginfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_assunderly_loginfo | ART | 是 | position_str, position_str |
| idx_assunderly_loginfo_type | ART | 是 | loginfo_type, loginfo_type |
| uk_rpt_assunderlyloginfo | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assunderly_loginfo | position_str, position_str |
| idx_assunderly_loginfo | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:08:57 | 3.0.6.59 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:08:57 | 3.0.6.59 | 李想 | 新增表 |

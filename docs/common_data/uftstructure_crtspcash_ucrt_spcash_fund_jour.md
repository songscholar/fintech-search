# ucrt_spcash_fund_jour - 客户专项头寸资金流水表

**表对象ID**: 8002
**所属模块**: crtspcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 34 个）

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
| 15 | remark | 否 |  |  |
| 16 | join_serial_no | 否 |  |  |
| 17 | real_action | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | curr_date | 否 |  |  |
| 21 | curr_microtime | 否 |  |  |
| 22 | operator_no | 否 |  |  |
| 23 | op_branch_no | 否 |  |  |
| 24 | op_entrust_way | 否 |  |  |
| 25 | op_station | 否 |  |  |
| 26 | cashgroup_no | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | business_flag | 否 |  |  |
| 29 | occur_balance | 否 |  |  |
| 30 | post_balance | 否 |  |  |
| 31 | cancel_serial_no | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | join_serial_no | 否 |  |  |
| 34 | real_action | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_spcash_fund_jour | ART | 是 | cashgroup_no, money_type, init_date, serial_no, cashgroup_no, money_type, init_date, serial_no |
| idx_ucrt_cash_fund_jour_cancelno | ART | 是 | cashgroup_no, money_type, cancel_serial_no, cashgroup_no, money_type, cancel_serial_no |
| uk_rpt_ucrtspcashfundjour | ART | 是 | init_date, cashgroup_no, serial_no, init_date, cashgroup_no, serial_no |
| idx_ucrt_spcash_fund_jour | ART | 是 | cashgroup_no, money_type, init_date, serial_no, cashgroup_no, money_type, init_date, serial_no |
| idx_ucrt_cash_fund_jour_cancelno | ART | 是 | cashgroup_no, money_type, cancel_serial_no, cashgroup_no, money_type, cancel_serial_no |
| uk_rpt_ucrtspcashfundjour | ART | 是 | init_date, cashgroup_no, serial_no, init_date, cashgroup_no, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_spcash_fund_jour | cashgroup_no, money_type, init_date, serial_no, cashgroup_no, money_type, init_date, serial_no |
| idx_ucrt_spcash_fund_jour | cashgroup_no, money_type, init_date, serial_no, cashgroup_no, money_type, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-21 17:46:02 | 0.3.3.140 | 程猛 | 增加字段real_action |
| 2023-08-16 20:58 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |
| 2023-06-10 16:57 | 0.0.0.7 | 徐世晗 | 表结构同步uqms |
| 2023-08-21 17:46:02 | 0.3.3.140 | 程猛 | 增加字段real_action |
| 2023-08-16 20:58 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |
| 2023-06-10 16:57 | 0.0.0.7 | 徐世晗 | 表结构同步uqms |

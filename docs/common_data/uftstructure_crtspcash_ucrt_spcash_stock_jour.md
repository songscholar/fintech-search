# ucrt_spcash_stock_jour - 客户专项头寸股份流水表

**表对象ID**: 8004
**所属模块**: crtspcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 42 个）

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
| 17 | remark | 否 |  |  |
| 18 | join_serial_no | 否 |  |  |
| 19 | real_action | 否 |  |  |
| 20 | stock_name | 否 | H |  |
| 21 | sub_stock_type | 否 | H |  |
| 22 | init_date | 否 |  |  |
| 23 | serial_no | 否 |  |  |
| 24 | curr_date | 否 |  |  |
| 25 | curr_microtime | 否 |  |  |
| 26 | operator_no | 否 |  |  |
| 27 | op_branch_no | 否 |  |  |
| 28 | op_entrust_way | 否 |  |  |
| 29 | op_station | 否 |  |  |
| 30 | cashgroup_no | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | stock_type | 否 |  |  |
| 34 | business_flag | 否 |  |  |
| 35 | occur_amount | 否 |  |  |
| 36 | post_amount | 否 |  |  |
| 37 | cancel_serial_no | 否 |  |  |
| 38 | remark | 否 |  |  |
| 39 | join_serial_no | 否 |  |  |
| 40 | real_action | 否 |  |  |
| 41 | stock_name | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_spcash_stock_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_ucrt_cash_stock_jour_cancel | ART | 是 | cashgroup_no, exchange_type, stock_code, cancel_serial_no, cashgroup_no, exchange_type, stock_code, cancel_serial_no |
| uk_rpt_ucrtspcashstockjour | ART | 是 | init_date, cashgroup_no, stock_code, exchange_type, serial_no, init_date, cashgroup_no, stock_code, exchange_type, serial_no |
| idx_ucrt_spcash_stock_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_ucrt_cash_stock_jour_cancel | ART | 是 | cashgroup_no, exchange_type, stock_code, cancel_serial_no, cashgroup_no, exchange_type, stock_code, cancel_serial_no |
| uk_rpt_ucrtspcashstockjour | ART | 是 | init_date, cashgroup_no, stock_code, exchange_type, serial_no, init_date, cashgroup_no, stock_code, exchange_type, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_spcash_stock_jour | init_date, serial_no, init_date, serial_no |
| idx_ucrt_spcash_stock_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-21 17:47:29 | 0.3.3.140 |  | 增加字段real_action |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-21 17:47:29 | 0.3.3.140 |  | 增加字段real_action |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

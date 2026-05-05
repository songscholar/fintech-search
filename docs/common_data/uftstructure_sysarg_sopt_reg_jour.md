# sopt_reg_jour - 自主行权股东名册流水表

**表对象ID**: 2362
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
| 8 | business_flag | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | holder_name | 否 |  |  |
| 12 | id_no | 否 |  |  |
| 13 | sopt_code | 否 |  |  |
| 14 | register_amount | 否 |  |  |
| 15 | confirm_amount | 否 |  |  |
| 16 | used_amount | 否 |  |  |
| 17 | frozen_amount | 否 |  |  |
| 18 | sopttax_kind | 否 |  |  |
| 19 | seat_no | 否 |  |  |
| 20 | executives_flag | 否 |  |  |
| 21 | stage_num | 否 |  |  |
| 22 | soptmatch_flag | 否 |  |  |
| 23 | soptreg_status | 否 |  |  |
| 24 | tax_months | 否 |  |  |
| 25 | sum_payable_tax | 否 |  |  |
| 26 | sum_paid_tax | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | position_str | 否 |  | curr_date(8)+serial_no(10) |
| 29 | execv_lock_ratio | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | curr_date | 否 |  |  |
| 33 | curr_time | 否 |  |  |
| 34 | op_branch_no | 否 |  |  |
| 35 | operator_no | 否 |  |  |
| 36 | op_station | 否 |  |  |
| 37 | business_flag | 否 |  |  |
| 38 | exchange_type | 否 |  |  |
| 39 | stock_account | 否 |  |  |
| 40 | holder_name | 否 |  |  |
| 41 | id_no | 否 |  |  |
| 42 | sopt_code | 否 |  |  |
| 43 | register_amount | 否 |  |  |
| 44 | confirm_amount | 否 |  |  |
| 45 | used_amount | 否 |  |  |
| 46 | frozen_amount | 否 |  |  |
| 47 | sopttax_kind | 否 |  |  |
| 48 | seat_no | 否 |  |  |
| 49 | executives_flag | 否 |  |  |
| 50 | stage_num | 否 |  |  |
| 51 | soptmatch_flag | 否 |  |  |
| 52 | soptreg_status | 否 |  |  |
| 53 | tax_months | 否 |  |  |
| 54 | sum_payable_tax | 否 |  |  |
| 55 | sum_paid_tax | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  | curr_date(8)+serial_no(10) |
| 58 | execv_lock_ratio | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_soptregjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_soptregjour_stkacct | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_soptregjour_pos | ART | 是 | position_str, position_str |
| idx_soptregjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_soptregjour_stkacct | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_soptregjour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_soptregjour | init_date, serial_no, init_date, serial_no |
| idx_soptregjour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-12-27 14:28:13 | V3.0.2.51 | 李江霖 | 增加position_str的备注 |
| 2025-01-14 19:45:33 | V3.0.2.50 | 杨森峰 | 不再回库 |
| 2025-01-09 17:59:16 | V3.0.2.49 | 杨涛 | 表作废，表结构保留。流水写入uqms_sopt_reg_jour |
| 2024-09-25 21:34:23 | V3.0.2.1008 | 张明月 | 新增 |
| 2024-12-27 14:28:13 | V3.0.2.51 | 李江霖 | 增加position_str的备注 |
| 2025-01-14 19:45:33 | V3.0.2.50 | 杨森峰 | 不再回库 |
| 2025-01-09 17:59:16 | V3.0.2.49 | 杨涛 | 表作废，表结构保留。流水写入uqms_sopt_reg_jour |
| 2024-09-25 21:34:23 | V3.0.2.1008 | 张明月 | 新增 |

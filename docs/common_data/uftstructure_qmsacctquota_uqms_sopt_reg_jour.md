# uqms_sopt_reg_jour - 额度管理自主行权股东名册流水表

**表对象ID**: 1617
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

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
| 28 | position_str | 否 |  |  |
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
| 57 | position_str | 否 |  |  |
| 58 | execv_lock_ratio | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_soptregjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_uqms_soptregjour_stkacct | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_uqms_soptregjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_uqmssoptregjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_uqms_soptregjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_uqms_soptregjour_stkacct | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_uqms_soptregjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_uqmssoptregjour | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_soptregjour | init_date, serial_no, init_date, serial_no |
| idx_uqms_soptregjour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:45:46 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-08 10:15:55 | 3.0.2.8 | 杨涛 | 新增 |
| 2026-03-05 16:45:46 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-08 10:15:55 | 3.0.2.8 | 杨涛 | 新增 |

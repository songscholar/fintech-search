# uqms_sopt_reg - 额度管理自主行权股东名册表

**表对象ID**: 1616
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | holder_name | 否 |  |  |
| 4 | id_kind | 否 |  |  |
| 5 | id_no | 否 |  |  |
| 6 | sopt_code | 否 |  |  |
| 7 | register_amount | 否 |  |  |
| 8 | confirm_amount | 否 |  |  |
| 9 | used_amount | 否 |  |  |
| 10 | frozen_amount | 否 |  |  |
| 11 | sopttax_kind | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | executives_flag | 否 |  |  |
| 14 | limitsell_days | 否 |  |  |
| 15 | soptmatch_flag | 否 |  |  |
| 16 | soptreg_status | 否 |  |  |
| 17 | tax_months | 否 |  |  |
| 18 | sum_payable_tax | 否 |  |  |
| 19 | sum_paid_tax | 否 |  |  |
| 20 | draw_tax | 否 |  |  |
| 21 | position_str | 否 |  | exchange_type+stock_account+sopt_code |
| 22 | execv_lock_ratio | 否 |  |  |
| 23 | use_date | 否 |  |  |
| 24 | sopttax_source | 否 |  |  |
| 25 | cont_entu_market_value_flag | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | holder_name | 否 |  |  |
| 32 | id_kind | 否 |  |  |
| 33 | id_no | 否 |  |  |
| 34 | sopt_code | 否 |  |  |
| 35 | register_amount | 否 |  |  |
| 36 | confirm_amount | 否 |  |  |
| 37 | used_amount | 否 |  |  |
| 38 | frozen_amount | 否 |  |  |
| 39 | sopttax_kind | 否 |  |  |
| 40 | seat_no | 否 |  |  |
| 41 | executives_flag | 否 |  |  |
| 42 | limitsell_days | 否 |  |  |
| 43 | soptmatch_flag | 否 |  |  |
| 44 | soptreg_status | 否 |  |  |
| 45 | tax_months | 否 |  |  |
| 46 | sum_payable_tax | 否 |  |  |
| 47 | sum_paid_tax | 否 |  |  |
| 48 | draw_tax | 否 |  |  |
| 49 | position_str | 否 |  | exchange_type+stock_account+sopt_code |
| 50 | execv_lock_ratio | 否 |  |  |
| 51 | use_date | 否 |  |  |
| 52 | sopttax_source | 否 |  |  |
| 53 | cont_entu_market_value_flag | 否 |  |  |
| 54 | transaction_no | 否 |  |  |
| 55 | update_date | 否 |  |  |
| 56 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_soptreg | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_uqms_soptreg_pos | ART | 是 | position_str, position_str |
| idx_uqms_soptreg | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_uqms_soptreg_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_soptreg | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_uqms_soptreg | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:45:04 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 10:22:42 | 3.0.6.1024 | 牟家乐 | 修改表不回库 |
| 2025-01-08 10:15:55 | 3.0.2.8 | 杨涛 | 新增 |
| 2026-03-05 16:45:04 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 10:22:42 | 3.0.6.1024 | 牟家乐 | 修改表不回库 |
| 2025-01-08 10:15:55 | 3.0.2.8 | 杨涛 | 新增 |

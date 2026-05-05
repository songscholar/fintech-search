# sopt_reg - 自主行权股东名册表

**表对象ID**: 2361
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

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
| 10 | frozen_amount | 否 |  | 作废 |
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
| 21 | position_str | 否 |  | stock_account(20)+sopt_code(8)+exchange_type(4) |
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
| 38 | frozen_amount | 否 |  | 作废 |
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
| 49 | position_str | 否 |  | stock_account(20)+sopt_code(8)+exchange_type(4) |
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
| idx_soptreg | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_soptreg_pos | ART | 是 | position_str, position_str |
| idx_soptreg | ART | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_soptreg_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_soptreg | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_soptreg | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-27 16:32:52 | 3.0.6.123 | 常行 | 物理表sopt_reg，添加了表字段(update_date);
物理表sopt_reg，添加了表字段(update_... |
| 2025-01-14 19:43:44 | V3.0.2.51 | 杨森峰 | sopt_reg表不再回库 |
| 2025-01-09 18:08:06 | V3.0.2.50 | 杨涛 | 此表frozen_amount字段作废，添加说明 |
| 2024-10-17 16:40:04 | 3.0.5.1001 | 董乾坤 | sopt_reg表从cbptrade移动到sysarg目录 |
| 2024-09-25 21:31:55 | V3.0.2.1008 | 张明月 | 新增 |
| 2025-02-27 16:32:52 | 3.0.6.123 | 常行 | 物理表sopt_reg，添加了表字段(update_date);
物理表sopt_reg，添加了表字段(update_... |
| 2025-01-14 19:43:44 | V3.0.2.51 | 杨森峰 | sopt_reg表不再回库 |
| 2025-01-09 18:08:06 | V3.0.2.50 | 杨涛 | 此表frozen_amount字段作废，添加说明 |
| 2024-10-17 16:40:04 | 3.0.5.1001 | 董乾坤 | sopt_reg表从cbptrade移动到sysarg目录 |
| 2024-09-25 21:31:55 | V3.0.2.1008 | 张明月 | 新增 |

# usps_sopt_code - 自主行权代码表

**表对象ID**: 2326
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | sopt_code | 否 |  |  |
| 3 | sopt_name | 否 |  |  |
| 4 | apply_code | 否 |  |  |
| 5 | source_code | 否 |  |  |
| 6 | grant_price | 否 |  |  |
| 7 | apply_price | 否 |  |  |
| 8 | apply_begin_date | 否 |  |  |
| 9 | apply_end_date | 否 |  |  |
| 10 | apply_unit | 否 |  |  |
| 11 | apply_low_amount | 否 |  |  |
| 12 | apply_high_amount | 否 |  |  |
| 13 | sopttax_kind | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | float_ratio | 否 |  |  |
| 16 | apply_status | 否 |  |  |
| 17 | sopt_report_code | 否 |  |  |
| 18 | sopt_tax_date | 否 |  |  |
| 19 | market_year | 否 |  |  |
| 20 | authority_times | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | exchange_type(4)+sopt_code(8) |
| 25 | exchange_type | 否 |  |  |
| 26 | sopt_code | 否 |  |  |
| 27 | sopt_name | 否 |  |  |
| 28 | apply_code | 否 |  |  |
| 29 | source_code | 否 |  |  |
| 30 | grant_price | 否 |  |  |
| 31 | apply_price | 否 |  |  |
| 32 | apply_begin_date | 否 |  |  |
| 33 | apply_end_date | 否 |  |  |
| 34 | apply_unit | 否 |  |  |
| 35 | apply_low_amount | 否 |  |  |
| 36 | apply_high_amount | 否 |  |  |
| 37 | sopttax_kind | 否 |  |  |
| 38 | seat_no | 否 |  |  |
| 39 | float_ratio | 否 |  |  |
| 40 | apply_status | 否 |  |  |
| 41 | sopt_report_code | 否 |  |  |
| 42 | sopt_tax_date | 否 |  |  |
| 43 | market_year | 否 |  |  |
| 44 | authority_times | 否 |  |  |
| 45 | transaction_no | 否 |  |  |
| 46 | update_date | 否 |  |  |
| 47 | update_time | 否 |  |  |
| 48 | position_str | 否 |  | exchange_type(4)+sopt_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_soptcode | ART | 是 | exchange_type, sopt_code, exchange_type, sopt_code |
| idx_soptcode | ART | 是 | exchange_type, sopt_code, exchange_type, sopt_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_soptcode | exchange_type, sopt_code, exchange_type, sopt_code |
| idx_soptcode | exchange_type, sopt_code, exchange_type, sopt_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 20:02:10 | 3.0.6.111 | 李想 | 物理表usps_sopt_code，添加了表字段(update_date);
物理表usps_sopt_code，添加... |
| 2024-10-15 09:44:02 | V3.0.5.1001 | 董乾坤 | usps_sopt_code表从cbptrade移动到sysarg目录，对象号由2326修改为94 |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |
| 2025-02-19 20:02:10 | 3.0.6.111 | 李想 | 物理表usps_sopt_code，添加了表字段(update_date);
物理表usps_sopt_code，添加... |
| 2024-10-15 09:44:02 | V3.0.5.1001 | 董乾坤 | usps_sopt_code表从cbptrade移动到sysarg目录，对象号由2326修改为94 |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |

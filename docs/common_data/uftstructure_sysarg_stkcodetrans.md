# stkcodetrans - 证券代码变换表

**表对象ID**: 368
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | register_date | 否 |  |  |
| 2 | curr_time | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | old_column_value | 否 |  |  |
| 6 | new_column_value | 否 |  |  |
| 7 | transform_type | 否 |  |  |
| 8 | deli_status | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | stock_name | 否 | H |  |
| 11 | stock_type | 否 | H |  |
| 12 | sub_stock_type | 否 | H |  |
| 13 | tohis_date | 否 | H |  |
| 14 | register_date | 否 |  |  |
| 15 | curr_time | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | old_column_value | 否 |  |  |
| 19 | new_column_value | 否 |  |  |
| 20 | transform_type | 否 |  |  |
| 21 | deli_status | 否 |  |  |
| 22 | date_clear | 否 |  |  |
| 23 | stock_name | 否 | H |  |
| 24 | stock_type | 否 | H |  |
| 25 | sub_stock_type | 否 | H |  |
| 26 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stkcodetrans | ART | 是 | register_date, curr_time, transform_type, exchange_type, stock_code, register_date, curr_time, transform_type, exchange_type, stock_code |
| idx_rpt_stkcodetrans | ART | 是 | tohis_date, register_date, curr_time, transform_type, exchange_type, stock_code, tohis_date, register_date, curr_time, transform_type, exchange_type, stock_code |
| idx_stkcodetrans | ART | 是 | register_date, curr_time, transform_type, exchange_type, stock_code, register_date, curr_time, transform_type, exchange_type, stock_code |
| idx_rpt_stkcodetrans | ART | 是 | tohis_date, register_date, curr_time, transform_type, exchange_type, stock_code, tohis_date, register_date, curr_time, transform_type, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stkcodetrans | register_date, curr_time, transform_type, exchange_type, stock_code, register_date, curr_time, transform_type, exchange_type, stock_code |
| idx_stkcodetrans | register_date, curr_time, transform_type, exchange_type, stock_code, register_date, curr_time, transform_type, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-04 09:21:47 | 3.0.2.88 | 杨森峰 |  |
| 2025-07-04 09:21:47 | 3.0.2.88 | 杨森峰 |  |

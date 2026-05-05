# usps_stknotice_info - 证券提示信息表

**表对象ID**: 29
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | notice_info | 否 |  |  |
| 4 | start_date | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | limit_times | 否 |  |  |
| 8 | sub_stock_type | 否 |  |  |
| 9 | notice_type | 否 |  |  |
| 10 | manage_reason | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+stock_code(8)+stock_type(4)+sub_stock_type( |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | notice_info | 否 |  |  |
| 18 | start_date | 否 |  |  |
| 19 | end_date | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | limit_times | 否 |  |  |
| 22 | sub_stock_type | 否 |  |  |
| 23 | notice_type | 否 |  |  |
| 24 | manage_reason | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | exchange_type(4)+stock_code(8)+stock_type(4)+sub_stock_type( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_stknotice_info | ART | 是 | stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date, stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date |
| idx_usps_stknotice_info | ART | 是 | stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date, stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_stknotice_info | stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date, stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date |
| idx_usps_stknotice_info | stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date, stock_code, exchange_type, stock_type, sub_stock_type, notice_type, start_date, end_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-07 10:43:25 | V3.0.2.53 | 洪略 | 和UF2.0的表结构保持一致 |
| 2025-02-19 15:05:47 | 3.0.6.92 | 李想 | 物理表usps_stknotice_info，添加了表字段(update_date);
物理表usps_stknoti... |
| 2025-02-07 10:43:25 | V3.0.2.53 | 洪略 | 和UF2.0的表结构保持一致 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-07 10:43:25 | V3.0.2.53 | 洪略 | 和UF2.0的表结构保持一致 |
| 2025-02-19 15:05:47 | 3.0.6.92 | 李想 | 物理表usps_stknotice_info，添加了表字段(update_date);
物理表usps_stknoti... |
| 2025-02-07 10:43:25 | V3.0.2.53 | 洪略 | 和UF2.0的表结构保持一致 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

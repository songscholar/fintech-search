# usps_cdr_fare - 存托服务费费率表

**表对象ID**: 36
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | sub_stock_type | 否 |  |  |
| 5 | cdr_fare_ratio | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | stock_code(8)+exchange_type(4)+stock_type(4)+sub_stock_type( |
| 10 | stock_code | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | sub_stock_type | 否 |  |  |
| 14 | cdr_fare_ratio | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | stock_code(8)+exchange_type(4)+stock_type(4)+sub_stock_type( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_cdr_fare | ART | 是 | stock_code, exchange_type, stock_type, sub_stock_type, stock_code, exchange_type, stock_type, sub_stock_type |
| idx_usps_cdr_fare | ART | 是 | stock_code, exchange_type, stock_type, sub_stock_type, stock_code, exchange_type, stock_type, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_cdr_fare | stock_code, exchange_type, stock_type, sub_stock_type, stock_code, exchange_type, stock_type, sub_stock_type |
| idx_usps_cdr_fare | stock_code, exchange_type, stock_type, sub_stock_type, stock_code, exchange_type, stock_type, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:16:58 | 3.0.6.98 | 李想 | 物理表usps_cdr_fare，添加了表字段(update_date);
物理表usps_cdr_fare，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-19 16:16:58 | 3.0.6.98 | 李想 | 物理表usps_cdr_fare，添加了表字段(update_date);
物理表usps_cdr_fare，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

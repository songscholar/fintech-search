# usps_stb_stkcode - 股转证券代码表

**表对象ID**: 31
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | issue_amount | 否 |  |  |
| 6 | modify_date | 否 |  |  |
| 7 | stb_issue_way | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | begin_date | 否 |  |  |
| 15 | end_date | 否 |  |  |
| 16 | issue_amount | 否 |  |  |
| 17 | modify_date | 否 |  |  |
| 18 | stb_issue_way | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_stb_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_stb_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_stb_stkcode | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_stb_stkcode | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 16:39:32 | 3.0.6.60 | 李想 | 物理表usps_stb_stkcode，添加了表字段(update_date);
物理表usps_stb_stkcod... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 16:39:32 | 3.0.6.60 | 李想 | 物理表usps_stb_stkcode，添加了表字段(update_date);
物理表usps_stb_stkcod... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

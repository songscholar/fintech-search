# usps_exit_stkcode - 退市证券代码表

**表对象ID**: 35
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | surplus_trade_date | 否 |  |  |
| 4 | modify_date | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | create_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | surplus_trade_date | 否 |  |  |
| 13 | modify_date | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | create_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_exit_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_exit_stkcode | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_exit_stkcode | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_exit_stkcode | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 09:55:14 | 3.0.2.85 | 乐闽庭 | 物理表usps_exit_stkcode，添加了表字段(create_date);
 |
| 2025-02-14 17:19:54 | 3.0.6.12 | 常行 | 物理表usps_exit_stkcode，添加了表字段(update_date);
物理表usps_exit_stkc... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-04-25 09:55:14 | 3.0.2.85 | 乐闽庭 | 物理表usps_exit_stkcode，添加了表字段(create_date);
 |
| 2025-02-14 17:19:54 | 3.0.6.12 | 常行 | 物理表usps_exit_stkcode，添加了表字段(update_date);
物理表usps_exit_stkc... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

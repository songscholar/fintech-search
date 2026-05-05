# usps_fjy_stkinfo - 非交易基础信息表

**表对象ID**: 49
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fjy_busi_type | 否 |  |  |
| 4 | begin_date | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | fjy_price | 否 |  |  |
| 7 | modify_date | 否 |  |  |
| 8 | low_amount | 否 |  |  |
| 9 | high_amount | 否 |  |  |
| 10 | fjy_rond_lot_unit | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+stock_code(8)+fjy_busi_type(4) |
| 15 | stock_code | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | fjy_busi_type | 否 |  |  |
| 18 | begin_date | 否 |  |  |
| 19 | end_date | 否 |  |  |
| 20 | fjy_price | 否 |  |  |
| 21 | modify_date | 否 |  |  |
| 22 | low_amount | 否 |  |  |
| 23 | high_amount | 否 |  |  |
| 24 | fjy_rond_lot_unit | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | exchange_type(4)+stock_code(8)+fjy_busi_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_fjy_stkinfo | ART | 是 | exchange_type, stock_code, fjy_busi_type, exchange_type, stock_code, fjy_busi_type |
| idx_usps_fjy_stkinfo | ART | 是 | exchange_type, stock_code, fjy_busi_type, exchange_type, stock_code, fjy_busi_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_fjy_stkinfo | exchange_type, stock_code, fjy_busi_type, exchange_type, stock_code, fjy_busi_type |
| idx_usps_fjy_stkinfo | exchange_type, stock_code, fjy_busi_type, exchange_type, stock_code, fjy_busi_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 16:49:31 | 3.0.6.62 | 李想 | 物理表usps_fjy_stkinfo，添加了表字段(update_date);
物理表usps_fjy_stkinf... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 16:49:31 | 3.0.6.62 | 李想 | 物理表usps_fjy_stkinfo，添加了表字段(update_date);
物理表usps_fjy_stkinf... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

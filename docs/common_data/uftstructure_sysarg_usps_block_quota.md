# usps_block_quota - 大宗交易限额表

**表对象ID**: 80
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | price_ratio | 否 |  |  |
| 4 | low_amount | 否 |  |  |
| 5 | low_balance | 否 |  |  |
| 6 | sub_stock_type | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | exchange_type(4)+stock_type(4)+sub_stock_type(4) |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | price_ratio | 否 |  |  |
| 14 | low_amount | 否 |  |  |
| 15 | low_balance | 否 |  |  |
| 16 | sub_stock_type | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | exchange_type(4)+stock_type(4)+sub_stock_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_blockquota | ART | 是 | exchange_type, stock_type, sub_stock_type, exchange_type, stock_type, sub_stock_type |
| idx_usps_blockquota | ART | 是 | exchange_type, stock_type, sub_stock_type, exchange_type, stock_type, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_blockquota | exchange_type, stock_type, sub_stock_type, exchange_type, stock_type, sub_stock_type |
| idx_usps_blockquota | exchange_type, stock_type, sub_stock_type, exchange_type, stock_type, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 15:20:56 | 3.0.6.94 | 李想 | 物理表usps_block_quota，添加了表字段(update_date);
物理表usps_block_quot... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-19 15:20:56 | 3.0.6.94 | 李想 | 物理表usps_block_quota，添加了表字段(update_date);
物理表usps_block_quot... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

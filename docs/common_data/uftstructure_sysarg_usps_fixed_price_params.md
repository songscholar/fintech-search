# usps_fixed_price_params - 盘后定价交易业务信息表

**表对象ID**: 30
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | buy_amount_max | 否 |  |  |
| 4 | sell_amount_max | 否 |  |  |
| 5 | buy_unit | 否 |  |  |
| 6 | sell_unit | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | buy_amount_max | 否 |  |  |
| 14 | sell_amount_max | 否 |  |  |
| 15 | buy_unit | 否 |  |  |
| 16 | sell_unit | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_fixed_price_params | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_fixed_price_params | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_fixed_price_params | exchange_type, stock_code, exchange_type, stock_code |
| idx_usps_fixed_price_params | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 16:32:39 | 3.0.6.59 | 李想 | 物理表usps_fixed_price_params，添加了表字段(update_date);
物理表usps_fix... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-18 16:32:39 | 3.0.6.59 | 李想 | 物理表usps_fixed_price_params，添加了表字段(update_date);
物理表usps_fix... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

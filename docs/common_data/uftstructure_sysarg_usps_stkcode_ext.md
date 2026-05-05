# usps_stkcode_ext - 证券代码扩展表

**表对象ID**: 27
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | bond_trade_type | 否 |  |  |
| 5 | high_price_step | 否 |  |  |
| 6 | up_price | 否 |  |  |
| 7 | down_price | 否 |  |  |
| 8 | high_amount_buy | 否 |  |  |
| 9 | high_amount_sell | 否 |  |  |
| 10 | low_amount_buy | 否 |  |  |
| 11 | low_amount_sell | 否 |  |  |
| 12 | buy_unit | 否 |  |  |
| 13 | sell_unit | 否 |  |  |
| 14 | tradestop_flag | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | call_auction_limit | 否 |  |  |
| 17 | cont_auction_limit | 否 |  |  |
| 18 | auction_limit_type | 否 |  |  |
| 19 | en_settle_type | 否 |  |  |
| 20 | modify_date | 否 |  |  |
| 21 | position_str | 否 |  | exchange_type(4)+stock_code(8)+bond_trade_type(4) |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | bond_trade_type | 否 |  |  |
| 26 | high_price_step | 否 |  |  |
| 27 | up_price | 否 |  |  |
| 28 | down_price | 否 |  |  |
| 29 | high_amount_buy | 否 |  |  |
| 30 | high_amount_sell | 否 |  |  |
| 31 | low_amount_buy | 否 |  |  |
| 32 | low_amount_sell | 否 |  |  |
| 33 | buy_unit | 否 |  |  |
| 34 | sell_unit | 否 |  |  |
| 35 | tradestop_flag | 否 |  |  |
| 36 | transaction_no | 否 |  |  |
| 37 | call_auction_limit | 否 |  |  |
| 38 | cont_auction_limit | 否 |  |  |
| 39 | auction_limit_type | 否 |  |  |
| 40 | en_settle_type | 否 |  |  |
| 41 | modify_date | 否 |  |  |
| 42 | position_str | 否 |  | exchange_type(4)+stock_code(8)+bond_trade_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_stkcodeext | ART | 是 | exchange_type, stock_code, bond_trade_type, exchange_type, stock_code, bond_trade_type |
| idx_usps_stkcodeext_stockcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_usps_stkcodeext | ART | 是 | exchange_type, stock_code, bond_trade_type, exchange_type, stock_code, bond_trade_type |
| idx_usps_stkcodeext_stockcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_stkcodeext | exchange_type, stock_code, bond_trade_type, exchange_type, stock_code, bond_trade_type |
| idx_usps_stkcodeext | exchange_type, stock_code, bond_trade_type, exchange_type, stock_code, bond_trade_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-04 20:37:17 | 3.0.2.94 | 高志强 | 所有表usps_stkcode_ext，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-01-06 16:15:07 | 3.0.2.51 | 周富安 | 物理表usps_stkcode_ext，添加了表字段(modify_date);
 |
| 2023-12-31 14:04:18 | V3.0.1.23 | 吴丽丽 | 物理表usps_stkcode_ext，添加了表字段(call_auction_limit);
物理表usps_stk... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-09-04 20:37:17 | 3.0.2.94 | 高志强 | 所有表usps_stkcode_ext，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-01-06 16:15:07 | 3.0.2.51 | 周富安 | 物理表usps_stkcode_ext，添加了表字段(modify_date);
 |
| 2023-12-31 14:04:18 | V3.0.1.23 | 吴丽丽 | 物理表usps_stkcode_ext，添加了表字段(call_auction_limit);
物理表usps_stk... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

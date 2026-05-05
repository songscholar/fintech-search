# product_basic_info_ext - 产品基础信息扩展表

**表对象ID**: 2512
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | bond_trade_type | 否 |  |  |
| 4 | begin_time | 否 |  |  |
| 5 | end_time | 否 |  |  |
| 6 | low_amount_buy | 否 |  |  |
| 7 | buy_unit | 否 |  |  |
| 8 | high_amount_buy | 否 |  |  |
| 9 | low_amount_sell | 否 |  |  |
| 10 | sell_unit | 否 |  |  |
| 11 | high_amount_sell | 否 |  |  |
| 12 | balance_change_unit | 否 |  |  |
| 13 | balance_lower_limit | 否 |  |  |
| 14 | up_price | 否 |  |  |
| 15 | down_price | 否 |  |  |
| 16 | price_tick | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | bond_trade_type | 否 |  |  |
| 21 | begin_time | 否 |  |  |
| 22 | end_time | 否 |  |  |
| 23 | low_amount_buy | 否 |  |  |
| 24 | buy_unit | 否 |  |  |
| 25 | high_amount_buy | 否 |  |  |
| 26 | low_amount_sell | 否 |  |  |
| 27 | sell_unit | 否 |  |  |
| 28 | high_amount_sell | 否 |  |  |
| 29 | balance_change_unit | 否 |  |  |
| 30 | balance_lower_limit | 否 |  |  |
| 31 | up_price | 否 |  |  |
| 32 | down_price | 否 |  |  |
| 33 | price_tick | 否 |  |  |
| 34 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_productbasicinfoext | ART | 是 | stock_code, exchange_type, bond_trade_type, stock_code, exchange_type, bond_trade_type |
| idx_productbasicinfoext | ART | 是 | stock_code, exchange_type, bond_trade_type, stock_code, exchange_type, bond_trade_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_productbasicinfoext | stock_code, exchange_type, bond_trade_type, stock_code, exchange_type, bond_trade_type |
| idx_productbasicinfoext | stock_code, exchange_type, bond_trade_type, stock_code, exchange_type, bond_trade_type |

# setttouftstbstockdetail - 清算全国股转证券余额信息表

**表对象ID**: 3028
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | seat_no | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | current_amount | 是 |  |  |
| 7 | frozen_amount | 是 |  |  |
| 8 | stock_property | 是 |  |  |
| 9 | ocpused_amount | 是 |  |  |
| 10 | sett_id | 是 |  |  |
| 11 | exchange_type | 是 |  |  |
| 12 | seat_no | 是 |  |  |
| 13 | stock_code | 是 |  |  |
| 14 | stock_account | 是 |  |  |
| 15 | current_amount | 是 |  |  |
| 16 | frozen_amount | 是 |  |  |
| 17 | stock_property | 是 |  |  |
| 18 | ocpused_amount | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stbstockdetail | 默认 | 是 | stock_account, exchange_type, stock_code, seat_no, stock_property, stock_account, exchange_type, stock_code, seat_no, stock_property |
| idx_stbstockdetail | 默认 | 是 | stock_account, exchange_type, stock_code, seat_no, stock_property, stock_account, exchange_type, stock_code, seat_no, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stbstockdetail | stock_account, stock_code, exchange_type, seat_no, stock_property, stock_account, stock_code, exchange_type, seat_no, stock_property |
| idx_stbstockdetail | stock_account, stock_code, exchange_type, seat_no, stock_property, stock_account, stock_code, exchange_type, seat_no, stock_property |

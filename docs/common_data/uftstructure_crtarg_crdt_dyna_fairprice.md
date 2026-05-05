# crdt_dyna_fairprice - 动态公允价信息表

**表对象ID**: 7093
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stop_date | 否 |  |  |
| 4 | last_price | 否 |  |  |
| 5 | fair_price_calcu_mode | 否 |  |  |
| 6 | begin_date | 否 |  |  |
| 7 | end_date | 否 |  |  |
| 8 | index_stock_code | 否 |  |  |
| 9 | base_price | 否 |  |  |
| 10 | en_dyna_fair_price_type | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+stock_code(8)+index_stock_code(16) |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | stop_date | 否 |  |  |
| 18 | last_price | 否 |  |  |
| 19 | fair_price_calcu_mode | 否 |  |  |
| 20 | begin_date | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | index_stock_code | 否 |  |  |
| 23 | base_price | 否 |  |  |
| 24 | en_dyna_fair_price_type | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | exchange_type(4)+stock_code(8)+index_stock_code(16) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_dyna_fairprice | ART | 是 | exchange_type, stock_code, index_stock_code, exchange_type, stock_code, index_stock_code |
| idx_crdt_dyna_fairprice | ART | 是 | exchange_type, stock_code, index_stock_code, exchange_type, stock_code, index_stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_dyna_fairprice | exchange_type, stock_code, index_stock_code, exchange_type, stock_code, index_stock_code |
| idx_crdt_dyna_fairprice | exchange_type, stock_code, index_stock_code, exchange_type, stock_code, index_stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 21:35:06 | 3.0.6.63 | 李想 | 新增表 |
| 2025-02-17 21:35:06 | 3.0.6.63 | 李想 | 新增表 |

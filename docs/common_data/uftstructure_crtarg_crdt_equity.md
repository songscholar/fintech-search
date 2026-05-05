# crdt_equity - 融资融券权益信息登记表

**表对象ID**: 7101
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | register_date | 否 |  |  |
| 2 | dr_date | 否 |  |  |
| 3 | pay_date | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | equity_type | 否 |  |  |
| 7 | distribute_ratio | 否 |  |  |
| 8 | alloted_price | 否 |  |  |
| 9 | recoup_type | 否 |  |  |
| 10 | recoup_ratio | 否 |  |  |
| 11 | deal_flag | 否 |  |  |
| 12 | close_price | 否 |  |  |
| 13 | market_date | 否 |  |  |
| 14 | equity_discount_ratio | 否 |  |  |
| 15 | equity_discount_flag | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | position_str | 否 |  | stock_code(8)+exchange_type(4)+equity_type(1)+register_date( |
| 20 | register_date | 否 |  |  |
| 21 | dr_date | 否 |  |  |
| 22 | pay_date | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | equity_type | 否 |  |  |
| 26 | distribute_ratio | 否 |  |  |
| 27 | alloted_price | 否 |  |  |
| 28 | recoup_type | 否 |  |  |
| 29 | recoup_ratio | 否 |  |  |
| 30 | deal_flag | 否 |  |  |
| 31 | close_price | 否 |  |  |
| 32 | market_date | 否 |  |  |
| 33 | equity_discount_ratio | 否 |  |  |
| 34 | equity_discount_flag | 否 |  |  |
| 35 | update_date | 否 |  |  |
| 36 | update_time | 否 |  |  |
| 37 | transaction_no | 否 |  |  |
| 38 | position_str | 否 |  | stock_code(8)+exchange_type(4)+equity_type(1)+register_date( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_equity | ART | 是 | stock_code, exchange_type, equity_type, register_date, stock_code, exchange_type, equity_type, register_date |
| idx_crdt_equity | ART | 是 | stock_code, exchange_type, equity_type, register_date, stock_code, exchange_type, equity_type, register_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_equity | stock_code, exchange_type, equity_type, register_date, stock_code, exchange_type, equity_type, register_date |
| idx_crdt_equity | stock_code, exchange_type, equity_type, register_date, stock_code, exchange_type, equity_type, register_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 10:39:27 | 3.0.6.87 | 李想 | 新增表 |
| 2025-02-19 10:39:27 | 3.0.6.87 | 李想 | 新增表 |

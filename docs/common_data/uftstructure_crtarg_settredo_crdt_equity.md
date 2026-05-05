# settredo_crdt_equity - 清算重做融资融券权益信息登记表

**表对象ID**: 7125
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

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
| 20 | init_date | 否 |  |  |
| 21 | sett_dml_type | 否 |  |  |
| 22 | sett_batch_no | 否 |  |  |
| 23 | register_date | 否 |  |  |
| 24 | dr_date | 否 |  |  |
| 25 | pay_date | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | equity_type | 否 |  |  |
| 29 | distribute_ratio | 否 |  |  |
| 30 | alloted_price | 否 |  |  |
| 31 | recoup_type | 否 |  |  |
| 32 | recoup_ratio | 否 |  |  |
| 33 | deal_flag | 否 |  |  |
| 34 | close_price | 否 |  |  |
| 35 | market_date | 否 |  |  |
| 36 | equity_discount_ratio | 否 |  |  |
| 37 | equity_discount_flag | 否 |  |  |
| 38 | update_date | 否 |  |  |
| 39 | update_time | 否 |  |  |
| 40 | transaction_no | 否 |  |  |
| 41 | position_str | 否 |  | stock_code(8)+exchange_type(4)+equity_type(1)+register_date( |
| 42 | init_date | 否 |  |  |
| 43 | sett_dml_type | 否 |  |  |
| 44 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_crdt_equity | ART | 是 | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |
| idx_settredo_crdt_equity | ART | 是 | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_crdt_equity | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |
| idx_settredo_crdt_equity | sett_batch_no, init_date, position_str, sett_batch_no, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-19 10:31:18 | 3.0.2.1 | 曾阳璞 | 新增表 |
| 2025-08-19 10:31:18 | 3.0.2.1 | 曾阳璞 | 新增表 |

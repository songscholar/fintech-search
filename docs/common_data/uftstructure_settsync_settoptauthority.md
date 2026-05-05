# settoptauthority - 清算期权标的证券权益信息表

**表对象ID**: 3218
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | authority_kind | 是 |  |  |
| 4 | authority_code | 是 |  |  |
| 5 | register_date | 是 |  |  |
| 6 | dr_date | 是 |  |  |
| 7 | pay_date | 是 |  |  |
| 8 | market_date | 是 |  |  |
| 9 | alloted_price | 是 |  |  |
| 10 | close_price | 是 |  |  |
| 11 | distribute_rate | 是 |  |  |
| 12 | circulate_change_per | 是 |  |  |
| 13 | modify_date | 是 |  |  |
| 14 | remark | 是 |  |  |
| 15 | modify_flag | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_code | 是 |  |  |
| 18 | authority_kind | 是 |  |  |
| 19 | authority_code | 是 |  |  |
| 20 | register_date | 是 |  |  |
| 21 | dr_date | 是 |  |  |
| 22 | pay_date | 是 |  |  |
| 23 | market_date | 是 |  |  |
| 24 | alloted_price | 是 |  |  |
| 25 | close_price | 是 |  |  |
| 26 | distribute_rate | 是 |  |  |
| 27 | circulate_change_per | 是 |  |  |
| 28 | modify_date | 是 |  |  |
| 29 | remark | 是 |  |  |
| 30 | modify_flag | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptauthority | 默认 | 是 | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |
| idx_settoptauthority | 默认 | 是 | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settoptauthority | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |
| idx_settoptauthority | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |

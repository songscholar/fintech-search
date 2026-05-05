# optunderlycode - 期权标的证券导出表

**表对象ID**: 3212
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | stock_type | 是 |  |  |
| 4 | amount_per_hand | 是 |  |  |
| 5 | valid_date | 是 |  |  |
| 6 | underly_status | 是 |  |  |
| 7 | update_type | 是 |  |  |
| 8 | hold_resopen_company | 是 |  |  |
| 9 | modify_date | 是 |  |  |
| 10 | closing_price | 是 |  |  |
| 11 | limit_value_up | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | stock_code | 是 |  |  |
| 14 | stock_type | 是 |  |  |
| 15 | amount_per_hand | 是 |  |  |
| 16 | valid_date | 是 |  |  |
| 17 | underly_status | 是 |  |  |
| 18 | update_type | 是 |  |  |
| 19 | hold_resopen_company | 是 |  |  |
| 20 | modify_date | 是 |  |  |
| 21 | closing_price | 是 |  |  |
| 22 | limit_value_up | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optunderlycode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_optunderlycode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optunderlycode | exchange_type, stock_code, exchange_type, stock_code |
| idx_optunderlycode | exchange_type, stock_code, exchange_type, stock_code |

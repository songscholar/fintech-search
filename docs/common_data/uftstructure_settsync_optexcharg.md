# optexcharg - 期权交易参数导出表

**表对象ID**: 3211
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | exchange_name | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | withdraw | 是 |  |  |
| 5 | square_type | 是 |  |  |
| 6 | intercept_len | 是 |  |  |
| 7 | prefix | 是 |  |  |
| 8 | seat_prefix_len | 是 |  |  |
| 9 | internal_len | 是 |  |  |
| 10 | init_date | 是 |  |  |
| 11 | exchange_status | 是 |  |  |
| 12 | fback_date | 是 |  |  |
| 13 | bback_date | 是 |  |  |
| 14 | treat_flag | 是 |  |  |
| 15 | hold_resopen_company | 是 |  |  |
| 16 | bail_resopen_company | 是 |  |  |
| 17 | covered_trans_mode | 是 |  |  |
| 18 | exchange_type | 是 |  |  |
| 19 | exchange_name | 是 |  |  |
| 20 | money_type | 是 |  |  |
| 21 | withdraw | 是 |  |  |
| 22 | square_type | 是 |  |  |
| 23 | intercept_len | 是 |  |  |
| 24 | prefix | 是 |  |  |
| 25 | seat_prefix_len | 是 |  |  |
| 26 | internal_len | 是 |  |  |
| 27 | init_date | 是 |  |  |
| 28 | exchange_status | 是 |  |  |
| 29 | fback_date | 是 |  |  |
| 30 | bback_date | 是 |  |  |
| 31 | treat_flag | 是 |  |  |
| 32 | hold_resopen_company | 是 |  |  |
| 33 | bail_resopen_company | 是 |  |  |
| 34 | covered_trans_mode | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optexcharg | 默认 | 是 | exchange_type, exchange_type |
| idx_optexcharg | 默认 | 是 | exchange_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optexcharg | exchange_type, exchange_type |
| idx_optexcharg | exchange_type, exchange_type |

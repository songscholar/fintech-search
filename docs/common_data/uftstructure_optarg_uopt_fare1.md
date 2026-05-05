# uopt_fare1 - 期权一级费用表

**表对象ID**: 9032
**所属模块**: optarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_type | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_type | 是 |  |  |
| 4 | option_code | 是 |  |  |
| 5 | entrust_bs | 是 |  |  |
| 6 | entrust_oc | 是 |  |  |
| 7 | money_type | 是 |  |  |
| 8 | balance_ratio | 是 |  |  |
| 9 | par_ratio | 是 |  |  |
| 10 | per_fare | 是 |  |  |
| 11 | min_fare | 是 |  |  |
| 12 | max_fare | 是 |  |  |
| 13 | segment_flag | 是 |  |  |
| 14 | segment_kind | 是 |  |  |
| 15 | update_date | 是 |  |  |
| 16 | update_time | 是 |  |  |
| 17 | transaction_no | 是 |  |  |
| 18 | fare_type | 是 |  |  |
| 19 | exchange_type | 是 |  |  |
| 20 | stock_type | 是 |  |  |
| 21 | option_code | 是 |  |  |
| 22 | entrust_bs | 是 |  |  |
| 23 | entrust_oc | 是 |  |  |
| 24 | money_type | 是 |  |  |
| 25 | balance_ratio | 是 |  |  |
| 26 | par_ratio | 是 |  |  |
| 27 | per_fare | 是 |  |  |
| 28 | min_fare | 是 |  |  |
| 29 | max_fare | 是 |  |  |
| 30 | segment_flag | 是 |  |  |
| 31 | segment_kind | 是 |  |  |
| 32 | update_date | 是 |  |  |
| 33 | update_time | 是 |  |  |
| 34 | transaction_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optfare1 | 默认 | 是 | stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code, stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code |
| idx_optfare1 | 默认 | 是 | stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code, stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optfare1 | stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code, stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code |
| idx_optfare1 | stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code, stock_type, fare_type, exchange_type, entrust_bs, entrust_oc, option_code |

# optfare2 - 期权二级费用导出表

**表对象ID**: 3210
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_type | 是 |  |  |
| 3 | fare_kind | 是 |  |  |
| 4 | fare_type | 是 |  |  |
| 5 | entrust_bs | 是 |  |  |
| 6 | entrust_oc | 是 |  |  |
| 7 | entrust_way | 是 |  |  |
| 8 | money_type | 是 |  |  |
| 9 | entrust_type | 是 |  |  |
| 10 | branch_no | 是 |  |  |
| 11 | balance_ratio | 是 |  |  |
| 12 | par_ratio | 是 |  |  |
| 13 | per_fare | 是 |  |  |
| 14 | per_min_fare | 是 |  |  |
| 15 | per_max_fare | 是 |  |  |
| 16 | min_fare | 是 |  |  |
| 17 | max_fare | 是 |  |  |
| 18 | dispart_count | 是 |  |  |
| 19 | rebate_flag | 是 |  |  |
| 20 | rebate_ratio | 是 |  |  |
| 21 | min_ratio | 是 |  |  |
| 22 | segment_flag | 是 |  |  |
| 23 | segment_kind | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | stock_type | 是 |  |  |
| 26 | fare_kind | 是 |  |  |
| 27 | fare_type | 是 |  |  |
| 28 | entrust_bs | 是 |  |  |
| 29 | entrust_oc | 是 |  |  |
| 30 | entrust_way | 是 |  |  |
| 31 | money_type | 是 |  |  |
| 32 | entrust_type | 是 |  |  |
| 33 | branch_no | 是 |  |  |
| 34 | balance_ratio | 是 |  |  |
| 35 | par_ratio | 是 |  |  |
| 36 | per_fare | 是 |  |  |
| 37 | per_min_fare | 是 |  |  |
| 38 | per_max_fare | 是 |  |  |
| 39 | min_fare | 是 |  |  |
| 40 | max_fare | 是 |  |  |
| 41 | dispart_count | 是 |  |  |
| 42 | rebate_flag | 是 |  |  |
| 43 | rebate_ratio | 是 |  |  |
| 44 | min_ratio | 是 |  |  |
| 45 | segment_flag | 是 |  |  |
| 46 | segment_kind | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optfare2 | 默认 | 是 | exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type, exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type |
| idx_optfare2 | 默认 | 是 | exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type, exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optfare2 | exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type, exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type |
| idx_optfare2 | exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type, exchange_type, stock_type, money_type, fare_kind, fare_type, entrust_bs, entrust_oc, entrust_way, entrust_type |

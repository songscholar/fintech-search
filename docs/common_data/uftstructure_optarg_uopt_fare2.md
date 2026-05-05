# uopt_fare2 - 期权二级费用

**表对象ID**: 9003
**所属模块**: optarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | optfare_kind | 否 |  |  |
| 2 | fare_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | entrust_oc | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | balance_ratio | 否 |  |  |
| 12 | par_ratio | 否 |  |  |
| 13 | per_fare | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | min_fare | 否 |  | uft20 |
| 17 | max_fare | 否 |  |  |
| 18 | per_min_fare | 否 |  |  |
| 19 | per_max_fare | 否 |  |  |
| 20 | min_ratio | 否 |  |  |
| 21 | segment_flag | 否 |  |  |
| 22 | segment_kind | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | optfare_kind | 否 |  |  |
| 25 | fare_type | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | entrust_bs | 否 |  |  |
| 29 | entrust_oc | 否 |  |  |
| 30 | entrust_way | 否 |  |  |
| 31 | money_type | 否 |  |  |
| 32 | entrust_type | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | balance_ratio | 否 |  |  |
| 35 | par_ratio | 否 |  |  |
| 36 | per_fare | 否 |  |  |
| 37 | update_date | 否 |  |  |
| 38 | update_time | 否 |  |  |
| 39 | min_fare | 否 |  | uft20 |
| 40 | max_fare | 否 |  |  |
| 41 | per_min_fare | 否 |  |  |
| 42 | per_max_fare | 否 |  |  |
| 43 | min_ratio | 否 |  |  |
| 44 | segment_flag | 否 |  |  |
| 45 | segment_kind | 否 |  |  |
| 46 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fare2 | 默认 | 是 | optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type, optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type |
| idx_uopt_fare2_qry | 默认 | 是 | exchange_type, stock_type, entrust_oc, money_type, optfare_kind, fare_type, entrust_bs, entrust_type, entrust_way, exchange_type, stock_type, entrust_oc, money_type, optfare_kind, fare_type, entrust_bs, entrust_type, entrust_way |
| idx_uopt_fare2_copy_batchdelete | 默认 | 是 | optfare_kind, fare_type, exchange_type, optfare_kind, fare_type, exchange_type |
| idx_uopt_fare2 | 默认 | 是 | optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type, optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type |
| idx_uopt_fare2_qry | 默认 | 是 | exchange_type, stock_type, entrust_oc, money_type, optfare_kind, fare_type, entrust_bs, entrust_type, entrust_way, exchange_type, stock_type, entrust_oc, money_type, optfare_kind, fare_type, entrust_bs, entrust_type, entrust_way |
| idx_uopt_fare2_copy_batchdelete | 默认 | 是 | optfare_kind, fare_type, exchange_type, optfare_kind, fare_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fare2 | optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type, optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type |
| idx_uopt_fare2 | optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type, optfare_kind, fare_type, exchange_type, stock_type, entrust_bs, entrust_oc, entrust_way, money_type, entrust_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-20 15:16:00 | V3.0.2.12 | wuxd | 调整索引idx_uopt_fare2_qry新增分级[optfare_kind|0_升序] |
| 2024-10-28 18:48:38 | V3.0.3.9 | 韦子晗 | 新增索引idx_uopt_fare2_copy_batchdelete |
| 2023-12-16 17:28:20 | 3.0.0.0 | wuxd |  |
| 2025-09-20 15:16:00 | V3.0.2.12 | wuxd | 调整索引idx_uopt_fare2_qry新增分级[optfare_kind|0_升序] |
| 2024-10-28 18:48:38 | V3.0.3.9 | 韦子晗 | 新增索引idx_uopt_fare2_copy_batchdelete |
| 2023-12-16 17:28:20 | 3.0.0.0 | wuxd |  |

# hfare2 - 二级回购费用表

**表对象ID**: 303
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_kind | 否 |  |  |
| 2 | fare_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | entrust_way | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | entrust_type | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | balance_ratio | 否 |  |  |
| 11 | par_ratio | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | max_fare | 否 |  |  |
| 14 | dispart_count | 否 |  |  |
| 15 | rebate_flag | 否 |  |  |
| 16 | rebate_ratio | 否 |  |  |
| 17 | min_ratio | 否 |  |  |
| 18 | segment_flag | 否 |  |  |
| 19 | segment_kind | 否 |  |  |
| 20 | entrust_prop | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | stock_code(8)+entrust_way(1)+fare_kind(10)+fare_type(1)+exch |
| 25 | fare_kind | 否 |  |  |
| 26 | fare_type | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | entrust_bs | 否 |  |  |
| 30 | entrust_way | 否 |  |  |
| 31 | money_type | 否 |  |  |
| 32 | entrust_type | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | balance_ratio | 否 |  |  |
| 35 | par_ratio | 否 |  |  |
| 36 | min_fare | 否 |  |  |
| 37 | max_fare | 否 |  |  |
| 38 | dispart_count | 否 |  |  |
| 39 | rebate_flag | 否 |  |  |
| 40 | rebate_ratio | 否 |  |  |
| 41 | min_ratio | 否 |  |  |
| 42 | segment_flag | 否 |  |  |
| 43 | segment_kind | 否 |  |  |
| 44 | entrust_prop | 否 |  |  |
| 45 | transaction_no | 否 |  |  |
| 46 | update_date | 否 |  |  |
| 47 | update_time | 否 |  |  |
| 48 | position_str | 否 |  | stock_code(8)+entrust_way(1)+fare_kind(10)+fare_type(1)+exch |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hfare2_cur | ART | 是 | entrust_way, fare_type, stock_code, exchange_type, entrust_bs, entrust_way, fare_type, stock_code, exchange_type, entrust_bs |
| idx_hfare2_branch | ART | 是 | branch_no, branch_no |
| idx_hfare2 | ART | 是 | stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop |
| idx_hfare2_cur | ART | 是 | entrust_way, fare_type, stock_code, exchange_type, entrust_bs, entrust_way, fare_type, stock_code, exchange_type, entrust_bs |
| idx_hfare2_branch | ART | 是 | branch_no, branch_no |
| idx_hfare2 | ART | 是 | stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hfare2 | stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop |
| idx_hfare2 | stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, stock_code, entrust_way, fare_kind, fare_type, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 17:23:05 | 3.0.6.44 | 李想 | 物理表hfare2，添加了表字段(update_date);
物理表hfare2，添加了表字段(update_time... |
| 2025-02-14 17:23:05 | 3.0.6.44 | 李想 | 物理表hfare2，添加了表字段(update_date);
物理表hfare2，添加了表字段(update_time... |

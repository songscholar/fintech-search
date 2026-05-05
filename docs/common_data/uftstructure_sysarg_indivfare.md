# indivfare - 独立佣金表

**表对象ID**: 147
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | indiv_fare_kind | 否 |  |  |
| 3 | fare_type | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | entrust_bs | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | balance_ratio | 否 |  |  |
| 11 | par_ratio | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | max_fare | 否 |  |  |
| 14 | dispart_count | 否 |  |  |
| 15 | min_ratio | 否 |  |  |
| 16 | entrust_prop | 否 |  |  |
| 17 | sub_stock_type | 否 |  |  |
| 18 | res_entrust_type | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | indiv_fare_kind(10)+fare_type(1)+stock_type(4)+entrust_way(1 |
| 23 | branch_no | 否 |  |  |
| 24 | indiv_fare_kind | 否 |  |  |
| 25 | fare_type | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | entrust_bs | 否 |  |  |
| 29 | entrust_way | 否 |  |  |
| 30 | money_type | 否 |  |  |
| 31 | entrust_type | 否 |  |  |
| 32 | balance_ratio | 否 |  |  |
| 33 | par_ratio | 否 |  |  |
| 34 | min_fare | 否 |  |  |
| 35 | max_fare | 否 |  |  |
| 36 | dispart_count | 否 |  |  |
| 37 | min_ratio | 否 |  |  |
| 38 | entrust_prop | 否 |  |  |
| 39 | sub_stock_type | 否 |  |  |
| 40 | res_entrust_type | 否 |  |  |
| 41 | update_date | 否 |  |  |
| 42 | update_time | 否 |  |  |
| 43 | transaction_no | 否 |  |  |
| 44 | position_str | 否 |  | indiv_fare_kind(10)+fare_type(1)+stock_type(4)+entrust_way(1 |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_indivfare | 默认 | 否 |  |
| idx_indivfare_cur | 默认 | 否 |  |
| idx_indivfare | ART | 是 | indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |
| idx_indivfare_cur | ART | 是 | indiv_fare_kind, entrust_bs, stock_type, exchange_type, indiv_fare_kind, entrust_bs, stock_type, exchange_type |
| idx_indivfare | 默认 | 否 |  |
| idx_indivfare_cur | 默认 | 否 |  |
| idx_indivfare | ART | 是 | indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |
| idx_indivfare_cur | ART | 是 | indiv_fare_kind, entrust_bs, stock_type, exchange_type, indiv_fare_kind, entrust_bs, stock_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_indivfare | indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |
| idx_indivfare | indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, indiv_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:44:28 | 3.0.2.103 | taocong45644 | 当前表indivfare，修改了索引idx_indivfare,索引字段修改为：(indiv_fare_kind,far... |
| 2025-12-01 14:44:28 | 3.0.2.103 | taocong45644 | 当前表indivfare，修改了索引idx_indivfare,索引字段修改为：(indiv_fare_kind,far... |

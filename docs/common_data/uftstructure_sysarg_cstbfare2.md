# cstbfare2 - 融资融券北交所二级费用表

**表对象ID**: 337
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_kind | 否 |  |  |
| 2 | fare_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | entrust_bs | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | balance_ratio | 否 |  |  |
| 12 | par_ratio | 否 |  |  |
| 13 | min_fare | 否 |  |  |
| 14 | max_fare | 否 |  |  |
| 15 | dispart_count | 否 |  |  |
| 16 | rebate_flag | 否 |  |  |
| 17 | rebate_ratio | 否 |  |  |
| 18 | min_ratio | 否 |  |  |
| 19 | segment_flag | 否 |  |  |
| 20 | segment_kind | 否 |  |  |
| 21 | entrust_prop | 否 |  |  |
| 22 | sub_stock_type | 否 |  |  |
| 23 | position_str_s | 否 |  | stock_type(4)+entrust_way(1)+fare_kind(10)+fare_type(1)+exch |
| 24 | position_str_d | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | fare_kind | 否 |  |  |
| 29 | fare_type | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | stock_type | 否 |  |  |
| 33 | entrust_bs | 否 |  |  |
| 34 | entrust_way | 否 |  |  |
| 35 | money_type | 否 |  |  |
| 36 | entrust_type | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | balance_ratio | 否 |  |  |
| 39 | par_ratio | 否 |  |  |
| 40 | min_fare | 否 |  |  |
| 41 | max_fare | 否 |  |  |
| 42 | dispart_count | 否 |  |  |
| 43 | rebate_flag | 否 |  |  |
| 44 | rebate_ratio | 否 |  |  |
| 45 | min_ratio | 否 |  |  |
| 46 | segment_flag | 否 |  |  |
| 47 | segment_kind | 否 |  |  |
| 48 | entrust_prop | 否 |  |  |
| 49 | sub_stock_type | 否 |  |  |
| 50 | position_str_s | 否 |  | stock_type(4)+entrust_way(1)+fare_kind(10)+fare_type(1)+exch |
| 51 | position_str_d | 否 |  |  |
| 52 | transaction_no | 否 |  |  |
| 53 | update_date | 否 |  |  |
| 54 | update_time | 否 |  |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cstbfare2 | 默认 | 否 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way |
| idx_cstbfare2 | 默认 | 否 |  |
| idx_cstbfare2 | 默认 | 否 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way |
| idx_cstbfare2 | 默认 | 否 |  |
| idx_cstbfare2 | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_cstbfare2_bra | ART | 是 | branch_no, branch_no |
| idx_cstbfare2_cur | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, entrust_way |
| idx_cstbfare2_pos | ART | 是 | position_str_s, position_str_s |
| idx_cstbfare2 | 默认 | 否 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way |
| idx_cstbfare2 | 默认 | 否 |  |
| idx_cstbfare2 | 默认 | 否 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_prop, entrust_type, sub_stock_type, entrust_way |
| idx_cstbfare2 | 默认 | 否 |  |
| idx_cstbfare2 | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_cstbfare2_bra | ART | 是 | branch_no, branch_no |
| idx_cstbfare2_cur | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, entrust_way |
| idx_cstbfare2_pos | ART | 是 | position_str_s, position_str_s |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cstbfare2 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_cstbfare2 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, sub_stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 20:13:27 | 3.0.6.13 | 李想 | 物理表cstbfare2，添加了表字段(update_date);
物理表cstbfare2，添加了表字段(updat... |
| 2025-03-07 10:06:29 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，增加索引(idx_cstbfare2:[fare_kind,exchange_type,sto... |
| 2025-03-07 10:11:37 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，删除了表索引(idx_cstbfare2);
 |
| 2025-03-07 10:06:29 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，增加索引(idx_cstbfare2:[fare_kind,exchange_type,sto... |
| 2025-03-07 10:11:37 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，删除了表索引(idx_cstbfare2);
 |
| 2024-09-26 19:27:48 | 3.0.3.14 | 张明月 | 物理表cstbfare2，添加了表字段(transaction_no);
 |
| 2024-09-23 16:16:55 | 3.0.3.7 | 张明月 | 新增 |
| 2025-02-13 20:13:27 | 3.0.6.13 | 李想 | 物理表cstbfare2，添加了表字段(update_date);
物理表cstbfare2，添加了表字段(updat... |
| 2025-03-07 10:06:29 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，增加索引(idx_cstbfare2:[fare_kind,exchange_type,sto... |
| 2025-03-07 10:11:37 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，删除了表索引(idx_cstbfare2);
 |
| 2025-03-07 10:06:29 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，增加索引(idx_cstbfare2:[fare_kind,exchange_type,sto... |
| 2025-03-07 10:11:37 | 3.0.6.18 | 徐世晗 | 物理表cstbfare2，删除了表索引(idx_cstbfare2);
 |
| 2024-09-26 19:27:48 | 3.0.3.14 | 张明月 | 物理表cstbfare2，添加了表字段(transaction_no);
 |
| 2024-09-23 16:16:55 | 3.0.3.7 | 张明月 | 新增 |

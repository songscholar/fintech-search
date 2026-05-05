# usps_bfare2 - 后台二级费用表

**表对象ID**: 7
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | balance_ratio | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | dispart_count | 否 |  |  |
| 4 | entrust_bs | 否 |  |  |
| 5 | entrust_prop | 否 |  |  |
| 6 | entrust_type | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | fare_kind | 否 |  |  |
| 10 | fare_type | 否 |  |  |
| 11 | max_fare | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | min_ratio | 否 |  |  |
| 14 | par_ratio | 否 |  |  |
| 15 | position_str_s | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |
| 16 | segment_flag | 否 |  |  |
| 17 | segment_kind | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | sub_stock_type | 否 |  |  |
| 20 | money_type | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str_d | 否 |  |  |
| 23 | rebate_flag | 否 |  |  |
| 24 | rebate_ratio | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | balance_ratio | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | dispart_count | 否 |  |  |
| 31 | entrust_bs | 否 |  |  |
| 32 | entrust_prop | 否 |  |  |
| 33 | entrust_type | 否 |  |  |
| 34 | entrust_way | 否 |  |  |
| 35 | exchange_type | 否 |  |  |
| 36 | fare_kind | 否 |  |  |
| 37 | fare_type | 否 |  |  |
| 38 | max_fare | 否 |  |  |
| 39 | min_fare | 否 |  |  |
| 40 | min_ratio | 否 |  |  |
| 41 | par_ratio | 否 |  |  |
| 42 | position_str_s | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |
| 43 | segment_flag | 否 |  |  |
| 44 | segment_kind | 否 |  |  |
| 45 | stock_type | 否 |  |  |
| 46 | sub_stock_type | 否 |  |  |
| 47 | money_type | 否 |  |  |
| 48 | transaction_no | 否 |  |  |
| 49 | position_str_d | 否 |  |  |
| 50 | rebate_flag | 否 |  |  |
| 51 | rebate_ratio | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | position_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_bfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_upbs_bfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_bfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_upbs_bfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 17:03:33 | 8.26.2.94 | 刘珊珊 | 所有表usps_bfare2，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:26:55 | 3.0.6.45 | 李想 | 物理表usps_bfare2，添加了表字段(rebate_flag);
物理表usps_bfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:01:46 | 3.0.3.12 | 张明月 | 物理表usps_bfare2，添加了表字段(position_str_d);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:00 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2025-11-21 17:03:33 | 8.26.2.94 | 刘珊珊 | 所有表usps_bfare2，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:26:55 | 3.0.6.45 | 李想 | 物理表usps_bfare2，添加了表字段(rebate_flag);
物理表usps_bfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:01:46 | 3.0.3.12 | 张明月 | 物理表usps_bfare2，添加了表字段(position_str_d);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:00 | 0.0.0.5 | 吴威 | 新增字段transaction_no |

# usps_cfare2 - 融资融券后台费用表

**表对象ID**: 70
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_kind | 否 |  |  |
| 2 | fare_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
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
| 15 | min_ratio | 否 |  |  |
| 16 | segment_flag | 否 |  |  |
| 17 | segment_kind | 否 |  |  |
| 18 | entrust_prop | 否 |  |  |
| 19 | sub_stock_type | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | position_str_s | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |
| 22 | position_str_d | 否 |  |  |
| 23 | rebate_flag | 否 |  |  |
| 24 | rebate_ratio | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | fare_kind | 否 |  |  |
| 28 | fare_type | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_type | 否 |  |  |
| 31 | entrust_bs | 否 |  |  |
| 32 | entrust_way | 否 |  |  |
| 33 | money_type | 否 |  |  |
| 34 | entrust_type | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | balance_ratio | 否 |  |  |
| 37 | par_ratio | 否 |  |  |
| 38 | min_fare | 否 |  |  |
| 39 | max_fare | 否 |  |  |
| 40 | dispart_count | 否 |  |  |
| 41 | min_ratio | 否 |  |  |
| 42 | segment_flag | 否 |  |  |
| 43 | segment_kind | 否 |  |  |
| 44 | entrust_prop | 否 |  |  |
| 45 | sub_stock_type | 否 |  |  |
| 46 | transaction_no | 否 |  |  |
| 47 | position_str_s | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |
| 48 | position_str_d | 否 |  |  |
| 49 | rebate_flag | 否 |  |  |
| 50 | rebate_ratio | 否 |  |  |
| 51 | update_date | 否 |  |  |
| 52 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_cfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_usps_cfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_cfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_usps_cfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 20:57:13 | 3.0.6.16 | 李想 | 物理表usps_cfare2，添加了表字段(rebate_flag);
物理表usps_cfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:02:59 | 3.0.3.12 | 张明月 | 物理表usps_cfare2，添加了表字段(position_str_d);
物理表usps_cfare2，添加了表字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 18:59 | 0.0.0.7 | 汪林 | 新增usps_cfare2表 |
| 2025-02-13 20:57:13 | 3.0.6.16 | 李想 | 物理表usps_cfare2，添加了表字段(rebate_flag);
物理表usps_cfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:02:59 | 3.0.3.12 | 张明月 | 物理表usps_cfare2，添加了表字段(position_str_d);
物理表usps_cfare2，添加了表字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 18:59 | 0.0.0.7 | 汪林 | 新增usps_cfare2表 |

# usps_offare2 - 场内开放式基金费用表

**表对象ID**: 18
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 56 个）

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
| 14 | money_type | 否 |  |  |
| 15 | par_ratio | 否 |  |  |
| 16 | position_str_d | 否 |  |  |
| 17 | rebate_flag | 否 |  |  |
| 18 | rebate_ratio | 否 |  |  |
| 19 | segment_flag | 否 |  |  |
| 20 | segment_kind | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str_s | 否 |  | fare_kind(10)+stock_type(4)+exchange_type(4)+entrust_bs(1)+f |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | position_str | 否 |  |  |
| 28 | sub_stock_type | 否 |  |  |
| 29 | balance_ratio | 否 |  |  |
| 30 | branch_no | 否 |  |  |
| 31 | dispart_count | 否 |  |  |
| 32 | entrust_bs | 否 |  |  |
| 33 | entrust_prop | 否 |  |  |
| 34 | entrust_type | 否 |  |  |
| 35 | entrust_way | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | fare_kind | 否 |  |  |
| 38 | fare_type | 否 |  |  |
| 39 | max_fare | 否 |  |  |
| 40 | min_fare | 否 |  |  |
| 41 | min_ratio | 否 |  |  |
| 42 | money_type | 否 |  |  |
| 43 | par_ratio | 否 |  |  |
| 44 | position_str_d | 否 |  |  |
| 45 | rebate_flag | 否 |  |  |
| 46 | rebate_ratio | 否 |  |  |
| 47 | segment_flag | 否 |  |  |
| 48 | segment_kind | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | stock_type | 否 |  |  |
| 51 | transaction_no | 否 |  |  |
| 52 | position_str_s | 否 |  | fare_kind(10)+stock_type(4)+exchange_type(4)+entrust_bs(1)+f |
| 53 | update_date | 否 |  |  |
| 54 | update_time | 否 |  |  |
| 55 | position_str | 否 |  |  |
| 56 | sub_stock_type | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_offare2_level | 默认 | 否 |  |
| idx_usps_offare2_code | 默认 | 否 |  |
| idx_usps_offare2_level | ART | 是 | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type |
| idx_usps_offare2_code | ART | 是 | stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, sub_stock_type, stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, sub_stock_type |
| idx_usps_offare2_level | 默认 | 否 |  |
| idx_usps_offare2_code | 默认 | 否 |  |
| idx_usps_offare2_level | ART | 是 | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type |
| idx_usps_offare2_code | ART | 是 | stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, sub_stock_type, stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_offare2_level | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type |
| idx_usps_offare2_level | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-12 10:47:14 | 3.0.6.45 | 蒋浩宇 | 当前表usps_offare2，修改了索引idx_usps_offare2_level,索引字段修改为：(fare_ki... |
| 2025-11-23 17:19:38 | 3.0.6.44 | 刘珊珊 | 所有表usps_offare2，添加了表字段(position_str);
所有表usps_offare2，添加了表字... |
| 2025-02-14 17:12:00 | 3.0.6.43 | 李想 | 物理表usps_offare2，添加了表字段(update_date);
物理表usps_offare2，添加了表字段... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:00:40 | 3.0.3.12 | 张明月 | 物理表usps_offare2，添加了表字段(position_str_s);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2026-01-12 10:47:14 | 3.0.6.45 | 蒋浩宇 | 当前表usps_offare2，修改了索引idx_usps_offare2_level,索引字段修改为：(fare_ki... |
| 2025-11-23 17:19:38 | 3.0.6.44 | 刘珊珊 | 所有表usps_offare2，添加了表字段(position_str);
所有表usps_offare2，添加了表字... |
| 2025-02-14 17:12:00 | 3.0.6.43 | 李想 | 物理表usps_offare2，添加了表字段(update_date);
物理表usps_offare2，添加了表字段... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2024-09-23 11:00:40 | 3.0.3.12 | 张明月 | 物理表usps_offare2，添加了表字段(position_str_s);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |

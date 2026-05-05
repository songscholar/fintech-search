# usps_coffare2 - 融资融券场内开放式基金费用表

**表对象ID**: 72
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

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
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fare_kind(10)+stock_type(4)+exchange_type(4)+entrust_bs(1)+f |
| 27 | balance_ratio | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | dispart_count | 否 |  |  |
| 30 | entrust_bs | 否 |  |  |
| 31 | entrust_prop | 否 |  |  |
| 32 | entrust_type | 否 |  |  |
| 33 | entrust_way | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | fare_kind | 否 |  |  |
| 36 | fare_type | 否 |  |  |
| 37 | max_fare | 否 |  |  |
| 38 | min_fare | 否 |  |  |
| 39 | min_ratio | 否 |  |  |
| 40 | money_type | 否 |  |  |
| 41 | par_ratio | 否 |  |  |
| 42 | position_str_d | 否 |  |  |
| 43 | rebate_flag | 否 |  |  |
| 44 | rebate_ratio | 否 |  |  |
| 45 | segment_flag | 否 |  |  |
| 46 | segment_kind | 否 |  |  |
| 47 | stock_code | 否 |  |  |
| 48 | stock_type | 否 |  |  |
| 49 | transaction_no | 否 |  |  |
| 50 | update_date | 否 |  |  |
| 51 | update_time | 否 |  |  |
| 52 | position_str | 否 |  | fare_kind(10)+stock_type(4)+exchange_type(4)+entrust_bs(1)+f |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_coffare2_level | ART | 是 | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way |
| idx_usps_coffare2_code | ART | 是 | stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way |
| idx_usps_coffare2_level | ART | 是 | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way |
| idx_usps_coffare2_code | ART | 是 | stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way, stock_type, exchange_type, entrust_bs, stock_code, fare_type, fare_kind, entrust_type, entrust_prop, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_coffare2_level | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way |
| idx_usps_coffare2_level | fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way, fare_kind, stock_type, exchange_type, entrust_bs, fare_type, stock_code, entrust_type, entrust_prop, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 20:27:19 | 3.0.6.14 | 李想 | 物理表usps_coffare2，添加了表字段(update_date);
物理表usps_coffare2，添加了表... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 19:00 | 0.0.0.7 | 汪林 | 新增usps_coffare2表 |
| 2025-02-13 20:27:19 | 3.0.6.14 | 李想 | 物理表usps_coffare2，添加了表字段(update_date);
物理表usps_coffare2，添加了表... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-13 19:00 | 0.0.0.7 | 汪林 | 新增usps_coffare2表 |

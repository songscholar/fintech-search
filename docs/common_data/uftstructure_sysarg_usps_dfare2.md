# usps_dfare2 - 大宗交易费用表

**表对象ID**: 45
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
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | sub_stock_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | entrust_way | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | entrust_type | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | balance_ratio | 否 |  |  |
| 13 | par_ratio | 否 |  |  |
| 14 | min_fare | 否 |  |  |
| 15 | max_fare | 否 |  |  |
| 16 | dispart_count | 否 |  |  |
| 17 | min_ratio | 否 |  |  |
| 18 | segment_flag | 否 |  |  |
| 19 | segment_kind | 否 |  |  |
| 20 | position_str_d | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | rebate_flag | 否 |  |  |
| 23 | rebate_ratio | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |
| 27 | fare_kind | 否 |  |  |
| 28 | fare_type | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | stock_type | 否 |  |  |
| 32 | sub_stock_type | 否 |  |  |
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
| 43 | min_ratio | 否 |  |  |
| 44 | segment_flag | 否 |  |  |
| 45 | segment_kind | 否 |  |  |
| 46 | position_str_d | 否 |  |  |
| 47 | transaction_no | 否 |  |  |
| 48 | rebate_flag | 否 |  |  |
| 49 | rebate_ratio | 否 |  |  |
| 50 | update_date | 否 |  |  |
| 51 | update_time | 否 |  |  |
| 52 | position_str | 否 |  | fare_kind(10)+exchange_type(4)+stock_type(4)+entrust_bs(1)+f |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_dfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way |
| idx_usps_dfare2_level | ART | 是 | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_dfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way |
| idx_usps_dfare2_level | fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way, fare_kind, exchange_type, stock_type, entrust_bs, fare_type, stock_code, entrust_type, sub_stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 17:08:12 | 3.0.6.42 | 李想 | 物理表usps_dfare2，添加了表字段(rebate_flag);
物理表usps_dfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-02-14 17:08:12 | 3.0.6.42 | 李想 | 物理表usps_dfare2，添加了表字段(rebate_flag);
物理表usps_dfare2，添加了表字段(r... |
| 2025-01-06 10:49:36 | 3.0.6.8 | 徐世晗 | fare_type索引调整为降序 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

# usps_ffare - 前台费用表

**表对象ID**: 10
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | entrust_way | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | fare | 否 |  |  |
| 5 | fare_kind | 否 |  |  |
| 6 | fare_type | 否 |  |  |
| 7 | max_fare | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | stock_type | 否 |  |  |
| 10 | position_str_d | 否 |  |  |
| 11 | sub_stock_type | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | rebate_flag | 否 |  |  |
| 14 | rebate_ratio | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | position_str | 否 |  | fare_kind(10)+fare_type(1)+exchange_type(4)+stock_type(4)+en |
| 18 | branch_no | 否 |  |  |
| 19 | entrust_way | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | fare | 否 |  |  |
| 22 | fare_kind | 否 |  |  |
| 23 | fare_type | 否 |  |  |
| 24 | max_fare | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | stock_type | 否 |  |  |
| 27 | position_str_d | 否 |  |  |
| 28 | sub_stock_type | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | rebate_flag | 否 |  |  |
| 31 | rebate_ratio | 否 |  |  |
| 32 | update_date | 否 |  |  |
| 33 | update_time | 否 |  |  |
| 34 | position_str | 否 |  | fare_kind(10)+fare_type(1)+exchange_type(4)+stock_type(4)+en |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_ffare | 默认 | 否 |  |
| idx_usps_ffare | 默认 | 否 | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |
| idx_usps_ffare | ART | 是 | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |
| idx_usps_ffare_norm | ART | 是 | fare_kind, fare_type, stock_type, exchange_type, sub_stock_type, entrust_way, fare_kind, fare_type, stock_type, exchange_type, sub_stock_type, entrust_way |
| idx_upbs_ffare | 默认 | 否 |  |
| idx_usps_ffare | 默认 | 否 | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |
| idx_usps_ffare | ART | 是 | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |
| idx_usps_ffare_norm | ART | 是 | fare_kind, fare_type, stock_type, exchange_type, sub_stock_type, entrust_way, fare_kind, fare_type, stock_type, exchange_type, sub_stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_ffare | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |
| idx_usps_ffare | fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type, fare_kind, fare_type, exchange_type, stock_type, entrust_way, money_type, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:30:11 | 3.0.6.46 | 李想 | 物理表usps_ffare，添加了表字段(rebate_flag);
物理表usps_ffare，添加了表字段(reb... |
| 2023-09-18 09:29:53 | V3.0.1.5 | 许琮擎 | 物理表usps_ffare，删除了表索引(idx_upbs_ffare);
 |
| 2023-09-18 09:29:05 | V3.0.1.5 | 许琮擎 | 物理表usps_ffare，增加索引(idx_usps_ffare:[fare_kind,fare_type,excha... |
| 2023-09-15 10:23:20 | V3.0.1.5 | 许琮擎 | 表索引重命名 |
| 2023-09-08 11:24:40 | V3.0.1.2 | 施凯 | usps_ffare索引顺序调整 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-14 21:15 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2017-04-14 15:40 | 0.0.0.1 | 杨丽 | 新增 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 17:30:11 | 3.0.6.46 | 李想 | 物理表usps_ffare，添加了表字段(rebate_flag);
物理表usps_ffare，添加了表字段(reb... |
| 2023-09-18 09:29:53 | V3.0.1.5 | 许琮擎 | 物理表usps_ffare，删除了表索引(idx_upbs_ffare);
 |
| 2023-09-18 09:29:05 | V3.0.1.5 | 许琮擎 | 物理表usps_ffare，增加索引(idx_usps_ffare:[fare_kind,fare_type,excha... |
| 2023-09-15 10:23:20 | V3.0.1.5 | 许琮擎 | 表索引重命名 |
| 2023-09-08 11:24:40 | V3.0.1.2 | 施凯 | usps_ffare索引顺序调整 |

> 共 18 条修改记录，仅显示最近15条

# usps_bfare1 - 一级费用表

**表对象ID**: 121
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | sub_stock_type | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | balance_ratio | 否 |  |  |
| 8 | par_ratio | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | max_fare | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | blocktrade_flag | 否 |  |  |
| 13 | segment_flag | 否 |  |  |
| 14 | segment_kind | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | stock_type(4)+fare_type(1)+exchange_type(4)+entrust_bs(1)+st |
| 19 | fare_type | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | sub_stock_type | 否 |  |  |
| 23 | entrust_bs | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | balance_ratio | 否 |  |  |
| 26 | par_ratio | 否 |  |  |
| 27 | min_fare | 否 |  |  |
| 28 | max_fare | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | blocktrade_flag | 否 |  |  |
| 31 | segment_flag | 否 |  |  |
| 32 | segment_kind | 否 |  |  |
| 33 | update_date | 否 |  |  |
| 34 | update_time | 否 |  |  |
| 35 | transaction_no | 否 |  |  |
| 36 | position_str | 否 |  | stock_type(4)+fare_type(1)+exchange_type(4)+entrust_bs(1)+st |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_bfare1 | 默认 | 否 |  |
| idx_usps_bfare1 | ART | 是 | stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type, stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type |
| idx_usps_bfare1 | 默认 | 否 |  |
| idx_usps_bfare1 | ART | 是 | stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type, stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_bfare1 | stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type, stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type |
| idx_usps_bfare1 | stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type, stock_type, fare_type, exchange_type, entrust_bs, stock_code, blocktrade_flag, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:40:22 | 3.0.2.103 | taocong45644 | 当前表usps_bfare1，修改了索引idx_usps_bfare1,索引字段修改为：(stock_type,fare... |
| 2025-02-17 10:45:14 | 3.0.6.48 | 李想 | 新增表 |
| 2025-12-01 15:40:22 | 3.0.2.103 | taocong45644 | 当前表usps_bfare1，修改了索引idx_usps_bfare1,索引字段修改为：(stock_type,fare... |
| 2025-02-17 10:45:14 | 3.0.6.48 | 李想 | 新增表 |

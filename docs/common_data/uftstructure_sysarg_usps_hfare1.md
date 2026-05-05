# usps_hfare1 - 一级回购费用表

**表对象ID**: 127
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | entrust_bs | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | balance_ratio | 否 |  |  |
| 8 | par_ratio | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | max_fare | 否 |  |  |
| 11 | segment_flag | 否 |  |  |
| 12 | segment_kind | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | position_str | 否 |  | stock_code(8)+fare_type(1)+exchange_type(4)+money_type(3)+en |
| 17 | fare_type | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | entrust_bs | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | balance_ratio | 否 |  |  |
| 24 | par_ratio | 否 |  |  |
| 25 | min_fare | 否 |  |  |
| 26 | max_fare | 否 |  |  |
| 27 | segment_flag | 否 |  |  |
| 28 | segment_kind | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | position_str | 否 |  | stock_code(8)+fare_type(1)+exchange_type(4)+money_type(3)+en |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_hfare1 | 默认 | 否 |  |
| idx_usps_hfare1_branch | 默认 | 否 |  |
| idx_usps_hfare1 | ART | 是 | stock_code, fare_type, exchange_type, money_type, entrust_bs, stock_code, fare_type, exchange_type, money_type, entrust_bs |
| idx_usps_hfare1_branch | ART | 是 | branch_no, branch_no |
| idx_usps_hfare1 | 默认 | 否 |  |
| idx_usps_hfare1_branch | 默认 | 否 |  |
| idx_usps_hfare1 | ART | 是 | stock_code, fare_type, exchange_type, money_type, entrust_bs, stock_code, fare_type, exchange_type, money_type, entrust_bs |
| idx_usps_hfare1_branch | ART | 是 | branch_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_hfare1 | stock_code, fare_type, exchange_type, money_type, entrust_bs, stock_code, fare_type, exchange_type, money_type, entrust_bs |
| idx_usps_hfare1 | stock_code, fare_type, exchange_type, money_type, entrust_bs, stock_code, fare_type, exchange_type, money_type, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:41:59 | 3.0.2.103 | taocong45644 | 当前表usps_hfare1，修改了索引idx_usps_hfare1,索引字段修改为：(stock_code,fare... |
| 2025-02-14 17:40:42 | 3.0.6.47 | 李想 | 新增表 |
| 2025-12-01 15:41:59 | 3.0.2.103 | taocong45644 | 当前表usps_hfare1，修改了索引idx_usps_hfare1,索引字段修改为：(stock_code,fare... |
| 2025-02-14 17:40:42 | 3.0.6.47 | 李想 | 新增表 |

# ref_fare - 转融通出借费用表

**表对象ID**: 6006
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | reffare_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | ref_term | 否 |  |  |
| 5 | balance_type | 否 |  |  |
| 6 | balance_ratio | 否 |  |  |
| 7 | balance_fare | 否 |  |  |
| 8 | max_fare | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | position_str | 否 |  | reffare_kind(10)+ref_term(5)+exchange_type(4)+stock_code(8) |
| 14 | reffare_kind | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | ref_term | 否 |  |  |
| 18 | balance_type | 否 |  |  |
| 19 | balance_ratio | 否 |  |  |
| 20 | balance_fare | 否 |  |  |
| 21 | max_fare | 否 |  |  |
| 22 | min_fare | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | reffare_kind(10)+ref_term(5)+exchange_type(4)+stock_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_fare | ART | 是 | reffare_kind, ref_term, exchange_type, stock_code, reffare_kind, ref_term, exchange_type, stock_code |
| idx_ref_fare | ART | 是 | reffare_kind, ref_term, exchange_type, stock_code, reffare_kind, ref_term, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_fare | reffare_kind, ref_term, exchange_type, stock_code, reffare_kind, ref_term, exchange_type, stock_code |
| idx_ref_fare | reffare_kind, ref_term, exchange_type, stock_code, reffare_kind, ref_term, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 10:58:12 | 1.0.0.5 | 李想 | 新增表 |
| 2025-02-21 10:58:12 | 1.0.0.5 | 李想 | 新增表 |

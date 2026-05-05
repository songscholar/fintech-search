# ref_exchange_time - 转融通交易时间表

**表对象ID**: 6011
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | time_kind | 否 |  |  |
| 3 | time_order | 否 |  |  |
| 4 | time_name | 否 |  |  |
| 5 | begin_time | 否 |  |  |
| 6 | end_time | 否 |  |  |
| 7 | en_refbusi_code | 否 |  |  |
| 8 | withdraw | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | time_kind(1)+time_order(5)+exchange_type(4) |
| 13 | exchange_type | 否 |  |  |
| 14 | time_kind | 否 |  |  |
| 15 | time_order | 否 |  |  |
| 16 | time_name | 否 |  |  |
| 17 | begin_time | 否 |  |  |
| 18 | end_time | 否 |  |  |
| 19 | en_refbusi_code | 否 |  |  |
| 20 | withdraw | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | position_str | 否 |  | time_kind(1)+time_order(5)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_exchange_time | ART | 是 | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_ref_exchange_time_normal | ART | 是 | time_kind, exchange_type, time_kind, exchange_type |
| idx_ref_exchange_time | ART | 是 | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_ref_exchange_time_normal | ART | 是 | time_kind, exchange_type, time_kind, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_exchange_time | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |
| idx_ref_exchange_time | time_kind, time_order, exchange_type, time_kind, time_order, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:09:21 | 1.0.0.10 | 李想 | 新增表 |
| 2025-02-21 11:09:21 | 1.0.0.10 | 李想 | 新增表 |

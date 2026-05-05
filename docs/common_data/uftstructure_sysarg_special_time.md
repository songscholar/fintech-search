# special_time - 特殊时间表

**表对象ID**: 365
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | special_time_kind | 否 |  |  |
| 2 | time_order | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | en_stock_type | 否 |  |  |
| 5 | res_stock_type | 否 |  |  |
| 6 | spec_time_name | 否 |  |  |
| 7 | begin_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | special_time_kind | 否 |  |  |
| 10 | time_order | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | en_stock_type | 否 |  |  |
| 13 | res_stock_type | 否 |  |  |
| 14 | spec_time_name | 否 |  |  |
| 15 | begin_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_special_time_ex | ART | 是 | special_time_kind, exchange_type, special_time_kind, exchange_type |
| idx_special_time | ART | 是 | time_order, time_order |
| idx_special_time_ex | ART | 是 | special_time_kind, exchange_type, special_time_kind, exchange_type |
| idx_special_time | ART | 是 | time_order, time_order |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_special_time | time_order, time_order |
| idx_special_time | time_order, time_order |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-10 11:19:25 | 3.0.2.75 | 彭雪锋 | 新增表 |
| 2025-02-10 11:19:25 | 3.0.2.75 | 彭雪锋 | 新增表 |

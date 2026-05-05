# uopt_exchtime - 期权交易时间表

**表对象ID**: 9002
**所属模块**: optarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | time_kind | 是 |  |  |
| 3 | time_order | 是 |  |  |
| 4 | time_name | 是 |  |  |
| 5 | begin_time | 是 |  |  |
| 6 | end_time | 是 |  |  |
| 7 | duration | 是 |  |  |
| 8 | withdraw | 是 |  |  |
| 9 | update_date | 是 |  |  |
| 10 | update_time | 是 |  |  |
| 11 | transaction_no | 是 |  |  |
| 12 | en_stock_type | 是 |  |  |
| 13 | en_option_type | 是 |  |  |
| 14 | en_entrust_oc | 是 |  |  |
| 15 | en_entrust_prop | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | time_kind | 是 |  |  |
| 18 | time_order | 是 |  |  |
| 19 | time_name | 是 |  |  |
| 20 | begin_time | 是 |  |  |
| 21 | end_time | 是 |  |  |
| 22 | duration | 是 |  |  |
| 23 | withdraw | 是 |  |  |
| 24 | update_date | 是 |  |  |
| 25 | update_time | 是 |  |  |
| 26 | transaction_no | 是 |  |  |
| 27 | en_stock_type | 是 |  |  |
| 28 | en_option_type | 是 |  |  |
| 29 | en_entrust_oc | 是 |  |  |
| 30 | en_entrust_prop | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_exchtime | 默认 | 是 | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |
| idx_uopt_exchtime | 默认 | 是 | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optexchtime | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |
| idx_optexchtime | exchange_type, time_kind, time_order, exchange_type, time_kind, time_order |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-04-25 09:39:26 | V3.0.3.1 | wuxd | 统一版本 |
| 2023-12-16 17:28:16 | 3.0.0.0 | wuxd |  |
| 2024-04-25 09:39:26 | V3.0.3.1 | wuxd | 统一版本 |
| 2023-12-16 17:28:16 | 3.0.0.0 | wuxd |  |

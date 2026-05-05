# usps_securate - 交易汇率表

**表对象ID**: 497
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | buy_exchange_rate | 否 |  |  |
| 3 | sell_exchange_rate | 否 |  |  |
| 4 | middle_exchange_rate | 否 |  |  |
| 5 | valid_date | 否 |  |  |
| 6 | buy_float_ratio | 否 |  |  |
| 7 | sell_float_ratio | 否 |  |  |
| 8 | buy_settlement_rate | 否 |  |  |
| 9 | sell_settlement_rate | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | buy_exchange_rate | 否 |  |  |
| 15 | sell_exchange_rate | 否 |  |  |
| 16 | middle_exchange_rate | 否 |  |  |
| 17 | valid_date | 否 |  |  |
| 18 | buy_float_ratio | 否 |  |  |
| 19 | sell_float_ratio | 否 |  |  |
| 20 | buy_settlement_rate | 否 |  |  |
| 21 | sell_settlement_rate | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_securate | ART | 是 | exchange_type, exchange_type |
| uk_rpt_uspssecurate | ART | 是 | valid_date, exchange_type, valid_date, exchange_type |
| idx_usps_securate | ART | 是 | exchange_type, exchange_type |
| uk_rpt_uspssecurate | ART | 是 | valid_date, exchange_type, valid_date, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_securate | exchange_type, exchange_type |
| idx_usps_securate | exchange_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-24 13:25:33 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-09-09 11:10:57 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2024-04-29 10:36:14 | 3.0.2.7 | 汪林 | 新增交易汇率表 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-24 13:25:33 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-09-09 11:10:57 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2024-04-29 10:36:14 | 3.0.2.7 | 汪林 | 新增交易汇率表 |

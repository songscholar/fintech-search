# stktrade_quota_used - 证券交易额度使用情况信息表

**表对象ID**: 1612
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | quota_flag | 否 |  |  |
| 5 | day_buy_used_amount | 否 |  |  |
| 6 | day_buy_used_quota | 否 |  |  |
| 7 | day_sell_used_amount | 否 |  |  |
| 8 | day_sell_used_quota | 否 |  |  |
| 9 | acode_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | quota_flag | 否 |  |  |
| 13 | day_buy_used_amount | 否 |  |  |
| 14 | day_buy_used_quota | 否 |  |  |
| 15 | day_sell_used_amount | 否 |  |  |
| 16 | day_sell_used_quota | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_stktrade_quota_used | ART | 是 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| uk_stktrade_quota_used | ART | 是 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stktrade_quota_used | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| idx_stktrade_quota_used | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:43:08 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2024-01-23 15:13:04 | V3.0.1.8 | 许琮擎 | 物理表stktrade_quota_used，删除了表字段(begin_date);
物理表stktrade_quot... |
| 2024-01-16 14:03:22 | V3.0.1.7 | 董瑞辉 | 新增表结构stktrade_quota_used |
| 2026-03-05 16:43:08 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2024-01-23 15:13:04 | V3.0.1.8 | 许琮擎 | 物理表stktrade_quota_used，删除了表字段(begin_date);
物理表stktrade_quot... |
| 2024-01-16 14:03:22 | V3.0.1.7 | 董瑞辉 | 新增表结构stktrade_quota_used |

# stktrade_quota - 证券交易额度信息表

**表对象ID**: 1611
**所属模块**: qmsacctquota
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | quota_flag | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | day_buy_amount_uplimit | 否 |  |  |
| 8 | day_buy_balance_uplimit | 否 |  |  |
| 9 | one_buy_amount_uplimit | 否 |  |  |
| 10 | one_buy_balance_uplimit | 否 |  |  |
| 11 | day_sell_amount_uplimit | 否 |  |  |
| 12 | day_sell_balance_uplimit | 否 |  |  |
| 13 | one_sell_amount_uplimit | 否 |  |  |
| 14 | one_sell_balance_uplimit | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | acode_account(20)+exchange_type(4)+stock_code(8)+quota_flag( |
| 20 | acode_account | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | quota_flag | 否 |  |  |
| 24 | begin_date | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | day_buy_amount_uplimit | 否 |  |  |
| 27 | day_buy_balance_uplimit | 否 |  |  |
| 28 | one_buy_amount_uplimit | 否 |  |  |
| 29 | one_buy_balance_uplimit | 否 |  |  |
| 30 | day_sell_amount_uplimit | 否 |  |  |
| 31 | day_sell_balance_uplimit | 否 |  |  |
| 32 | one_sell_amount_uplimit | 否 |  |  |
| 33 | one_sell_balance_uplimit | 否 |  |  |
| 34 | transaction_no | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | acode_account(20)+exchange_type(4)+stock_code(8)+quota_flag( |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stktrade_quota | 默认 | 否 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| uk_stktrade_quota | 默认 | 否 |  |
| uk_stktrade_quota | ART | 是 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| idx_stktrade_quota | 默认 | 否 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| uk_stktrade_quota | 默认 | 否 |  |
| uk_stktrade_quota | ART | 是 | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stktrade_quota | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |
| idx_stktrade_quota | acode_account, exchange_type, stock_code, quota_flag, acode_account, exchange_type, stock_code, quota_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:42:40 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 18:09:16 | 3.0.6.13 | 常行 | 物理表stktrade_quota，增加索引(idx_stktrade_quota:[acode_account,exc... |
| 2025-07-17 18:08:31 | 3.0.6.13 | 常行 | 物理表stktrade_quota，删除了表索引(uk_stktrade_quota);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2025-02-19 15:22:01 | 3.0.2.9 | 李想 | 物理表stktrade_quota，添加了表字段(remark);
物理表stktrade_quota，添加了表字段(... |
| 2024-01-19 17:24:10 | V3.0.1.8 | 许琮擎 | 物理表stktrade_quota，添加了表字段(transaction_no);
 |
| 2024-01-16 14:01:48 | V3.0.1.7 | 董瑞辉 | 新增表结构stktrade_quota |
| 2026-03-05 16:42:40 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 18:09:16 | 3.0.6.13 | 常行 | 物理表stktrade_quota，增加索引(idx_stktrade_quota:[acode_account,exc... |
| 2025-07-17 18:08:31 | 3.0.6.13 | 常行 | 物理表stktrade_quota，删除了表索引(uk_stktrade_quota);
 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2025-02-19 15:22:01 | 3.0.2.9 | 李想 | 物理表stktrade_quota，添加了表字段(remark);
物理表stktrade_quota，添加了表字段(... |
| 2024-01-19 17:24:10 | V3.0.1.8 | 许琮擎 | 物理表stktrade_quota，添加了表字段(transaction_no);
 |
| 2024-01-16 14:01:48 | V3.0.1.7 | 董瑞辉 | 新增表结构stktrade_quota |

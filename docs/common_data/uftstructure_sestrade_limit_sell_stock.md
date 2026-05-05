# limit_sell_stock - 限售股份信息表

**表对象ID**: 5521
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | limit_type | 否 |  |  |
| 7 | limit_flag | 否 |  |  |
| 8 | month_sell_amount | 否 |  |  |
| 9 | month_limit_ratio | 否 |  |  |
| 10 | total_sell_amount | 否 |  |  |
| 11 | total_limit_ratio | 否 |  |  |
| 12 | occur_times | 否 |  |  |
| 13 | create_date | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | client_id | 否 |  |  |
| 20 | limit_type | 否 |  |  |
| 21 | limit_flag | 否 |  |  |
| 22 | month_sell_amount | 否 |  |  |
| 23 | month_limit_ratio | 否 |  |  |
| 24 | total_sell_amount | 否 |  |  |
| 25 | total_limit_ratio | 否 |  |  |
| 26 | occur_times | 否 |  |  |
| 27 | create_date | 否 |  |  |
| 28 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_limit_sell_stock | 默认 | 否 | fund_account, fund_account |
| idx_limit_sell_stock | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type |
| idx_limit_sell_stock_acct | ART | 是 | fund_account, fund_account |
| idx_limit_sell_stock | 默认 | 否 | fund_account, fund_account |
| idx_limit_sell_stock | ART | 是 | stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type |
| idx_limit_sell_stock_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_limit_sell_stock | stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type |
| idx_limit_sell_stock | stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:44:46 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-25 10:38:41 | 3.0.2.47 | 程猛 | 物理表limit_sell_stock，增加索引字段(索引idx_limit_sell_stock:增加了索引字段：fu... |
| 2024-05-29 21:23:15 | 3.0.2.13 | 祝丁恺 | 勾选不回库选项 |
| 2026-03-09 13:44:46 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-25 10:38:41 | 3.0.2.47 | 程猛 | 物理表limit_sell_stock，增加索引字段(索引idx_limit_sell_stock:增加了索引字段：fu... |
| 2024-05-29 21:23:15 | 3.0.2.13 | 祝丁恺 | 勾选不回库选项 |

# uft_ses_fund_detail - UFT证券交易资金详细信息表

**表对象ID**: 5977
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | business_frozen_balance | 否 |  |  |
| 6 | business_unfrozen_balance | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | partition_no | 否 |  |  |
| 9 | order_no | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | business_frozen_balance | 否 |  |  |
| 15 | business_unfrozen_balance | 否 |  |  |
| 16 | fund_enable_level | 否 |  |  |
| 17 | partition_no | 否 |  |  |
| 18 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_ses_fund_detail | 默认 | 否 |  |
| uk_uft_ses_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| uk_uft_ses_fund_detail | 默认 | 否 |  |
| uk_uft_ses_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_ses_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| uk_uft_ses_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:51:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:29:12 | 3.0.2.104 | taocong45644 | 当前表uft_ses_fund_detail，修改了索引uk_uft_ses_fund_detail,索引字段修改为：(... |
| 2025-03-11 11:06:36 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-09 14:51:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:29:12 | 3.0.2.104 | taocong45644 | 当前表uft_ses_fund_detail，修改了索引uk_uft_ses_fund_detail,索引字段修改为：(... |
| 2025-03-11 11:06:36 | 3.0.2.2001 | 杨新照 | 新增表结构 |

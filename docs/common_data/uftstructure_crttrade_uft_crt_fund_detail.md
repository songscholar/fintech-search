# uft_crt_fund_detail - UFT融资融券资金详细信息表

**表对象ID**: 7993
**所属模块**: crttrade
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

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_crt_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_uft_crt_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_crt_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_uft_crt_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

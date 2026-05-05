# uopt_rates - 期权利率参数表

**表对象ID**: 9033
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | optrates_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | interest_rate | 否 |  |  |
| 10 | fine_rate | 否 |  |  |
| 11 | fare_rate | 否 |  |  |
| 12 | float_ratio | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | company_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | optrates_type | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | money_type | 否 |  |  |
| 23 | stock_type | 否 |  |  |
| 24 | interest_rate | 否 |  |  |
| 25 | fine_rate | 否 |  |  |
| 26 | fare_rate | 否 |  |  |
| 27 | float_ratio | 否 |  |  |
| 28 | update_date | 否 |  |  |
| 29 | update_time | 否 |  |  |
| 30 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optrates | 默认 | 是 | fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type, fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type |
| idx_optrates | 默认 | 是 | fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type, fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optrates | fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type, fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type |
| idx_optrates | fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type, fund_account, company_no, optrates_type, exchange_type, stock_type, stock_code, money_type |

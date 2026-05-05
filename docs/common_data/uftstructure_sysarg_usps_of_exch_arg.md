# usps_of_exch_arg - 基金交易参数表

**表对象ID**: 95
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_company | 否 |  |  |
| 2 | company_name | 否 |  |  |
| 3 | companysimple_name | 否 |  |  |
| 4 | agency_no | 否 |  |  |
| 5 | account_len | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | dividend_flag | 否 |  |  |
| 8 | exchange_status | 否 |  |  |
| 9 | subscribe_type | 否 |  |  |
| 10 | ofexcharg_flag | 否 |  |  |
| 11 | address | 否 |  |  |
| 12 | phone | 否 |  |  |
| 13 | en_company_no | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | fund_company | 否 |  |  |
| 16 | company_name | 否 |  |  |
| 17 | companysimple_name | 否 |  |  |
| 18 | agency_no | 否 |  |  |
| 19 | account_len | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | dividend_flag | 否 |  |  |
| 22 | exchange_status | 否 |  |  |
| 23 | subscribe_type | 否 |  |  |
| 24 | ofexcharg_flag | 否 |  |  |
| 25 | address | 否 |  |  |
| 26 | phone | 否 |  |  |
| 27 | en_company_no | 否 |  |  |
| 28 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ofexcharg | ART | 是 | fund_company, fund_company |
| idx_ofexcharg | ART | 是 | fund_company, fund_company |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ofexcharg | fund_company, fund_company |
| idx_ofexcharg | fund_company, fund_company |

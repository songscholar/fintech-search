# uopt_company_account - 期权公司账户表

**表对象ID**: 9023
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | opt_cmpacct_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | partition_no | 否 |  |  |
| 10 | company_no | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | opt_cmpacct_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_company_account | 默认 | 是 | company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account |
| idx_uopt_company_account | 默认 | 是 | company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_company_account | company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account |
| idx_uopt_company_account | company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-14 17:03:48 | V3.0.2.1 | 韦子晗 | uopt_company_account表新增partition_no字段 |
| 2025-08-14 17:03:48 | V3.0.2.1 | 韦子晗 | uopt_company_account表新增partition_no字段 |

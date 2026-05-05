# uopt_acct_marginfloat - 期权客户保证金浮动比例表

**表对象ID**: 9608
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | update_date | 否 |  |  |
| 3 | update_time | 否 |  |  |
| 4 | op_remark | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | option_type | 否 |  |  |
| 10 | option_code | 否 |  |  |
| 11 | margin_ratio | 否 |  |  |
| 12 | near_final_days | 否 |  |  |
| 13 | near_final_time | 否 |  |  |
| 14 | near_final_ratio | 否 |  |  |
| 15 | near_final_ratio_kind | 否 |  |  |
| 16 | comb_upbail_balance | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | op_remark | 否 |  |  |
| 25 | company_no | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_type | 否 |  |  |
| 29 | option_type | 否 |  |  |
| 30 | option_code | 否 |  |  |
| 31 | margin_ratio | 否 |  |  |
| 32 | near_final_days | 否 |  |  |
| 33 | near_final_time | 否 |  |  |
| 34 | near_final_ratio | 否 |  |  |
| 35 | near_final_ratio_kind | 否 |  |  |
| 36 | comb_upbail_balance | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | remark | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_acct_marginfloat | 默认 | 否 | exchange_type, stock_type, option_code, company_no, option_type, stock_code, exchange_type, stock_type, option_code, company_no, option_type, stock_code |
| idx_uopt_acct_marginfloat_cmpno | 默认 | 是 | company_no, fund_account, company_no, fund_account |
| idx_uopt_acct_marginfloat_qry | 默认 | 是 | fund_account, exchange_type, company_no, option_type, stock_type, stock_code, option_code, fund_account, exchange_type, company_no, option_type, stock_type, stock_code, option_code |
| idx_uopt_acct_marginfloat_qrycomb | 默认 | 是 | fund_account, exchange_type, option_type, company_no, stock_type, option_code, stock_code, fund_account, exchange_type, option_type, company_no, stock_type, option_code, stock_code |
| idx_uopt_acct_marginfloat_temp | 默认 | 是 | stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code, stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code |
| idx_uopt_acct_marginfloat | 默认 | 否 | exchange_type, stock_type, option_code, company_no, option_type, stock_code, exchange_type, stock_type, option_code, company_no, option_type, stock_code |
| idx_uopt_acct_marginfloat_cmpno | 默认 | 是 | company_no, fund_account, company_no, fund_account |
| idx_uopt_acct_marginfloat_qry | 默认 | 是 | fund_account, exchange_type, company_no, option_type, stock_type, stock_code, option_code, fund_account, exchange_type, company_no, option_type, stock_type, stock_code, option_code |
| idx_uopt_acct_marginfloat_qrycomb | 默认 | 是 | fund_account, exchange_type, option_type, company_no, stock_type, option_code, stock_code, fund_account, exchange_type, option_type, company_no, stock_type, option_code, stock_code |
| idx_uopt_acct_marginfloat_temp | 默认 | 是 | stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code, stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_acct_marginfloat | stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code, stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code |
| idx_uopt_acct_marginfloat | stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code, stock_type, fund_account, exchange_type, company_no, option_type, option_code, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-20 17:17:38 | V3.0.2.12 | 韦子晗 | 新增临时索引idx_uopt_acct_marginfloat_temp支持数据二次上场 |
| 2025-09-20 17:17:38 | V3.0.2.12 | 韦子晗 | 新增临时索引idx_uopt_acct_marginfloat_temp支持数据二次上场 |

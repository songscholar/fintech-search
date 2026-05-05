# of_cash_arg - 现金产品参数表

**表对象ID**: 353
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_company | 否 |  |  |
| 2 | fund_code | 否 |  |  |
| 3 | firm_id | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | total_quota | 否 |  |  |
| 7 | en_bank_no | 否 |  |  |
| 8 | fund_account_dest | 否 |  |  |
| 9 | channel_type | 否 |  |  |
| 10 | company_no | 否 |  |  |
| 11 | ofcashpro_quota | 否 |  |  |
| 12 | ofcashpro_sum_balance | 否 |  |  |
| 13 | ofcash_ctrlstr | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | fund_company | 否 |  |  |
| 16 | fund_code | 否 |  |  |
| 17 | firm_id | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | total_quota | 否 |  |  |
| 21 | en_bank_no | 否 |  |  |
| 22 | fund_account_dest | 否 |  |  |
| 23 | channel_type | 否 |  |  |
| 24 | company_no | 否 |  |  |
| 25 | ofcashpro_quota | 否 |  |  |
| 26 | ofcashpro_sum_balance | 否 |  |  |
| 27 | ofcash_ctrlstr | 否 |  |  |
| 28 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ofcasharg | ART | 是 | fund_company, fund_code, company_no, fund_company, fund_code, company_no |
| idx_ofcasharg | ART | 是 | fund_company, fund_code, company_no, fund_company, fund_code, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ofcasharg | fund_company, fund_code, company_no, fund_company, fund_code, company_no |
| idx_ofcasharg | fund_company, fund_code, company_no, fund_company, fund_code, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-12-10 13:55:30 | 3.0.2.34 | 范文浩 | 新增 |
| 2024-12-10 13:55:30 | 3.0.2.34 | 范文浩 | 新增 |

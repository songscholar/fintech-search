# uref_csdc_fund - 保证金资金对账原始数据

**表对象ID**: 6157
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | fund_account_join | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | current_balance | 否 |  |  |
| 6 | frozen_balance | 否 |  |  |
| 7 | ref_value | 否 |  |  |
| 8 | csfc_borrow_accttype | 否 |  |  |
| 9 | init_date | 否 |  |  |
| 10 | company_no | 否 |  |  |
| 11 | fund_account_join | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | current_balance | 否 |  |  |
| 14 | frozen_balance | 否 |  |  |
| 15 | ref_value | 否 |  |  |
| 16 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcsdcfund | ART | 是 | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |
| idx_refcsdcfund | ART | 是 | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcsdcfund | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |
| idx_refcsdcfund | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |

# uref_fund_correct - 保证金资金对账结果

**表对象ID**: 6158
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | csdc_current_balance | 否 |  |  |
| 6 | csdc_frozen_balance | 否 |  |  |
| 7 | current_balance | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | ref_value | 否 |  |  |
| 10 | check_flag | 否 |  |  |
| 11 | csfc_borrow_accttype | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | company_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | money_type | 否 |  |  |
| 16 | csdc_current_balance | 否 |  |  |
| 17 | csdc_frozen_balance | 否 |  |  |
| 18 | current_balance | 否 |  |  |
| 19 | frozen_balance | 否 |  |  |
| 20 | ref_value | 否 |  |  |
| 21 | check_flag | 否 |  |  |
| 22 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reffundcorrect | ART | 是 | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |
| idx_reffundcorrect | ART | 是 | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reffundcorrect | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |
| idx_reffundcorrect | init_date, money_type, company_no, csfc_borrow_accttype, init_date, money_type, company_no, csfc_borrow_accttype |

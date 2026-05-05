# uref_stock_correct - 保证金证券对账结果

**表对象ID**: 6160
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | csdc_current_amount | 否 |  |  |
| 8 | csdc_frozen_amount | 否 |  |  |
| 9 | current_amount | 否 |  |  |
| 10 | frozen_amount | 否 |  |  |
| 11 | last_price | 否 |  |  |
| 12 | assure_ratio | 否 |  |  |
| 13 | market_value | 否 |  |  |
| 14 | check_flag | 否 |  |  |
| 15 | csfc_borrow_accttype | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | company_no | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | csdc_current_amount | 否 |  |  |
| 23 | csdc_frozen_amount | 否 |  |  |
| 24 | current_amount | 否 |  |  |
| 25 | frozen_amount | 否 |  |  |
| 26 | last_price | 否 |  |  |
| 27 | assure_ratio | 否 |  |  |
| 28 | market_value | 否 |  |  |
| 29 | check_flag | 否 |  |  |
| 30 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refstockcorrect | ART | 是 | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |
| idx_refstockcorrect | ART | 是 | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refstockcorrect | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |
| idx_refstockcorrect | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |

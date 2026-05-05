# uref_csdc_stock - 保证金证券对账原始数据

**表对象ID**: 6159
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | last_price | 否 |  |  |
| 9 | assure_ratio | 否 |  |  |
| 10 | market_value | 否 |  |  |
| 11 | csfc_last_price | 否 |  |  |
| 12 | csfc_borrow_accttype | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | current_amount | 否 |  |  |
| 19 | frozen_amount | 否 |  |  |
| 20 | last_price | 否 |  |  |
| 21 | assure_ratio | 否 |  |  |
| 22 | market_value | 否 |  |  |
| 23 | csfc_last_price | 否 |  |  |
| 24 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcsdcstock | ART | 是 | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |
| idx_refcsdcstock | ART | 是 | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcsdcstock | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |
| idx_refcsdcstock | init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype, init_date, exchange_type, stock_code, company_no, csfc_borrow_accttype |

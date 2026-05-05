# uref_bond_putback - 保证金债券回售业务表

**表对象ID**: 6058
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | begin_amount | 否 |  |  |
| 9 | revocable_amount | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | csfc_borrow_accttype | 否 |  |  |
| 12 | company_no | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | begin_amount | 否 |  |  |
| 20 | revocable_amount | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbondputback | ART | 是 | fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype, fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype |
| idx_refbondputback | ART | 是 | fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype, fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbondputback | fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype, fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype |
| idx_refbondputback | fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype, fund_account, stock_account, stock_code, exchange_type, csfc_borrow_accttype |

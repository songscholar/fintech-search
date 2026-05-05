# uref_bail_acct - 保证金账户表

**表对象ID**: 6050
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | client_name | 否 |  |  |
| 6 | refbailacct_type | 否 |  |  |
| 7 | unen_refbs_flag | 否 |  |  |
| 8 | unen_stock_type | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | open_date | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | client_name | 否 |  |  |
| 19 | refbailacct_type | 否 |  |  |
| 20 | unen_refbs_flag | 否 |  |  |
| 21 | unen_stock_type | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_account | 否 |  |  |
| 24 | seat_no | 否 |  |  |
| 25 | open_date | 否 |  |  |
| 26 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refbailacct | ART | 是 | fund_account, company_no, exchange_type, stock_account, fund_account, company_no, exchange_type, stock_account |
| idx_refbailacct | ART | 是 | fund_account, company_no, exchange_type, stock_account, fund_account, company_no, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refbailacct | fund_account, company_no, exchange_type, stock_account, fund_account, company_no, exchange_type, stock_account |
| idx_refbailacct | fund_account, company_no, exchange_type, stock_account, fund_account, company_no, exchange_type, stock_account |

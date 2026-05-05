# uopt_cash_settlement - 期权现金结算保证金参数表

**表对象ID**: 9034
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | margin_ratio | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | margin_ratio | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optcashsettlement | 默认 | 是 | company_no, branch_no, fund_account, exchange_type, stock_type, stock_code, company_no, branch_no, fund_account, exchange_type, stock_type, stock_code |
| idx_optcashsettlement_acct | 默认 | 是 | fund_account, fund_account |
| idx_optcashsettlement_bran | 默认 | 是 | branch_no, branch_no |
| idx_optcashsettlement | 默认 | 是 | company_no, branch_no, fund_account, exchange_type, stock_type, stock_code, company_no, branch_no, fund_account, exchange_type, stock_type, stock_code |
| idx_optcashsettlement_acct | 默认 | 是 | fund_account, fund_account |
| idx_optcashsettlement_bran | 默认 | 是 | branch_no, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optcashsettlement | company_no, branch_no, fund_account, exchange_type, stock_type, stock_code, company_no, branch_no, fund_account, exchange_type, stock_type, stock_code |
| idx_optcashsettlement | company_no, branch_no, fund_account, exchange_type, stock_type, stock_code, company_no, branch_no, fund_account, exchange_type, stock_type, stock_code |

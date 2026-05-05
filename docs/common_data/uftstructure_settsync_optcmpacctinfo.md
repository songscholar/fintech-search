# optcmpacctinfo - 公司账户信息导出表

**表对象ID**: 3213
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | opt_cmpacct_type | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | seat_no | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | company_no | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | opt_cmpacct_type | 是 |  |  |
| 12 | stock_account | 是 |  |  |
| 13 | seat_no | 是 |  |  |
| 14 | branch_no | 是 |  |  |
| 15 | client_id | 是 |  |  |
| 16 | fund_account | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optcmpacctinfo_stkacc | 默认 | 是 | stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type |
| idx_optcmpacctinfo_stkacc | 默认 | 是 | stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optcmpacctinfo_stkacc | stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type |
| idx_optcmpacctinfo_stkacc | stock_account, company_no, exchange_type, opt_cmpacct_type, stock_account, company_no, exchange_type, opt_cmpacct_type |

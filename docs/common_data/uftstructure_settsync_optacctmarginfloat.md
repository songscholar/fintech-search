# optacctmarginfloat - 期权客户保证金浮动比例导出表

**表对象ID**: 3219
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | stock_type | 是 |  |  |
| 5 | option_type | 是 |  |  |
| 6 | option_code | 是 |  |  |
| 7 | margin_ratio | 是 |  |  |
| 8 | near_final_days | 是 |  |  |
| 9 | near_final_ratio | 是 |  |  |
| 10 | remark | 是 |  |  |
| 11 | near_final_ratio_kind | 是 |  |  |
| 12 | comb_upbail_balance | 是 |  |  |
| 13 | near_final_time | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | company_no | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | exchange_type | 是 |  |  |
| 18 | stock_type | 是 |  |  |
| 19 | option_type | 是 |  |  |
| 20 | option_code | 是 |  |  |
| 21 | margin_ratio | 是 |  |  |
| 22 | near_final_days | 是 |  |  |
| 23 | near_final_ratio | 是 |  |  |
| 24 | remark | 是 |  |  |
| 25 | near_final_ratio_kind | 是 |  |  |
| 26 | comb_upbail_balance | 是 |  |  |
| 27 | near_final_time | 是 |  |  |
| 28 | stock_code | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optacctmarginfloat | 默认 | 是 | fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type, fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type |
| idx_optacctmarginfloat | 默认 | 是 | fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type, fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optacctmarginfloat | fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type, fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type |
| idx_optacctmarginfloat | fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type, fund_account, company_no, exchange_type, option_code, option_type, stock_code, stock_type |

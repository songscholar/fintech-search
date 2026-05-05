# optmarginacctcash - 衍生品保证金账户头寸导出表

**表对象ID**: 3205
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | optmargin_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | fund_balance | 是 |  |  |
| 5 | enable_bail_balance | 是 |  |  |
| 6 | used_bail_balance | 是 |  |  |
| 7 | in_balance | 是 |  |  |
| 8 | out_balance | 是 |  |  |
| 9 | min_prepare_balance | 是 |  |  |
| 10 | etf_exeuncome_balance | 是 |  |  |
| 11 | exelock_bail_balance | 是 |  |  |
| 12 | etf_exeback_balance | 是 |  |  |
| 13 | exenet_balance | 是 |  |  |
| 14 | exercise_balance | 是 |  |  |
| 15 | opt_cash_balance | 是 |  |  |
| 16 | net_balance | 是 |  |  |
| 17 | total_in_balance | 是 |  |  |
| 18 | total_out_balance | 是 |  |  |
| 19 | company_no | 是 |  |  |
| 20 | optmargin_account | 是 |  |  |
| 21 | exchange_type | 是 |  |  |
| 22 | fund_balance | 是 |  |  |
| 23 | enable_bail_balance | 是 |  |  |
| 24 | used_bail_balance | 是 |  |  |
| 25 | in_balance | 是 |  |  |
| 26 | out_balance | 是 |  |  |
| 27 | min_prepare_balance | 是 |  |  |
| 28 | etf_exeuncome_balance | 是 |  |  |
| 29 | exelock_bail_balance | 是 |  |  |
| 30 | etf_exeback_balance | 是 |  |  |
| 31 | exenet_balance | 是 |  |  |
| 32 | exercise_balance | 是 |  |  |
| 33 | opt_cash_balance | 是 |  |  |
| 34 | net_balance | 是 |  |  |
| 35 | total_in_balance | 是 |  |  |
| 36 | total_out_balance | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optmarginacctcash | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |
| idx_optmarginacctcash | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optmarginacctcash | company_no, exchange_type, company_no, exchange_type |
| idx_optmarginacctcash | company_no, exchange_type, company_no, exchange_type |

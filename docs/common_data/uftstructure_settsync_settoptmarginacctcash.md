# settoptmarginacctcash - 清算期权保证金账户头寸表

**表对象ID**: 3224
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

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
| 17 | modify_flag | 是 |  |  |
| 18 | total_in_balance | 是 |  |  |
| 19 | total_out_balance | 是 |  |  |
| 20 | company_no | 是 |  |  |
| 21 | optmargin_account | 是 |  |  |
| 22 | exchange_type | 是 |  |  |
| 23 | fund_balance | 是 |  |  |
| 24 | enable_bail_balance | 是 |  |  |
| 25 | used_bail_balance | 是 |  |  |
| 26 | in_balance | 是 |  |  |
| 27 | out_balance | 是 |  |  |
| 28 | min_prepare_balance | 是 |  |  |
| 29 | etf_exeuncome_balance | 是 |  |  |
| 30 | exelock_bail_balance | 是 |  |  |
| 31 | etf_exeback_balance | 是 |  |  |
| 32 | exenet_balance | 是 |  |  |
| 33 | exercise_balance | 是 |  |  |
| 34 | opt_cash_balance | 是 |  |  |
| 35 | net_balance | 是 |  |  |
| 36 | modify_flag | 是 |  |  |
| 37 | total_in_balance | 是 |  |  |
| 38 | total_out_balance | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptmarginacctcash | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |
| idx_settoptmarginacctcash | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settoptmarginacctcash | company_no, exchange_type, company_no, exchange_type |
| idx_settoptmarginacctcash | company_no, exchange_type, company_no, exchange_type |

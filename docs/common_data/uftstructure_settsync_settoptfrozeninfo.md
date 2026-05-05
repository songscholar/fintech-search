# settoptfrozeninfo - 清算期权冻结信息表

**表对象ID**: 3231
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | company_no | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | client_id | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | money_type | 是 |  |  |
| 7 | opt_frozen_type | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_type | 是 |  |  |
| 12 | frozen_amount | 是 |  |  |
| 13 | frozen_balance | 是 |  |  |
| 14 | date_clear | 是 |  |  |
| 15 | remark | 是 |  |  |
| 16 | init_date | 是 |  |  |
| 17 | company_no | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | client_id | 是 |  |  |
| 20 | fund_account | 是 |  |  |
| 21 | money_type | 是 |  |  |
| 22 | opt_frozen_type | 是 |  |  |
| 23 | exchange_type | 是 |  |  |
| 24 | stock_account | 是 |  |  |
| 25 | stock_code | 是 |  |  |
| 26 | stock_type | 是 |  |  |
| 27 | frozen_amount | 是 |  |  |
| 28 | frozen_balance | 是 |  |  |
| 29 | date_clear | 是 |  |  |
| 30 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptfrozeninfo | 默认 | 是 | fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type, fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type |
| idx_settoptfrozeninfo | 默认 | 是 | fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type, fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settoptfrozeninfo | fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type, fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type |
| idx_settoptfrozeninfo | fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type, fund_account, exchange_type, stock_type, opt_frozen_type, stock_code, money_type |

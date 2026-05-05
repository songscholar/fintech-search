# settoptexedeliver - 清算期权行权交收表

**表对象ID**: 3230
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | money_type | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | stock_type | 是 |  |  |
| 11 | clear_amount | 是 |  |  |
| 12 | settle_amount | 是 |  |  |
| 13 | short_amount | 是 |  |  |
| 14 | advance_amount | 是 |  |  |
| 15 | report_amount | 是 |  |  |
| 16 | clear_balance | 是 |  |  |
| 17 | opt_cash_amount | 是 |  |  |
| 18 | opt_cash_balance | 是 |  |  |
| 19 | date_clear | 是 |  |  |
| 20 | position_str | 是 |  |  |
| 21 | init_date | 是 |  |  |
| 22 | serial_no | 是 |  |  |
| 23 | branch_no | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | money_type | 是 |  |  |
| 26 | client_id | 是 |  |  |
| 27 | fund_account | 是 |  |  |
| 28 | stock_account | 是 |  |  |
| 29 | stock_code | 是 |  |  |
| 30 | stock_type | 是 |  |  |
| 31 | clear_amount | 是 |  |  |
| 32 | settle_amount | 是 |  |  |
| 33 | short_amount | 是 |  |  |
| 34 | advance_amount | 是 |  |  |
| 35 | report_amount | 是 |  |  |
| 36 | clear_balance | 是 |  |  |
| 37 | opt_cash_amount | 是 |  |  |
| 38 | opt_cash_balance | 是 |  |  |
| 39 | date_clear | 是 |  |  |
| 40 | position_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settoptexedeliver | 默认 | 是 | position_str, position_str |
| idx_settoptexedeliver | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settoptexedeliver | position_str, position_str |
| idx_settoptexedeliver | position_str, position_str |

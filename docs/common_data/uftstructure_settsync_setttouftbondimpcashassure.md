# setttouftbondimpcashassure - 清债券回购现金担保品余额表

**表对象ID**: 3007
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | reserve_account | 是 |  |  |
| 6 | seat_no | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | cashassure_amount | 是 |  |  |
| 10 | used_fetch_amount | 是 |  |  |
| 11 | position_str | 是 |  |  |
| 12 | set_seat_no | 是 |  |  |
| 13 | init_date | 是 |  |  |
| 14 | branch_no | 是 |  |  |
| 15 | client_id | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | reserve_account | 是 |  |  |
| 18 | seat_no | 是 |  |  |
| 19 | exchange_type | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | cashassure_amount | 是 |  |  |
| 22 | used_fetch_amount | 是 |  |  |
| 23 | position_str | 是 |  |  |
| 24 | set_seat_no | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settbondimpcashassure_pos | 默认 | 是 | position_str, position_str |
| idx_settbondimpcashassure_acct | 默认 | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |
| idx_settbondimpcashassure_pos | 默认 | 是 | position_str, position_str |
| idx_settbondimpcashassure_acct | 默认 | 是 | fund_account, stock_account, exchange_type, fund_account, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settbondimpcashassure_pos | position_str, position_str |
| idx_settbondimpcashassure_pos | position_str, position_str |

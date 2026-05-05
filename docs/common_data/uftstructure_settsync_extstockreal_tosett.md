# extstockreal_tosett - 股份交易信息拓展表

**表对象ID**: 3074
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | money_type | 是 |  |  |
| 9 | stock_type | 是 |  |  |
| 10 | available_amount | 是 |  |  |
| 11 | frozen_amount | 是 |  |  |
| 12 | unfrozen_amount | 是 |  |  |
| 13 | trade_amount | 是 |  |  |
| 14 | seat_no | 是 |  |  |
| 15 | check_str | 是 |  |  |
| 16 | position_str | 是 |  |  |
| 17 | date_clear | 是 |  |  |
| 18 | init_date | 是 |  |  |
| 19 | stock_account | 是 |  |  |
| 20 | stock_code | 是 |  |  |
| 21 | branch_no | 是 |  |  |
| 22 | exchange_type | 是 |  |  |
| 23 | fund_account | 是 |  |  |
| 24 | client_id | 是 |  |  |
| 25 | money_type | 是 |  |  |
| 26 | stock_type | 是 |  |  |
| 27 | available_amount | 是 |  |  |
| 28 | frozen_amount | 是 |  |  |
| 29 | unfrozen_amount | 是 |  |  |
| 30 | trade_amount | 是 |  |  |
| 31 | seat_no | 是 |  |  |
| 32 | check_str | 是 |  |  |
| 33 | position_str | 是 |  |  |
| 34 | date_clear | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_extstockreal_pos | 默认 | 是 | position_str, position_str |
| idx_extstockreal_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_extstockreal_pos | position_str, position_str |
| idx_extstockreal_pos | position_str, position_str |

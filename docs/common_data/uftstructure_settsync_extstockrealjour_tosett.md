# extstockrealjour_tosett - 股份交易信息拓展流水表

**表对象ID**: 3075
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | curr_date | 是 |  |  |
| 4 | curr_time | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | seat_no | 是 |  |  |
| 12 | real_action | 是 |  |  |
| 13 | business_flag | 是 |  |  |
| 14 | occur_amount | 是 |  |  |
| 15 | post_amount | 是 |  |  |
| 16 | cancel_serialno | 是 |  |  |
| 17 | remark | 是 |  |  |
| 18 | position_str | 是 |  |  |
| 19 | update_date | 是 |  |  |
| 20 | update_time | 是 |  |  |
| 21 | transaction_no | 是 |  |  |
| 22 | asset_prop | 是 |  |  |
| 23 | init_date | 是 |  |  |
| 24 | serial_no | 是 |  |  |
| 25 | curr_date | 是 |  |  |
| 26 | curr_time | 是 |  |  |
| 27 | branch_no | 是 |  |  |
| 28 | client_id | 是 |  |  |
| 29 | fund_account | 是 |  |  |
| 30 | exchange_type | 是 |  |  |
| 31 | stock_account | 是 |  |  |
| 32 | stock_code | 是 |  |  |
| 33 | seat_no | 是 |  |  |
| 34 | real_action | 是 |  |  |
| 35 | business_flag | 是 |  |  |
| 36 | occur_amount | 是 |  |  |
| 37 | post_amount | 是 |  |  |
| 38 | cancel_serialno | 是 |  |  |
| 39 | remark | 是 |  |  |
| 40 | position_str | 是 |  |  |
| 41 | update_date | 是 |  |  |
| 42 | update_time | 是 |  |  |
| 43 | transaction_no | 是 |  |  |
| 44 | asset_prop | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_extstockrealjour_pos | 默认 | 是 | position_str, position_str |
| idx_extstockrealjour_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_extstockrealjour_pos | position_str, position_str |
| idx_extstockrealjour_pos | position_str, position_str |

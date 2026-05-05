# setttouftstock - 清算入账股份表

**表对象ID**: 3089
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | seat_no | 是 |  |  |
| 5 | stock_type | 是 |  |  |
| 6 | money_type | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | client_id | 是 |  |  |
| 9 | begin_amount | 是 |  | 全量 |
| 10 | current_amount | 是 |  | 增量 |
| 11 | uncome_buy_amount | 是 |  | 增量 |
| 12 | uncome_sell_amount | 是 |  | 增量 |
| 13 | frozen_amount | 是 |  | 增量 |
| 14 | unfrozen_amount | 是 |  | 增量 |
| 15 | correct_amount | 是 |  | 增量 |
| 16 | enable_amount | 是 |  | 增量 |
| 17 | sum_buy_amount | 是 |  | 增量 |
| 18 | sum_buy_balance | 是 |  | 增量 |
| 19 | sum_sell_amount | 是 |  | 增量 |
| 20 | sum_sell_balance | 是 |  | 增量 |
| 21 | cost_price | 是 |  | 全量 |
| 22 | asset_prop | 是 |  |  |
| 23 | stock_flag | 是 |  |  |
| 24 | flow_count | 是 |  |  |
| 25 | exchange_type | 是 |  |  |
| 26 | stock_account | 是 |  |  |
| 27 | stock_code | 是 |  |  |
| 28 | seat_no | 是 |  |  |
| 29 | stock_type | 是 |  |  |
| 30 | money_type | 是 |  |  |
| 31 | fund_account | 是 |  |  |
| 32 | client_id | 是 |  |  |
| 33 | begin_amount | 是 |  | 全量 |
| 34 | current_amount | 是 |  | 增量 |
| 35 | uncome_buy_amount | 是 |  | 增量 |
| 36 | uncome_sell_amount | 是 |  | 增量 |
| 37 | frozen_amount | 是 |  | 增量 |
| 38 | unfrozen_amount | 是 |  | 增量 |
| 39 | correct_amount | 是 |  | 增量 |
| 40 | enable_amount | 是 |  | 增量 |
| 41 | sum_buy_amount | 是 |  | 增量 |
| 42 | sum_buy_balance | 是 |  | 增量 |
| 43 | sum_sell_amount | 是 |  | 增量 |
| 44 | sum_sell_balance | 是 |  | 增量 |
| 45 | cost_price | 是 |  | 全量 |
| 46 | asset_prop | 是 |  |  |
| 47 | stock_flag | 是 |  |  |
| 48 | flow_count | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| sett_stock_idx | 默认 | 是 | flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no, flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no |
| sett_stock_idx | 默认 | 是 | flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no, flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| sett_stock_idx | flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no, flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no |
| sett_stock_idx | flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no, flow_count, fund_account, stock_account, stock_code, exchange_type, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |

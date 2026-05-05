# uft_ses_stock_real - UFT证券股份交易信息表

**表对象ID**: 5974
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | correct_amount | 否 |  |  |
| 2 | cost_price | 否 |  |  |
| 3 | current_amount | 否 |  |  |
| 4 | enable_amount | 否 |  |  |
| 5 | entrust_sell_amount | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | real_buy_amount | 否 |  |  |
| 11 | real_buy_balance | 否 |  |  |
| 12 | real_sell_amount | 否 |  |  |
| 13 | real_sell_balance | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_flag | 否 |  |  |
| 17 | stock_type | 否 |  |  |
| 18 | sum_buy_amount | 否 |  |  |
| 19 | sum_buy_balance | 否 |  |  |
| 20 | sum_sell_amount | 否 |  |  |
| 21 | sum_sell_balance | 否 |  |  |
| 22 | uncome_buy_amount | 否 |  |  |
| 23 | uncome_sell_amount | 否 |  |  |
| 24 | unfrozen_amount | 否 |  |  |
| 25 | sub_stock_type | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 27 | trustee_seat_no | 否 |  |  |
| 28 | order_no | 否 |  |  |
| 29 | correct_amount | 否 |  |  |
| 30 | cost_price | 否 |  |  |
| 31 | current_amount | 否 |  |  |
| 32 | enable_amount | 否 |  |  |
| 33 | entrust_sell_amount | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | frozen_amount | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | money_type | 否 |  |  |
| 38 | real_buy_amount | 否 |  |  |
| 39 | real_buy_balance | 否 |  |  |
| 40 | real_sell_amount | 否 |  |  |
| 41 | real_sell_balance | 否 |  |  |
| 42 | stock_account | 否 |  |  |
| 43 | stock_code | 否 |  |  |
| 44 | stock_flag | 否 |  |  |
| 45 | stock_type | 否 |  |  |
| 46 | sum_buy_amount | 否 |  |  |
| 47 | sum_buy_balance | 否 |  |  |
| 48 | sum_sell_amount | 否 |  |  |
| 49 | sum_sell_balance | 否 |  |  |
| 50 | uncome_buy_amount | 否 |  |  |
| 51 | uncome_sell_amount | 否 |  |  |
| 52 | unfrozen_amount | 否 |  |  |
| 53 | sub_stock_type | 否 |  |  |
| 54 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 55 | trustee_seat_no | 否 |  |  |
| 56 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ses_stockreal_unique | 默认 | 否 |  |
| idx_uft_ses_stockreal_unique | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_uft_ses_stockreal_unique | 默认 | 否 |  |
| idx_uft_ses_stockreal_unique | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ses_stockreal_unique | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_uft_ses_stockreal_unique | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:49:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:35:36 | 3.0.2.104 | taocong45644 | 当前表uft_ses_stock_real，修改了索引idx_uft_ses_stockreal_unique,索引字段... |
| 2025-03-11 11:04:41 | 3.0.2.2001 |  | 新增表结构 |
| 2026-03-09 14:49:47 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:35:36 | 3.0.2.104 | taocong45644 | 当前表uft_ses_stock_real，修改了索引idx_uft_ses_stockreal_unique,索引字段... |
| 2025-03-11 11:04:41 | 3.0.2.2001 |  | 新增表结构 |

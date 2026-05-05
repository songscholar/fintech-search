# uft_ucrt_stock_real - UFT融资融券股份交易信息表

**表对象ID**: 7998
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | current_amount | 否 |  |  |
| 10 | uncome_buy_amount | 否 |  |  |
| 11 | uncome_sell_amount | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | unfrozen_amount | 否 |  |  |
| 14 | correct_amount | 否 |  |  |
| 15 | enable_amount | 否 |  |  |
| 16 | real_buy_amount | 否 |  |  |
| 17 | real_buy_balance | 否 |  |  |
| 18 | real_sell_amount | 否 |  |  |
| 19 | real_sell_balance | 否 |  |  |
| 20 | entrust_sell_amount | 否 |  |  |
| 21 | sum_buy_amount | 否 |  |  |
| 22 | sum_buy_balance | 否 |  |  |
| 23 | sum_sell_amount | 否 |  |  |
| 24 | sum_sell_balance | 否 |  |  |
| 25 | cost_price | 否 |  |  |
| 26 | check_str | 否 |  |  |
| 27 | order_no | 否 |  |  |
| 28 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 29 | ref_due_amount | 否 |  |  |
| 30 | sub_stock_type | 否 |  |  |
| 31 | trustee_seat_no | 否 |  |  |
| 32 | stock_account | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | exchange_type | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | money_type | 否 |  |  |
| 39 | stock_type | 否 |  |  |
| 40 | current_amount | 否 |  |  |
| 41 | uncome_buy_amount | 否 |  |  |
| 42 | uncome_sell_amount | 否 |  |  |
| 43 | frozen_amount | 否 |  |  |
| 44 | unfrozen_amount | 否 |  |  |
| 45 | correct_amount | 否 |  |  |
| 46 | enable_amount | 否 |  |  |
| 47 | real_buy_amount | 否 |  |  |
| 48 | real_buy_balance | 否 |  |  |
| 49 | real_sell_amount | 否 |  |  |
| 50 | real_sell_balance | 否 |  |  |
| 51 | entrust_sell_amount | 否 |  |  |
| 52 | sum_buy_amount | 否 |  |  |
| 53 | sum_buy_balance | 否 |  |  |
| 54 | sum_sell_amount | 否 |  |  |
| 55 | sum_sell_balance | 否 |  |  |
| 56 | cost_price | 否 |  |  |
| 57 | check_str | 否 |  |  |
| 58 | order_no | 否 |  |  |
| 59 | position_str | 否 |  | fund_account(18)+exchange_type(4) +stock_account(20) +stock_ |
| 60 | ref_due_amount | 否 |  |  |
| 61 | sub_stock_type | 否 |  |  |
| 62 | trustee_seat_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ucrt_stock_real_unique | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_uft_ucrt_stock_real_unique | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ucrt_stock_real_unique | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_uft_ucrt_stock_real_unique | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-24 10:00:26 | 3.0.2.2002 | 宋作强 | 新增表结构 |
| 2025-03-24 10:00:26 | 3.0.2.2002 | 宋作强 | 新增表结构 |

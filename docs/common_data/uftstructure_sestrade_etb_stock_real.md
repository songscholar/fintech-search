# etb_stock_real - 互联互通债券交易持仓表

**表对象ID**: 5854
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code_long | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | sub_stock_type | 否 |  |  |
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
| 26 | position_str | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | stock_code_long | 否 |  |  |
| 33 | exchange_type | 否 |  |  |
| 34 | stock_type | 否 |  |  |
| 35 | sub_stock_type | 否 |  |  |
| 36 | current_amount | 否 |  |  |
| 37 | uncome_buy_amount | 否 |  |  |
| 38 | uncome_sell_amount | 否 |  |  |
| 39 | frozen_amount | 否 |  |  |
| 40 | unfrozen_amount | 否 |  |  |
| 41 | correct_amount | 否 |  |  |
| 42 | enable_amount | 否 |  |  |
| 43 | real_buy_amount | 否 |  |  |
| 44 | real_buy_balance | 否 |  |  |
| 45 | real_sell_amount | 否 |  |  |
| 46 | real_sell_balance | 否 |  |  |
| 47 | entrust_sell_amount | 否 |  |  |
| 48 | sum_buy_amount | 否 |  |  |
| 49 | sum_buy_balance | 否 |  |  |
| 50 | sum_sell_amount | 否 |  |  |
| 51 | sum_sell_balance | 否 |  |  |
| 52 | cost_price | 否 |  |  |
| 53 | position_str | 否 |  |  |
| 54 | money_type | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etb_stock_real_pos | ART | 是 | position_str, position_str |
| idx_etb_stock_real | ART | 是 | branch_no, exchange_type, stock_account, stock_code_long, branch_no, exchange_type, stock_account, stock_code_long |
| idx_etb_stock_real_fund | ART | 是 | fund_account, fund_account |
| idx_etb_stock_real_stk | ART | 是 | stock_code_long, exchange_type, stock_code_long, exchange_type |
| idx_etb_stock_real_pos | ART | 是 | position_str, position_str |
| idx_etb_stock_real | ART | 是 | branch_no, exchange_type, stock_account, stock_code_long, branch_no, exchange_type, stock_account, stock_code_long |
| idx_etb_stock_real_fund | ART | 是 | fund_account, fund_account |
| idx_etb_stock_real_stk | ART | 是 | stock_code_long, exchange_type, stock_code_long, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etb_stock_real_pos | position_str, position_str |
| idx_etb_stock_real_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:47:19 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:47:19 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

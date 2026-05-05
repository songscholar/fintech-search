# usms_exit_stock - 退市股份表

**表对象ID**: 2828
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | money_type | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | current_amount | 是 |  |  |
| 10 | uncome_sell_amount | 是 |  |  |
| 11 | uncome_buy_amount | 是 |  |  |
| 12 | frozen_amount | 是 |  |  |
| 13 | unfrozen_amount | 是 |  |  |
| 14 | correct_amount | 是 |  |  |
| 15 | begin_amount | 是 |  |  |
| 16 | sum_buy_amount | 是 |  |  |
| 17 | sum_buy_balance | 是 |  |  |
| 18 | sum_sell_amount | 是 |  |  |
| 19 | sum_sell_balance | 是 |  |  |
| 20 | cost_price | 是 |  |  |
| 21 | check_str | 是 |  |  |
| 22 | position_str | 是 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 23 | client_group | 是 |  |  |
| 24 | stock_code_long | 是 |  |  |
| 25 | room_code | 是 |  |  |
| 26 | asset_prop | 是 |  |  |
| 27 | limit_flag | 是 |  |  |
| 28 | risk_level | 是 |  |  |
| 29 | corp_client_group | 是 |  |  |
| 30 | corp_risk_level | 是 |  |  |
| 31 | asset_level | 是 |  |  |
| 32 | client_name | 是 |  |  |
| 33 | stock_name | 是 |  |  |
| 34 | close_price | 是 |  |  |
| 35 | store_unit | 是 |  |  |
| 36 | price_step | 是 |  |  |
| 37 | branch_no | 是 |  |  |
| 38 | exchange_type | 是 |  |  |
| 39 | stock_account | 是 |  |  |
| 40 | stock_code | 是 |  |  |
| 41 | fund_account | 是 |  |  |
| 42 | client_id | 是 |  |  |
| 43 | money_type | 是 |  |  |
| 44 | stock_type | 是 |  |  |
| 45 | current_amount | 是 |  |  |
| 46 | uncome_sell_amount | 是 |  |  |
| 47 | uncome_buy_amount | 是 |  |  |
| 48 | frozen_amount | 是 |  |  |
| 49 | unfrozen_amount | 是 |  |  |
| 50 | correct_amount | 是 |  |  |
| 51 | begin_amount | 是 |  |  |
| 52 | sum_buy_amount | 是 |  |  |
| 53 | sum_buy_balance | 是 |  |  |
| 54 | sum_sell_amount | 是 |  |  |
| 55 | sum_sell_balance | 是 |  |  |
| 56 | cost_price | 是 |  |  |
| 57 | check_str | 是 |  |  |
| 58 | position_str | 是 |  | branch_no(5) +fund_account(18)+exchange_type(4) +stock_accou |
| 59 | client_group | 是 |  |  |
| 60 | stock_code_long | 是 |  |  |
| 61 | room_code | 是 |  |  |
| 62 | asset_prop | 是 |  |  |
| 63 | limit_flag | 是 |  |  |
| 64 | risk_level | 是 |  |  |
| 65 | corp_client_group | 是 |  |  |
| 66 | corp_risk_level | 是 |  |  |
| 67 | asset_level | 是 |  |  |
| 68 | client_name | 是 |  |  |
| 69 | stock_name | 是 |  |  |
| 70 | close_price | 是 |  |  |
| 71 | store_unit | 是 |  |  |
| 72 | price_step | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_exit_stock | 默认 | 否 |  |
| idx_exit_stock | 默认 | 是 | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |
| idx_exit_stock | 默认 | 否 |  |
| idx_exit_stock | 默认 | 是 | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_exit_stock | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |
| idx_exit_stock | exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-21 17:04:10 | 3.0.6.88 | 常行 | 物理表usms_exit_stock，增加索引字段(索引idx_exit_stock:增加了索引字段：stock_acc... |
| 2025-03-24 10:46:22 | 3.0.2.2002 | 宋作强 | 新增表结构 |
| 2025-07-21 17:04:10 | 3.0.6.88 | 常行 | 物理表usms_exit_stock，增加索引字段(索引idx_exit_stock:增加了索引字段：stock_acc... |
| 2025-03-24 10:46:22 | 3.0.2.2002 | 宋作强 | 新增表结构 |

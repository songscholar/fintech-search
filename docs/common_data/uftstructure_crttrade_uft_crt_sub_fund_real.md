# uft_crt_sub_fund_real - UFT融资融券交易子中心资金表

**表对象ID**: 7574
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | asset_prop | 否 |  |  |
| 6 | system_no | 否 |  |  |
| 7 | current_balance | 否 |  |  |
| 8 | enable_balance | 否 |  |  |
| 9 | cash_balance | 否 |  |  |
| 10 | check_balance | 否 |  |  |
| 11 | frozen_balance | 否 |  |  |
| 12 | unfrozen_balance | 否 |  |  |
| 13 | entrust_buy_balance | 否 |  |  |
| 14 | real_buy_balance | 否 |  |  |
| 15 | real_sell_balance | 否 |  |  |
| 16 | uncome_buy_balance | 否 |  |  |
| 17 | uncome_sell_balance | 否 |  |  |
| 18 | uncome_correct_balance | 否 |  |  |
| 19 | correct_balance | 否 |  |  |
| 20 | foregift_balance | 否 |  |  |
| 21 | mortgage_balance | 否 |  |  |
| 22 | order_no | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | deal_flag | 否 |  |  |
| 25 | client_id | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | asset_prop | 否 |  |  |
| 30 | system_no | 否 |  |  |
| 31 | current_balance | 否 |  |  |
| 32 | enable_balance | 否 |  |  |
| 33 | cash_balance | 否 |  |  |
| 34 | check_balance | 否 |  |  |
| 35 | frozen_balance | 否 |  |  |
| 36 | unfrozen_balance | 否 |  |  |
| 37 | entrust_buy_balance | 否 |  |  |
| 38 | real_buy_balance | 否 |  |  |
| 39 | real_sell_balance | 否 |  |  |
| 40 | uncome_buy_balance | 否 |  |  |
| 41 | uncome_sell_balance | 否 |  |  |
| 42 | uncome_correct_balance | 否 |  |  |
| 43 | correct_balance | 否 |  |  |
| 44 | foregift_balance | 否 |  |  |
| 45 | mortgage_balance | 否 |  |  |
| 46 | order_no | 否 |  |  |
| 47 | position_str | 否 |  |  |
| 48 | deal_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_crt_sub_fund_real | ART | 是 | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_crt_sub_fund_real_pos | ART | 是 | position_str, position_str |
| idx_uft_crt_sub_fund_real | ART | 是 | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_crt_sub_fund_real_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_crt_sub_fund_real | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_crt_sub_fund_real | fund_account, money_type, system_no, fund_account, money_type, system_no |

# uft_crt_fund_real - UFT融资融券交易资金表

**表对象ID**: 7992
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | asset_prop | 否 |  |  |
| 5 | current_balance | 否 |  |  |
| 6 | enable_balance | 否 |  |  |
| 7 | cash_balance | 否 |  |  |
| 8 | check_balance | 否 |  |  |
| 9 | frozen_balance | 否 |  |  |
| 10 | unfrozen_balance | 否 |  |  |
| 11 | entrust_buy_balance | 否 |  |  |
| 12 | real_buy_balance | 否 |  |  |
| 13 | real_sell_balance | 否 |  |  |
| 14 | uncome_buy_balance | 否 |  |  |
| 15 | uncome_sell_balance | 否 |  |  |
| 16 | uncome_correct_balance | 否 |  |  |
| 17 | correct_balance | 否 |  |  |
| 18 | foregift_balance | 否 |  |  |
| 19 | mortgage_balance | 否 |  |  |
| 20 | branch_no | 否 |  |  |
| 21 | order_no | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | asset_prop | 否 |  |  |
| 27 | current_balance | 否 |  |  |
| 28 | enable_balance | 否 |  |  |
| 29 | cash_balance | 否 |  |  |
| 30 | check_balance | 否 |  |  |
| 31 | frozen_balance | 否 |  |  |
| 32 | unfrozen_balance | 否 |  |  |
| 33 | entrust_buy_balance | 否 |  |  |
| 34 | real_buy_balance | 否 |  |  |
| 35 | real_sell_balance | 否 |  |  |
| 36 | uncome_buy_balance | 否 |  |  |
| 37 | uncome_sell_balance | 否 |  |  |
| 38 | uncome_correct_balance | 否 |  |  |
| 39 | correct_balance | 否 |  |  |
| 40 | foregift_balance | 否 |  |  |
| 41 | mortgage_balance | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | order_no | 否 |  |  |
| 44 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ucrt_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_uft_ucrt_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ucrt_fund_real | fund_account, money_type, fund_account, money_type |
| idx_uft_ucrt_fund_real | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-07 10:41:26 | 3.0.6.52 | 卢杰 | 物理表uft_crt_fund_real，添加了表字段(branch_no);
物理表uft_crt_fund_rea... |
| 2025-07-07 10:41:26 | 3.0.6.52 | 卢杰 | 物理表uft_crt_fund_real，添加了表字段(branch_no);
物理表uft_crt_fund_rea... |

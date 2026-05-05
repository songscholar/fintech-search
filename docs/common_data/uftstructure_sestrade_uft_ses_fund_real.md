# uft_ses_fund_real - UFT证券交易资金表

**表对象ID**: 5976
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

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
| 20 | order_no | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | asset_prop | 否 |  |  |
| 26 | current_balance | 否 |  |  |
| 27 | enable_balance | 否 |  |  |
| 28 | cash_balance | 否 |  |  |
| 29 | check_balance | 否 |  |  |
| 30 | frozen_balance | 否 |  |  |
| 31 | unfrozen_balance | 否 |  |  |
| 32 | entrust_buy_balance | 否 |  |  |
| 33 | real_buy_balance | 否 |  |  |
| 34 | real_sell_balance | 否 |  |  |
| 35 | uncome_buy_balance | 否 |  |  |
| 36 | uncome_sell_balance | 否 |  |  |
| 37 | uncome_correct_balance | 否 |  |  |
| 38 | correct_balance | 否 |  |  |
| 39 | foregift_balance | 否 |  |  |
| 40 | mortgage_balance | 否 |  |  |
| 41 | order_no | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+money_type(3) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ses_fundreal | 默认 | 否 |  |
| idx_uft_ses_fundreal_pos | 默认 | 否 |  |
| idx_uft_ses_fundreal | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_uft_ses_fundreal_pos | ART | 是 | position_str, position_str |
| idx_uft_ses_fundreal | 默认 | 否 |  |
| idx_uft_ses_fundreal_pos | 默认 | 否 |  |
| idx_uft_ses_fundreal | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_uft_ses_fundreal_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ses_fundreal | fund_account, money_type, fund_account, money_type |
| idx_uft_ses_fundreal_pos | position_str, position_str |
| idx_uft_ses_fundreal | fund_account, money_type, fund_account, money_type |
| idx_uft_ses_fundreal_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:51:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:29:53 | 3.0.2.104 | taocong45644 | 当前表uft_ses_fund_real，修改了索引idx_uft_ses_fundreal,索引字段修改为：(fund... |
| 2025-03-11 11:06:07 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-09 14:51:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:29:53 | 3.0.2.104 | taocong45644 | 当前表uft_ses_fund_real，修改了索引idx_uft_ses_fundreal,索引字段修改为：(fund... |
| 2025-03-11 11:06:07 | 3.0.2.2001 | 杨新照 | 新增表结构 |

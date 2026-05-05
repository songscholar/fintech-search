# uft_ses_sub_fund_real - UFT证券交易子中心资金表

**表对象ID**: 5975
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

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
| 22 | deal_flag | 否 |  |  |
| 23 | system_no | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | asset_prop | 否 |  |  |
| 28 | current_balance | 否 |  |  |
| 29 | enable_balance | 否 |  |  |
| 30 | cash_balance | 否 |  |  |
| 31 | check_balance | 否 |  |  |
| 32 | frozen_balance | 否 |  |  |
| 33 | unfrozen_balance | 否 |  |  |
| 34 | entrust_buy_balance | 否 |  |  |
| 35 | real_buy_balance | 否 |  |  |
| 36 | real_sell_balance | 否 |  |  |
| 37 | uncome_buy_balance | 否 |  |  |
| 38 | uncome_sell_balance | 否 |  |  |
| 39 | uncome_correct_balance | 否 |  |  |
| 40 | correct_balance | 否 |  |  |
| 41 | foregift_balance | 否 |  |  |
| 42 | mortgage_balance | 否 |  |  |
| 43 | order_no | 否 |  |  |
| 44 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 45 | deal_flag | 否 |  |  |
| 46 | system_no | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ses_subfundreal | 默认 | 否 |  |
| idx_uft_ses_subfundreal_pos | 默认 | 否 |  |
| idx_uft_ses_subfundreal | 默认 | 否 | system_no, system_no |
| idx_uft_ses_subfundreal | ART | 是 | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_ses_subfundreal_pos | ART | 是 | position_str, position_str |
| idx_uft_ses_subfundreal | 默认 | 否 |  |
| idx_uft_ses_subfundreal_pos | 默认 | 否 |  |
| idx_uft_ses_subfundreal | 默认 | 否 | system_no, system_no |
| idx_uft_ses_subfundreal | ART | 是 | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_ses_subfundreal_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ses_subfundreal | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_ses_subfundreal_pos | position_str, position_str |
| idx_uft_ses_subfundreal | fund_account, money_type, system_no, fund_account, money_type, system_no |
| idx_uft_ses_subfundreal_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:50:39 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:37:28 | 3.0.2.104 | taocong45644 | 当前表uft_ses_sub_fund_real，修改了索引idx_uft_ses_subfundreal,索引字段修改... |
| 2025-06-04 14:50:32 | 3.0.6.23 |  | 物理表uft_ses_sub_fund_real，增加索引字段(索引idx_uft_ses_subfundreal:增加... |
| 2025-06-04 14:49:06 | 3.0.6.23 | 杨新照 | 物理表uft_ses_sub_fund_real，添加了表字段(system_no);
 |
| 2025-03-11 11:05:31 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-09 14:50:39 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:37:28 | 3.0.2.104 | taocong45644 | 当前表uft_ses_sub_fund_real，修改了索引idx_uft_ses_subfundreal,索引字段修改... |
| 2025-06-04 14:50:32 | 3.0.6.23 |  | 物理表uft_ses_sub_fund_real，增加索引字段(索引idx_uft_ses_subfundreal:增加... |
| 2025-06-04 14:49:06 | 3.0.6.23 | 杨新照 | 物理表uft_ses_sub_fund_real，添加了表字段(system_no);
 |
| 2025-03-11 11:05:31 | 3.0.2.2001 | 杨新照 | 新增表结构 |

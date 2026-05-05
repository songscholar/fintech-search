# ucrt_fund_real - 融资融券交易资金表

**表对象ID**: 7532
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

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
| 21 | position_str | 否 |  | branch_no(5)+fund_account(18)+money_type(3) |
| 22 | client_group | 否 | H |  |
| 23 | room_code | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | corp_risk_level | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | tohis_date | 否 | H |  |
| 32 | client_id | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | money_type | 否 |  |  |
| 35 | asset_prop | 否 |  |  |
| 36 | current_balance | 否 |  |  |
| 37 | enable_balance | 否 |  |  |
| 38 | cash_balance | 否 |  |  |
| 39 | check_balance | 否 |  |  |
| 40 | frozen_balance | 否 |  |  |
| 41 | unfrozen_balance | 否 |  |  |
| 42 | entrust_buy_balance | 否 |  |  |
| 43 | real_buy_balance | 否 |  |  |
| 44 | real_sell_balance | 否 |  |  |
| 45 | uncome_buy_balance | 否 |  |  |
| 46 | uncome_sell_balance | 否 |  |  |
| 47 | uncome_correct_balance | 否 |  |  |
| 48 | correct_balance | 否 |  |  |
| 49 | foregift_balance | 否 |  |  |
| 50 | mortgage_balance | 否 |  |  |
| 51 | branch_no | 否 |  |  |
| 52 | position_str | 否 |  | branch_no(5)+fund_account(18)+money_type(3) |
| 53 | client_group | 否 | H |  |
| 54 | room_code | 否 | H |  |
| 55 | limit_flag | 否 | H |  |
| 56 | risk_level | 否 | H |  |
| 57 | corp_client_group | 否 | H |  |
| 58 | corp_risk_level | 否 | H |  |
| 59 | asset_level | 否 | H |  |
| 60 | client_name | 否 | H |  |
| 61 | client_prop | 否 | H |  |
| 62 | tohis_date | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_ucrtfundreal | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_ucrtfundreal_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |
| idx_ucrt_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |
| uk_rpt_ucrtfundreal | ART | 是 | tohis_date, branch_no, position_str, tohis_date, branch_no, position_str |
| idx_rpt_ucrtfundreal_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_real | fund_account, money_type, fund_account, money_type |
| idx_ucrt_fund_real | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-23 11:15:43 | 3.0.6.1067 | 徐世晗 | 物理表ucrt_fund_real，添加了表字段(branch_no);
物理表ucrt_fund_real，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:26 | 0.0.0.7 | 程猛 | 删除表字段order_no |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-08-23 11:15:43 | 3.0.6.1067 | 徐世晗 | 物理表ucrt_fund_real，添加了表字段(branch_no);
物理表ucrt_fund_real，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:26 | 0.0.0.7 | 程猛 | 删除表字段order_no |

# uref_fund - 保证金资金表

**表对象ID**: 6051
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | begin_balance | 否 |  |  |
| 7 | current_balance | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | unfrozen_balance | 否 |  |  |
| 10 | entrust_buy_balance | 否 |  |  |
| 11 | real_buy_balance | 否 |  |  |
| 12 | real_sell_balance | 否 |  |  |
| 13 | deposit_balance | 否 |  |  |
| 14 | fetch_balance | 否 |  |  |
| 15 | csfc_use_balance | 否 |  |  |
| 16 | enable_balance | 否 |  |  |
| 17 | correct_balance | 否 |  |  |
| 18 | integral_balance | 否 |  |  |
| 19 | interest | 否 |  |  |
| 20 | integral_update | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | csfc_borrow_accttype | 否 |  |  |
| 23 | tohis_date | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | asset_prop | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | asset_level | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | fund_account | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | company_no | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | money_type | 否 |  |  |
| 39 | begin_balance | 否 |  |  |
| 40 | current_balance | 否 |  |  |
| 41 | frozen_balance | 否 |  |  |
| 42 | unfrozen_balance | 否 |  |  |
| 43 | entrust_buy_balance | 否 |  |  |
| 44 | real_buy_balance | 否 |  |  |
| 45 | real_sell_balance | 否 |  |  |
| 46 | deposit_balance | 否 |  |  |
| 47 | fetch_balance | 否 |  |  |
| 48 | csfc_use_balance | 否 |  |  |
| 49 | enable_balance | 否 |  |  |
| 50 | correct_balance | 否 |  |  |
| 51 | integral_balance | 否 |  |  |
| 52 | interest | 否 |  |  |
| 53 | integral_update | 否 |  |  |
| 54 | position_str | 否 |  |  |
| 55 | csfc_borrow_accttype | 否 |  |  |
| 56 | tohis_date | 否 | H |  |
| 57 | client_group | 否 | H |  |
| 58 | room_code | 否 | H |  |
| 59 | asset_prop | 否 | H |  |
| 60 | client_prop | 否 | H |  |
| 61 | limit_flag | 否 | H |  |
| 62 | client_name | 否 | H |  |
| 63 | corp_client_group | 否 | H |  |
| 64 | asset_level | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reffund | ART | 是 | position_str, position_str |
| idx_reffund_csfc | ART | 是 | company_no, fund_account, money_type, csfc_borrow_accttype, company_no, fund_account, money_type, csfc_borrow_accttype |
| idx_reffund | ART | 是 | position_str, position_str |
| idx_reffund_csfc | ART | 是 | company_no, fund_account, money_type, csfc_borrow_accttype, company_no, fund_account, money_type, csfc_borrow_accttype |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_reffund | position_str, position_str |
| uk_rpt_ureffund | tohis_date, position_str, tohis_date, position_str |
| idx_reffund | position_str, position_str |
| uk_rpt_ureffund | tohis_date, position_str, tohis_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:01:09 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_fund，添加了表字段(corp_client_group);
历史表(... |
| 2025-10-16 10:34:10 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:01:09 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_fund，添加了表字段(corp_client_group);
历史表(... |
| 2025-10-16 10:34:10 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

# uref_stock - 保证金股份表

**表对象ID**: 6053
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | begin_amount | 否 |  |  |
| 10 | current_amount | 否 |  |  |
| 11 | frozen_amount | 否 |  |  |
| 12 | unfrozen_amount | 否 |  |  |
| 13 | entrust_sell_amount | 否 |  |  |
| 14 | real_buy_amount | 否 |  |  |
| 15 | real_sell_amount | 否 |  |  |
| 16 | deposit_amount | 否 |  |  |
| 17 | fetch_amount | 否 |  |  |
| 18 | csfc_use_amount | 否 |  |  |
| 19 | enable_amount | 否 |  |  |
| 20 | correct_amount | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | csfc_borrow_accttype | 否 |  |  |
| 23 | tohis_date | 否 | H |  |
| 24 | stock_name | 否 | H |  |
| 25 | market_value | 否 | H |  |
| 26 | assure_ratio | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | client_name | 否 | H |  |
| 33 | sub_stock_type | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | risk_level | 否 | H |  |
| 37 | corp_risk_level | 否 | H |  |
| 38 | fund_account | 否 |  |  |
| 39 | client_id | 否 |  |  |
| 40 | company_no | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | exchange_type | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | stock_type | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | begin_amount | 否 |  |  |
| 47 | current_amount | 否 |  |  |
| 48 | frozen_amount | 否 |  |  |
| 49 | unfrozen_amount | 否 |  |  |
| 50 | entrust_sell_amount | 否 |  |  |
| 51 | real_buy_amount | 否 |  |  |
| 52 | real_sell_amount | 否 |  |  |
| 53 | deposit_amount | 否 |  |  |
| 54 | fetch_amount | 否 |  |  |
| 55 | csfc_use_amount | 否 |  |  |
| 56 | enable_amount | 否 |  |  |
| 57 | correct_amount | 否 |  |  |
| 58 | position_str | 否 |  |  |
| 59 | csfc_borrow_accttype | 否 |  |  |
| 60 | tohis_date | 否 | H |  |
| 61 | stock_name | 否 | H |  |
| 62 | market_value | 否 | H |  |
| 63 | assure_ratio | 否 | H |  |
| 64 | client_group | 否 | H |  |
| 65 | room_code | 否 | H |  |
| 66 | asset_prop | 否 | H |  |
| 67 | client_prop | 否 | H |  |
| 68 | limit_flag | 否 | H |  |
| 69 | client_name | 否 | H |  |
| 70 | sub_stock_type | 否 | H |  |
| 71 | corp_client_group | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_risk_level | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refstock | ART | 是 | exchange_type, stock_account, stock_code, csfc_borrow_accttype, exchange_type, stock_account, stock_code, csfc_borrow_accttype |
| idx_refstock_id | ART | 是 | client_id, client_id |
| idx_refstock_acct | ART | 是 | fund_account, fund_account |
| idx_refstock_pos | ART | 是 | position_str, position_str |
| idx_refstock | ART | 是 | exchange_type, stock_account, stock_code, csfc_borrow_accttype, exchange_type, stock_account, stock_code, csfc_borrow_accttype |
| idx_refstock_id | ART | 是 | client_id, client_id |
| idx_refstock_acct | ART | 是 | fund_account, fund_account |
| idx_refstock_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_refstock_pos | position_str, position_str |
| uk_rpt_urefstock | tohis_date, position_str, tohis_date, position_str |
| idx_refstock_pos | position_str, position_str |
| uk_rpt_urefstock | tohis_date, position_str, tohis_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:38:42 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_stock，添加了表字段(corp_client_group);
历史表... |
| 2025-10-16 10:34:45 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:38:42 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_stock，添加了表字段(corp_client_group);
历史表... |
| 2025-10-16 10:34:45 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

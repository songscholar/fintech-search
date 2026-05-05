# ucrt_stock_real_total - 融资融券股份汇总表

**表对象ID**: 7561
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | stock_type | 否 |  |  |
| 12 | current_amount | 否 |  |  |
| 13 | enable_amount | 否 |  |  |
| 14 | frozen_amount | 否 |  |  |
| 15 | unfrozen_amount | 否 |  |  |
| 16 | correct_amount | 否 |  |  |
| 17 | uncome_buy_amount | 否 |  |  |
| 18 | uncome_sell_amount | 否 |  |  |
| 19 | sum_buy_amount | 否 |  |  |
| 20 | sum_buy_balance | 否 |  |  |
| 21 | sum_sell_amount | 否 |  |  |
| 22 | sum_sell_balance | 否 |  |  |
| 23 | cost_price | 否 |  |  |
| 24 | seat_no | 否 |  |  |
| 25 | trans_amount | 否 |  |  |
| 26 | sett_batch_no | 否 |  |  |
| 27 | stock_name | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | client_group | 否 | H |  |
| 38 | room_code | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | money_type | 否 |  |  |
| 42 | curr_date | 否 |  |  |
| 43 | curr_time | 否 |  |  |
| 44 | stock_account | 否 |  |  |
| 45 | stock_code | 否 |  |  |
| 46 | branch_no | 否 |  |  |
| 47 | exchange_type | 否 |  |  |
| 48 | client_id | 否 |  |  |
| 49 | stock_type | 否 |  |  |
| 50 | current_amount | 否 |  |  |
| 51 | enable_amount | 否 |  |  |
| 52 | frozen_amount | 否 |  |  |
| 53 | unfrozen_amount | 否 |  |  |
| 54 | correct_amount | 否 |  |  |
| 55 | uncome_buy_amount | 否 |  |  |
| 56 | uncome_sell_amount | 否 |  |  |
| 57 | sum_buy_amount | 否 |  |  |
| 58 | sum_buy_balance | 否 |  |  |
| 59 | sum_sell_amount | 否 |  |  |
| 60 | sum_sell_balance | 否 |  |  |
| 61 | cost_price | 否 |  |  |
| 62 | seat_no | 否 |  |  |
| 63 | trans_amount | 否 |  |  |
| 64 | sett_batch_no | 否 |  |  |
| 65 | stock_name | 否 | H |  |
| 66 | sub_stock_type | 否 | H |  |
| 67 | asset_prop | 否 | H |  |
| 68 | limit_flag | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | corp_risk_level | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | client_name | 否 | H |  |
| 74 | client_prop | 否 | H |  |
| 75 | client_group | 否 | H |  |
| 76 | room_code | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_real_total | ART | 是 | stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no, stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no |
| uk_rpt_ucrtstockrealtotal | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no |
| idx_ucrt_stock_real_total | ART | 是 | stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no, stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no |
| uk_rpt_ucrtstockrealtotal | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtstockrealtotal | stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no, stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no |
| idx_crdtstockrealtotal_acct | fund_account, fund_account |
| idx_crdtstockrealtotal | stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no, stock_account, branch_no, stock_code, exchange_type, fund_account, init_date, sett_batch_no |
| idx_crdtstockrealtotal_acct | fund_account, fund_account |

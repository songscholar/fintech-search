# ucrt_fund_real_total - 融资融券交易资金汇总表

**表对象ID**: 7559
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | current_balance | 否 |  |  |
| 6 | enable_balance | 否 |  |  |
| 7 | frozen_balance | 否 |  |  |
| 8 | unfrozen_balance | 否 |  |  |
| 9 | correct_balance | 否 |  |  |
| 10 | uncome_buy_balance | 否 |  |  |
| 11 | uncome_sell_balance | 否 |  |  |
| 12 | uncome_correct_balance | 否 |  |  |
| 13 | foregift_balance | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |
| 15 | client_id | 否 | H |  |
| 16 | asset_prop | 否 | H |  |
| 17 | limit_flag | 否 | H |  |
| 18 | risk_level | 否 | H |  |
| 19 | corp_client_group | 否 | H |  |
| 20 | corp_risk_level | 否 | H |  |
| 21 | asset_level | 否 | H |  |
| 22 | client_name | 否 | H |  |
| 23 | client_prop | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | money_type | 否 |  |  |
| 30 | current_balance | 否 |  |  |
| 31 | enable_balance | 否 |  |  |
| 32 | frozen_balance | 否 |  |  |
| 33 | unfrozen_balance | 否 |  |  |
| 34 | correct_balance | 否 |  |  |
| 35 | uncome_buy_balance | 否 |  |  |
| 36 | uncome_sell_balance | 否 |  |  |
| 37 | uncome_correct_balance | 否 |  |  |
| 38 | foregift_balance | 否 |  |  |
| 39 | sett_batch_no | 否 |  |  |
| 40 | client_id | 否 | H |  |
| 41 | asset_prop | 否 | H |  |
| 42 | limit_flag | 否 | H |  |
| 43 | risk_level | 否 | H |  |
| 44 | corp_client_group | 否 | H |  |
| 45 | corp_risk_level | 否 | H |  |
| 46 | asset_level | 否 | H |  |
| 47 | client_name | 否 | H |  |
| 48 | client_prop | 否 | H |  |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_real_total | 默认 | 否 |  |
| idx_ucrt_fund_real_total | ART | 是 | fund_account, money_type, init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no |
| uk_rpt_ucrtfundrealtotal | ART | 是 | init_date, client_id, fund_account, money_type, sett_batch_no, init_date, client_id, fund_account, money_type, sett_batch_no |
| idx_ucrt_fund_real_total | 默认 | 否 |  |
| idx_ucrt_fund_real_total | ART | 是 | fund_account, money_type, init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no |
| uk_rpt_ucrtfundrealtotal | ART | 是 | init_date, client_id, fund_account, money_type, sett_batch_no, init_date, client_id, fund_account, money_type, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundrealtotal | fund_account, money_type, init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no |
| idx_fundrealtotal | fund_account, money_type, init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-25 09:31:04 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_real_total，修改了索引idx_ucrt_fund_real_total,索引字段修改... |
| 2025-11-25 09:31:04 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_real_total，修改了索引idx_ucrt_fund_real_total,索引字段修改... |

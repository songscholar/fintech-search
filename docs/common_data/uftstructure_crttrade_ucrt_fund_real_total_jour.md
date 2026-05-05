# ucrt_fund_real_total_jour - 融资融券交易资金汇总流水表

**表对象ID**: 7560
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_time | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | current_balance | 否 |  |  |
| 9 | enable_balance | 否 |  |  |
| 10 | frozen_balance | 否 |  |  |
| 11 | unfrozen_balance | 否 |  |  |
| 12 | correct_balance | 否 |  |  |
| 13 | uncome_buy_balance | 否 |  |  |
| 14 | uncome_sell_balance | 否 |  |  |
| 15 | uncome_correct_balance | 否 |  |  |
| 16 | foregift_balance | 否 |  |  |
| 17 | sett_batch_no | 否 |  |  |
| 18 | client_id | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | risk_level | 否 | H |  |
| 22 | corp_client_group | 否 | H |  |
| 23 | corp_risk_level | 否 | H |  |
| 24 | asset_level | 否 | H |  |
| 25 | client_name | 否 | H |  |
| 26 | client_prop | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | serial_no | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | branch_no | 否 |  |  |
| 33 | curr_date | 否 |  |  |
| 34 | curr_time | 否 |  |  |
| 35 | money_type | 否 |  |  |
| 36 | current_balance | 否 |  |  |
| 37 | enable_balance | 否 |  |  |
| 38 | frozen_balance | 否 |  |  |
| 39 | unfrozen_balance | 否 |  |  |
| 40 | correct_balance | 否 |  |  |
| 41 | uncome_buy_balance | 否 |  |  |
| 42 | uncome_sell_balance | 否 |  |  |
| 43 | uncome_correct_balance | 否 |  |  |
| 44 | foregift_balance | 否 |  |  |
| 45 | sett_batch_no | 否 |  |  |
| 46 | client_id | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | corp_risk_level | 否 | H |  |
| 52 | asset_level | 否 | H |  |
| 53 | client_name | 否 | H |  |
| 54 | client_prop | 否 | H |  |
| 55 | client_group | 否 | H |  |
| 56 | room_code | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_rpt_ucrtfundrealtotaljour | 默认 | 否 |  |
| idx_fundrealtotaljour | 默认 | 否 | fund_account, money_type, serial_no, fund_account, money_type, serial_no |
| idx_ucrt_fund_real_total_jour | ART | 是 | fund_account, money_type, serial_no, fund_account, money_type, serial_no |
| idx_rpt_ucrtfundrealtotaljour | ART | 是 | init_date, client_id, fund_account, money_type, sett_batch_no, serial_no, init_date, client_id, fund_account, money_type, sett_batch_no, serial_no |
| idx_rpt_ucrtfundrealtotaljour | 默认 | 否 |  |
| idx_fundrealtotaljour | 默认 | 否 | fund_account, money_type, serial_no, fund_account, money_type, serial_no |
| idx_ucrt_fund_real_total_jour | ART | 是 | fund_account, money_type, serial_no, fund_account, money_type, serial_no |
| idx_rpt_ucrtfundrealtotaljour | ART | 是 | init_date, client_id, fund_account, money_type, sett_batch_no, serial_no, init_date, client_id, fund_account, money_type, sett_batch_no, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundrealtotaljour | fund_account, money_type, serial_no, fund_account, money_type, serial_no |
| idx_fundrealtotaljour | fund_account, money_type, serial_no, fund_account, money_type, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-12 18:04:18 | 3.0.8.11 | 沈勋 | 历史表(归档表)his_(fil_)ucrt_fund_real_total_jour，修改了索引idx_rpt_ucr... |
| 2026-01-12 18:03:39 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_real_total_jour，修改了索引idx_fundrealtotaljour,索引字段... |
| 2026-01-12 18:04:18 | 3.0.8.11 | 沈勋 | 历史表(归档表)his_(fil_)ucrt_fund_real_total_jour，修改了索引idx_rpt_ucr... |
| 2026-01-12 18:03:39 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_real_total_jour，修改了索引idx_fundrealtotaljour,索引字段... |

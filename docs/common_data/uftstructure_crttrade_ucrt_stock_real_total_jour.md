# ucrt_stock_real_total_jour - 融资融券股份汇总流水表

**表对象ID**: 7562
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 78 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | current_amount | 否 |  |  |
| 14 | enable_amount | 否 |  |  |
| 15 | frozen_amount | 否 |  |  |
| 16 | unfrozen_amount | 否 |  |  |
| 17 | correct_amount | 否 |  |  |
| 18 | uncome_buy_amount | 否 |  |  |
| 19 | uncome_sell_amount | 否 |  |  |
| 20 | sum_buy_amount | 否 |  |  |
| 21 | sum_buy_balance | 否 |  |  |
| 22 | sum_sell_amount | 否 |  |  |
| 23 | sum_sell_balance | 否 |  |  |
| 24 | cost_price | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | seat_no | 否 |  |  |
| 27 | sett_batch_no | 否 |  |  |
| 28 | stock_name | 否 | H |  |
| 29 | sub_stock_type | 否 | H |  |
| 30 | asset_prop | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_client_group | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | client_name | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | init_date | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | curr_date | 否 |  |  |
| 43 | curr_time | 否 |  |  |
| 44 | branch_no | 否 |  |  |
| 45 | client_id | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | exchange_type | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | money_type | 否 |  |  |
| 51 | stock_type | 否 |  |  |
| 52 | current_amount | 否 |  |  |
| 53 | enable_amount | 否 |  |  |
| 54 | frozen_amount | 否 |  |  |
| 55 | unfrozen_amount | 否 |  |  |
| 56 | correct_amount | 否 |  |  |
| 57 | uncome_buy_amount | 否 |  |  |
| 58 | uncome_sell_amount | 否 |  |  |
| 59 | sum_buy_amount | 否 |  |  |
| 60 | sum_buy_balance | 否 |  |  |
| 61 | sum_sell_amount | 否 |  |  |
| 62 | sum_sell_balance | 否 |  |  |
| 63 | cost_price | 否 |  |  |
| 64 | remark | 否 |  |  |
| 65 | seat_no | 否 |  |  |
| 66 | sett_batch_no | 否 |  |  |
| 67 | stock_name | 否 | H |  |
| 68 | sub_stock_type | 否 | H |  |
| 69 | asset_prop | 否 | H |  |
| 70 | limit_flag | 否 | H |  |
| 71 | risk_level | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | corp_risk_level | 否 | H |  |
| 74 | asset_level | 否 | H |  |
| 75 | client_name | 否 | H |  |
| 76 | client_prop | 否 | H |  |
| 77 | client_group | 否 | H |  |
| 78 | room_code | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_rpt_ucrtstockrealtotaljour | 默认 | 否 |  |
| idx_cstockrltojour | 默认 | 否 | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |
| idx_ucrt_stock_real_total_jour | ART | 是 | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |
| idx_rpt_ucrtstockrealtotaljour | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, serial_no, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, serial_no |
| idx_rpt_ucrtstockrealtotaljour | 默认 | 否 |  |
| idx_cstockrltojour | 默认 | 否 | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |
| idx_ucrt_stock_real_total_jour | ART | 是 | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |
| idx_rpt_ucrtstockrealtotaljour | ART | 是 | init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, serial_no, init_date, client_id, fund_account, stock_account, stock_code, exchange_type, sett_batch_no, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cstockrltojour | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |
| idx_cstockrltojour | stock_account, branch_no, stock_code, exchange_type, serial_no, stock_account, branch_no, stock_code, exchange_type, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-12 18:02:45 | 3.0.8.11 | 沈勋 | 历史表(归档表)his_(fil_)ucrt_stock_real_total_jour，修改了索引idx_rpt_uc... |
| 2026-01-12 18:02:06 | 3.0.8.11 | 沈勋 | 当前表ucrt_stock_real_total_jour，修改了索引idx_cstockrltojour,索引字段修改... |
| 2026-01-12 18:02:45 | 3.0.8.11 | 沈勋 | 历史表(归档表)his_(fil_)ucrt_stock_real_total_jour，修改了索引idx_rpt_uc... |
| 2026-01-12 18:02:06 | 3.0.8.11 | 沈勋 | 当前表ucrt_stock_real_total_jour，修改了索引idx_cstockrltojour,索引字段修改... |

# uses_stock_real_total - 证券股份交易信息汇总表

**表对象ID**: 5988
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | trustee_seat_no | 否 |  |  |
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
| 24 | post_enable_amount | 否 |  |  |
| 25 | flow_count | 否 |  |  |
| 26 | init_date | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | curr_date | 否 |  |  |
| 30 | curr_time | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | trustee_seat_no | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | stock_type | 否 |  |  |
| 37 | current_amount | 否 |  |  |
| 38 | enable_amount | 否 |  |  |
| 39 | frozen_amount | 否 |  |  |
| 40 | unfrozen_amount | 否 |  |  |
| 41 | correct_amount | 否 |  |  |
| 42 | uncome_buy_amount | 否 |  |  |
| 43 | uncome_sell_amount | 否 |  |  |
| 44 | sum_buy_amount | 否 |  |  |
| 45 | sum_buy_balance | 否 |  |  |
| 46 | sum_sell_amount | 否 |  |  |
| 47 | sum_sell_balance | 否 |  |  |
| 48 | cost_price | 否 |  |  |
| 49 | post_enable_amount | 否 |  |  |
| 50 | flow_count | 否 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesstockrealtotal_st_acct | ART | 是 | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |
| idx_usesstockrealtotal | 默认 | 否 |  |
| idx_usesstockrealtotal | 默认 | 否 |  |
| idx_usesstockrealtotal | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count |
| idx_usesstockrealtotal_st_acct | ART | 是 | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |
| idx_rpt_usesstockrealtotal | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count |
| idx_usesstockrealtotal_st_acct | ART | 是 | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |
| idx_usesstockrealtotal | 默认 | 否 |  |
| idx_usesstockrealtotal | 默认 | 否 |  |
| idx_usesstockrealtotal | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count |
| idx_usesstockrealtotal_st_acct | ART | 是 | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |
| idx_rpt_usesstockrealtotal | ART | 是 | stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count, stock_account, stock_code, exchange_type, fund_account, trustee_seat_no, init_date, flow_count |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesstockrealtotal | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |
| idx_usesstockrealtotal | stock_account, stock_code, exchange_type, init_date, flow_count, stock_account, stock_code, exchange_type, init_date, flow_count |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:54:10 | V3.0.2.106 | taocong45644 | 当前表uses_stock_real_total，增加索引（ idx_usesstockrealtotal_st_acc... |
| 2025-12-22 09:04:37 | V3.0.8.32 | 洪略 | 修复唯一索引错误的问题 |
| 2025-12-08 13:29:07 | V3.0.8.24 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:49:35 | 3.0.2.104 | taocong45644 | 当前表uses_stock_real_total，修改了索引idx_usesstockrealtotal,索引字段修改为... |
| 2025-11-07 10:20:32 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2026-03-09 14:54:10 | V3.0.2.106 | taocong45644 | 当前表uses_stock_real_total，增加索引（ idx_usesstockrealtotal_st_acc... |
| 2025-12-22 09:04:37 | V3.0.8.32 | 洪略 | 修复唯一索引错误的问题 |
| 2025-12-08 13:29:07 | V3.0.8.24 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:49:35 | 3.0.2.104 | taocong45644 | 当前表uses_stock_real_total，修改了索引idx_usesstockrealtotal,索引字段修改为... |
| 2025-11-07 10:20:32 | V3.0.2.103 | 洪略 | 增加历史表 |

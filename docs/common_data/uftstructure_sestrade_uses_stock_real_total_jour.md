# uses_stock_real_total_jour - 证券股份交易信息汇总流水表

**表对象ID**: 5991
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | curr_time | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | trustee_seat_no | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | client_id | 否 |  |  |
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
| 26 | flow_count | 否 |  |  |
| 27 | init_date | 否 |  |  |
| 28 | serial_no | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | money_type | 否 |  |  |
| 31 | curr_date | 否 |  |  |
| 32 | curr_time | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | trustee_seat_no | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | stock_type | 否 |  |  |
| 39 | current_amount | 否 |  |  |
| 40 | enable_amount | 否 |  |  |
| 41 | frozen_amount | 否 |  |  |
| 42 | unfrozen_amount | 否 |  |  |
| 43 | correct_amount | 否 |  |  |
| 44 | uncome_buy_amount | 否 |  |  |
| 45 | uncome_sell_amount | 否 |  |  |
| 46 | sum_buy_amount | 否 |  |  |
| 47 | sum_buy_balance | 否 |  |  |
| 48 | sum_sell_amount | 否 |  |  |
| 49 | sum_sell_balance | 否 |  |  |
| 50 | cost_price | 否 |  |  |
| 51 | remark | 否 |  |  |
| 52 | flow_count | 否 |  |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesstockrealtotaljour | 默认 | 否 |  |
| idx_usesstockrealtotaljour_acct | 默认 | 否 |  |
| idx_usesstockrealtotaljour | 默认 | 否 |  |
| idx_usesstockrealtotaljour_acct | 默认 | 否 |  |
| idx_usesstockrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_usesstockrealtotaljour_acct | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_rpt_usesstockrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usesstockrealtotaljour_acct | ART | 是 | init_date, stock_account, stock_code, exchange_type, init_date, stock_account, stock_code, exchange_type |
| idx_usesstockrealtotaljour | 默认 | 否 |  |
| idx_usesstockrealtotaljour_acct | 默认 | 否 |  |
| idx_usesstockrealtotaljour | 默认 | 否 |  |
| idx_usesstockrealtotaljour_acct | 默认 | 否 |  |
| idx_usesstockrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_usesstockrealtotaljour_acct | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_rpt_usesstockrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usesstockrealtotaljour_acct | ART | 是 | init_date, stock_account, stock_code, exchange_type, init_date, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesstockrealtotaljour | init_date, serial_no, init_date, serial_no |
| idx_usesstockrealtotaljour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:54:55 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:29:22 | V3.0.8.26 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:51:56 | 3.0.2.104 | taocong45644 | 当前表uses_stock_real_total_jour，修改了索引idx_usesstockrealtotaljou... |
| 2025-11-07 11:06:37 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2026-03-09 14:54:55 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:29:22 | V3.0.8.26 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:51:56 | 3.0.2.104 | taocong45644 | 当前表uses_stock_real_total_jour，修改了索引idx_usesstockrealtotaljou... |
| 2025-11-07 11:06:37 | V3.0.2.103 | 洪略 | 增加历史表 |

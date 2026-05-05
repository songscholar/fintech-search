# uopt_realtime - 期权实时成交表

**表对象ID**: 9610
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | curr_date | 是 |  |  |
| 3 | curr_microtime | 是 |  |  |
| 4 | trace_id | 是 |  |  |
| 5 | serial_no | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | seat_no | 是 |  |  |
| 10 | stock_account | 是 |  |  |
| 11 | option_code | 是 |  |  |
| 12 | optcomb_id | 是 |  |  |
| 13 | stock_code | 是 |  |  |
| 14 | entrust_bs | 是 |  |  |
| 15 | entrust_oc | 是 |  |  |
| 16 | covered_flag | 是 |  |  |
| 17 | entrust_prop | 是 |  |  |
| 18 | entrust_src | 是 |  |  |
| 19 | entrust_no | 是 |  |  |
| 20 | report_no | 是 |  |  |
| 21 | business_amount | 是 |  |  |
| 22 | opt_business_price | 是 |  |  |
| 23 | business_balance | 是 |  |  |
| 24 | opp_account | 是 |  |  |
| 25 | business_id | 是 |  |  |
| 26 | business_microtime | 是 |  |  |
| 27 | real_type | 是 |  |  |
| 28 | real_status | 是 |  |  |
| 29 | cancel_serial_no | 是 |  |  |
| 30 | order_id | 是 |  |  |
| 31 | orig_order_id | 是 |  |  |
| 32 | init_date | 是 |  |  |
| 33 | curr_date | 是 |  |  |
| 34 | curr_microtime | 是 |  |  |
| 35 | trace_id | 是 |  |  |
| 36 | serial_no | 是 |  |  |
| 37 | client_id | 是 |  |  |
| 38 | fund_account | 是 |  |  |
| 39 | exchange_type | 是 |  |  |
| 40 | seat_no | 是 |  |  |
| 41 | stock_account | 是 |  |  |
| 42 | option_code | 是 |  |  |
| 43 | optcomb_id | 是 |  |  |
| 44 | stock_code | 是 |  |  |
| 45 | entrust_bs | 是 |  |  |
| 46 | entrust_oc | 是 |  |  |
| 47 | covered_flag | 是 |  |  |
| 48 | entrust_prop | 是 |  |  |
| 49 | entrust_src | 是 |  |  |
| 50 | entrust_no | 是 |  |  |
| 51 | report_no | 是 |  |  |
| 52 | business_amount | 是 |  |  |
| 53 | opt_business_price | 是 |  |  |
| 54 | business_balance | 是 |  |  |
| 55 | opp_account | 是 |  |  |
| 56 | business_id | 是 |  |  |
| 57 | business_microtime | 是 |  |  |
| 58 | real_type | 是 |  |  |
| 59 | real_status | 是 |  |  |
| 60 | cancel_serial_no | 是 |  |  |
| 61 | order_id | 是 |  |  |
| 62 | orig_order_id | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_realtime | 默认 | 否 | serial_no, serial_no |
| idx_uopt_realtime_global | 默认 | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_uopt_realtime_serial_no | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_uopt_realtime | 默认 | 否 | serial_no, serial_no |
| idx_uopt_realtime_global | 默认 | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_uopt_realtime_serial_no | 默认 | 否 | init_date, serial_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_realtime | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_uopt_realtime | init_date, serial_no, fund_account, init_date, serial_no, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-08-29 15:11:13 | V3.0.3.12 | wuxd | 字段curr_time调整为curr_microtime;business_time调整为business_microt... |
| 2024-08-29 15:11:13 | V3.0.3.12 | wuxd | 字段curr_time调整为curr_microtime;business_time调整为business_microt... |

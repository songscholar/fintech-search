# uopt_entrust_uncome - 期权在途订单表

**表对象ID**: 9623
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | entrust_no | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | batch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | option_type | 否 |  |  |
| 16 | option_code | 否 |  |  |
| 17 | optcomb_id | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | entrust_bs | 否 |  |  |
| 21 | entrust_oc | 否 |  |  |
| 22 | covered_flag | 否 |  |  |
| 23 | entrust_amount | 否 |  |  |
| 24 | opt_entrust_price | 否 |  |  |
| 25 | entrust_type | 否 |  |  |
| 26 | entrust_prop | 否 |  |  |
| 27 | entrust_src | 否 |  |  |
| 28 | report_time | 否 |  |  |
| 29 | join_report_no | 否 |  |  |
| 30 | record_no | 否 |  |  |
| 31 | business_amount | 否 |  |  |
| 32 | withdraw_amount | 否 |  |  |
| 33 | opt_business_price | 否 |  |  |
| 34 | business_balance | 否 |  |  |
| 35 | clear_balance | 否 |  |  |
| 36 | prev_balance | 否 |  |  |
| 37 | error_no | 否 |  |  |
| 38 | entrust_status | 否 |  |  |
| 39 | money_type | 否 |  |  |
| 40 | fare_kind | 否 |  |  |
| 41 | cancel_serial_no | 否 |  |  |
| 42 | order_id | 否 |  |  |
| 43 | orig_order_id | 否 |  |  |
| 44 | init_date | 否 |  |  |
| 45 | curr_date | 否 |  |  |
| 46 | curr_time | 否 |  |  |
| 47 | entrust_no | 否 |  |  |
| 48 | op_branch_no | 否 |  |  |
| 49 | operator_no | 否 |  |  |
| 50 | op_entrust_way | 否 |  |  |
| 51 | op_station | 否 |  |  |
| 52 | batch_no | 否 |  |  |
| 53 | fund_account | 否 |  |  |
| 54 | client_id | 否 |  |  |
| 55 | exchange_type | 否 |  |  |
| 56 | stock_account | 否 |  |  |
| 57 | seat_no | 否 |  |  |
| 58 | option_type | 否 |  |  |
| 59 | option_code | 否 |  |  |
| 60 | optcomb_id | 否 |  |  |
| 61 | stock_code | 否 |  |  |
| 62 | stock_type | 否 |  |  |
| 63 | entrust_bs | 否 |  |  |
| 64 | entrust_oc | 否 |  |  |
| 65 | covered_flag | 否 |  |  |
| 66 | entrust_amount | 否 |  |  |
| 67 | opt_entrust_price | 否 |  |  |
| 68 | entrust_type | 否 |  |  |
| 69 | entrust_prop | 否 |  |  |
| 70 | entrust_src | 否 |  |  |
| 71 | report_time | 否 |  |  |
| 72 | join_report_no | 否 |  |  |
| 73 | record_no | 否 |  |  |
| 74 | business_amount | 否 |  |  |
| 75 | withdraw_amount | 否 |  |  |
| 76 | opt_business_price | 否 |  |  |
| 77 | business_balance | 否 |  |  |
| 78 | clear_balance | 否 |  |  |
| 79 | prev_balance | 否 |  |  |
| 80 | error_no | 否 |  |  |
| 81 | entrust_status | 否 |  |  |
| 82 | money_type | 否 |  |  |
| 83 | fare_kind | 否 |  |  |
| 84 | cancel_serial_no | 否 |  |  |
| 85 | order_id | 否 |  |  |
| 86 | orig_order_id | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_entrust_uncome | 默认 | 否 | init_date, init_date |
| idx_uopt_entrust_uncome | 默认 | 否 | init_date, entrust_no, init_date, entrust_no |
| idx_uopt_entrust_uncome_temp | 默认 | 是 | init_date, entrust_no, fund_account, exchange_type, stock_account, init_date, entrust_no, fund_account, exchange_type, stock_account |
| idx_uopt_entrust_uncome | 默认 | 否 | init_date, init_date |
| idx_uopt_entrust_uncome | 默认 | 否 | init_date, entrust_no, init_date, entrust_no |
| idx_uopt_entrust_uncome_temp | 默认 | 是 | init_date, entrust_no, fund_account, exchange_type, stock_account, init_date, entrust_no, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_entrust_uncome | init_date, entrust_no, fund_account, exchange_type, stock_account, init_date, entrust_no, fund_account, exchange_type, stock_account |
| idx_uopt_entrust_uncome | init_date, entrust_no, fund_account, exchange_type, stock_account, init_date, entrust_no, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 11:38:56 | V3.0.2.3 | 吴笑东 | 物理表uopt_entrust_uncome，增加索引字段(索引idx_uopt_entrust_uncome:增加了索... |
| 2025-08-07 11:38:56 | V3.0.2.3 | 吴笑东 | 物理表uopt_entrust_uncome，增加索引字段(索引idx_uopt_entrust_uncome:增加了索... |

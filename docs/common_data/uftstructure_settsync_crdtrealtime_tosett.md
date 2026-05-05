# crdtrealtime_tosett - 清算实时成交表

**表对象ID**: 3084
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | curr_date | 是 |  |  |
| 3 | curr_time | 是 |  |  |
| 4 | serial_no | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | seat_no | 是 |  |  |
| 10 | stock_account | 是 |  |  |
| 11 | stock_code | 是 |  |  |
| 12 | entrust_bs | 是 |  |  |
| 13 | entrust_prop | 是 |  |  |
| 14 | entrust_no | 是 |  |  |
| 15 | report_no | 是 |  |  |
| 16 | order_id | 是 |  |  |
| 17 | orig_order_id | 是 |  |  |
| 18 | business_amount | 是 |  |  |
| 19 | business_price | 是 |  |  |
| 20 | business_balance | 是 |  |  |
| 21 | opp_account | 是 |  |  |
| 22 | business_no | 是 |  |  |
| 23 | business_id | 是 |  |  |
| 24 | business_time | 是 |  |  |
| 25 | real_type | 是 |  |  |
| 26 | real_status | 是 |  |  |
| 27 | cancel_serialno | 是 |  |  |
| 28 | position_str | 是 |  |  |
| 29 | followdate_flag | 是 |  |  |
| 30 | exch_return_time | 是 |  |  |
| 31 | update_date | 是 |  |  |
| 32 | update_time | 是 |  |  |
| 33 | transaction_no | 是 |  |  |
| 34 | asset_prop | 是 |  |  |
| 35 | init_date | 是 |  |  |
| 36 | curr_date | 是 |  |  |
| 37 | curr_time | 是 |  |  |
| 38 | serial_no | 是 |  |  |
| 39 | branch_no | 是 |  |  |
| 40 | fund_account | 是 |  |  |
| 41 | client_id | 是 |  |  |
| 42 | exchange_type | 是 |  |  |
| 43 | seat_no | 是 |  |  |
| 44 | stock_account | 是 |  |  |
| 45 | stock_code | 是 |  |  |
| 46 | entrust_bs | 是 |  |  |
| 47 | entrust_prop | 是 |  |  |
| 48 | entrust_no | 是 |  |  |
| 49 | report_no | 是 |  |  |
| 50 | order_id | 是 |  |  |
| 51 | orig_order_id | 是 |  |  |
| 52 | business_amount | 是 |  |  |
| 53 | business_price | 是 |  |  |
| 54 | business_balance | 是 |  |  |
| 55 | opp_account | 是 |  |  |
| 56 | business_no | 是 |  |  |
| 57 | business_id | 是 |  |  |
| 58 | business_time | 是 |  |  |
| 59 | real_type | 是 |  |  |
| 60 | real_status | 是 |  |  |
| 61 | cancel_serialno | 是 |  |  |
| 62 | position_str | 是 |  |  |
| 63 | followdate_flag | 是 |  |  |
| 64 | exch_return_time | 是 |  |  |
| 65 | update_date | 是 |  |  |
| 66 | update_time | 是 |  |  |
| 67 | transaction_no | 是 |  |  |
| 68 | asset_prop | 是 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtrealtime | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_crdtrealtime_serialno | 默认 | 是 | order_id, business_no, branch_no, order_id, business_no, branch_no |
| idx_crdtrealtime_fund | 默认 | 是 | fund_account, fund_account |
| idx_crdtrealtime_id | 默认 | 是 | client_id, client_id |
| idx_crdtrealtime_pos | 默认 | 是 | position_str, position_str |
| idx_crdtrealtime_no | 默认 | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_crdtrealtime | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_crdtrealtime_serialno | 默认 | 是 | order_id, business_no, branch_no, order_id, business_no, branch_no |
| idx_crdtrealtime_fund | 默认 | 是 | fund_account, fund_account |
| idx_crdtrealtime_id | 默认 | 是 | client_id, client_id |
| idx_crdtrealtime_pos | 默认 | 是 | position_str, position_str |
| idx_crdtrealtime_no | 默认 | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtrealtime_pos | position_str, position_str |
| idx_crdtrealtime_pos | position_str, position_str |

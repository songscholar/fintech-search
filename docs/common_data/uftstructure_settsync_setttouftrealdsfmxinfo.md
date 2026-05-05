# setttouftrealdsfmxinfo - 清算实时代收代付明细表

**表对象ID**: 3055
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | csdc_order_no | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | square_seat | 是 |  |  |
| 5 | csdc_seat_no | 是 |  |  |
| 6 | seat_no | 是 |  |  |
| 7 | stock_account | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | stock_code2 | 是 |  |  |
| 10 | clear_busi_type | 是 |  |  |
| 11 | order_id | 是 |  |  |
| 12 | other_id | 是 |  |  |
| 13 | csdc_execute_no | 是 |  |  |
| 14 | clear_serial_no | 是 |  |  |
| 15 | net_balance | 是 |  |  |
| 16 | balance_t | 是 |  |  |
| 17 | fare_sx | 是 |  |  |
| 18 | trade_date | 是 |  |  |
| 19 | begin_clear_date | 是 |  |  |
| 20 | csdc_send_date | 是 |  |  |
| 21 | csdc_real_status | 是 |  |  |
| 22 | csdc_by1 | 是 |  |  |
| 23 | csdc_by2 | 是 |  |  |
| 24 | csdc_by3_f | 是 |  |  |
| 25 | branch_no | 是 |  |  |
| 26 | fund_account | 是 |  |  |
| 27 | match_status | 是 |  |  |
| 28 | deal_flag | 是 |  |  |
| 29 | position_str | 是 |  |  |
| 30 | sub_balance | 是 |  |  |
| 31 | curr_time | 是 |  |  |
| 32 | asset_prop | 是 |  |  |
| 33 | set_seat_no | 是 |  |  |
| 34 | file_type | 是 |  |  |
| 35 | file_kind | 是 |  |  |
| 36 | uft_data_change_status | 是 |  |  |
| 37 | settle_mark | 是 |  |  |
| 38 | supply_chk_balance | 是 |  |  |
| 39 | revert_serial_no | 是 |  |  |
| 40 | record_type | 是 |  |  |
| 41 | serial_no | 是 |  |  |
| 42 | init_date | 是 |  |  |
| 43 | csdc_order_no | 是 |  |  |
| 44 | exchange_type | 是 |  |  |
| 45 | square_seat | 是 |  |  |
| 46 | csdc_seat_no | 是 |  |  |
| 47 | seat_no | 是 |  |  |
| 48 | stock_account | 是 |  |  |
| 49 | stock_code | 是 |  |  |
| 50 | stock_code2 | 是 |  |  |
| 51 | clear_busi_type | 是 |  |  |
| 52 | order_id | 是 |  |  |
| 53 | other_id | 是 |  |  |
| 54 | csdc_execute_no | 是 |  |  |
| 55 | clear_serial_no | 是 |  |  |
| 56 | net_balance | 是 |  |  |
| 57 | balance_t | 是 |  |  |
| 58 | fare_sx | 是 |  |  |
| 59 | trade_date | 是 |  |  |
| 60 | begin_clear_date | 是 |  |  |
| 61 | csdc_send_date | 是 |  |  |
| 62 | csdc_real_status | 是 |  |  |
| 63 | csdc_by1 | 是 |  |  |
| 64 | csdc_by2 | 是 |  |  |
| 65 | csdc_by3_f | 是 |  |  |
| 66 | branch_no | 是 |  |  |
| 67 | fund_account | 是 |  |  |
| 68 | match_status | 是 |  |  |
| 69 | deal_flag | 是 |  |  |
| 70 | position_str | 是 |  |  |
| 71 | sub_balance | 是 |  |  |
| 72 | curr_time | 是 |  |  |
| 73 | asset_prop | 是 |  |  |
| 74 | set_seat_no | 是 |  |  |
| 75 | file_type | 是 |  |  |
| 76 | file_kind | 是 |  |  |
| 77 | uft_data_change_status | 是 |  |  |
| 78 | settle_mark | 是 |  |  |
| 79 | supply_chk_balance | 是 |  |  |
| 80 | revert_serial_no | 是 |  |  |
| 81 | record_type | 是 |  |  |
| 82 | serial_no | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settrealdsfmxinfo | 默认 | 是 | position_str, position_str |
| idx_settrealdsfmxinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_settrealdsfmxinfo_fund | 默认 | 是 | fund_account, stock_code, exchange_type, record_type, fund_account, stock_code, exchange_type, record_type |
| idx_settrealdsfmxinfo | 默认 | 是 | position_str, position_str |
| idx_settrealdsfmxinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_settrealdsfmxinfo_fund | 默认 | 是 | fund_account, stock_code, exchange_type, record_type, fund_account, stock_code, exchange_type, record_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settrealdsfmxinfo | position_str, position_str |
| idx_settrealdsfmxinfo | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-05-18 17:07 | 8.26.2.68 | 张军 | 增加表字段supply_chk_balance、revert_serial_no、record_type、serial_... |
| 2024-03-19 17:50 | 8.26.2.62 | 张军 | 增加settle_mark字段 |
| 2022-11-29 14:37 | 8.26.2.48 | 张军 | 新增 |
| 2024-05-18 17:07 | 8.26.2.68 | 张军 | 增加表字段supply_chk_balance、revert_serial_no、record_type、serial_... |
| 2024-03-19 17:50 | 8.26.2.62 | 张军 | 增加settle_mark字段 |
| 2022-11-29 14:37 | 8.26.2.48 | 张军 | 新增 |

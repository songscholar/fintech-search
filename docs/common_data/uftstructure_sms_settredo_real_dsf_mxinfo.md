# settredo_real_dsf_mxinfo - 清算重做实时代收代付明细临时表

**表对象ID**: 2853
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 88 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | position_str | 否 |  |  |
| 2 | supply_chk_balance | 否 |  |  |
| 3 | sett_dml_type | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | init_date | 是 |  |  |
| 6 | csdc_order_no | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | square_seat | 是 |  |  |
| 9 | csdc_seat_no | 是 |  |  |
| 10 | seat_no | 是 |  |  |
| 11 | stock_account | 是 |  |  |
| 12 | stock_code | 是 |  |  |
| 13 | stock_code2 | 是 |  |  |
| 14 | clear_busi_type | 是 |  |  |
| 15 | order_id | 是 |  |  |
| 16 | other_id | 是 |  |  |
| 17 | csdc_execute_no | 是 |  |  |
| 18 | clear_serial_no | 是 |  |  |
| 19 | net_balance | 是 |  |  |
| 20 | balance_t | 是 |  |  |
| 21 | fare_sx | 是 |  |  |
| 22 | trade_date | 是 |  |  |
| 23 | begin_clear_date | 是 |  |  |
| 24 | csdc_send_date | 是 |  |  |
| 25 | csdc_real_status | 是 |  |  |
| 26 | csdc_by1 | 是 |  |  |
| 27 | csdc_by2 | 是 |  |  |
| 28 | csdc_by3_f | 是 |  |  |
| 29 | branch_no | 是 |  |  |
| 30 | fund_account | 是 |  |  |
| 31 | match_status | 是 |  |  |
| 32 | deal_flag | 是 |  |  |
| 33 | sub_balance | 是 |  |  |
| 34 | curr_time | 是 |  |  |
| 35 | asset_prop | 是 |  |  |
| 36 | set_seat_no | 是 |  |  |
| 37 | file_type | 是 |  |  |
| 38 | file_kind | 是 |  |  |
| 39 | settle_mark | 是 |  |  |
| 40 | revert_serial_no | 是 |  |  |
| 41 | record_type | 是 |  |  |
| 42 | serial_no | 是 |  |  |
| 43 | rtgs_settle_way | 是 |  |  |
| 44 | remark | 是 |  |  |
| 45 | position_str | 否 |  |  |
| 46 | supply_chk_balance | 否 |  |  |
| 47 | sett_dml_type | 否 |  |  |
| 48 | sett_batch_no | 否 |  |  |
| 49 | init_date | 是 |  |  |
| 50 | csdc_order_no | 是 |  |  |
| 51 | exchange_type | 是 |  |  |
| 52 | square_seat | 是 |  |  |
| 53 | csdc_seat_no | 是 |  |  |
| 54 | seat_no | 是 |  |  |
| 55 | stock_account | 是 |  |  |
| 56 | stock_code | 是 |  |  |
| 57 | stock_code2 | 是 |  |  |
| 58 | clear_busi_type | 是 |  |  |
| 59 | order_id | 是 |  |  |
| 60 | other_id | 是 |  |  |
| 61 | csdc_execute_no | 是 |  |  |
| 62 | clear_serial_no | 是 |  |  |
| 63 | net_balance | 是 |  |  |
| 64 | balance_t | 是 |  |  |
| 65 | fare_sx | 是 |  |  |
| 66 | trade_date | 是 |  |  |
| 67 | begin_clear_date | 是 |  |  |
| 68 | csdc_send_date | 是 |  |  |
| 69 | csdc_real_status | 是 |  |  |
| 70 | csdc_by1 | 是 |  |  |
| 71 | csdc_by2 | 是 |  |  |
| 72 | csdc_by3_f | 是 |  |  |
| 73 | branch_no | 是 |  |  |
| 74 | fund_account | 是 |  |  |
| 75 | match_status | 是 |  |  |
| 76 | deal_flag | 是 |  |  |
| 77 | sub_balance | 是 |  |  |
| 78 | curr_time | 是 |  |  |
| 79 | asset_prop | 是 |  |  |
| 80 | set_seat_no | 是 |  |  |
| 81 | file_type | 是 |  |  |
| 82 | file_kind | 是 |  |  |
| 83 | settle_mark | 是 |  |  |
| 84 | revert_serial_no | 是 |  |  |
| 85 | record_type | 是 |  |  |
| 86 | serial_no | 是 |  |  |
| 87 | rtgs_settle_way | 是 |  |  |
| 88 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_realdsfmxinfo | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_realdsfmxinfo | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_realdsfmxinfo | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_realdsfmxinfo | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-11 10:56:08 | 8.26.2.92 | 马天宇 | 所有表settredo_real_dsf_mxinfo，添加了表字段(init_date);
所有表settredo_... |
| 2025-08-04 15:54:35 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2025-11-11 10:56:08 | 8.26.2.92 | 马天宇 | 所有表settredo_real_dsf_mxinfo，添加了表字段(init_date);
所有表settredo_... |
| 2025-08-04 15:54:35 | 8.26.2.91 | 马天宇 | 新建表结构 |

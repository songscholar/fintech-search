# etfreal_dsf_hzinfo - ETF实时代收代付汇总表

**表对象ID**: 2839
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | dcom_busi_type | 否 |  |  |
| 4 | clear_serial_no | 否 |  |  |
| 5 | clear_busi_type | 否 |  |  |
| 6 | square_seat_src | 否 |  |  |
| 7 | square_seat_name_src | 否 |  |  |
| 8 | square_seat_dest | 否 |  |  |
| 9 | square_seat_name_dest | 否 |  |  |
| 10 | fare_sx_src | 否 |  |  |
| 11 | fare_sx_dest | 否 |  |  |
| 12 | net_balance | 否 |  |  |
| 13 | checklist_flag | 否 |  |  |
| 14 | deal_flag | 否 |  |  |
| 15 | csdc_send_date | 否 |  |  |
| 16 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@clear_serial_no,16,'0') |
| 17 | curr_date | 否 |  |  |
| 18 | curr_time | 否 |  |  |
| 19 | touch_count | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | dcom_busi_type | 否 |  |  |
| 23 | clear_serial_no | 否 |  |  |
| 24 | clear_busi_type | 否 |  |  |
| 25 | square_seat_src | 否 |  |  |
| 26 | square_seat_name_src | 否 |  |  |
| 27 | square_seat_dest | 否 |  |  |
| 28 | square_seat_name_dest | 否 |  |  |
| 29 | fare_sx_src | 否 |  |  |
| 30 | fare_sx_dest | 否 |  |  |
| 31 | net_balance | 否 |  |  |
| 32 | checklist_flag | 否 |  |  |
| 33 | deal_flag | 否 |  |  |
| 34 | csdc_send_date | 否 |  |  |
| 35 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@clear_serial_no,16,'0') |
| 36 | curr_date | 否 |  |  |
| 37 | curr_time | 否 |  |  |
| 38 | touch_count | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etfrealdsfhzinfo_no | 默认 | 否 | clear_serial_no, clear_serial_no |
| idx_etfrealdsfhzinfo | 默认 | 是 | position_str, position_str |
| idx_etfrealdsfhzinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_rpt_etfrealdsfhzinfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_etfrealdsfhzinfo_no | 默认 | 否 | clear_serial_no, clear_serial_no |
| idx_etfrealdsfhzinfo | 默认 | 是 | position_str, position_str |
| idx_etfrealdsfhzinfo_no | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_rpt_etfrealdsfhzinfo | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_etfrealdsfhzinfo | position_str, position_str |
| idx_etfrealdsfhzinfo_no | clear_serial_no, clear_serial_no |
| idx_etfrealdsfhzinfo | position_str, position_str |
| idx_etfrealdsfhzinfo_no | clear_serial_no, clear_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-06 14:08:27 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-07-21 17:43:29 | 3.0.6.88 | 常行 | 物理表etfreal_dsf_hzinfo，增加索引(idx_etfrealdsfhzinfo_no:[clear_se... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2025-11-06 14:08:27 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-07-21 17:43:29 | 3.0.6.88 | 常行 | 物理表etfreal_dsf_hzinfo，增加索引(idx_etfrealdsfhzinfo_no:[clear_se... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

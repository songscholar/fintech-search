# ucbp_data_swap - 存管外部数据交换表

**表对象ID**: 2307
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | order_id | 否 |  |  |
| 10 | report_date | 否 |  |  |
| 11 | report_time | 否 |  |  |
| 12 | return_date | 否 |  |  |
| 13 | return_time | 否 |  |  |
| 14 | assettrans_status | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | req_content | 否 |  |  |
| 20 | rep_content | 否 |  |  |
| 21 | total_count | 否 |  |  |
| 22 | deal_count | 否 |  |  |
| 23 | business_date | 否 |  |  |
| 24 | deal_flag | 否 |  |  |
| 25 | deal_info | 否 |  |  |
| 26 | date_clear | 否 |  |  |
| 27 | inter_type | 否 |  |  |
| 28 | sub_inter_type | 否 |  |  |
| 29 | record_no | 否 |  |  |
| 30 | enable_polling | 否 |  |  |
| 31 | cancel_serialno | 否 |  |  |
| 32 | holder_kind | 否 |  |  |
| 33 | return_code | 否 |  |  |
| 34 | return_info | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 36 | remark | 否 |  |  |
| 37 | branch_no | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | asset_prop | 否 | H |  |
| 41 | limit_flag | 否 | H |  |
| 42 | risk_level | 否 | H |  |
| 43 | corp_client_group | 否 | H |  |
| 44 | corp_risk_level | 否 | H |  |
| 45 | asset_level | 否 | H |  |
| 46 | client_prop | 否 | H |  |
| 47 | client_name | 否 | H |  |
| 48 | init_date | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | curr_date | 否 |  |  |
| 51 | curr_time | 否 |  |  |
| 52 | op_branch_no | 否 |  |  |
| 53 | operator_no | 否 |  |  |
| 54 | op_station | 否 |  |  |
| 55 | op_entrust_way | 否 |  |  |
| 56 | order_id | 否 |  |  |
| 57 | report_date | 否 |  |  |
| 58 | report_time | 否 |  |  |
| 59 | return_date | 否 |  |  |
| 60 | return_time | 否 |  |  |
| 61 | assettrans_status | 否 |  |  |
| 62 | client_id | 否 |  |  |
| 63 | fund_account | 否 |  |  |
| 64 | stock_account | 否 |  |  |
| 65 | exchange_type | 否 |  |  |
| 66 | req_content | 否 |  |  |
| 67 | rep_content | 否 |  |  |
| 68 | total_count | 否 |  |  |
| 69 | deal_count | 否 |  |  |
| 70 | business_date | 否 |  |  |
| 71 | deal_flag | 否 |  |  |
| 72 | deal_info | 否 |  |  |
| 73 | date_clear | 否 |  |  |
| 74 | inter_type | 否 |  |  |
| 75 | sub_inter_type | 否 |  |  |
| 76 | record_no | 否 |  |  |
| 77 | enable_polling | 否 |  |  |
| 78 | cancel_serialno | 否 |  |  |
| 79 | holder_kind | 否 |  |  |
| 80 | return_code | 否 |  |  |
| 81 | return_info | 否 |  |  |
| 82 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 83 | remark | 否 |  |  |
| 84 | branch_no | 否 | H |  |
| 85 | client_group | 否 | H |  |
| 86 | room_code | 否 | H |  |
| 87 | asset_prop | 否 | H |  |
| 88 | limit_flag | 否 | H |  |
| 89 | risk_level | 否 | H |  |
| 90 | corp_client_group | 否 | H |  |
| 91 | corp_risk_level | 否 | H |  |
| 92 | asset_level | 否 | H |  |
| 93 | client_prop | 否 | H |  |
| 94 | client_name | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_dataswap_report | 默认 | 否 |  |
| idx_ucbp_dataswap_report | 默认 | 否 | order_id, order_id |
| idx_ucbp_dataswap | ART | 是 | fund_account, fund_account |
| idx_ucbp_dataswap_report | ART | 是 | order_id, order_id |
| idx_ucbp_dataswap_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_time, order_id, exchange_type, enable_polling, curr_date, curr_time, order_id |
| idx_ucbp_dataswap_qry | ART | 是 | fund_account, exchange_type, init_date, serial_no, fund_account, exchange_type, init_date, serial_no |
| uk_rpt_ucbpdataswap | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpdataswap_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucbpdataswap_tolast | ART | 是 | date_clear, date_clear |
| idx_ucbp_dataswap_report | 默认 | 否 |  |
| idx_ucbp_dataswap_report | 默认 | 否 | order_id, order_id |
| idx_ucbp_dataswap | ART | 是 | fund_account, fund_account |
| idx_ucbp_dataswap_report | ART | 是 | order_id, order_id |
| idx_ucbp_dataswap_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_time, order_id, exchange_type, enable_polling, curr_date, curr_time, order_id |
| idx_ucbp_dataswap_qry | ART | 是 | fund_account, exchange_type, init_date, serial_no, fund_account, exchange_type, init_date, serial_no |
| uk_rpt_ucbpdataswap | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpdataswap_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucbpdataswap_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_dataswap_report | order_id, order_id |
| idx_ucbp_dataswap_report | order_id, order_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:10:47 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |
| 2025-08-25 16:25:12 | V3.0.2.59 | 刘珊珊 | 物理表ucbp_data_swap，添加了表字段(remark);
 |
| 2025-08-16 17:19:36 | 8.26.2.92 | 周兆军 | 所有表ucbp_data_swap，添加了表字段(position_str);
 |
| 2025-06-17 15:31:37 | V3.0.2.58 | 张云焘 | 物理表ucbp_data_swap，添加了表字段(return_code);
物理表ucbp_data_swap，添加... |
| 2025-01-21 13:20:40 | V3.0.2.52 | 杨涛 | 物理表ucbp_data_swap，添加了表字段(holder_kind);
 |
| 2025-01-03 15:20:15 | 3.0.2.49 | 杨涛 | 内存表ucbp_data_swap，新增cancel_serialno字段 |
| 2024-08-20 14:20:15 | V3.0.2.1006 | 张云焘 | 内存表ucbp_data_swap，新增idx_ucbp_dataswap_qry索引 |
| 2024-05-28 18:46:00 | V3.0.1.9 | 张云焘 | 物理表ucbp_data_swap，添加了表字段(enable_polling);新增索引idx_ucbp_datasw... |
| 2023-10-18 11:20:14 | V3.0.1.8 | yangsf | 物理表ucbp_data_swap，添加了表字段(record_no);
 |
| 2023-09-30 16:14:37 | V3.0.1.5 | huangzh | 物理表ucbp_data_swap，添加了表字段(inter_type);
物理表ucbp_data_swap，添加了... |
| 2023-09-30 10:48:17 | V3.0.1.5 | huangzh | 物理表ucbp_data_swap，增加索引(idx_ucbp_dataswap_report:[order_id]);... |
| 2023-09-07 15:06:35 | V3.0.1.2 | huangzh | 新增表结构 |
| 2026-03-04 15:10:47 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |

> 共 26 条修改记录，仅显示最近15条

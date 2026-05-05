# ucrt_realtime - 融资融券实时成交表

**表对象ID**: 7544
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_microtime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | entrust_prop | 否 |  |  |
| 13 | entrust_no | 否 |  |  |
| 14 | business_amount | 否 |  |  |
| 15 | business_price | 否 |  |  |
| 16 | business_balance | 否 |  |  |
| 17 | opp_account | 否 |  |  |
| 18 | business_no | 否 |  |  |
| 19 | business_microtime | 否 |  |  |
| 20 | real_type | 否 |  |  |
| 21 | real_status | 否 |  |  |
| 22 | cancel_serial_no | 否 |  |  |
| 23 | business_id | 否 |  |  |
| 24 | order_id | 否 |  |  |
| 25 | orig_order_id | 否 |  |  |
| 26 | report_no | 否 |  |  |
| 27 | position_str | 否 |  | init_date(8)+partition_no(2)+curr_microtime(9)+branch_no(5)+ |
| 28 | branch_no | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | stock_name | 否 | H |  |
| 39 | stock_type | 否 | H |  |
| 40 | client_prop | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | curr_microtime | 否 |  |  |
| 45 | serial_no | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | seat_no | 否 |  |  |
| 50 | stock_account | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | entrust_bs | 否 |  |  |
| 53 | entrust_prop | 否 |  |  |
| 54 | entrust_no | 否 |  |  |
| 55 | business_amount | 否 |  |  |
| 56 | business_price | 否 |  |  |
| 57 | business_balance | 否 |  |  |
| 58 | opp_account | 否 |  |  |
| 59 | business_no | 否 |  |  |
| 60 | business_microtime | 否 |  |  |
| 61 | real_type | 否 |  |  |
| 62 | real_status | 否 |  |  |
| 63 | cancel_serial_no | 否 |  |  |
| 64 | business_id | 否 |  |  |
| 65 | order_id | 否 |  |  |
| 66 | orig_order_id | 否 |  |  |
| 67 | report_no | 否 |  |  |
| 68 | position_str | 否 |  | init_date(8)+partition_no(2)+curr_microtime(9)+branch_no(5)+ |
| 69 | branch_no | 否 | H |  |
| 70 | client_group | 否 | H |  |
| 71 | room_code | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | asset_prop | 否 | H |  |
| 74 | risk_level | 否 | H |  |
| 75 | corp_client_group | 否 | H |  |
| 76 | corp_risk_level | 否 | H |  |
| 77 | asset_level | 否 | H |  |
| 78 | client_name | 否 | H |  |
| 79 | stock_name | 否 | H |  |
| 80 | stock_type | 否 | H |  |
| 81 | client_prop | 否 | H |  |
| 82 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_realtime | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_realtime_no | ART | 是 | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |
| uk_rptucrtrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_realtime | ART | 是 | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_realtime_no | ART | 是 | fund_account, entrust_no, init_date, serial_no, fund_account, entrust_no, init_date, serial_no |
| uk_rptucrtrealtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtrealtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_realtime | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| idx_ucrt_realtime | fund_account, init_date, serial_no, fund_account, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-05-27 09:29:38 | 3.0.2.2001 | 宋作强 | 物理表ucrt_realtime，添加了表字段(report_no);
 |
| 2025-03-11 10:13:40 | 3.0.6.38 | 汪杰 | 物理表ucrt_realtime，添加了表字段(report_no);
 |
| 2024-07-23 15:51:25 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-05-27 09:29:38 | 3.0.2.2001 | 宋作强 | 物理表ucrt_realtime，添加了表字段(report_no);
 |
| 2025-03-11 10:13:40 | 3.0.6.38 | 汪杰 | 物理表ucrt_realtime，添加了表字段(report_no);
 |
| 2024-07-23 15:51:25 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# ucrt_stock_real_jour - 融资融券股份交易信息流水表

**表对象ID**: 7539
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | real_action | 否 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | occur_amount | 否 |  |  |
| 13 | post_amount | 否 |  |  |
| 14 | frozen_amount | 否 |  |  |
| 15 | unfrozen_amount | 否 |  |  |
| 16 | correct_amount | 否 |  |  |
| 17 | trustee_seat_no | 否 |  |  |
| 18 | cancel_serial_no | 否 |  |  |
| 19 | join_info | 否 |  |  |
| 20 | op_branch_no | 否 |  |  |
| 21 | operator_no | 否 |  |  |
| 22 | op_station | 否 |  |  |
| 23 | op_entrust_way | 否 |  |  |
| 24 | real_buy_used_amount | 否 |  |  |
| 25 | sett_batch_no | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 28 | remark | 是 |  |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | stock_type | 否 | H |  |
| 39 | stock_name | 否 | H |  |
| 40 | client_prop | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | serial_no | 否 |  |  |
| 44 | curr_date | 否 |  |  |
| 45 | curr_microtime | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | stock_account | 否 |  |  |
| 50 | stock_code | 否 |  |  |
| 51 | real_action | 否 |  |  |
| 52 | business_flag | 否 |  |  |
| 53 | occur_amount | 否 |  |  |
| 54 | post_amount | 否 |  |  |
| 55 | frozen_amount | 否 |  |  |
| 56 | unfrozen_amount | 否 |  |  |
| 57 | correct_amount | 否 |  |  |
| 58 | trustee_seat_no | 否 |  |  |
| 59 | cancel_serial_no | 否 |  |  |
| 60 | join_info | 否 |  |  |
| 61 | op_branch_no | 否 |  |  |
| 62 | operator_no | 否 |  |  |
| 63 | op_station | 否 |  |  |
| 64 | op_entrust_way | 否 |  |  |
| 65 | real_buy_used_amount | 否 |  |  |
| 66 | sett_batch_no | 否 |  |  |
| 67 | branch_no | 否 |  |  |
| 68 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 69 | remark | 是 |  |  |
| 70 | client_group | 否 | H |  |
| 71 | room_code | 否 | H |  |
| 72 | asset_prop | 否 | H |  |
| 73 | limit_flag | 否 | H |  |
| 74 | risk_level | 否 | H |  |
| 75 | corp_client_group | 否 | H |  |
| 76 | corp_risk_level | 否 | H |  |
| 77 | asset_level | 否 | H |  |
| 78 | client_name | 否 | H |  |
| 79 | stock_type | 否 | H |  |
| 80 | stock_name | 否 | H |  |
| 81 | client_prop | 否 | H |  |
| 82 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_real_jour | 默认 | 否 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, init_date, serial_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, init_date, serial_no |
| idx_ucrt_stock_real_jour_no | ART | 是 | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no |
| idx_ucrt_stock_real_jour_cancel | 默认 | 是 | fund_account, cancel_serial_no, fund_account, cancel_serial_no |
| uk_rpt_ucrtstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_stock_real_jour | 默认 | 否 | fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, init_date, serial_no, fund_account, stock_account, exchange_type, stock_code, trustee_seat_no, init_date, serial_no |
| idx_ucrt_stock_real_jour_no | ART | 是 | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no |
| idx_ucrt_stock_real_jour_cancel | 默认 | 是 | fund_account, cancel_serial_no, fund_account, cancel_serial_no |
| uk_rpt_ucrtstockrealjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtstockrealjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_real_jour | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no |
| idx_ucrt_stock_real_jour | fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no, fund_account, exchange_type, stock_account, stock_code, trustee_seat_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 10:44:15 | 3.0.8.19 | 袁文龙 | 当前表ucrt_stock_real_jour，修改了索引idx_ucrt_stock_real_jour,索引字段修改... |
| 2025-12-31 11:08:50 | 3.0.8.11 | 汪杰 | 所有表ucrt_stock_real_jour，添加了表字段(remark);
 |
| 2025-08-21 14:43:49 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_stock_real_jour，添加了表字段(branch_no);
物理表ucrt_stock_re... |
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-18 08:58:47 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_stock_real_jour，添加了表字段(sett_batch_no);
 |
| 2024-08-12 20:28:33 | 3.0.3.7 | 汪杰 | 物理表ucrt_stock_real_jour，添加了表字段(real_buy_used_amount);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-02-28 10:44:15 | 3.0.8.19 | 袁文龙 | 当前表ucrt_stock_real_jour，修改了索引idx_ucrt_stock_real_jour,索引字段修改... |
| 2025-12-31 11:08:50 | 3.0.8.11 | 汪杰 | 所有表ucrt_stock_real_jour，添加了表字段(remark);
 |
| 2025-08-21 14:43:49 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_stock_real_jour，添加了表字段(branch_no);
物理表ucrt_stock_re... |
| 2025-08-27 11:09:52 | 3.0.6.1065 | 周兆军 | 所有表ucrt_fund_detail_jour，添加了表字段(position_str);
 |
| 2025-08-18 08:58:47 | 3.0.2.1 | 曾阳璞 | 所有表ucrt_stock_real_jour，添加了表字段(sett_batch_no);
 |
| 2024-08-12 20:28:33 | 3.0.3.7 | 汪杰 | 物理表ucrt_stock_real_jour，添加了表字段(real_buy_used_amount);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

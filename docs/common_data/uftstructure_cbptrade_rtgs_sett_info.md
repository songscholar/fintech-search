# rtgs_sett_info - RTGS清算信息

**表对象ID**: 2481
**所属模块**: cbptrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 132 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | dcom_busi_type | 否 |  |  |
| 3 | clear_serial_no | 否 |  |  |
| 4 | csdc_execute_no | 否 |  |  |
| 5 | order_id | 否 |  |  |
| 6 | square_seat | 否 |  |  |
| 7 | clear_busi_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | csdc_seat_no | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | business_amount | 否 |  |  |
| 13 | business_price | 否 |  |  |
| 14 | clear_amount | 否 |  |  |
| 15 | clear_price | 否 |  |  |
| 16 | currency_code | 否 |  |  |
| 17 | clear_balance | 否 |  |  |
| 18 | fare1 | 否 |  |  |
| 19 | sipf_fare2 | 否 |  |  |
| 20 | regulatory_fee | 否 |  |  |
| 21 | fare2 | 否 |  |  |
| 22 | clearing_fee | 否 |  |  |
| 23 | net_balance | 否 |  |  |
| 24 | business_date | 否 |  |  |
| 25 | clear_date | 否 |  |  |
| 26 | settle_date | 否 |  |  |
| 27 | old_business_date | 否 |  |  |
| 28 | contract_id | 否 |  |  |
| 29 | deal_way | 否 |  |  |
| 30 | report_flag | 否 |  |  |
| 31 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@dcom_busi_type,4,'0') || lpa |
| 32 | branch_no | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | fund_account | 否 |  |  |
| 35 | return_code | 否 |  |  |
| 36 | return_info | 否 |  |  |
| 37 | settle_mark | 否 |  |  |
| 38 | business_time | 否 |  |  |
| 39 | curr_time | 否 |  |  |
| 40 | curr_date | 否 |  |  |
| 41 | stock_code_long | 否 |  |  |
| 42 | etb_trade_id | 否 |  |  |
| 43 | etb_square_id | 否 |  |  |
| 44 | sipf_fare0 | 否 |  |  |
| 45 | risk_fund | 否 |  |  |
| 46 | first_trans_status | 否 |  |  |
| 47 | first_real_status | 否 |  |  |
| 48 | hundred_accrued_interest | 否 |  |  |
| 49 | square_seat_src | 否 |  |  |
| 50 | square_seat_name_src | 否 |  |  |
| 51 | oppo_stkaccount | 否 |  |  |
| 52 | prop_account_name | 否 |  |  |
| 53 | settle_balance_total_sz | 否 |  |  |
| 54 | settle_apply_flag | 否 |  |  |
| 55 | match_result | 否 |  |  |
| 56 | js_flag | 否 |  |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_client_group | 否 | H |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | asset_prop | 否 | H |  |
| 62 | limit_flag | 否 | H |  |
| 63 | client_prop | 否 | H |  |
| 64 | asset_level | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_risk_level | 否 | H |  |
| 67 | init_date | 否 |  |  |
| 68 | dcom_busi_type | 否 |  |  |
| 69 | clear_serial_no | 否 |  |  |
| 70 | csdc_execute_no | 否 |  |  |
| 71 | order_id | 否 |  |  |
| 72 | square_seat | 否 |  |  |
| 73 | clear_busi_type | 否 |  |  |
| 74 | stock_code | 否 |  |  |
| 75 | csdc_seat_no | 否 |  |  |
| 76 | seat_no | 否 |  |  |
| 77 | stock_account | 否 |  |  |
| 78 | business_amount | 否 |  |  |
| 79 | business_price | 否 |  |  |
| 80 | clear_amount | 否 |  |  |
| 81 | clear_price | 否 |  |  |
| 82 | currency_code | 否 |  |  |
| 83 | clear_balance | 否 |  |  |
| 84 | fare1 | 否 |  |  |
| 85 | sipf_fare2 | 否 |  |  |
| 86 | regulatory_fee | 否 |  |  |
| 87 | fare2 | 否 |  |  |
| 88 | clearing_fee | 否 |  |  |
| 89 | net_balance | 否 |  |  |
| 90 | business_date | 否 |  |  |
| 91 | clear_date | 否 |  |  |
| 92 | settle_date | 否 |  |  |
| 93 | old_business_date | 否 |  |  |
| 94 | contract_id | 否 |  |  |
| 95 | deal_way | 否 |  |  |
| 96 | report_flag | 否 |  |  |
| 97 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@dcom_busi_type,4,'0') || lpa |
| 98 | branch_no | 否 |  |  |
| 99 | client_id | 否 |  |  |
| 100 | fund_account | 否 |  |  |
| 101 | return_code | 否 |  |  |
| 102 | return_info | 否 |  |  |
| 103 | settle_mark | 否 |  |  |
| 104 | business_time | 否 |  |  |
| 105 | curr_time | 否 |  |  |
| 106 | curr_date | 否 |  |  |
| 107 | stock_code_long | 否 |  |  |
| 108 | etb_trade_id | 否 |  |  |
| 109 | etb_square_id | 否 |  |  |
| 110 | sipf_fare0 | 否 |  |  |
| 111 | risk_fund | 否 |  |  |
| 112 | first_trans_status | 否 |  |  |
| 113 | first_real_status | 否 |  |  |
| 114 | hundred_accrued_interest | 否 |  |  |
| 115 | square_seat_src | 否 |  |  |
| 116 | square_seat_name_src | 否 |  |  |
| 117 | oppo_stkaccount | 否 |  |  |
| 118 | prop_account_name | 否 |  |  |
| 119 | settle_balance_total_sz | 否 |  |  |
| 120 | settle_apply_flag | 否 |  |  |
| 121 | match_result | 否 |  |  |
| 122 | js_flag | 否 |  |  |
| 123 | client_name | 否 | H |  |
| 124 | corp_client_group | 否 | H |  |
| 125 | client_group | 否 | H |  |
| 126 | room_code | 否 | H |  |
| 127 | asset_prop | 否 | H |  |
| 128 | limit_flag | 否 | H |  |
| 129 | client_prop | 否 | H |  |
| 130 | asset_level | 否 | H |  |
| 131 | risk_level | 否 | H |  |
| 132 | corp_risk_level | 否 | H |  |

## 索引（共 28 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_rtgssettinfo_positionstr | 默认 | 否 |  |
| idx_rtgssettinfo_dcombusitype | 默认 | 否 |  |
| idx_rtgssettinfo_stockaccount | 默认 | 否 |  |
| idx_rtgssettinfo_stkcode | 默认 | 否 |  |
| idx_rtgssettinfo_reportflag | 默认 | 否 |  |
| idx_rtgssettinfo_acct | 默认 | 否 |  |
| idx_rtgssettinfo_positionstr | ART | 是 | position_str, position_str |
| idx_rtgssettinfo_dcombusitype | ART | 是 | dcom_busi_type, dcom_busi_type |
| idx_rtgssettinfo_stockaccount | ART | 是 | stock_account, stock_account |
| idx_rtgssettinfo_stkcode | ART | 是 | stock_code, stock_code |
| idx_rtgssettinfo_reportflag | ART | 是 | report_flag, report_flag |
| idx_rtgssettinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_rtgssettinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_rtgssettinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rtgssettinfo_positionstr | 默认 | 否 |  |
| idx_rtgssettinfo_dcombusitype | 默认 | 否 |  |
| idx_rtgssettinfo_stockaccount | 默认 | 否 |  |
| idx_rtgssettinfo_stkcode | 默认 | 否 |  |
| idx_rtgssettinfo_reportflag | 默认 | 否 |  |
| idx_rtgssettinfo_acct | 默认 | 否 |  |
| idx_rtgssettinfo_positionstr | ART | 是 | position_str, position_str |
| idx_rtgssettinfo_dcombusitype | ART | 是 | dcom_busi_type, dcom_busi_type |
| idx_rtgssettinfo_stockaccount | ART | 是 | stock_account, stock_account |
| idx_rtgssettinfo_stkcode | ART | 是 | stock_code, stock_code |
| idx_rtgssettinfo_reportflag | ART | 是 | report_flag, report_flag |
| idx_rtgssettinfo_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_rtgssettinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_rtgssettinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_rtgssettinfo_positionstr | position_str, position_str |
| idx_rtgssettinfo_positionstr | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:46:47 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-16 11:00:11 | 3.0.2.75 | 洪略 | 补齐历史表资源 |
| 2025-12-01 13:47:50 | 3.0.2.75 | taocong45644 | 当前表rtgs_sett_info，修改了索引idx_rtgssettinfo_positionstr,索引字段修改为：... |
| 2025-10-20 14:24:02 | V3.0.2.63 | 於达 | 新增字段js_flag |
| 2025-09-04 16:48:46 | V3.0.2.62 | 於达 | 增加MDB |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2026-03-04 15:46:47 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-16 11:00:11 | 3.0.2.75 | 洪略 | 补齐历史表资源 |
| 2025-12-01 13:47:50 | 3.0.2.75 | taocong45644 | 当前表rtgs_sett_info，修改了索引idx_rtgssettinfo_positionstr,索引字段修改为：... |
| 2025-10-20 14:24:02 | V3.0.2.63 | 於达 | 新增字段js_flag |
| 2025-09-04 16:48:46 | V3.0.2.62 | 於达 | 增加MDB |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

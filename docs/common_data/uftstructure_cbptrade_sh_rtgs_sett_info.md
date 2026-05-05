# sh_rtgs_sett_info - 上海RTGS清算信息

**表对象ID**: 2645
**所属模块**: cbptrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 130 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | deal_way | 否 |  |  |
| 2 | busin_kind | 否 |  |  |
| 3 | clear_flag | 否 |  |  |
| 4 | transfer_type | 否 |  |  |
| 5 | settle_no | 否 |  |  |
| 6 | business_id | 否 |  |  |
| 7 | cbp_business_id | 否 |  |  |
| 8 | report_id | 否 |  |  |
| 9 | init_date | 否 |  |  |
| 10 | clear_date | 否 |  |  |
| 11 | settle_date | 否 |  |  |
| 12 | other_date | 否 |  |  |
| 13 | entrust_time | 否 |  |  |
| 14 | business_time | 否 |  |  |
| 15 | seat_no | 否 |  |  |
| 16 | shdc_clear_unit | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | stock_code_a | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | shdc_circulate_type | 否 |  |  |
| 21 | shdc_authority_type | 否 |  |  |
| 22 | shdc_market_year | 否 |  |  |
| 23 | entrust_bs | 否 |  |  |
| 24 | settle_amount | 否 |  |  |
| 25 | business_amount | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | business_price | 否 |  |  |
| 28 | entrust_price2 | 否 |  |  |
| 29 | clear_balance | 否 |  |  |
| 30 | fare1 | 否 |  |  |
| 31 | sipf_fare2 | 否 |  |  |
| 32 | fare2 | 否 |  |  |
| 33 | sipf_fare4 | 否 |  |  |
| 34 | sipf_fare0 | 否 |  |  |
| 35 | csdc_other_balance1 | 否 |  |  |
| 36 | csdc_other_balance2 | 否 |  |  |
| 37 | csdc_other_balance3 | 否 |  |  |
| 38 | business_balance | 否 |  |  |
| 39 | return_code | 否 |  |  |
| 40 | other_info | 否 |  |  |
| 41 | result_info | 否 |  |  |
| 42 | shdc_by | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | branch_no | 否 |  |  |
| 46 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@dcom_busi_type,4,'0') || lpa |
| 47 | report_flag | 否 |  |  |
| 48 | return_info | 否 |  |  |
| 49 | curr_date | 否 |  |  |
| 50 | curr_time | 否 |  |  |
| 51 | settle_mark | 否 |  |  |
| 52 | stock_code_long | 否 |  |  |
| 53 | stock_code_long_a | 否 |  |  |
| 54 | settle_apply_flag | 否 |  |  |
| 55 | match_result | 否 |  |  |
| 56 | js_flag | 否 |  |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_client_group | 否 | H |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | limit_flag | 否 | H |  |
| 62 | client_prop | 否 | H |  |
| 63 | asset_level | 否 | H |  |
| 64 | risk_level | 否 | H |  |
| 65 | corp_risk_level | 否 | H |  |
| 66 | deal_way | 否 |  |  |
| 67 | busin_kind | 否 |  |  |
| 68 | clear_flag | 否 |  |  |
| 69 | transfer_type | 否 |  |  |
| 70 | settle_no | 否 |  |  |
| 71 | business_id | 否 |  |  |
| 72 | cbp_business_id | 否 |  |  |
| 73 | report_id | 否 |  |  |
| 74 | init_date | 否 |  |  |
| 75 | clear_date | 否 |  |  |
| 76 | settle_date | 否 |  |  |
| 77 | other_date | 否 |  |  |
| 78 | entrust_time | 否 |  |  |
| 79 | business_time | 否 |  |  |
| 80 | seat_no | 否 |  |  |
| 81 | shdc_clear_unit | 否 |  |  |
| 82 | stock_account | 否 |  |  |
| 83 | stock_code_a | 否 |  |  |
| 84 | stock_code | 否 |  |  |
| 85 | shdc_circulate_type | 否 |  |  |
| 86 | shdc_authority_type | 否 |  |  |
| 87 | shdc_market_year | 否 |  |  |
| 88 | entrust_bs | 否 |  |  |
| 89 | settle_amount | 否 |  |  |
| 90 | business_amount | 否 |  |  |
| 91 | money_type | 否 |  |  |
| 92 | business_price | 否 |  |  |
| 93 | entrust_price2 | 否 |  |  |
| 94 | clear_balance | 否 |  |  |
| 95 | fare1 | 否 |  |  |
| 96 | sipf_fare2 | 否 |  |  |
| 97 | fare2 | 否 |  |  |
| 98 | sipf_fare4 | 否 |  |  |
| 99 | sipf_fare0 | 否 |  |  |
| 100 | csdc_other_balance1 | 否 |  |  |
| 101 | csdc_other_balance2 | 否 |  |  |
| 102 | csdc_other_balance3 | 否 |  |  |
| 103 | business_balance | 否 |  |  |
| 104 | return_code | 否 |  |  |
| 105 | other_info | 否 |  |  |
| 106 | result_info | 否 |  |  |
| 107 | shdc_by | 否 |  |  |
| 108 | fund_account | 否 |  |  |
| 109 | client_id | 否 |  |  |
| 110 | branch_no | 否 |  |  |
| 111 | position_str | 否 |  | lpad(@init_date,8,'0') || lpad(@dcom_busi_type,4,'0') || lpa |
| 112 | report_flag | 否 |  |  |
| 113 | return_info | 否 |  |  |
| 114 | curr_date | 否 |  |  |
| 115 | curr_time | 否 |  |  |
| 116 | settle_mark | 否 |  |  |
| 117 | stock_code_long | 否 |  |  |
| 118 | stock_code_long_a | 否 |  |  |
| 119 | settle_apply_flag | 否 |  |  |
| 120 | match_result | 否 |  |  |
| 121 | js_flag | 否 |  |  |
| 122 | client_name | 否 | H |  |
| 123 | corp_client_group | 否 | H |  |
| 124 | client_group | 否 | H |  |
| 125 | room_code | 否 | H |  |
| 126 | limit_flag | 否 | H |  |
| 127 | client_prop | 否 | H |  |
| 128 | asset_level | 否 | H |  |
| 129 | risk_level | 否 | H |  |
| 130 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pos | 默认 | 否 |  |
| idx_fundacc | 默认 | 否 |  |
| idx_pos | ART | 是 | position_str, position_str |
| idx_fundacc | ART | 是 | fund_account, fund_account |
| uk_rpt_shrtgssettinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_shrtgssettinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_pos | 默认 | 否 |  |
| idx_fundacc | 默认 | 否 |  |
| idx_pos | ART | 是 | position_str, position_str |
| idx_fundacc | ART | 是 | fund_account, fund_account |
| uk_rpt_shrtgssettinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_shrtgssettinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pos | position_str, position_str |
| idx_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:30:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-16 11:24:50 | 3.0.2.75 | 洪略 | 补齐历史资源 |
| 2025-12-01 13:52:06 | 3.0.2.75 | taocong45644 | 当前表sh_rtgs_sett_info，修改了索引idx_pos,索引字段修改为：(position_str),索引唯... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2026-03-04 16:30:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-16 11:24:50 | 3.0.2.75 | 洪略 | 补齐历史资源 |
| 2025-12-01 13:52:06 | 3.0.2.75 | taocong45644 | 当前表sh_rtgs_sett_info，修改了索引idx_pos,索引字段修改为：(position_str),索引唯... |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

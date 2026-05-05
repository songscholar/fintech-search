# sopt_entrust - 非交易报送委托表

**表对象ID**: 2312
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 166 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | batch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | report_account | 否 |  |  |
| 15 | seat_no | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | stock_type | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | entrust_type | 否 |  |  |
| 21 | entrust_prop | 否 |  |  |
| 22 | entrust_amount | 否 |  |  |
| 23 | entrust_price | 否 |  |  |
| 24 | sopt_tax | 否 |  |  |
| 25 | report_microtime | 否 |  |  |
| 26 | report_no | 否 |  |  |
| 27 | record_no | 否 |  |  |
| 28 | contract_id | 否 |  |  |
| 29 | business_amount | 否 |  |  |
| 30 | withdraw_amount | 否 |  |  |
| 31 | business_price | 否 |  |  |
| 32 | business_balance | 否 |  |  |
| 33 | clear_balance | 否 |  |  |
| 34 | prev_balance | 否 |  |  |
| 35 | report_bs | 否 |  |  |
| 36 | store_unit | 否 |  |  |
| 37 | report_unit | 否 |  |  |
| 38 | error_no | 否 |  |  |
| 39 | entrust_status | 否 |  |  |
| 40 | client_group | 否 |  |  |
| 41 | room_code | 否 |  |  |
| 42 | cancel_serial_no | 否 |  |  |
| 43 | fare_kind | 否 |  |  |
| 44 | position_str | 否 |  | curr_date(8)+branch_no(5)+entrust_no(8) |
| 45 | company_no | 否 |  |  |
| 46 | sopt_report_code | 否 |  |  |
| 47 | return_serial_no | 否 |  |  |
| 48 | return_time | 否 |  |  |
| 49 | return_code | 否 |  |  |
| 50 | return_info | 否 |  |  |
| 51 | stock_account_dest | 否 |  |  |
| 52 | seat_no_dest | 否 |  |  |
| 53 | ext_order_id | 否 |  |  |
| 54 | sub_stock_type | 否 |  |  |
| 55 | secu_organ_no | 否 |  |  |
| 56 | secu_organ_code | 否 |  |  |
| 57 | control_kind | 否 |  |  |
| 58 | total_capital | 否 |  |  |
| 59 | high_quota | 否 |  |  |
| 60 | note | 否 |  |  |
| 61 | threshold_flag | 否 |  |  |
| 62 | shdc_circulate_type | 否 |  |  |
| 63 | shdc_authority_type | 否 |  |  |
| 64 | shdc_market_year | 否 |  |  |
| 65 | szdc_market_prop | 否 |  |  |
| 66 | stock_property | 否 |  |  |
| 67 | join_serial_no | 否 |  |  |
| 68 | stock_code_long | 否 |  |  |
| 69 | clear_serial_no | 否 |  |  |
| 70 | clear_busi_type | 否 |  |  |
| 71 | fare_sx_src | 否 |  |  |
| 72 | fare_sx_dest | 否 |  |  |
| 73 | enable_polling | 否 |  |  |
| 74 | branch_no | 否 |  |  |
| 75 | client_name | 否 | H |  |
| 76 | corp_client_group | 否 | H |  |
| 77 | asset_prop | 否 | H |  |
| 78 | limit_flag | 否 | H |  |
| 79 | client_prop | 否 | H |  |
| 80 | asset_level | 否 | H |  |
| 81 | risk_level | 否 | H |  |
| 82 | corp_risk_level | 否 | H |  |
| 83 | stock_name | 否 | H |  |
| 84 | init_date | 否 |  |  |
| 85 | entrust_no | 否 |  |  |
| 86 | curr_date | 否 |  |  |
| 87 | curr_microtime | 否 |  |  |
| 88 | op_branch_no | 否 |  |  |
| 89 | operator_no | 否 |  |  |
| 90 | op_entrust_way | 否 |  |  |
| 91 | op_station | 否 |  |  |
| 92 | batch_no | 否 |  |  |
| 93 | fund_account | 否 |  |  |
| 94 | client_id | 否 |  |  |
| 95 | exchange_type | 否 |  |  |
| 96 | stock_account | 否 |  |  |
| 97 | report_account | 否 |  |  |
| 98 | seat_no | 否 |  |  |
| 99 | stock_code | 否 |  |  |
| 100 | stock_type | 否 |  |  |
| 101 | money_type | 否 |  |  |
| 102 | entrust_bs | 否 |  |  |
| 103 | entrust_type | 否 |  |  |
| 104 | entrust_prop | 否 |  |  |
| 105 | entrust_amount | 否 |  |  |
| 106 | entrust_price | 否 |  |  |
| 107 | sopt_tax | 否 |  |  |
| 108 | report_microtime | 否 |  |  |
| 109 | report_no | 否 |  |  |
| 110 | record_no | 否 |  |  |
| 111 | contract_id | 否 |  |  |
| 112 | business_amount | 否 |  |  |
| 113 | withdraw_amount | 否 |  |  |
| 114 | business_price | 否 |  |  |
| 115 | business_balance | 否 |  |  |
| 116 | clear_balance | 否 |  |  |
| 117 | prev_balance | 否 |  |  |
| 118 | report_bs | 否 |  |  |
| 119 | store_unit | 否 |  |  |
| 120 | report_unit | 否 |  |  |
| 121 | error_no | 否 |  |  |
| 122 | entrust_status | 否 |  |  |
| 123 | client_group | 否 |  |  |
| 124 | room_code | 否 |  |  |
| 125 | cancel_serial_no | 否 |  |  |
| 126 | fare_kind | 否 |  |  |
| 127 | position_str | 否 |  | curr_date(8)+branch_no(5)+entrust_no(8) |
| 128 | company_no | 否 |  |  |
| 129 | sopt_report_code | 否 |  |  |
| 130 | return_serial_no | 否 |  |  |
| 131 | return_time | 否 |  |  |
| 132 | return_code | 否 |  |  |
| 133 | return_info | 否 |  |  |
| 134 | stock_account_dest | 否 |  |  |
| 135 | seat_no_dest | 否 |  |  |
| 136 | ext_order_id | 否 |  |  |
| 137 | sub_stock_type | 否 |  |  |
| 138 | secu_organ_no | 否 |  |  |
| 139 | secu_organ_code | 否 |  |  |
| 140 | control_kind | 否 |  |  |
| 141 | total_capital | 否 |  |  |
| 142 | high_quota | 否 |  |  |
| 143 | note | 否 |  |  |
| 144 | threshold_flag | 否 |  |  |
| 145 | shdc_circulate_type | 否 |  |  |
| 146 | shdc_authority_type | 否 |  |  |
| 147 | shdc_market_year | 否 |  |  |
| 148 | szdc_market_prop | 否 |  |  |
| 149 | stock_property | 否 |  |  |
| 150 | join_serial_no | 否 |  |  |
| 151 | stock_code_long | 否 |  |  |
| 152 | clear_serial_no | 否 |  |  |
| 153 | clear_busi_type | 否 |  |  |
| 154 | fare_sx_src | 否 |  |  |
| 155 | fare_sx_dest | 否 |  |  |
| 156 | enable_polling | 否 |  |  |
| 157 | branch_no | 否 |  |  |
| 158 | client_name | 否 | H |  |
| 159 | corp_client_group | 否 | H |  |
| 160 | asset_prop | 否 | H |  |
| 161 | limit_flag | 否 | H |  |
| 162 | client_prop | 否 | H |  |
| 163 | asset_level | 否 | H |  |
| 164 | risk_level | 否 | H |  |
| 165 | corp_risk_level | 否 | H |  |
| 166 | stock_name | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sopt_entrust | 默认 | 否 |  |
| idx_sopt_entrust | 默认 | 否 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_sopt_entrust | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_sopt_entrust_rpt | ART | 是 | report_account, report_no, report_account, report_no |
| idx_sopt_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| uk_rpt_soptentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_soptentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_sopt_entrust | 默认 | 否 |  |
| idx_sopt_entrust | 默认 | 否 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_sopt_entrust | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_sopt_entrust_rpt | ART | 是 | report_account, report_no, report_account, report_no |
| idx_sopt_entrust_polling | ART | 是 | exchange_type, enable_polling, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, curr_date, curr_microtime, entrust_no |
| uk_rpt_soptentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_soptentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sopt_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_sopt_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:16:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | V3.0.2.2 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:41:33 | V3.0.2.1008 | 张明月 | 物理表sopt_entrust，添加了表字段(branch_no);
 |
| 2024-08-19 10:21:38 | V3.0.2.1 | 李江霖 | 物理表sopt_entrust，添加了表字段(enable_polling);
 |
| 2024-07-06 11:07:01 | V3.0.1.13 | 张训华 | cancel_serialno字段改成cancel_serial_no字段 |
| 2024-07-02 16:44:32 | V3.0.1.12 | 张训华 | 物理表sopt_entrust，增加索引(idx_sopt_entrust:[entrust_no,init_date,... |
| 2026-03-04 15:16:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | V3.0.2.2 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:41:33 | V3.0.2.1008 | 张明月 | 物理表sopt_entrust，添加了表字段(branch_no);
 |
| 2024-08-19 10:21:38 | V3.0.2.1 | 李江霖 | 物理表sopt_entrust，添加了表字段(enable_polling);
 |
| 2024-07-06 11:07:01 | V3.0.1.13 | 张训华 | cancel_serialno字段改成cancel_serial_no字段 |
| 2024-07-02 16:44:32 | V3.0.1.12 | 张训华 | 物理表sopt_entrust，增加索引(idx_sopt_entrust:[entrust_no,init_date,... |

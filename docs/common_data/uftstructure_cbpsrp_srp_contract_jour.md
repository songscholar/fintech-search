# srp_contract_jour - 股票质押合同流水表

**表对象ID**: 2602
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 240 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | sign_operator_no | 否 |  |  |
| 11 | contract_id | 否 |  |  |
| 12 | join_contract_id | 否 |  |  |
| 13 | papercont_id | 否 |  |  |
| 14 | srp_contract_type | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | stock_account | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | money_type | 否 |  |  |
| 23 | entrust_amount | 否 |  |  |
| 24 | expire_year_rate | 否 |  |  |
| 25 | entrust_balance | 否 |  |  |
| 26 | back_balance | 否 |  |  |
| 27 | date_back | 否 |  |  |
| 28 | real_year_rate | 否 |  |  |
| 29 | real_back_balance | 否 |  |  |
| 30 | real_date_back | 否 |  |  |
| 31 | srp_contract_status | 否 |  |  |
| 32 | date_clear | 否 |  |  |
| 33 | sign_date | 否 |  |  |
| 34 | entrust_date | 否 |  |  |
| 35 | entrust_no | 否 |  |  |
| 36 | remark | 否 |  |  |
| 37 | position_str | 否 |  | secu_init_date(8)+serial_no(10) |
| 38 | cbp_business_id | 否 |  |  |
| 39 | fund_usage | 否 |  |  |
| 40 | assure_price | 否 |  |  |
| 41 | srp_agent_flag | 否 |  |  |
| 42 | funder_no | 否 |  |  |
| 43 | rate_mode | 否 |  |  |
| 44 | bonus_amount | 否 |  |  |
| 45 | bonus_balance | 否 |  |  |
| 46 | back_type | 否 |  |  |
| 47 | prev_status | 否 |  |  |
| 48 | sum_back_amount | 否 |  |  |
| 49 | sum_back_balance | 否 |  |  |
| 50 | stock_property | 否 |  |  |
| 51 | lift_date | 否 |  |  |
| 52 | repaid_balance | 否 |  |  |
| 53 | settle_interest | 否 |  |  |
| 54 | unsettle_interest | 否 |  |  |
| 55 | report_id | 否 |  |  |
| 56 | impawn_id | 否 |  |  |
| 57 | executives_flag | 否 |  |  |
| 58 | limit_transfer_price | 否 |  |  |
| 59 | limit_orig_value | 否 |  |  |
| 60 | assure_ratio | 否 |  |  |
| 61 | margin_focus_ratio | 否 |  |  |
| 62 | margin_alert_ratio | 否 |  |  |
| 63 | margin_treat_ratio | 否 |  |  |
| 64 | integral_balance | 否 |  |  |
| 65 | cancel_serialno | 否 |  |  |
| 66 | integral_update | 否 |  |  |
| 67 | last_interest_date | 否 |  |  |
| 68 | batch_unsettle_interest | 否 |  |  |
| 69 | srp_kind | 否 |  |  |
| 70 | ipo_pre_interest | 否 |  |  |
| 71 | ipo_pre_fare | 否 |  |  |
| 72 | ask_date_back | 否 |  |  |
| 73 | ask_back_balance | 否 |  |  |
| 74 | recoup_rate | 否 |  |  |
| 75 | max_recoup_days | 否 |  |  |
| 76 | recoup_balance | 否 |  |  |
| 77 | fine_rate | 否 |  |  |
| 78 | fine_interest | 否 |  |  |
| 79 | back_principal | 否 |  |  |
| 80 | impawn_busin_type | 否 |  |  |
| 81 | interest_period_type | 否 |  |  |
| 82 | adv_entrust_balance | 否 |  |  |
| 83 | pre_back_flag | 否 |  |  |
| 84 | sum_spb_amount | 否 |  |  |
| 85 | fund_usage_type | 否 |  |  |
| 86 | fine_balance | 否 |  |  |
| 87 | uninterest_balance | 否 |  |  |
| 88 | execv_lock_flag | 否 |  |  |
| 89 | deduct_balance | 否 |  |  |
| 90 | prodterm_change_flag | 否 |  |  |
| 91 | first_date | 否 |  |  |
| 92 | other_assure_value | 否 |  |  |
| 93 | other_assure_desc | 否 |  |  |
| 94 | csfc_holder_type | 否 |  |  |
| 95 | csfc_execv_type | 否 |  |  |
| 96 | csfc_stock_source | 否 |  |  |
| 97 | csfc_other_reduction | 否 |  |  |
| 98 | impawn_asset_type | 否 |  |  |
| 99 | occur_amount | 否 |  |  |
| 100 | occur_impawn_balance | 否 |  |  |
| 101 | occur_balance | 否 |  |  |
| 102 | srp_occur_settle_interest | 否 |  |  |
| 103 | srp_occur_repaid_balance | 否 |  |  |
| 104 | margin_immtreat_ratio | 否 |  |  |
| 105 | unrepaid_fine_balance | 否 |  |  |
| 106 | prev_back_type | 否 |  |  |
| 107 | assure_contract_id | 否 |  |  |
| 108 | srp_special_account | 否 |  |  |
| 109 | client_name | 否 | H |  |
| 110 | corp_client_group | 否 | H |  |
| 111 | client_group | 否 | H |  |
| 112 | room_code | 否 | H |  |
| 113 | asset_prop | 否 | H |  |
| 114 | limit_flag | 否 | H |  |
| 115 | client_prop | 否 | H |  |
| 116 | asset_level | 否 | H |  |
| 117 | risk_level | 否 | H |  |
| 118 | corp_risk_level | 否 | H |  |
| 119 | stock_name | 否 | H |  |
| 120 | sub_stock_type | 否 | H |  |
| 121 | init_date | 否 |  |  |
| 122 | serial_no | 否 |  |  |
| 123 | curr_date | 否 |  |  |
| 124 | curr_time | 否 |  |  |
| 125 | op_branch_no | 否 |  |  |
| 126 | operator_no | 否 |  |  |
| 127 | op_entrust_way | 否 |  |  |
| 128 | op_station | 否 |  |  |
| 129 | business_flag | 否 |  |  |
| 130 | sign_operator_no | 否 |  |  |
| 131 | contract_id | 否 |  |  |
| 132 | join_contract_id | 否 |  |  |
| 133 | papercont_id | 否 |  |  |
| 134 | srp_contract_type | 否 |  |  |
| 135 | branch_no | 否 |  |  |
| 136 | fund_account | 否 |  |  |
| 137 | client_id | 否 |  |  |
| 138 | stock_account | 否 |  |  |
| 139 | exchange_type | 否 |  |  |
| 140 | stock_code | 否 |  |  |
| 141 | stock_type | 否 |  |  |
| 142 | money_type | 否 |  |  |
| 143 | entrust_amount | 否 |  |  |
| 144 | expire_year_rate | 否 |  |  |
| 145 | entrust_balance | 否 |  |  |
| 146 | back_balance | 否 |  |  |
| 147 | date_back | 否 |  |  |
| 148 | real_year_rate | 否 |  |  |
| 149 | real_back_balance | 否 |  |  |
| 150 | real_date_back | 否 |  |  |
| 151 | srp_contract_status | 否 |  |  |
| 152 | date_clear | 否 |  |  |
| 153 | sign_date | 否 |  |  |
| 154 | entrust_date | 否 |  |  |
| 155 | entrust_no | 否 |  |  |
| 156 | remark | 否 |  |  |
| 157 | position_str | 否 |  | secu_init_date(8)+serial_no(10) |
| 158 | cbp_business_id | 否 |  |  |
| 159 | fund_usage | 否 |  |  |
| 160 | assure_price | 否 |  |  |
| 161 | srp_agent_flag | 否 |  |  |
| 162 | funder_no | 否 |  |  |
| 163 | rate_mode | 否 |  |  |
| 164 | bonus_amount | 否 |  |  |
| 165 | bonus_balance | 否 |  |  |
| 166 | back_type | 否 |  |  |
| 167 | prev_status | 否 |  |  |
| 168 | sum_back_amount | 否 |  |  |
| 169 | sum_back_balance | 否 |  |  |
| 170 | stock_property | 否 |  |  |
| 171 | lift_date | 否 |  |  |
| 172 | repaid_balance | 否 |  |  |
| 173 | settle_interest | 否 |  |  |
| 174 | unsettle_interest | 否 |  |  |
| 175 | report_id | 否 |  |  |
| 176 | impawn_id | 否 |  |  |
| 177 | executives_flag | 否 |  |  |
| 178 | limit_transfer_price | 否 |  |  |
| 179 | limit_orig_value | 否 |  |  |
| 180 | assure_ratio | 否 |  |  |
| 181 | margin_focus_ratio | 否 |  |  |
| 182 | margin_alert_ratio | 否 |  |  |
| 183 | margin_treat_ratio | 否 |  |  |
| 184 | integral_balance | 否 |  |  |
| 185 | cancel_serialno | 否 |  |  |
| 186 | integral_update | 否 |  |  |
| 187 | last_interest_date | 否 |  |  |
| 188 | batch_unsettle_interest | 否 |  |  |
| 189 | srp_kind | 否 |  |  |
| 190 | ipo_pre_interest | 否 |  |  |
| 191 | ipo_pre_fare | 否 |  |  |
| 192 | ask_date_back | 否 |  |  |
| 193 | ask_back_balance | 否 |  |  |
| 194 | recoup_rate | 否 |  |  |
| 195 | max_recoup_days | 否 |  |  |
| 196 | recoup_balance | 否 |  |  |
| 197 | fine_rate | 否 |  |  |
| 198 | fine_interest | 否 |  |  |
| 199 | back_principal | 否 |  |  |
| 200 | impawn_busin_type | 否 |  |  |
| 201 | interest_period_type | 否 |  |  |
| 202 | adv_entrust_balance | 否 |  |  |
| 203 | pre_back_flag | 否 |  |  |
| 204 | sum_spb_amount | 否 |  |  |
| 205 | fund_usage_type | 否 |  |  |
| 206 | fine_balance | 否 |  |  |
| 207 | uninterest_balance | 否 |  |  |
| 208 | execv_lock_flag | 否 |  |  |
| 209 | deduct_balance | 否 |  |  |
| 210 | prodterm_change_flag | 否 |  |  |
| 211 | first_date | 否 |  |  |
| 212 | other_assure_value | 否 |  |  |
| 213 | other_assure_desc | 否 |  |  |
| 214 | csfc_holder_type | 否 |  |  |
| 215 | csfc_execv_type | 否 |  |  |
| 216 | csfc_stock_source | 否 |  |  |
| 217 | csfc_other_reduction | 否 |  |  |
| 218 | impawn_asset_type | 否 |  |  |
| 219 | occur_amount | 否 |  |  |
| 220 | occur_impawn_balance | 否 |  |  |
| 221 | occur_balance | 否 |  |  |
| 222 | srp_occur_settle_interest | 否 |  |  |
| 223 | srp_occur_repaid_balance | 否 |  |  |
| 224 | margin_immtreat_ratio | 否 |  |  |
| 225 | unrepaid_fine_balance | 否 |  |  |
| 226 | prev_back_type | 否 |  |  |
| 227 | assure_contract_id | 否 |  |  |
| 228 | srp_special_account | 否 |  |  |
| 229 | client_name | 否 | H |  |
| 230 | corp_client_group | 否 | H |  |
| 231 | client_group | 否 | H |  |
| 232 | room_code | 否 | H |  |
| 233 | asset_prop | 否 | H |  |
| 234 | limit_flag | 否 | H |  |
| 235 | client_prop | 否 | H |  |
| 236 | asset_level | 否 | H |  |
| 237 | risk_level | 否 | H |  |
| 238 | corp_risk_level | 否 | H |  |
| 239 | stock_name | 否 | H |  |
| 240 | sub_stock_type | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpcontractjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpcontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_srpcontractjour_id | ART | 是 | client_id, client_id |
| idx_srpcontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpcontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpcontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_srpcontractjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpcontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_srpcontractjour_id | ART | 是 | client_id, client_id |
| idx_srpcontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpcontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpcontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpcontractjour | serial_no, init_date, serial_no, init_date |
| idx_srpcontractjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:43:44 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:02:19 | 3.0.3.1 | wuxd | 新增uft对象 |
| 2026-03-06 16:43:44 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:02:19 | 3.0.3.1 | wuxd | 新增uft对象 |

# srp_contract - 股票质押合同表

**表对象ID**: 2315
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 216 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | sign_operator_no | 否 |  |  |
| 3 | contract_id | 否 |  |  |
| 4 | join_contract_id | 否 |  |  |
| 5 | papercont_id | 否 |  |  |
| 6 | srp_contract_type | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | entrust_amount | 否 |  |  |
| 16 | expire_year_rate | 否 |  |  |
| 17 | entrust_balance | 否 |  |  |
| 18 | back_balance | 否 |  |  |
| 19 | date_back | 否 |  |  |
| 20 | real_year_rate | 否 |  |  |
| 21 | real_back_balance | 否 |  |  |
| 22 | real_date_back | 否 |  |  |
| 23 | srp_contract_status | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | sign_date | 否 |  |  |
| 26 | entrust_date | 否 |  |  |
| 27 | entrust_no | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 30 | cbp_business_id | 否 |  |  |
| 31 | fund_usage | 否 |  |  |
| 32 | assure_price | 否 |  |  |
| 33 | srp_agent_flag | 否 |  |  |
| 34 | funder_no | 否 |  |  |
| 35 | rate_mode | 否 |  |  |
| 36 | bonus_amount | 否 |  |  |
| 37 | bonus_balance | 否 |  |  |
| 38 | back_type | 否 |  |  |
| 39 | prev_status | 否 |  |  |
| 40 | sum_back_amount | 否 |  |  |
| 41 | sum_back_balance | 否 |  |  |
| 42 | stock_property | 否 |  |  |
| 43 | lift_date | 否 |  |  |
| 44 | repaid_balance | 否 |  |  |
| 45 | settle_interest | 否 |  |  |
| 46 | unsettle_interest | 否 |  |  |
| 47 | report_id | 否 |  |  |
| 48 | impawn_id | 否 |  |  |
| 49 | executives_flag | 否 |  |  |
| 50 | limit_transfer_price | 否 |  |  |
| 51 | limit_orig_value | 否 |  |  |
| 52 | assure_ratio | 否 |  |  |
| 53 | margin_focus_ratio | 否 |  |  |
| 54 | margin_alert_ratio | 否 |  |  |
| 55 | margin_treat_ratio | 否 |  |  |
| 56 | integral_balance | 否 |  |  |
| 57 | integral_update | 否 |  |  |
| 58 | last_interest_date | 否 |  |  |
| 59 | batch_unsettle_interest | 否 |  |  |
| 60 | srp_kind | 否 |  |  |
| 61 | ipo_pre_interest | 否 |  |  |
| 62 | ipo_pre_fare | 否 |  |  |
| 63 | ask_date_back | 否 |  |  |
| 64 | ask_back_balance | 否 |  |  |
| 65 | recoup_rate | 否 |  |  |
| 66 | max_recoup_days | 否 |  |  |
| 67 | recoup_balance | 否 |  |  |
| 68 | fine_rate | 否 |  |  |
| 69 | fine_interest | 否 |  |  |
| 70 | back_principal | 否 |  |  |
| 71 | impawn_busin_type | 否 |  |  |
| 72 | interest_period_type | 否 |  |  |
| 73 | adv_entrust_balance | 否 |  |  |
| 74 | pre_back_flag | 否 |  |  |
| 75 | sum_spb_amount | 否 |  |  |
| 76 | fund_usage_type | 否 |  |  |
| 77 | fine_balance | 否 |  |  |
| 78 | execv_lock_flag | 否 |  |  |
| 79 | deduct_balance | 否 |  |  |
| 80 | prodterm_change_flag | 否 |  |  |
| 81 | first_date | 否 |  |  |
| 82 | other_assure_value | 否 |  |  |
| 83 | other_assure_desc | 否 |  |  |
| 84 | csfc_holder_type | 否 |  |  |
| 85 | csfc_execv_type | 否 |  |  |
| 86 | csfc_stock_source | 否 |  |  |
| 87 | csfc_other_reduction | 否 |  |  |
| 88 | impawn_asset_type | 否 |  |  |
| 89 | op_entrust_way | 否 |  |  |
| 90 | srp_special_account | 否 |  |  |
| 91 | allow_advance_date | 否 |  |  |
| 92 | margin_immtreat_ratio | 否 |  |  |
| 93 | interest_cycle | 否 |  |  |
| 94 | unrepaid_fine_balance | 否 |  |  |
| 95 | prev_back_type | 否 |  |  |
| 96 | assure_contract_id | 否 |  |  |
| 97 | client_name | 否 | H |  |
| 98 | corp_client_group | 否 | H |  |
| 99 | client_group | 否 | H |  |
| 100 | room_code | 否 | H |  |
| 101 | asset_prop | 否 | H |  |
| 102 | limit_flag | 否 | H |  |
| 103 | client_prop | 否 | H |  |
| 104 | asset_level | 否 | H |  |
| 105 | risk_level | 否 | H |  |
| 106 | corp_risk_level | 否 | H |  |
| 107 | stock_name | 否 | H |  |
| 108 | sub_stock_type | 否 | H |  |
| 109 | init_date | 否 |  |  |
| 110 | sign_operator_no | 否 |  |  |
| 111 | contract_id | 否 |  |  |
| 112 | join_contract_id | 否 |  |  |
| 113 | papercont_id | 否 |  |  |
| 114 | srp_contract_type | 否 |  |  |
| 115 | branch_no | 否 |  |  |
| 116 | fund_account | 否 |  |  |
| 117 | client_id | 否 |  |  |
| 118 | stock_account | 否 |  |  |
| 119 | exchange_type | 否 |  |  |
| 120 | stock_code | 否 |  |  |
| 121 | stock_type | 否 |  |  |
| 122 | money_type | 否 |  |  |
| 123 | entrust_amount | 否 |  |  |
| 124 | expire_year_rate | 否 |  |  |
| 125 | entrust_balance | 否 |  |  |
| 126 | back_balance | 否 |  |  |
| 127 | date_back | 否 |  |  |
| 128 | real_year_rate | 否 |  |  |
| 129 | real_back_balance | 否 |  |  |
| 130 | real_date_back | 否 |  |  |
| 131 | srp_contract_status | 否 |  |  |
| 132 | date_clear | 否 |  |  |
| 133 | sign_date | 否 |  |  |
| 134 | entrust_date | 否 |  |  |
| 135 | entrust_no | 否 |  |  |
| 136 | remark | 否 |  |  |
| 137 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 138 | cbp_business_id | 否 |  |  |
| 139 | fund_usage | 否 |  |  |
| 140 | assure_price | 否 |  |  |
| 141 | srp_agent_flag | 否 |  |  |
| 142 | funder_no | 否 |  |  |
| 143 | rate_mode | 否 |  |  |
| 144 | bonus_amount | 否 |  |  |
| 145 | bonus_balance | 否 |  |  |
| 146 | back_type | 否 |  |  |
| 147 | prev_status | 否 |  |  |
| 148 | sum_back_amount | 否 |  |  |
| 149 | sum_back_balance | 否 |  |  |
| 150 | stock_property | 否 |  |  |
| 151 | lift_date | 否 |  |  |
| 152 | repaid_balance | 否 |  |  |
| 153 | settle_interest | 否 |  |  |
| 154 | unsettle_interest | 否 |  |  |
| 155 | report_id | 否 |  |  |
| 156 | impawn_id | 否 |  |  |
| 157 | executives_flag | 否 |  |  |
| 158 | limit_transfer_price | 否 |  |  |
| 159 | limit_orig_value | 否 |  |  |
| 160 | assure_ratio | 否 |  |  |
| 161 | margin_focus_ratio | 否 |  |  |
| 162 | margin_alert_ratio | 否 |  |  |
| 163 | margin_treat_ratio | 否 |  |  |
| 164 | integral_balance | 否 |  |  |
| 165 | integral_update | 否 |  |  |
| 166 | last_interest_date | 否 |  |  |
| 167 | batch_unsettle_interest | 否 |  |  |
| 168 | srp_kind | 否 |  |  |
| 169 | ipo_pre_interest | 否 |  |  |
| 170 | ipo_pre_fare | 否 |  |  |
| 171 | ask_date_back | 否 |  |  |
| 172 | ask_back_balance | 否 |  |  |
| 173 | recoup_rate | 否 |  |  |
| 174 | max_recoup_days | 否 |  |  |
| 175 | recoup_balance | 否 |  |  |
| 176 | fine_rate | 否 |  |  |
| 177 | fine_interest | 否 |  |  |
| 178 | back_principal | 否 |  |  |
| 179 | impawn_busin_type | 否 |  |  |
| 180 | interest_period_type | 否 |  |  |
| 181 | adv_entrust_balance | 否 |  |  |
| 182 | pre_back_flag | 否 |  |  |
| 183 | sum_spb_amount | 否 |  |  |
| 184 | fund_usage_type | 否 |  |  |
| 185 | fine_balance | 否 |  |  |
| 186 | execv_lock_flag | 否 |  |  |
| 187 | deduct_balance | 否 |  |  |
| 188 | prodterm_change_flag | 否 |  |  |
| 189 | first_date | 否 |  |  |
| 190 | other_assure_value | 否 |  |  |
| 191 | other_assure_desc | 否 |  |  |
| 192 | csfc_holder_type | 否 |  |  |
| 193 | csfc_execv_type | 否 |  |  |
| 194 | csfc_stock_source | 否 |  |  |
| 195 | csfc_other_reduction | 否 |  |  |
| 196 | impawn_asset_type | 否 |  |  |
| 197 | op_entrust_way | 否 |  |  |
| 198 | srp_special_account | 否 |  |  |
| 199 | allow_advance_date | 否 |  |  |
| 200 | margin_immtreat_ratio | 否 |  |  |
| 201 | interest_cycle | 否 |  |  |
| 202 | unrepaid_fine_balance | 否 |  |  |
| 203 | prev_back_type | 否 |  |  |
| 204 | assure_contract_id | 否 |  |  |
| 205 | client_name | 否 | H |  |
| 206 | corp_client_group | 否 | H |  |
| 207 | client_group | 否 | H |  |
| 208 | room_code | 否 | H |  |
| 209 | asset_prop | 否 | H |  |
| 210 | limit_flag | 否 | H |  |
| 211 | client_prop | 否 | H |  |
| 212 | asset_level | 否 | H |  |
| 213 | risk_level | 否 | H |  |
| 214 | corp_risk_level | 否 | H |  |
| 215 | stock_name | 否 | H |  |
| 216 | sub_stock_type | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_contract | 默认 | 否 |  |
| idx_srp_contract | ART | 是 | contract_id, contract_id |
| idx_srp_contract_acct | ART | 是 | fund_account, fund_account |
| idx_srp_contract_id | ART | 是 | client_id, client_id |
| idx_srp_contract_pos | ART | 是 | position_str, position_str |
| idx_srp_contract_join | ART | 是 | join_contract_id, join_contract_id |
| uk_rpt_srpcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpcontract_tolast | ART | 是 | date_clear, date_clear |
| idx_srp_contract | 默认 | 否 |  |
| idx_srp_contract | ART | 是 | contract_id, contract_id |
| idx_srp_contract_acct | ART | 是 | fund_account, fund_account |
| idx_srp_contract_id | ART | 是 | client_id, client_id |
| idx_srp_contract_pos | ART | 是 | position_str, position_str |
| idx_srp_contract_join | ART | 是 | join_contract_id, join_contract_id |
| uk_rpt_srpcontract | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpcontract_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpcontract_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_contract | contract_id, contract_id |
| idx_srp_contract | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:18:08 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-06-27 22:26:58 | V3.0.1.11 | 董乾坤 | 新增 |
| 2026-03-04 15:18:08 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-06-27 22:26:58 | V3.0.1.11 | 董乾坤 | 新增 |

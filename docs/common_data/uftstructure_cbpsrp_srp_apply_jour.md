# srp_apply_jour - 股票质押申请流水表

**表对象ID**: 2607
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 208 个）

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
| 10 | contract_id | 否 |  |  |
| 11 | join_contract_id | 否 |  |  |
| 12 | papercont_id | 否 |  |  |
| 13 | srp_contract_type | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | entrust_amount | 否 |  |  |
| 23 | expire_year_rate | 否 |  |  |
| 24 | entrust_balance | 否 |  |  |
| 25 | back_balance | 否 |  |  |
| 26 | date_back | 否 |  |  |
| 27 | sign_date | 否 |  |  |
| 28 | sign_operator_no | 否 |  |  |
| 29 | entrust_date | 否 |  |  |
| 30 | entrust_no | 否 |  |  |
| 31 | date_clear | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 34 | fund_usage | 否 |  |  |
| 35 | audit_remark | 否 |  |  |
| 36 | assure_price | 否 |  |  |
| 37 | srp_agent_flag | 否 |  |  |
| 38 | funder_no | 否 |  |  |
| 39 | srp_apply_type | 否 |  |  |
| 40 | srp_apply_status | 否 |  |  |
| 41 | rate_mode | 否 |  |  |
| 42 | prev_status | 否 |  |  |
| 43 | stock_property | 否 |  |  |
| 44 | lift_date | 否 |  |  |
| 45 | report_id | 否 |  |  |
| 46 | bonus_balance | 否 |  |  |
| 47 | executives_flag | 否 |  |  |
| 48 | limit_transfer_price | 否 |  |  |
| 49 | limit_orig_value | 否 |  |  |
| 50 | assure_ratio | 否 |  |  |
| 51 | margin_focus_ratio | 否 |  |  |
| 52 | margin_alert_ratio | 否 |  |  |
| 53 | margin_treat_ratio | 否 |  |  |
| 54 | cancel_serialno | 否 |  |  |
| 55 | back_principal | 否 |  |  |
| 56 | fund_usage_type | 否 |  |  |
| 57 | execv_lock_flag | 否 |  |  |
| 58 | interest_period_type | 否 |  |  |
| 59 | srp_unimpawn_type | 否 |  |  |
| 60 | srpcontract_mod_mode | 否 |  |  |
| 61 | srp_kind | 否 |  |  |
| 62 | csfc_holder_type | 否 |  |  |
| 63 | csfc_execv_type | 否 |  |  |
| 64 | csfc_stock_source | 否 |  |  |
| 65 | csfc_other_reduction | 否 |  |  |
| 66 | orig_date_back | 否 |  |  |
| 67 | orig_year_rate | 否 |  |  |
| 68 | orig_back_balance | 否 |  |  |
| 69 | agreed_audit_date | 否 |  |  |
| 70 | srp_special_account | 否 |  |  |
| 71 | allow_advance_date | 否 |  |  |
| 72 | recoup_rate | 否 |  |  |
| 73 | recoup_balance | 否 |  |  |
| 74 | margin_immtreat_ratio | 否 |  |  |
| 75 | interest_cycle | 否 |  |  |
| 76 | original_date | 否 |  |  |
| 77 | original_serial_no | 否 |  |  |
| 78 | fine_rate | 否 |  |  |
| 79 | con_contract_id | 否 |  |  |
| 80 | orig_allow_advance_date | 否 |  |  |
| 81 | orig_recoup_rate | 否 |  |  |
| 82 | orig_recoup_balance | 否 |  |  |
| 83 | spb_repaid_order | 否 |  |  |
| 84 | srp_conmod_sync_type | 否 |  |  |
| 85 | assure_contract_id | 否 |  |  |
| 86 | orig_papercont_id | 否 |  |  |
| 87 | rate_mode_orgin | 否 |  |  |
| 88 | margin_focus_ratio_orgin | 否 |  |  |
| 89 | margin_alert_ratio_orgin | 否 |  |  |
| 90 | margin_treat_ratio_orgin | 否 |  |  |
| 91 | margin_immtreat_ratio_orgin | 否 |  |  |
| 92 | join_serial_no | 否 |  |  |
| 93 | client_name | 否 | H |  |
| 94 | corp_client_group | 否 | H |  |
| 95 | client_group | 否 | H |  |
| 96 | room_code | 否 | H |  |
| 97 | asset_prop | 否 | H |  |
| 98 | limit_flag | 否 | H |  |
| 99 | client_prop | 否 | H |  |
| 100 | asset_level | 否 | H |  |
| 101 | risk_level | 否 | H |  |
| 102 | corp_risk_level | 否 | H |  |
| 103 | stock_name | 否 | H |  |
| 104 | sub_stock_type | 否 | H |  |
| 105 | init_date | 否 |  |  |
| 106 | serial_no | 否 |  |  |
| 107 | curr_date | 否 |  |  |
| 108 | curr_time | 否 |  |  |
| 109 | op_branch_no | 否 |  |  |
| 110 | operator_no | 否 |  |  |
| 111 | op_entrust_way | 否 |  |  |
| 112 | op_station | 否 |  |  |
| 113 | business_flag | 否 |  |  |
| 114 | contract_id | 否 |  |  |
| 115 | join_contract_id | 否 |  |  |
| 116 | papercont_id | 否 |  |  |
| 117 | srp_contract_type | 否 |  |  |
| 118 | branch_no | 否 |  |  |
| 119 | fund_account | 否 |  |  |
| 120 | client_id | 否 |  |  |
| 121 | stock_account | 否 |  |  |
| 122 | exchange_type | 否 |  |  |
| 123 | stock_code | 否 |  |  |
| 124 | stock_type | 否 |  |  |
| 125 | money_type | 否 |  |  |
| 126 | entrust_amount | 否 |  |  |
| 127 | expire_year_rate | 否 |  |  |
| 128 | entrust_balance | 否 |  |  |
| 129 | back_balance | 否 |  |  |
| 130 | date_back | 否 |  |  |
| 131 | sign_date | 否 |  |  |
| 132 | sign_operator_no | 否 |  |  |
| 133 | entrust_date | 否 |  |  |
| 134 | entrust_no | 否 |  |  |
| 135 | date_clear | 否 |  |  |
| 136 | remark | 否 |  |  |
| 137 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 138 | fund_usage | 否 |  |  |
| 139 | audit_remark | 否 |  |  |
| 140 | assure_price | 否 |  |  |
| 141 | srp_agent_flag | 否 |  |  |
| 142 | funder_no | 否 |  |  |
| 143 | srp_apply_type | 否 |  |  |
| 144 | srp_apply_status | 否 |  |  |
| 145 | rate_mode | 否 |  |  |
| 146 | prev_status | 否 |  |  |
| 147 | stock_property | 否 |  |  |
| 148 | lift_date | 否 |  |  |
| 149 | report_id | 否 |  |  |
| 150 | bonus_balance | 否 |  |  |
| 151 | executives_flag | 否 |  |  |
| 152 | limit_transfer_price | 否 |  |  |
| 153 | limit_orig_value | 否 |  |  |
| 154 | assure_ratio | 否 |  |  |
| 155 | margin_focus_ratio | 否 |  |  |
| 156 | margin_alert_ratio | 否 |  |  |
| 157 | margin_treat_ratio | 否 |  |  |
| 158 | cancel_serialno | 否 |  |  |
| 159 | back_principal | 否 |  |  |
| 160 | fund_usage_type | 否 |  |  |
| 161 | execv_lock_flag | 否 |  |  |
| 162 | interest_period_type | 否 |  |  |
| 163 | srp_unimpawn_type | 否 |  |  |
| 164 | srpcontract_mod_mode | 否 |  |  |
| 165 | srp_kind | 否 |  |  |
| 166 | csfc_holder_type | 否 |  |  |
| 167 | csfc_execv_type | 否 |  |  |
| 168 | csfc_stock_source | 否 |  |  |
| 169 | csfc_other_reduction | 否 |  |  |
| 170 | orig_date_back | 否 |  |  |
| 171 | orig_year_rate | 否 |  |  |
| 172 | orig_back_balance | 否 |  |  |
| 173 | agreed_audit_date | 否 |  |  |
| 174 | srp_special_account | 否 |  |  |
| 175 | allow_advance_date | 否 |  |  |
| 176 | recoup_rate | 否 |  |  |
| 177 | recoup_balance | 否 |  |  |
| 178 | margin_immtreat_ratio | 否 |  |  |
| 179 | interest_cycle | 否 |  |  |
| 180 | original_date | 否 |  |  |
| 181 | original_serial_no | 否 |  |  |
| 182 | fine_rate | 否 |  |  |
| 183 | con_contract_id | 否 |  |  |
| 184 | orig_allow_advance_date | 否 |  |  |
| 185 | orig_recoup_rate | 否 |  |  |
| 186 | orig_recoup_balance | 否 |  |  |
| 187 | spb_repaid_order | 否 |  |  |
| 188 | srp_conmod_sync_type | 否 |  |  |
| 189 | assure_contract_id | 否 |  |  |
| 190 | orig_papercont_id | 否 |  |  |
| 191 | rate_mode_orgin | 否 |  |  |
| 192 | margin_focus_ratio_orgin | 否 |  |  |
| 193 | margin_alert_ratio_orgin | 否 |  |  |
| 194 | margin_treat_ratio_orgin | 否 |  |  |
| 195 | margin_immtreat_ratio_orgin | 否 |  |  |
| 196 | join_serial_no | 否 |  |  |
| 197 | client_name | 否 | H |  |
| 198 | corp_client_group | 否 | H |  |
| 199 | client_group | 否 | H |  |
| 200 | room_code | 否 | H |  |
| 201 | asset_prop | 否 | H |  |
| 202 | limit_flag | 否 | H |  |
| 203 | client_prop | 否 | H |  |
| 204 | asset_level | 否 | H |  |
| 205 | risk_level | 否 | H |  |
| 206 | corp_risk_level | 否 | H |  |
| 207 | stock_name | 否 | H |  |
| 208 | sub_stock_type | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpapplyjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_srpapplyjour_id | ART | 是 | client_id, client_id |
| idx_srpapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_srpapplyjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_srpapplyjour_id | ART | 是 | client_id, client_id |
| idx_srpapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpapplyjour | serial_no, init_date, serial_no, init_date |
| idx_srpapplyjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:46:30 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:30 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:46:30 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:30 | 3.0.3.1 | wuxd | 新增 |

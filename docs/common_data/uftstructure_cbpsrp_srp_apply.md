# srp_apply - 股票质押申请表

**表对象ID**: 2606
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 228 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
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
| 20 | sign_date | 否 |  |  |
| 21 | sign_operator_no | 否 |  |  |
| 22 | entrust_date | 否 |  |  |
| 23 | entrust_no | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 27 | fund_usage | 否 |  |  |
| 28 | audit_remark | 否 |  |  |
| 29 | assure_price | 否 |  |  |
| 30 | srp_agent_flag | 否 |  |  |
| 31 | funder_no | 否 |  |  |
| 32 | srp_apply_type | 否 |  |  |
| 33 | srp_apply_status | 否 |  |  |
| 34 | rate_mode | 否 |  |  |
| 35 | prev_status | 否 |  |  |
| 36 | stock_property | 否 |  |  |
| 37 | lift_date | 否 |  |  |
| 38 | report_id | 否 |  |  |
| 39 | bonus_balance | 否 |  |  |
| 40 | executives_flag | 否 |  |  |
| 41 | limit_transfer_price | 否 |  |  |
| 42 | limit_orig_value | 否 |  |  |
| 43 | assure_ratio | 否 |  |  |
| 44 | margin_focus_ratio | 否 |  |  |
| 45 | margin_alert_ratio | 否 |  |  |
| 46 | margin_treat_ratio | 否 |  |  |
| 47 | back_principal | 否 |  |  |
| 48 | fund_usage_type | 否 |  |  |
| 49 | execv_lock_flag | 否 |  |  |
| 50 | interest_period_type | 否 |  |  |
| 51 | srp_unimpawn_type | 否 |  |  |
| 52 | srpcontract_mod_mode | 否 |  |  |
| 53 | srp_kind | 否 |  |  |
| 54 | csfc_holder_type | 否 |  |  |
| 55 | csfc_execv_type | 否 |  |  |
| 56 | csfc_stock_source | 否 |  |  |
| 57 | csfc_other_reduction | 否 |  |  |
| 58 | op_entrust_way | 否 |  |  |
| 59 | orig_date_back | 否 |  |  |
| 60 | orig_year_rate | 否 |  |  |
| 61 | orig_back_balance | 否 |  |  |
| 62 | agreed_audit_date | 否 |  |  |
| 63 | srp_special_account | 否 |  |  |
| 64 | allow_advance_date | 否 |  |  |
| 65 | recoup_rate | 否 |  |  |
| 66 | recoup_balance | 否 |  |  |
| 67 | margin_immtreat_ratio | 否 |  |  |
| 68 | interest_cycle | 否 |  |  |
| 69 | last_interest_date | 否 |  |  |
| 70 | unrepaid_fine_balance | 否 |  |  |
| 71 | report_date_back | 否 |  |  |
| 72 | claimassure_days | 否 |  |  |
| 73 | margin_assurescale_ratio | 否 |  |  |
| 74 | relation_info | 否 |  |  |
| 75 | occur_balance | 否 |  |  |
| 76 | occur_interest | 否 |  |  |
| 77 | occur_fine | 否 |  |  |
| 78 | occur_recoup | 否 |  |  |
| 79 | occur_amount | 否 |  |  |
| 80 | busin_chan_info | 否 |  |  |
| 81 | busin_chan_desc | 否 |  |  |
| 82 | margin_num | 否 |  |  |
| 83 | srp_chan_balance | 否 |  |  |
| 84 | srp_chan_interest | 否 |  |  |
| 85 | srp_chan_fine | 否 |  |  |
| 86 | srp_chan_recoup | 否 |  |  |
| 87 | seat_no | 否 |  |  |
| 88 | fine_rate | 否 |  |  |
| 89 | con_contract_id | 否 |  |  |
| 90 | orig_allow_advance_date | 否 |  |  |
| 91 | orig_recoup_rate | 否 |  |  |
| 92 | orig_recoup_balance | 否 |  |  |
| 93 | spb_repaid_order | 否 |  |  |
| 94 | srp_conmod_sync_type | 否 |  |  |
| 95 | assure_contract_id | 否 |  |  |
| 96 | orig_papercont_id | 否 |  |  |
| 97 | rate_mode_orgin | 否 |  |  |
| 98 | margin_focus_ratio_orgin | 否 |  |  |
| 99 | margin_alert_ratio_orgin | 否 |  |  |
| 100 | margin_treat_ratio_orgin | 否 |  |  |
| 101 | margin_immtreat_ratio_orgin | 否 |  |  |
| 102 | join_serial_no | 否 |  |  |
| 103 | client_name | 否 | H |  |
| 104 | corp_client_group | 否 | H |  |
| 105 | client_group | 否 | H |  |
| 106 | room_code | 否 | H |  |
| 107 | asset_prop | 否 | H |  |
| 108 | limit_flag | 否 | H |  |
| 109 | client_prop | 否 | H |  |
| 110 | asset_level | 否 | H |  |
| 111 | risk_level | 否 | H |  |
| 112 | corp_risk_level | 否 | H |  |
| 113 | stock_name | 否 | H |  |
| 114 | sub_stock_type | 否 | H |  |
| 115 | init_date | 否 |  |  |
| 116 | serial_no | 否 |  |  |
| 117 | contract_id | 否 |  |  |
| 118 | join_contract_id | 否 |  |  |
| 119 | papercont_id | 否 |  |  |
| 120 | srp_contract_type | 否 |  |  |
| 121 | branch_no | 否 |  |  |
| 122 | fund_account | 否 |  |  |
| 123 | client_id | 否 |  |  |
| 124 | stock_account | 否 |  |  |
| 125 | exchange_type | 否 |  |  |
| 126 | stock_code | 否 |  |  |
| 127 | stock_type | 否 |  |  |
| 128 | money_type | 否 |  |  |
| 129 | entrust_amount | 否 |  |  |
| 130 | expire_year_rate | 否 |  |  |
| 131 | entrust_balance | 否 |  |  |
| 132 | back_balance | 否 |  |  |
| 133 | date_back | 否 |  |  |
| 134 | sign_date | 否 |  |  |
| 135 | sign_operator_no | 否 |  |  |
| 136 | entrust_date | 否 |  |  |
| 137 | entrust_no | 否 |  |  |
| 138 | date_clear | 否 |  |  |
| 139 | remark | 否 |  |  |
| 140 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 141 | fund_usage | 否 |  |  |
| 142 | audit_remark | 否 |  |  |
| 143 | assure_price | 否 |  |  |
| 144 | srp_agent_flag | 否 |  |  |
| 145 | funder_no | 否 |  |  |
| 146 | srp_apply_type | 否 |  |  |
| 147 | srp_apply_status | 否 |  |  |
| 148 | rate_mode | 否 |  |  |
| 149 | prev_status | 否 |  |  |
| 150 | stock_property | 否 |  |  |
| 151 | lift_date | 否 |  |  |
| 152 | report_id | 否 |  |  |
| 153 | bonus_balance | 否 |  |  |
| 154 | executives_flag | 否 |  |  |
| 155 | limit_transfer_price | 否 |  |  |
| 156 | limit_orig_value | 否 |  |  |
| 157 | assure_ratio | 否 |  |  |
| 158 | margin_focus_ratio | 否 |  |  |
| 159 | margin_alert_ratio | 否 |  |  |
| 160 | margin_treat_ratio | 否 |  |  |
| 161 | back_principal | 否 |  |  |
| 162 | fund_usage_type | 否 |  |  |
| 163 | execv_lock_flag | 否 |  |  |
| 164 | interest_period_type | 否 |  |  |
| 165 | srp_unimpawn_type | 否 |  |  |
| 166 | srpcontract_mod_mode | 否 |  |  |
| 167 | srp_kind | 否 |  |  |
| 168 | csfc_holder_type | 否 |  |  |
| 169 | csfc_execv_type | 否 |  |  |
| 170 | csfc_stock_source | 否 |  |  |
| 171 | csfc_other_reduction | 否 |  |  |
| 172 | op_entrust_way | 否 |  |  |
| 173 | orig_date_back | 否 |  |  |
| 174 | orig_year_rate | 否 |  |  |
| 175 | orig_back_balance | 否 |  |  |
| 176 | agreed_audit_date | 否 |  |  |
| 177 | srp_special_account | 否 |  |  |
| 178 | allow_advance_date | 否 |  |  |
| 179 | recoup_rate | 否 |  |  |
| 180 | recoup_balance | 否 |  |  |
| 181 | margin_immtreat_ratio | 否 |  |  |
| 182 | interest_cycle | 否 |  |  |
| 183 | last_interest_date | 否 |  |  |
| 184 | unrepaid_fine_balance | 否 |  |  |
| 185 | report_date_back | 否 |  |  |
| 186 | claimassure_days | 否 |  |  |
| 187 | margin_assurescale_ratio | 否 |  |  |
| 188 | relation_info | 否 |  |  |
| 189 | occur_balance | 否 |  |  |
| 190 | occur_interest | 否 |  |  |
| 191 | occur_fine | 否 |  |  |
| 192 | occur_recoup | 否 |  |  |
| 193 | occur_amount | 否 |  |  |
| 194 | busin_chan_info | 否 |  |  |
| 195 | busin_chan_desc | 否 |  |  |
| 196 | margin_num | 否 |  |  |
| 197 | srp_chan_balance | 否 |  |  |
| 198 | srp_chan_interest | 否 |  |  |
| 199 | srp_chan_fine | 否 |  |  |
| 200 | srp_chan_recoup | 否 |  |  |
| 201 | seat_no | 否 |  |  |
| 202 | fine_rate | 否 |  |  |
| 203 | con_contract_id | 否 |  |  |
| 204 | orig_allow_advance_date | 否 |  |  |
| 205 | orig_recoup_rate | 否 |  |  |
| 206 | orig_recoup_balance | 否 |  |  |
| 207 | spb_repaid_order | 否 |  |  |
| 208 | srp_conmod_sync_type | 否 |  |  |
| 209 | assure_contract_id | 否 |  |  |
| 210 | orig_papercont_id | 否 |  |  |
| 211 | rate_mode_orgin | 否 |  |  |
| 212 | margin_focus_ratio_orgin | 否 |  |  |
| 213 | margin_alert_ratio_orgin | 否 |  |  |
| 214 | margin_treat_ratio_orgin | 否 |  |  |
| 215 | margin_immtreat_ratio_orgin | 否 |  |  |
| 216 | join_serial_no | 否 |  |  |
| 217 | client_name | 否 | H |  |
| 218 | corp_client_group | 否 | H |  |
| 219 | client_group | 否 | H |  |
| 220 | room_code | 否 | H |  |
| 221 | asset_prop | 否 | H |  |
| 222 | limit_flag | 否 | H |  |
| 223 | client_prop | 否 | H |  |
| 224 | asset_level | 否 | H |  |
| 225 | risk_level | 否 | H |  |
| 226 | corp_risk_level | 否 | H |  |
| 227 | stock_name | 否 | H |  |
| 228 | sub_stock_type | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpapply | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpapply_acct | ART | 是 | fund_account, fund_account |
| idx_srpapply_cid | ART | 是 | contract_id, contract_id |
| idx_srpapply_id | ART | 是 | client_id, client_id |
| idx_srpapply_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpapply_tolast | ART | 是 | date_clear, date_clear |
| idx_srpapply | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_srpapply_acct | ART | 是 | fund_account, fund_account |
| idx_srpapply_cid | ART | 是 | contract_id, contract_id |
| idx_srpapply_id | ART | 是 | client_id, client_id |
| idx_srpapply_pos | ART | 是 | position_str, position_str |
| uk_rpt_srpapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpapply_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpapply | serial_no, init_date, serial_no, init_date |
| idx_srpapply | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:46:04 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:21 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:46:04 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:21:21 | 3.0.3.1 | wuxd | 新增 |

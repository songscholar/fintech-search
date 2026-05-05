# finexe_contract_jour - 融资行权合约流水表

**表对象ID**: 2363
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 144 个）

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
| 12 | finexe_contract_type | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | sopt_code | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | entrust_amount | 否 |  |  |
| 23 | entrust_balance | 否 |  |  |
| 24 | self_balance | 否 |  |  |
| 25 | sopt_tax | 否 |  |  |
| 26 | bfare_balance | 否 |  |  |
| 27 | expire_year_rate | 否 |  |  |
| 28 | recoup_rate | 否 |  |  |
| 29 | fine_rate | 否 |  |  |
| 30 | back_balance | 否 |  |  |
| 31 | date_back | 否 |  |  |
| 32 | finexe_contract_status | 否 |  |  |
| 33 | real_year_rate | 否 |  |  |
| 34 | real_back_balance | 否 |  |  |
| 35 | real_date_back | 否 |  |  |
| 36 | entrust_date | 否 |  |  |
| 37 | entrust_no | 否 |  |  |
| 38 | repaid_balance | 否 |  |  |
| 39 | fin_sell_balance | 否 |  |  |
| 40 | recoup_balance | 否 |  |  |
| 41 | fine_balance | 否 |  |  |
| 42 | settle_interest | 否 |  |  |
| 43 | unsettle_interest | 否 |  |  |
| 44 | sum_back_amount | 否 |  |  |
| 45 | executives_flag | 否 |  |  |
| 46 | margin_focus_ratio | 否 |  |  |
| 47 | margin_alert_ratio | 否 |  |  |
| 48 | margin_treat_ratio | 否 |  |  |
| 49 | integral_balance | 否 |  |  |
| 50 | integral_update | 否 |  |  |
| 51 | last_interest_date | 否 |  |  |
| 52 | batch_unsettle_interest | 否 |  |  |
| 53 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 54 | date_clear | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | margin_draw_ratio | 否 |  |  |
| 57 | interest_balance | 否 |  |  |
| 58 | is_auto_impawn | 否 |  |  |
| 59 | overdue_fine_balance | 否 |  |  |
| 60 | repaid_overdue_fine_balance | 否 |  |  |
| 61 | opp_report_id | 否 |  |  |
| 62 | client_name | 否 | H |  |
| 63 | corp_client_group | 否 | H |  |
| 64 | client_group | 否 | H |  |
| 65 | room_code | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_prop | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |
| 71 | stock_name | 否 | H |  |
| 72 | sub_stock_type | 否 | H |  |
| 73 | init_date | 否 |  |  |
| 74 | serial_no | 否 |  |  |
| 75 | curr_date | 否 |  |  |
| 76 | curr_time | 否 |  |  |
| 77 | op_branch_no | 否 |  |  |
| 78 | operator_no | 否 |  |  |
| 79 | op_entrust_way | 否 |  |  |
| 80 | op_station | 否 |  |  |
| 81 | business_flag | 否 |  |  |
| 82 | contract_id | 否 |  |  |
| 83 | join_contract_id | 否 |  |  |
| 84 | finexe_contract_type | 否 |  |  |
| 85 | branch_no | 否 |  |  |
| 86 | fund_account | 否 |  |  |
| 87 | client_id | 否 |  |  |
| 88 | stock_account | 否 |  |  |
| 89 | exchange_type | 否 |  |  |
| 90 | sopt_code | 否 |  |  |
| 91 | stock_code | 否 |  |  |
| 92 | stock_type | 否 |  |  |
| 93 | money_type | 否 |  |  |
| 94 | entrust_amount | 否 |  |  |
| 95 | entrust_balance | 否 |  |  |
| 96 | self_balance | 否 |  |  |
| 97 | sopt_tax | 否 |  |  |
| 98 | bfare_balance | 否 |  |  |
| 99 | expire_year_rate | 否 |  |  |
| 100 | recoup_rate | 否 |  |  |
| 101 | fine_rate | 否 |  |  |
| 102 | back_balance | 否 |  |  |
| 103 | date_back | 否 |  |  |
| 104 | finexe_contract_status | 否 |  |  |
| 105 | real_year_rate | 否 |  |  |
| 106 | real_back_balance | 否 |  |  |
| 107 | real_date_back | 否 |  |  |
| 108 | entrust_date | 否 |  |  |
| 109 | entrust_no | 否 |  |  |
| 110 | repaid_balance | 否 |  |  |
| 111 | fin_sell_balance | 否 |  |  |
| 112 | recoup_balance | 否 |  |  |
| 113 | fine_balance | 否 |  |  |
| 114 | settle_interest | 否 |  |  |
| 115 | unsettle_interest | 否 |  |  |
| 116 | sum_back_amount | 否 |  |  |
| 117 | executives_flag | 否 |  |  |
| 118 | margin_focus_ratio | 否 |  |  |
| 119 | margin_alert_ratio | 否 |  |  |
| 120 | margin_treat_ratio | 否 |  |  |
| 121 | integral_balance | 否 |  |  |
| 122 | integral_update | 否 |  |  |
| 123 | last_interest_date | 否 |  |  |
| 124 | batch_unsettle_interest | 否 |  |  |
| 125 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 126 | date_clear | 否 |  |  |
| 127 | remark | 否 |  |  |
| 128 | margin_draw_ratio | 否 |  |  |
| 129 | interest_balance | 否 |  |  |
| 130 | is_auto_impawn | 否 |  |  |
| 131 | overdue_fine_balance | 否 |  |  |
| 132 | repaid_overdue_fine_balance | 否 |  |  |
| 133 | opp_report_id | 否 |  |  |
| 134 | client_name | 否 | H |  |
| 135 | corp_client_group | 否 | H |  |
| 136 | client_group | 否 | H |  |
| 137 | room_code | 否 | H |  |
| 138 | limit_flag | 否 | H |  |
| 139 | client_prop | 否 | H |  |
| 140 | asset_level | 否 | H |  |
| 141 | risk_level | 否 | H |  |
| 142 | corp_risk_level | 否 | H |  |
| 143 | stock_name | 否 | H |  |
| 144 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexecontractjour | 默认 | 否 |  |
| idx_finexecontractjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_finexecontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_finexecontractjour_id | ART | 是 | client_id, client_id |
| idx_finexecontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexecontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexecontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_finexecontractjour | 默认 | 否 |  |
| idx_finexecontractjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_finexecontractjour_acct | ART | 是 | fund_account, fund_account |
| idx_finexecontractjour_id | ART | 是 | client_id, client_id |
| idx_finexecontractjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexecontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexecontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexecontractjour | serial_no, init_date, serial_no, init_date |
| idx_finexecontractjour | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:42:01 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |
| 2026-03-04 15:42:01 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |

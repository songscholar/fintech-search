# uref_lendagreement_jour - 出借委托代理协议流水表

**表对象ID**: 6035
**所属模块**: refacct
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 94 个）

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
| 9 | branch_no | 否 |  |  |
| 10 | business_flag | 否 |  |  |
| 11 | agreement_id | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | money_type | 否 |  |  |
| 15 | agreement_status | 否 |  |  |
| 16 | begin_date | 否 |  |  |
| 17 | end_date | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | en_ref_term | 否 |  |  |
| 23 | default_term | 否 |  |  |
| 24 | upper_lend_amount | 否 |  |  |
| 25 | min_ratio | 否 |  |  |
| 26 | used_amount | 否 |  |  |
| 27 | reserve_flag | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | position_str | 否 |  |  |
| 30 | stiblend_flag | 否 |  |  |
| 31 | shdc_circulate_type | 否 |  |  |
| 32 | stock_property | 否 |  |  |
| 33 | reggem_lend_flag | 否 |  |  |
| 34 | approvegem_lend_flag | 否 |  |  |
| 35 | client_group | 否 | H |  |
| 36 | room_code | 否 | H |  |
| 37 | asset_prop | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | limit_flag | 否 | H |  |
| 40 | risk_level | 否 | H |  |
| 41 | corp_client_group | 否 | H |  |
| 42 | corp_risk_level | 否 | H |  |
| 43 | client_name | 否 | H |  |
| 44 | asset_level | 否 | H |  |
| 45 | stock_name | 否 | H |  |
| 46 | stock_type | 否 | H |  |
| 47 | sub_stock_type | 否 | H |  |
| 48 | init_date | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | curr_date | 否 |  |  |
| 51 | curr_time | 否 |  |  |
| 52 | op_branch_no | 否 |  |  |
| 53 | operator_no | 否 |  |  |
| 54 | op_entrust_way | 否 |  |  |
| 55 | op_station | 否 |  |  |
| 56 | branch_no | 否 |  |  |
| 57 | business_flag | 否 |  |  |
| 58 | agreement_id | 否 |  |  |
| 59 | client_id | 否 |  |  |
| 60 | fund_account | 否 |  |  |
| 61 | money_type | 否 |  |  |
| 62 | agreement_status | 否 |  |  |
| 63 | begin_date | 否 |  |  |
| 64 | end_date | 否 |  |  |
| 65 | date_clear | 否 |  |  |
| 66 | exchange_type | 否 |  |  |
| 67 | stock_account | 否 |  |  |
| 68 | stock_code | 否 |  |  |
| 69 | en_ref_term | 否 |  |  |
| 70 | default_term | 否 |  |  |
| 71 | upper_lend_amount | 否 |  |  |
| 72 | min_ratio | 否 |  |  |
| 73 | used_amount | 否 |  |  |
| 74 | reserve_flag | 否 |  |  |
| 75 | remark | 否 |  |  |
| 76 | position_str | 否 |  |  |
| 77 | stiblend_flag | 否 |  |  |
| 78 | shdc_circulate_type | 否 |  |  |
| 79 | stock_property | 否 |  |  |
| 80 | reggem_lend_flag | 否 |  |  |
| 81 | approvegem_lend_flag | 否 |  |  |
| 82 | client_group | 否 | H |  |
| 83 | room_code | 否 | H |  |
| 84 | asset_prop | 否 | H |  |
| 85 | client_prop | 否 | H |  |
| 86 | limit_flag | 否 | H |  |
| 87 | risk_level | 否 | H |  |
| 88 | corp_client_group | 否 | H |  |
| 89 | corp_risk_level | 否 | H |  |
| 90 | client_name | 否 | H |  |
| 91 | asset_level | 否 | H |  |
| 92 | stock_name | 否 | H |  |
| 93 | stock_type | 否 | H |  |
| 94 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reflagreementjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reflagreementjour_cont | ART | 是 | agreement_id, agreement_id |
| idx_reflagreementjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reflagreementjour_cont | ART | 是 | agreement_id, agreement_id |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_reflagreementjour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ureflendagreementjour_pos | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendagreementjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendagreementjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendagreementjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_reflagreementjour | fund_account, init_date, serial_no, fund_account, init_date, serial_no |
| uk_rpt_ureflendagreementjour_pos | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendagreementjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendagreementjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendagreementjour_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:34:55 | 3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_lendagreement_jour，添加了表字段(stock_name)... |
| 2025-10-16 10:31:24 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:34:55 | 3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_lendagreement_jour，添加了表字段(stock_name)... |
| 2025-10-16 10:31:24 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |

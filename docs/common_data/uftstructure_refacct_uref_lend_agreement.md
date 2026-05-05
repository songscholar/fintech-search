# uref_lend_agreement - 出借委托代理协议

**表对象ID**: 6034
**所属模块**: refacct
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | agreement_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | agreement_status | 否 |  |  |
| 8 | begin_date | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | ref_type | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | en_ref_term | 否 |  |  |
| 16 | default_term | 否 |  |  |
| 17 | upper_lend_amount | 否 |  |  |
| 18 | min_ratio | 否 |  |  |
| 19 | used_amount | 否 |  |  |
| 20 | reserve_flag | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | stiblend_flag | 否 |  |  |
| 24 | shdc_circulate_type | 否 |  |  |
| 25 | stock_property | 否 |  |  |
| 26 | reggem_lend_flag | 否 |  |  |
| 27 | approvegem_lend_flag | 否 |  |  |
| 28 | client_group | 否 | H |  |
| 29 | room_code | 否 | H |  |
| 30 | asset_prop | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | client_name | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | stock_name | 否 | H |  |
| 39 | stock_type | 否 | H |  |
| 40 | sub_stock_type | 否 | H |  |
| 41 | init_date | 否 |  |  |
| 42 | agreement_id | 否 |  |  |
| 43 | branch_no | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | money_type | 否 |  |  |
| 47 | agreement_status | 否 |  |  |
| 48 | begin_date | 否 |  |  |
| 49 | end_date | 否 |  |  |
| 50 | date_clear | 否 |  |  |
| 51 | ref_type | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | stock_account | 否 |  |  |
| 54 | stock_code | 否 |  |  |
| 55 | en_ref_term | 否 |  |  |
| 56 | default_term | 否 |  |  |
| 57 | upper_lend_amount | 否 |  |  |
| 58 | min_ratio | 否 |  |  |
| 59 | used_amount | 否 |  |  |
| 60 | reserve_flag | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | position_str | 否 |  |  |
| 63 | stiblend_flag | 否 |  |  |
| 64 | shdc_circulate_type | 否 |  |  |
| 65 | stock_property | 否 |  |  |
| 66 | reggem_lend_flag | 否 |  |  |
| 67 | approvegem_lend_flag | 否 |  |  |
| 68 | client_group | 否 | H |  |
| 69 | room_code | 否 | H |  |
| 70 | asset_prop | 否 | H |  |
| 71 | client_prop | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_client_group | 否 | H |  |
| 75 | corp_risk_level | 否 | H |  |
| 76 | client_name | 否 | H |  |
| 77 | asset_level | 否 | H |  |
| 78 | stock_name | 否 | H |  |
| 79 | stock_type | 否 | H |  |
| 80 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reflagreement | ART | 是 | agreement_id, agreement_id |
| idx_reflagreement_id | ART | 是 | client_id, client_id |
| idx_reflagreement_acct | ART | 是 | fund_account, fund_account |
| idx_reflagreement_acco | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |
| idx_reflagreement_pos | ART | 是 | position_str, position_str |
| idx_reflagreement | ART | 是 | agreement_id, agreement_id |
| idx_reflagreement_id | ART | 是 | client_id, client_id |
| idx_reflagreement_acct | ART | 是 | fund_account, fund_account |
| idx_reflagreement_acco | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |
| idx_reflagreement_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_reflagreement | agreement_id, agreement_id |
| uk_rpt_ureflendagreement_pos | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendagreement_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendagreement_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendagreement_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_reflagreement | agreement_id, agreement_id |
| uk_rpt_ureflendagreement_pos | init_date, position_str, init_date, position_str |
| idx_rpt_ureflendagreement_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureflendagreement_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureflendagreement_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:25:22 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:25:22 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |

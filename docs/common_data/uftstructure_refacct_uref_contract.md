# uref_contract - 转融通资格合同

**表对象ID**: 6032
**所属模块**: refacct
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 78 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | client_name | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | refacct_type | 否 |  |  |
| 8 | refcash_rate_kind | 否 |  |  |
| 9 | reffare_kind | 否 |  |  |
| 10 | id_kind | 否 |  |  |
| 11 | id_no | 否 |  |  |
| 12 | begin_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | agreement_flag | 否 |  |  |
| 15 | refcontract_status | 否 |  |  |
| 16 | papercont_id | 否 |  |  |
| 17 | date_clear | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | refcontract_rights | 否 |  |  |
| 21 | stiblend_flag | 否 |  |  |
| 22 | stiblend_valid_date | 否 |  |  |
| 23 | reggem_lend_flag | 否 |  |  |
| 24 | approvegem_lend_flag | 否 |  |  |
| 25 | single_report_flag | 否 |  |  |
| 26 | organ_prodtrustee_name | 否 |  |  |
| 27 | trustee_csdc_person_code | 否 |  |  |
| 28 | trustee_csfc_clear_organ | 否 |  |  |
| 29 | lendflag_str | 否 |  |  |
| 30 | client_group | 否 |  |  |
| 31 | room_code | 否 |  |  |
| 32 | asset_prop | 否 |  |  |
| 33 | asset_level | 否 |  |  |
| 34 | limit_flag | 否 |  |  |
| 35 | risk_level | 否 |  |  |
| 36 | corp_client_group | 否 |  |  |
| 37 | corp_risk_level | 否 |  |  |
| 38 | client_prop | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | init_date | 否 |  |  |
| 41 | contract_id | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | client_id | 否 |  |  |
| 44 | client_name | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | refacct_type | 否 |  |  |
| 47 | refcash_rate_kind | 否 |  |  |
| 48 | reffare_kind | 否 |  |  |
| 49 | id_kind | 否 |  |  |
| 50 | id_no | 否 |  |  |
| 51 | begin_date | 否 |  |  |
| 52 | end_date | 否 |  |  |
| 53 | agreement_flag | 否 |  |  |
| 54 | refcontract_status | 否 |  |  |
| 55 | papercont_id | 否 |  |  |
| 56 | date_clear | 否 |  |  |
| 57 | remark | 否 |  |  |
| 58 | position_str | 否 |  |  |
| 59 | refcontract_rights | 否 |  |  |
| 60 | stiblend_flag | 否 |  |  |
| 61 | stiblend_valid_date | 否 |  |  |
| 62 | reggem_lend_flag | 否 |  |  |
| 63 | approvegem_lend_flag | 否 |  |  |
| 64 | single_report_flag | 否 |  |  |
| 65 | organ_prodtrustee_name | 否 |  |  |
| 66 | trustee_csdc_person_code | 否 |  |  |
| 67 | trustee_csfc_clear_organ | 否 |  |  |
| 68 | lendflag_str | 否 |  |  |
| 69 | client_group | 否 |  |  |
| 70 | room_code | 否 |  |  |
| 71 | asset_prop | 否 |  |  |
| 72 | asset_level | 否 |  |  |
| 73 | limit_flag | 否 |  |  |
| 74 | risk_level | 否 |  |  |
| 75 | corp_client_group | 否 |  |  |
| 76 | corp_risk_level | 否 |  |  |
| 77 | client_prop | 否 |  |  |
| 78 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcontract | ART | 是 | contract_id, contract_id |
| idx_refcontract_id | ART | 是 | client_id, client_id |
| idx_refcontract_acct | ART | 是 | fund_account, fund_account |
| idx_refcontract_pos | ART | 是 | position_str, position_str |
| idx_refcontract | ART | 是 | contract_id, contract_id |
| idx_refcontract_id | ART | 是 | client_id, client_id |
| idx_refcontract_acct | ART | 是 | fund_account, fund_account |
| idx_refcontract_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcontract | contract_id, contract_id |
| uk_rpt_urefcontract | init_date, position_str, init_date, position_str |
| idx_rpt_urefcontract_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefcontract_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefcontract_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_refcontract | contract_id, contract_id |
| uk_rpt_urefcontract | init_date, position_str, init_date, position_str |
| idx_rpt_urefcontract_id | client_id, position_str, client_id, position_str |
| idx_rpt_urefcontract_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_urefcontract_bra | init_date, branch_no, position_str, init_date, branch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:23:58 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-09-22 19:11:47 | 3.0.2.2 | T202509226170 | 物理表uref_contract，添加了表字段(transaction_no);
 |
| 2025-08-26 17:16:18 | 3.0.2.2 | 高志强 | 数据存储介质改为DB+MDB |
| 2025-10-16 10:23:58 | 3.0.2.3 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-09-22 19:11:47 | 3.0.2.2 | T202509226170 | 物理表uref_contract，添加了表字段(transaction_no);
 |
| 2025-08-26 17:16:18 | 3.0.2.2 | 高志强 | 数据存储介质改为DB+MDB |

# finexe_apply_jour - 融资行权申请流水表

**表对象ID**: 2636
**所属模块**: cbpsrp
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
| 7 | op_station | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
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
| 21 | entrust_balance | 否 |  |  |
| 22 | entrust_amount | 否 |  |  |
| 23 | repaid_balance | 否 |  |  |
| 24 | date_back | 否 |  |  |
| 25 | back_balance | 否 |  |  |
| 26 | finexe_apply_type | 否 |  |  |
| 27 | finexe_apply_status | 否 |  |  |
| 28 | expire_year_rate | 否 |  |  |
| 29 | orig_real_date_back | 否 |  |  |
| 30 | orig_real_year_rate | 否 |  |  |
| 31 | orig_back_balance | 否 |  |  |
| 32 | audit_remark | 否 |  |  |
| 33 | remark | 否 |  |  |
| 34 | date_clear | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 36 | client_name | 否 | H |  |
| 37 | corp_client_group | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | asset_prop | 否 | H |  |
| 41 | limit_flag | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | asset_level | 否 | H |  |
| 44 | risk_level | 否 | H |  |
| 45 | corp_risk_level | 否 | H |  |
| 46 | stock_name | 否 | H |  |
| 47 | sub_stock_type | 否 | H |  |
| 48 | init_date | 否 |  |  |
| 49 | serial_no | 否 |  |  |
| 50 | curr_date | 否 |  |  |
| 51 | curr_time | 否 |  |  |
| 52 | op_branch_no | 否 |  |  |
| 53 | operator_no | 否 |  |  |
| 54 | op_station | 否 |  |  |
| 55 | op_entrust_way | 否 |  |  |
| 56 | business_flag | 否 |  |  |
| 57 | contract_id | 否 |  |  |
| 58 | join_contract_id | 否 |  |  |
| 59 | finexe_contract_type | 否 |  |  |
| 60 | branch_no | 否 |  |  |
| 61 | fund_account | 否 |  |  |
| 62 | client_id | 否 |  |  |
| 63 | stock_account | 否 |  |  |
| 64 | exchange_type | 否 |  |  |
| 65 | sopt_code | 否 |  |  |
| 66 | stock_code | 否 |  |  |
| 67 | stock_type | 否 |  |  |
| 68 | entrust_balance | 否 |  |  |
| 69 | entrust_amount | 否 |  |  |
| 70 | repaid_balance | 否 |  |  |
| 71 | date_back | 否 |  |  |
| 72 | back_balance | 否 |  |  |
| 73 | finexe_apply_type | 否 |  |  |
| 74 | finexe_apply_status | 否 |  |  |
| 75 | expire_year_rate | 否 |  |  |
| 76 | orig_real_date_back | 否 |  |  |
| 77 | orig_real_year_rate | 否 |  |  |
| 78 | orig_back_balance | 否 |  |  |
| 79 | audit_remark | 否 |  |  |
| 80 | remark | 否 |  |  |
| 81 | date_clear | 否 |  |  |
| 82 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 83 | client_name | 否 | H |  |
| 84 | corp_client_group | 否 | H |  |
| 85 | client_group | 否 | H |  |
| 86 | room_code | 否 | H |  |
| 87 | asset_prop | 否 | H |  |
| 88 | limit_flag | 否 | H |  |
| 89 | client_prop | 否 | H |  |
| 90 | asset_level | 否 | H |  |
| 91 | risk_level | 否 | H |  |
| 92 | corp_risk_level | 否 | H |  |
| 93 | stock_name | 否 | H |  |
| 94 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexeapplyjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_finexeapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_finexeapplyjour_id | ART | 是 | client_id, client_id |
| idx_finexeapplyjour_cid | ART | 是 | contract_id, contract_id |
| idx_finexeapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_finexeapplyjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_finexeapplyjour_acct | ART | 是 | fund_account, fund_account |
| idx_finexeapplyjour_id | ART | 是 | client_id, client_id |
| idx_finexeapplyjour_cid | ART | 是 | contract_id, contract_id |
| idx_finexeapplyjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeapplyjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeapplyjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexeapplyjour | init_date, serial_no, init_date, serial_no |
| idx_finexeapplyjour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:58:48 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:49 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:58:48 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:49 | 3.0.3.1 | wuxd | 新增 |

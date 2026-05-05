# finexe_apply - 融资行权申请表

**表对象ID**: 2635
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | contract_id | 否 |  |  |
| 4 | join_contract_id | 否 |  |  |
| 5 | finexe_contract_type | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | sopt_code | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | entrust_balance | 否 |  |  |
| 15 | entrust_amount | 否 |  |  |
| 16 | repaid_balance | 否 |  |  |
| 17 | date_back | 否 |  |  |
| 18 | back_balance | 否 |  |  |
| 19 | finexe_apply_type | 否 |  |  |
| 20 | finexe_apply_status | 否 |  |  |
| 21 | expire_year_rate | 否 |  |  |
| 22 | orig_real_date_back | 否 |  |  |
| 23 | orig_real_year_rate | 否 |  |  |
| 24 | orig_back_balance | 否 |  |  |
| 25 | audit_remark | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 29 | client_name | 否 | H |  |
| 30 | corp_client_group | 否 | H |  |
| 31 | client_group | 否 | H |  |
| 32 | room_code | 否 | H |  |
| 33 | asset_prop | 否 | H |  |
| 34 | limit_flag | 否 | H |  |
| 35 | client_prop | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_risk_level | 否 | H |  |
| 39 | stock_name | 否 | H |  |
| 40 | sub_stock_type | 否 | H |  |
| 41 | init_date | 否 |  |  |
| 42 | serial_no | 否 |  |  |
| 43 | contract_id | 否 |  |  |
| 44 | join_contract_id | 否 |  |  |
| 45 | finexe_contract_type | 否 |  |  |
| 46 | branch_no | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | client_id | 否 |  |  |
| 49 | stock_account | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | sopt_code | 否 |  |  |
| 52 | stock_code | 否 |  |  |
| 53 | stock_type | 否 |  |  |
| 54 | entrust_balance | 否 |  |  |
| 55 | entrust_amount | 否 |  |  |
| 56 | repaid_balance | 否 |  |  |
| 57 | date_back | 否 |  |  |
| 58 | back_balance | 否 |  |  |
| 59 | finexe_apply_type | 否 |  |  |
| 60 | finexe_apply_status | 否 |  |  |
| 61 | expire_year_rate | 否 |  |  |
| 62 | orig_real_date_back | 否 |  |  |
| 63 | orig_real_year_rate | 否 |  |  |
| 64 | orig_back_balance | 否 |  |  |
| 65 | audit_remark | 否 |  |  |
| 66 | remark | 否 |  |  |
| 67 | date_clear | 否 |  |  |
| 68 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 69 | client_name | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | client_group | 否 | H |  |
| 72 | room_code | 否 | H |  |
| 73 | asset_prop | 否 | H |  |
| 74 | limit_flag | 否 | H |  |
| 75 | client_prop | 否 | H |  |
| 76 | asset_level | 否 | H |  |
| 77 | risk_level | 否 | H |  |
| 78 | corp_risk_level | 否 | H |  |
| 79 | stock_name | 否 | H |  |
| 80 | sub_stock_type | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexeapply | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_finexe_acct | ART | 是 | fund_account, fund_account |
| idx_finexe_id | ART | 是 | client_id, client_id |
| idx_finexe_cid | ART | 是 | contract_id, contract_id |
| idx_finexe_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_finexeapply_tolast | ART | 是 | date_clear, date_clear |
| idx_finexeapply | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_finexe_acct | ART | 是 | fund_account, fund_account |
| idx_finexe_id | ART | 是 | client_id, client_id |
| idx_finexe_cid | ART | 是 | contract_id, contract_id |
| idx_finexe_pos | ART | 是 | position_str, position_str |
| uk_rpt_finexeapply | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_finexeapply_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_finexeapply_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexeapply | init_date, serial_no, init_date, serial_no |
| idx_finexeapply | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:58:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:58 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:58:23 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.7 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:58 | 3.0.3.1 | wuxd | 新增 |

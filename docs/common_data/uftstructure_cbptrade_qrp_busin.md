# qrp_busin - 报价回购业务计划表

**表对象ID**: 2339
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 90 个）

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
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | entrust_prop | 否 |  |  |
| 16 | entrust_type | 否 |  |  |
| 17 | entrust_bs | 否 |  |  |
| 18 | entrust_amount | 否 |  |  |
| 19 | entrust_balance | 否 |  |  |
| 20 | postpone_flag | 否 |  |  |
| 21 | qrpmin_rate | 否 |  |  |
| 22 | start_date | 否 |  |  |
| 23 | end_date | 否 |  |  |
| 24 | entrust_date | 否 |  |  |
| 25 | entrust_no | 否 |  |  |
| 26 | valid_date | 否 |  |  |
| 27 | orig_business_id | 否 |  |  |
| 28 | qrpbusin_status | 否 |  |  |
| 29 | remark | 否 |  |  |
| 30 | date_clear | 否 |  |  |
| 31 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 32 | qrp_code | 否 |  |  |
| 33 | client_name | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | client_group | 否 | H |  |
| 36 | room_code | 否 | H |  |
| 37 | asset_prop | 否 | H |  |
| 38 | limit_flag | 否 | H |  |
| 39 | client_prop | 否 | H |  |
| 40 | asset_level | 否 | H |  |
| 41 | risk_level | 否 | H |  |
| 42 | corp_risk_level | 否 | H |  |
| 43 | stock_name | 否 | H |  |
| 44 | stock_type | 否 | H |  |
| 45 | sub_stock_type | 否 | H |  |
| 46 | init_date | 否 |  |  |
| 47 | serial_no | 否 |  |  |
| 48 | curr_date | 否 |  |  |
| 49 | curr_time | 否 |  |  |
| 50 | op_branch_no | 否 |  |  |
| 51 | operator_no | 否 |  |  |
| 52 | op_station | 否 |  |  |
| 53 | op_entrust_way | 否 |  |  |
| 54 | branch_no | 否 |  |  |
| 55 | fund_account | 否 |  |  |
| 56 | client_id | 否 |  |  |
| 57 | exchange_type | 否 |  |  |
| 58 | stock_code | 否 |  |  |
| 59 | stock_account | 否 |  |  |
| 60 | entrust_prop | 否 |  |  |
| 61 | entrust_type | 否 |  |  |
| 62 | entrust_bs | 否 |  |  |
| 63 | entrust_amount | 否 |  |  |
| 64 | entrust_balance | 否 |  |  |
| 65 | postpone_flag | 否 |  |  |
| 66 | qrpmin_rate | 否 |  |  |
| 67 | start_date | 否 |  |  |
| 68 | end_date | 否 |  |  |
| 69 | entrust_date | 否 |  |  |
| 70 | entrust_no | 否 |  |  |
| 71 | valid_date | 否 |  |  |
| 72 | orig_business_id | 否 |  |  |
| 73 | qrpbusin_status | 否 |  |  |
| 74 | remark | 否 |  |  |
| 75 | date_clear | 否 |  |  |
| 76 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 77 | qrp_code | 否 |  |  |
| 78 | client_name | 否 | H |  |
| 79 | corp_client_group | 否 | H |  |
| 80 | client_group | 否 | H |  |
| 81 | room_code | 否 | H |  |
| 82 | asset_prop | 否 | H |  |
| 83 | limit_flag | 否 | H |  |
| 84 | client_prop | 否 | H |  |
| 85 | asset_level | 否 | H |  |
| 86 | risk_level | 否 | H |  |
| 87 | corp_risk_level | 否 | H |  |
| 88 | stock_name | 否 | H |  |
| 89 | stock_type | 否 | H |  |
| 90 | sub_stock_type | 否 | H |  |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_busin | 默认 | 否 |  |
| idx_qrp_busin | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_qrp_busin_pos | ART | 是 | position_str, position_str |
| idx_qrp_busin_acct | ART | 是 | fund_account, fund_account |
| idx_qrp_busin_id | ART | 是 | client_id, client_id |
| uk_rpt_qrpbusin | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_qrpbusin_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_qrpbusin_tolast | ART | 是 | date_clear, date_clear |
| idx_qrp_busin | 默认 | 否 |  |
| idx_qrp_busin | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_qrp_busin_pos | ART | 是 | position_str, position_str |
| idx_qrp_busin_acct | ART | 是 | fund_account, fund_account |
| idx_qrp_busin_id | ART | 是 | client_id, client_id |
| uk_rpt_qrpbusin | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_qrpbusin_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_qrpbusin_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_busin | serial_no, init_date, serial_no, init_date |
| idx_qrp_busin | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:31:32 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-05 09:02:25 | V3.0.2.14 | 曾剑辉 | 新增表结构 |
| 2026-03-04 15:31:32 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-05 09:02:25 | V3.0.2.14 | 曾剑辉 | 新增表结构 |

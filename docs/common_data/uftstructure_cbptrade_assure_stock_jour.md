# assure_stock_jour - 担保持仓流水表

**表对象ID**: 2366
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_station | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | business_flag | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | stock_open_date | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | assure_type | 否 |  |  |
| 18 | occur_amount | 否 |  |  |
| 19 | impawn_amount | 否 |  |  |
| 20 | pre_impawn_amount | 否 |  |  |
| 21 | cancel_serial_no | 否 |  |  |
| 22 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 23 | remark | 否 |  |  |
| 24 | out_impawn_amount | 否 |  |  |
| 25 | client_name | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | client_prop | 否 | H |  |
| 32 | asset_level | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | stock_name | 否 | H |  |
| 36 | sub_stock_type | 否 | H |  |
| 37 | init_date | 否 |  |  |
| 38 | serial_no | 否 |  |  |
| 39 | curr_date | 否 |  |  |
| 40 | curr_time | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | op_station | 否 |  |  |
| 43 | op_entrust_way | 否 |  |  |
| 44 | business_flag | 否 |  |  |
| 45 | branch_no | 否 |  |  |
| 46 | fund_account | 否 |  |  |
| 47 | client_id | 否 |  |  |
| 48 | stock_account | 否 |  |  |
| 49 | stock_open_date | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | stock_type | 否 |  |  |
| 53 | assure_type | 否 |  |  |
| 54 | occur_amount | 否 |  |  |
| 55 | impawn_amount | 否 |  |  |
| 56 | pre_impawn_amount | 否 |  |  |
| 57 | cancel_serial_no | 否 |  |  |
| 58 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 59 | remark | 否 |  |  |
| 60 | out_impawn_amount | 否 |  |  |
| 61 | client_name | 否 | H |  |
| 62 | corp_client_group | 否 | H |  |
| 63 | client_group | 否 | H |  |
| 64 | room_code | 否 | H |  |
| 65 | asset_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_prop | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |
| 71 | stock_name | 否 | H |  |
| 72 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assurestockjour_pos | ART | 是 | position_str, position_str |
| idx_assurestockjour_acct | ART | 是 | fund_account, fund_account |
| idx_assurestockjour_id | ART | 是 | client_id, client_id |
| uk_rpt_assurestockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_assurestockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_assurestockjour_pos | ART | 是 | position_str, position_str |
| idx_assurestockjour_acct | ART | 是 | fund_account, fund_account |
| idx_assurestockjour_id | ART | 是 | client_id, client_id |
| uk_rpt_assurestockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_assurestockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assurestockjour_pos | position_str, position_str |
| idx_assurestockjour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:43:15 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-29 09:28:58 | V3.0.2.1008 |  | 物理表assure_stock_jour，删除了表字段(cancel_serialno);
,物理表assure_st... |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |
| 2026-03-04 15:43:15 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-29 09:28:58 | V3.0.2.1008 |  | 物理表assure_stock_jour，删除了表字段(cancel_serialno);
,物理表assure_st... |
| 2024-09-25 21:37:18 | V3.0.2.1008 | 张明月 | 新增 |

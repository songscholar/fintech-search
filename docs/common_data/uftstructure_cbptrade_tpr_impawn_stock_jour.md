# tpr_impawn_stock_jour - 三方回购质押券信息流水表

**表对象ID**: 2547
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | basket_id | 否 |  |  |
| 10 | bond_end_date | 否 |  |  |
| 11 | store_amount | 否 |  |  |
| 12 | reg_impawn_amount | 否 |  |  |
| 13 | pre_out_amount | 否 |  |  |
| 14 | used_amount | 否 |  |  |
| 15 | fruits | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | curr_due_amount | 否 |  |  |
| 19 | client_name | 否 | H |  |
| 20 | corp_client_group | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_risk_level | 否 | H |  |
| 29 | stock_name | 否 | H |  |
| 30 | stock_type | 否 | H |  |
| 31 | sub_stock_type | 否 | H |  |
| 32 | init_date | 否 |  |  |
| 33 | serial_no | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | client_id | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | exchange_type | 否 |  |  |
| 38 | stock_account | 否 |  |  |
| 39 | stock_code | 否 |  |  |
| 40 | basket_id | 否 |  |  |
| 41 | bond_end_date | 否 |  |  |
| 42 | store_amount | 否 |  |  |
| 43 | reg_impawn_amount | 否 |  |  |
| 44 | pre_out_amount | 否 |  |  |
| 45 | used_amount | 否 |  |  |
| 46 | fruits | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | position_str | 否 |  |  |
| 49 | curr_due_amount | 否 |  |  |
| 50 | client_name | 否 | H |  |
| 51 | corp_client_group | 否 | H |  |
| 52 | client_group | 否 | H |  |
| 53 | room_code | 否 | H |  |
| 54 | asset_prop | 否 | H |  |
| 55 | limit_flag | 否 | H |  |
| 56 | client_prop | 否 | H |  |
| 57 | asset_level | 否 | H |  |
| 58 | risk_level | 否 | H |  |
| 59 | corp_risk_level | 否 | H |  |
| 60 | stock_name | 否 | H |  |
| 61 | stock_type | 否 | H |  |
| 62 | sub_stock_type | 否 | H |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprimpstkjour_no | 默认 | 否 |  |
| idx_tprimpstkjour_acct | 默认 | 否 |  |
| idx_tprimpstkjour_pos | 默认 | 否 |  |
| idx_tprimpstkjour_no | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_tprimpstkjour_no | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_tprimpstkjour_acct | ART | 是 | fund_account, fund_account |
| idx_tprimpstkjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprimpawnstockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprimpawnstockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_tprimpstkjour_no | 默认 | 否 |  |
| idx_tprimpstkjour_acct | 默认 | 否 |  |
| idx_tprimpstkjour_pos | 默认 | 否 |  |
| idx_tprimpstkjour_no | 默认 | 否 | init_date, serial_no, init_date, serial_no |
| idx_tprimpstkjour_no | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_tprimpstkjour_acct | ART | 是 | fund_account, fund_account |
| idx_tprimpstkjour_pos | ART | 是 | position_str, position_str |
| uk_rpt_tprimpawnstockjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_tprimpawnstockjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprimpstkjour_no | init_date, serial_no, init_date, serial_no |
| idx_tprimpstkjour_no | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:28:13 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:55:56 | 3.0.2.75 | taocong45644 | 当前表tpr_impawn_stock_jour，修改了索引idx_tprimpstkjour_no,索引字段修改为：(... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |
| 2026-03-04 16:28:13 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 13:55:56 | 3.0.2.75 | taocong45644 | 当前表tpr_impawn_stock_jour，修改了索引idx_tprimpstkjour_no,索引字段修改为：(... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |

# stock_locking_jour - 备兑证券锁定流水表

**表对象ID**: 5573
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 52 个）

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
| 9 | stock_type | 否 |  |  |
| 10 | begin_amount | 否 |  |  |
| 11 | sell_frozen_amount1 | 否 |  |  |
| 12 | sell_frozen_amount2 | 否 |  |  |
| 13 | cancel_serial_no | 否 |  |  |
| 14 | position_str | 否 |  | init_date(8) +partition_no(2)+branch_no(5)+serial_no(10) |
| 15 | client_name | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | client_group | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | limit_flag | 否 | H |  |
| 21 | client_prop | 否 | H |  |
| 22 | asset_level | 否 | H |  |
| 23 | risk_level | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | stock_name | 否 | H |  |
| 26 | sub_stock_type | 否 | H |  |
| 27 | init_date | 否 |  |  |
| 28 | serial_no | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_account | 否 |  |  |
| 34 | stock_code | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | begin_amount | 否 |  |  |
| 37 | sell_frozen_amount1 | 否 |  |  |
| 38 | sell_frozen_amount2 | 否 |  |  |
| 39 | cancel_serial_no | 否 |  |  |
| 40 | position_str | 否 |  | init_date(8) +partition_no(2)+branch_no(5)+serial_no(10) |
| 41 | client_name | 否 | H |  |
| 42 | corp_client_group | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | client_prop | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |
| 51 | stock_name | 否 | H |  |
| 52 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stock_locking_jour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_stock_locking_jour_fund | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| uk_rpt_stocklockingjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stocklockingjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_stock_locking_jour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_stock_locking_jour_fund | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| uk_rpt_stocklockingjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stocklockingjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stock_locking_jour | init_date, position_str, init_date, position_str |
| idx_stock_locking_jour | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:21:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.46 | 李江霖 | 增加position_str的备注 |
| 2024-09-10 13:43:50 | 3.0.2.45 | 洪略 | 新增表 |
| 2026-03-09 14:21:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.46 | 李江霖 | 增加position_str的备注 |
| 2024-09-10 13:43:50 | 3.0.2.45 | 洪略 | 新增表 |

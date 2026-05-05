# judifrozenjour - 司法冻结流水表

**表对象ID**: 2542
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | seat_no | 否 |  |  |
| 16 | frozen_amount | 否 |  |  |
| 17 | stbcontain_flag | 否 |  |  |
| 18 | csdc_sellfro_flag | 否 |  |  |
| 19 | begin_date | 否 |  |  |
| 20 | end_date | 否 |  |  |
| 21 | juti_type | 否 |  |  |
| 22 | judiorgan_name | 否 |  |  |
| 23 | judiorgan_kind | 否 |  |  |
| 24 | judireport_id | 否 |  |  |
| 25 | judifrozen_id | 否 |  |  |
| 26 | judiwait_id | 否 |  |  |
| 27 | judi_status | 否 |  |  |
| 28 | remark | 否 |  |  |
| 29 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 30 | sz_frozen_organname | 否 |  |  |
| 31 | principal | 否 |  |  |
| 32 | dividend | 否 |  |  |
| 33 | impawn_frozen_no | 否 |  |  |
| 34 | market_status | 否 |  |  |
| 35 | reporter_source | 否 |  |  |
| 36 | init_date | 否 |  |  |
| 37 | serial_no | 否 |  |  |
| 38 | curr_date | 否 |  |  |
| 39 | curr_time | 否 |  |  |
| 40 | operator_no | 否 |  |  |
| 41 | op_branch_no | 否 |  |  |
| 42 | op_entrust_way | 否 |  |  |
| 43 | op_station | 否 |  |  |
| 44 | branch_no | 否 |  |  |
| 45 | fund_account | 否 |  |  |
| 46 | client_id | 否 |  |  |
| 47 | stock_account | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | seat_no | 否 |  |  |
| 51 | frozen_amount | 否 |  |  |
| 52 | stbcontain_flag | 否 |  |  |
| 53 | csdc_sellfro_flag | 否 |  |  |
| 54 | begin_date | 否 |  |  |
| 55 | end_date | 否 |  |  |
| 56 | juti_type | 否 |  |  |
| 57 | judiorgan_name | 否 |  |  |
| 58 | judiorgan_kind | 否 |  |  |
| 59 | judireport_id | 否 |  |  |
| 60 | judifrozen_id | 否 |  |  |
| 61 | judiwait_id | 否 |  |  |
| 62 | judi_status | 否 |  |  |
| 63 | remark | 否 |  |  |
| 64 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 65 | sz_frozen_organname | 否 |  |  |
| 66 | principal | 否 |  |  |
| 67 | dividend | 否 |  |  |
| 68 | impawn_frozen_no | 否 |  |  |
| 69 | market_status | 否 |  |  |
| 70 | reporter_source | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_judifrozenj | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_judifrozenj_id | ART | 是 | client_id, client_id |
| idx_judifrozenj_acct | ART | 是 | fund_account, fund_account |
| idx_judifrozenj_pos | ART | 是 | position_str, position_str |
| idx_judifrozenj | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_judifrozenj_id | ART | 是 | client_id, client_id |
| idx_judifrozenj_acct | ART | 是 | fund_account, fund_account |
| idx_judifrozenj_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_judifrozenj | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_judifrozenj | serial_no, branch_no, init_date, serial_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:25:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-01-21 16:47:54 | 8.26.2.94 | 刘大为 | 所有表judifrozenjour，添加了表字段(reporter_source);
 |
| 2025-09-22 15:40:12 | V3.0.8.5 | dongh | 物理表judifrozenjour，添加了表字段(principal);
物理表judifrozenjour，添加了表... |
| 2024-12-21 17:05:00 | V3.0.2.1004 | 周富安 |  |
| 2026-03-04 16:25:55 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-01-21 16:47:54 | 8.26.2.94 | 刘大为 | 所有表judifrozenjour，添加了表字段(reporter_source);
 |
| 2025-09-22 15:40:12 | V3.0.8.5 | dongh | 物理表judifrozenjour，添加了表字段(principal);
物理表judifrozenjour，添加了表... |
| 2024-12-21 17:05:00 | V3.0.2.1004 | 周富安 |  |

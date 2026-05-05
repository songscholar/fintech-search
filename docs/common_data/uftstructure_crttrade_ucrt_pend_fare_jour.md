# ucrt_pend_fare_jour - 待扣收流水表

**表对象ID**: 7521
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | pendfare_id | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | compact_id | 否 |  |  |
| 17 | money_type | 否 |  |  |
| 18 | pendfare_type | 否 |  |  |
| 19 | occur_fare | 否 |  |  |
| 20 | post_fare | 否 |  |  |
| 21 | real_action | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | cashgroup_no | 否 |  |  |
| 24 | prefer_balance | 否 |  |  |
| 25 | frozen_balance | 否 |  |  |
| 26 | cashcompact_id | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | sub_stock_type | 否 | H |  |
| 40 | stock_name | 否 | H |  |
| 41 | init_date | 否 |  |  |
| 42 | serial_no | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | curr_microtime | 否 |  |  |
| 45 | operator_no | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | op_entrust_way | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | pendfare_id | 否 |  |  |
| 50 | client_id | 否 |  |  |
| 51 | fund_account | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | stock_account | 否 |  |  |
| 54 | stock_type | 否 |  |  |
| 55 | stock_code | 否 |  |  |
| 56 | compact_id | 否 |  |  |
| 57 | money_type | 否 |  |  |
| 58 | pendfare_type | 否 |  |  |
| 59 | occur_fare | 否 |  |  |
| 60 | post_fare | 否 |  |  |
| 61 | real_action | 否 |  |  |
| 62 | remark | 否 |  |  |
| 63 | cashgroup_no | 否 |  |  |
| 64 | prefer_balance | 否 |  |  |
| 65 | frozen_balance | 否 |  |  |
| 66 | cashcompact_id | 否 |  |  |
| 67 | branch_no | 否 |  |  |
| 68 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 69 | client_group | 否 | H |  |
| 70 | room_code | 否 | H |  |
| 71 | asset_prop | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_client_group | 否 | H |  |
| 75 | corp_risk_level | 否 | H |  |
| 76 | asset_level | 否 | H |  |
| 77 | client_name | 否 | H |  |
| 78 | client_prop | 否 | H |  |
| 79 | sub_stock_type | 否 | H |  |
| 80 | stock_name | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_pend_fare_jour | 默认 | 否 | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |
| idx_ucrt_pend_fare_jour_no | ART | 是 | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |
| uk_rpt_ucrtpendfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtpendfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_pend_fare_jour | 默认 | 否 | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |
| idx_ucrt_pend_fare_jour_no | ART | 是 | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |
| uk_rpt_ucrtpendfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtpendfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_pend_fare_jour | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |
| idx_ucrt_pend_fare_jour | fund_account, pendfare_id, init_date, serial_no, fund_account, pendfare_id, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 10:13:44 | 3.0.8.19 | 袁文龙 | 当前表ucrt_pend_fare_jour，修改了索引idx_ucrt_pend_fare_jour,索引字段修改为：... |
| 2025-08-21 14:09:18 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_pend_fare_jour，添加了表字段(branch_no);
物理表ucrt_pend_fare... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-02-28 10:13:44 | 3.0.8.19 | 袁文龙 | 当前表ucrt_pend_fare_jour，修改了索引idx_ucrt_pend_fare_jour,索引字段修改为：... |
| 2025-08-21 14:09:18 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_pend_fare_jour，添加了表字段(branch_no);
物理表ucrt_pend_fare... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

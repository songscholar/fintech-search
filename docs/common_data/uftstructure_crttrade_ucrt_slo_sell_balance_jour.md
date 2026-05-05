# ucrt_slo_sell_balance_jour - 融券卖出所得流水表

**表对象ID**: 7512
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | operator_no | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | op_entrust_way | 否 |  |  |
| 6 | op_station | 否 |  |  |
| 7 | curr_time | 否 |  |  |
| 8 | curr_date | 否 |  |  |
| 9 | money_type | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | business_flag | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | post_balance | 否 |  |  |
| 15 | occur_used_balance | 否 |  |  |
| 16 | post_used_balance | 否 |  |  |
| 17 | occur_frozen_balance | 否 |  |  |
| 18 | post_frozen_balance | 否 |  |  |
| 19 | real_action | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | position_str | 否 |  | iinit_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 23 | client_group | 否 | H |  |
| 24 | room_code | 否 | H |  |
| 25 | asset_prop | 否 | H |  |
| 26 | limit_flag | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | corp_risk_level | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | client_name | 否 | H |  |
| 32 | client_prop | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | serial_no | 否 |  |  |
| 35 | operator_no | 否 |  |  |
| 36 | op_branch_no | 否 |  |  |
| 37 | op_entrust_way | 否 |  |  |
| 38 | op_station | 否 |  |  |
| 39 | curr_time | 否 |  |  |
| 40 | curr_date | 否 |  |  |
| 41 | money_type | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | business_flag | 否 |  |  |
| 45 | occur_balance | 否 |  |  |
| 46 | post_balance | 否 |  |  |
| 47 | occur_used_balance | 否 |  |  |
| 48 | post_used_balance | 否 |  |  |
| 49 | occur_frozen_balance | 否 |  |  |
| 50 | post_frozen_balance | 否 |  |  |
| 51 | real_action | 否 |  |  |
| 52 | remark | 否 |  |  |
| 53 | branch_no | 否 |  |  |
| 54 | position_str | 否 |  | iinit_date(8)+node_id(2)+branch_no(5)+serial_no(10) |
| 55 | client_group | 否 | H |  |
| 56 | room_code | 否 | H |  |
| 57 | asset_prop | 否 | H |  |
| 58 | limit_flag | 否 | H |  |
| 59 | risk_level | 否 | H |  |
| 60 | corp_client_group | 否 | H |  |
| 61 | corp_risk_level | 否 | H |  |
| 62 | asset_level | 否 | H |  |
| 63 | client_name | 否 | H |  |
| 64 | client_prop | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_slo_sell_balance_jour | 默认 | 否 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| idx_ucrt_slo_sell_balance_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| uk_rpt_ucrtslosellbalancejour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_ucrt_slo_sell_balance_jour | 默认 | 否 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| idx_ucrt_slo_sell_balance_jour | ART | 是 | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| uk_rpt_ucrtslosellbalancejour | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_slo_sell_balance_jour | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |
| idx_ucrt_slo_sell_balance_jour | fund_account, money_type, init_date, serial_no, fund_account, money_type, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 10:40:58 | 3.0.8.19 | 袁文龙 | 当前表ucrt_slo_sell_balance_jour，修改了索引idx_ucrt_slo_sell_balance... |
| 2025-08-21 14:21:30 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_slo_sell_balance_jour，添加了表字段(branch_no);
物理表ucrt_sl... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-02-28 10:40:58 | 3.0.8.19 | 袁文龙 | 当前表ucrt_slo_sell_balance_jour，修改了索引idx_ucrt_slo_sell_balance... |
| 2025-08-21 14:21:30 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_slo_sell_balance_jour，添加了表字段(branch_no);
物理表ucrt_sl... |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

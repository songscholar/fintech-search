# fund_revert_jour - 资金反向操作流水表

**表对象ID**: 5540
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_microtime | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | op_branch_no | 否 |  |  |
| 11 | operator_no | 否 |  |  |
| 12 | op_station | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | post_balance | 否 |  |  |
| 15 | treat_status | 否 |  |  |
| 16 | valid_date | 否 |  |  |
| 17 | frozen_reason | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | order_no | 否 |  |  |
| 20 | position_str | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | serial_no | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | curr_date | 否 |  |  |
| 28 | curr_microtime | 否 |  |  |
| 29 | business_flag | 否 |  |  |
| 30 | op_branch_no | 否 |  |  |
| 31 | operator_no | 否 |  |  |
| 32 | op_station | 否 |  |  |
| 33 | occur_balance | 否 |  |  |
| 34 | post_balance | 否 |  |  |
| 35 | treat_status | 否 |  |  |
| 36 | valid_date | 否 |  |  |
| 37 | frozen_reason | 否 |  |  |
| 38 | remark | 否 |  |  |
| 39 | order_no | 否 |  |  |
| 40 | position_str | 否 |  |  |

## 索引（共 18 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fundrevertjour_pos | 默认 | 否 | position_str, position_str |
| idx_fundrevertjour | 默认 | 否 |  |
| idx_fundrevertjour | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_fundrevertjour_fk | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_fundrevertjour_id | ART | 是 | client_id, client_id |
| idx_fundrevertjour_pos | ART | 是 | position_str, position_str |
| idx_rpt_fundrevertjour_fk | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_rpt_fundrevertjour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_fundrevertjour_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_fundrevertjour_pos | 默认 | 否 | position_str, position_str |
| idx_fundrevertjour | 默认 | 否 |  |
| idx_fundrevertjour | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_fundrevertjour_fk | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_fundrevertjour_id | ART | 是 | client_id, client_id |
| idx_fundrevertjour_pos | ART | 是 | position_str, position_str |
| idx_rpt_fundrevertjour_fk | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_rpt_fundrevertjour_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_fundrevertjour_id | ART | 是 | client_id, position_str, client_id, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundrevertjour_pos | position_str, position_str |
| idx_fundrevertjour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:54:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 17:07:20 | V3.0.2.74 | 洪略 | 支持分区存储 |
| 2025-12-08 13:27:25 | V3.0.8.14 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-06 16:06:20 | V3.0.2.73 | 洪略 | 增加历史表 |
| 2025-07-08 19:36:47 | 3.0.6.1003 | 马天宇 | 物理表fund_revert_jour，增加索引(idx_fundrevertjour_pos:[position_st... |
| 2025-07-09 14:43:34 | 3.0.6.1003 | 马天宇 | 物理表fund_revert_jour，删除了表索引(idx_fundrevertjour);
 |
| 2025-06-24 20:32:22 | 3.0.2.71 | 马天宇 | 物理表fund_revert_jour，添加了表字段(position_str);
 |
| 2024-06-22 11:01:35 | 3.0.2.21 | 祝丁恺 | 物理表fund_revert_jour，添加了表字段(init_date);
物理表fund_revert_jour，... |
| 2026-03-09 13:54:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 17:07:20 | V3.0.2.74 | 洪略 | 支持分区存储 |
| 2025-12-08 13:27:25 | V3.0.8.14 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-06 16:06:20 | V3.0.2.73 | 洪略 | 增加历史表 |
| 2025-07-08 19:36:47 | 3.0.6.1003 | 马天宇 | 物理表fund_revert_jour，增加索引(idx_fundrevertjour_pos:[position_st... |
| 2025-07-09 14:43:34 | 3.0.6.1003 | 马天宇 | 物理表fund_revert_jour，删除了表索引(idx_fundrevertjour);
 |
| 2025-06-24 20:32:22 | 3.0.2.71 | 马天宇 | 物理表fund_revert_jour，添加了表字段(position_str);
 |

> 共 16 条修改记录，仅显示最近15条

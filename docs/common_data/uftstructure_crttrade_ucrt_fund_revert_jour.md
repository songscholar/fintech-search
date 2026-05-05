# ucrt_fund_revert_jour - 融资融券资金反向操作流水表

**表对象ID**: 7997
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | curr_date | 否 |  |  |
| 7 | curr_microtime | 否 |  |  |
| 8 | business_flag | 否 |  |  |
| 9 | op_branch_no | 否 |  |  |
| 10 | operator_no | 否 |  |  |
| 11 | op_station | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | post_balance | 否 |  |  |
| 15 | treat_status | 否 |  |  |
| 16 | valid_date | 否 |  |  |
| 17 | frozen_reason | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | order_no | 否 |  |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | corp_risk_level | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | client_name | 否 | H |  |
| 30 | client_prop | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | serial_no | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | fund_account | 否 |  |  |
| 35 | money_type | 否 |  |  |
| 36 | curr_date | 否 |  |  |
| 37 | curr_microtime | 否 |  |  |
| 38 | business_flag | 否 |  |  |
| 39 | op_branch_no | 否 |  |  |
| 40 | operator_no | 否 |  |  |
| 41 | op_station | 否 |  |  |
| 42 | branch_no | 否 |  |  |
| 43 | occur_balance | 否 |  |  |
| 44 | post_balance | 否 |  |  |
| 45 | treat_status | 否 |  |  |
| 46 | valid_date | 否 |  |  |
| 47 | frozen_reason | 否 |  |  |
| 48 | remark | 否 |  |  |
| 49 | position_str | 否 |  |  |
| 50 | order_no | 否 |  |  |
| 51 | client_group | 否 | H |  |
| 52 | room_code | 否 | H |  |
| 53 | asset_prop | 否 | H |  |
| 54 | limit_flag | 否 | H |  |
| 55 | risk_level | 否 | H |  |
| 56 | corp_client_group | 否 | H |  |
| 57 | corp_risk_level | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | client_name | 否 | H |  |
| 60 | client_prop | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrtfundrevertjour | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_ucrt_fund_revert_jour | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| uk_rpt_ucrtfundrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfundrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtfundrevertjour_tolast | ART | 是 | valid_date, valid_date |
| idx_ucrtfundrevertjour | ART | 是 | init_date, branch_no, serial_no, init_date, branch_no, serial_no |
| idx_ucrt_fund_revert_jour | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| uk_rpt_ucrtfundrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtfundrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucrtfundrevertjour_tolast | ART | 是 | valid_date, valid_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_revert_jour | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_ucrt_fund_revert_jour | init_date, fund_account, serial_no, init_date, fund_account, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-19 09:36:44 | 3.0.2.2016 | huangzh | 所有表ucrt_fund_revert_jour，删除了表字段（cashgroup_prop）；
所有表ucrt_fu... |
| 2025-06-20 13:35:38 | 3.0.2.2005 | huangzh | 新增表 |
| 2025-09-19 09:36:44 | 3.0.2.2016 | huangzh | 所有表ucrt_fund_revert_jour，删除了表字段（cashgroup_prop）；
所有表ucrt_fu... |
| 2025-06-20 13:35:38 | 3.0.2.2005 | huangzh | 新增表 |

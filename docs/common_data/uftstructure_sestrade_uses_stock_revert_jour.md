# uses_stock_revert_jour - 证券反向操作流水表

**表对象ID**: 5972
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_time | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | op_branch_no | 否 |  |  |
| 11 | operator_no | 否 |  |  |
| 12 | op_station | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | occur_amount | 否 |  |  |
| 16 | treat_status | 否 |  |  |
| 17 | valid_date | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | client_group | 否 |  |  |
| 20 | room_code | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | cancel_serialno | 否 |  |  |
| 24 | frozen_reason | 否 |  |  |
| 25 | stock_code_long | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | client_name | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
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
| 39 | stock_account | 否 |  |  |
| 40 | stock_code | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | exchange_type | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | curr_time | 否 |  |  |
| 45 | business_flag | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | operator_no | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | fund_account | 否 |  |  |
| 50 | client_id | 否 |  |  |
| 51 | occur_amount | 否 |  |  |
| 52 | treat_status | 否 |  |  |
| 53 | valid_date | 否 |  |  |
| 54 | position_str | 否 |  |  |
| 55 | client_group | 否 |  |  |
| 56 | room_code | 否 |  |  |
| 57 | money_type | 否 |  |  |
| 58 | stock_type | 否 |  |  |
| 59 | cancel_serialno | 否 |  |  |
| 60 | frozen_reason | 否 |  |  |
| 61 | stock_code_long | 否 |  |  |
| 62 | remark | 否 |  |  |
| 63 | client_name | 否 | H |  |
| 64 | corp_client_group | 否 | H |  |
| 65 | asset_prop | 否 | H |  |
| 66 | limit_flag | 否 | H |  |
| 67 | client_prop | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |
| 71 | stock_name | 否 | H |  |
| 72 | sub_stock_type | 否 | H |  |

## 索引（共 30 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stockrevertjour_bn | ART | 是 | serial_no, init_date, branch_no, serial_no, init_date, branch_no |
| idx_stockrevertjour | 默认 | 否 |  |
| idx_stkrjour_valid | 默认 | 否 |  |
| idx_stkrjour_id | 默认 | 否 |  |
| idx_stkrjour_acct | 默认 | 否 |  |
| idx_stkrjour_pos | 默认 | 否 |  |
| idx_stockrevertjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_stkrjour_valid | ART | 是 | valid_date, valid_date |
| idx_stkrjour_id | ART | 是 | client_id, client_id |
| idx_stkrjour_acct | ART | 是 | fund_account, fund_account |
| idx_stkrjour_pos | ART | 是 | position_str, position_str |
| idx_stockrevertjour_bn | ART | 是 | serial_no, init_date, branch_no, serial_no, init_date, branch_no |
| uk_rpt_usesstockrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesstockrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_usesstockrevertjour_tolast | ART | 是 | valid_date, valid_date |
| idx_stockrevertjour_bn | ART | 是 | serial_no, init_date, branch_no, serial_no, init_date, branch_no |
| idx_stockrevertjour | 默认 | 否 |  |
| idx_stkrjour_valid | 默认 | 否 |  |
| idx_stkrjour_id | 默认 | 否 |  |
| idx_stkrjour_acct | 默认 | 否 |  |
| idx_stkrjour_pos | 默认 | 否 |  |
| idx_stockrevertjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_stkrjour_valid | ART | 是 | valid_date, valid_date |
| idx_stkrjour_id | ART | 是 | client_id, client_id |
| idx_stkrjour_acct | ART | 是 | fund_account, fund_account |
| idx_stkrjour_pos | ART | 是 | position_str, position_str |
| idx_stockrevertjour_bn | ART | 是 | serial_no, init_date, branch_no, serial_no, init_date, branch_no |
| uk_rpt_usesstockrevertjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesstockrevertjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_usesstockrevertjour_tolast | ART | 是 | valid_date, valid_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stockrevertjour | serial_no, init_date, branch_no, serial_no, init_date, branch_no |
| idx_stockrevertjour | serial_no, init_date, branch_no, serial_no, init_date, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:49:00 | V3.0.2.106 | taocong45644 | 当前表uses_stock_revert_jour，增加索引（ idx_stockrevertjour_bn:[seri... |
| 2025-12-18 17:12:27 | V3.0.8.31 | 洪略 | 支持分区存储 |
| 2025-12-01 16:52:49 | 3.0.2.104 | taocong45644 | 当前表uses_stock_revert_jour，修改了索引idx_stockrevertjour,索引字段修改为：(... |
| 2025-08-22 17:39:06 | 3.0.2.77 | 洪略 | 唯一索引删除branch_no字段 |
| 2025-05-02 09:40:13 | 3.0.2.2002 | honglue | 索引增加branch_no字段 |
| 2025-02-25 10:08:55 | 3.0.2.2001 | 蒋浩 | 新增表结构 |
| 2026-03-09 14:49:00 | V3.0.2.106 | taocong45644 | 当前表uses_stock_revert_jour，增加索引（ idx_stockrevertjour_bn:[seri... |
| 2025-12-18 17:12:27 | V3.0.8.31 | 洪略 | 支持分区存储 |
| 2025-12-01 16:52:49 | 3.0.2.104 | taocong45644 | 当前表uses_stock_revert_jour，修改了索引idx_stockrevertjour,索引字段修改为：(... |
| 2025-08-22 17:39:06 | 3.0.2.77 | 洪略 | 唯一索引删除branch_no字段 |
| 2025-05-02 09:40:13 | 3.0.2.2002 | honglue | 索引增加branch_no字段 |
| 2025-02-25 10:08:55 | 3.0.2.2001 | 蒋浩 | 新增表结构 |

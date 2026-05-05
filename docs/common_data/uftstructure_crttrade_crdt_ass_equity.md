# crdt_ass_equity - 担保证券权益信息表

**表对象ID**: 7578
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

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
| 15 | stock_type | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | equity_type | 否 |  |  |
| 18 | current_amount | 否 |  |  |
| 19 | recoup_amount | 否 |  |  |
| 20 | recoup_balance | 否 |  |  |
| 21 | register_date | 否 |  |  |
| 22 | divid_date | 否 |  |  |
| 23 | deal_status | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | client_group | 否 | H |  |
| 28 | room_code | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | stock_name | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | curr_date | 否 |  |  |
| 42 | curr_time | 否 |  |  |
| 43 | operator_no | 否 |  |  |
| 44 | op_branch_no | 否 |  |  |
| 45 | op_entrust_way | 否 |  |  |
| 46 | op_station | 否 |  |  |
| 47 | branch_no | 否 |  |  |
| 48 | fund_account | 否 |  |  |
| 49 | client_id | 否 |  |  |
| 50 | stock_account | 否 |  |  |
| 51 | exchange_type | 否 |  |  |
| 52 | stock_code | 否 |  |  |
| 53 | stock_type | 否 |  |  |
| 54 | money_type | 否 |  |  |
| 55 | equity_type | 否 |  |  |
| 56 | current_amount | 否 |  |  |
| 57 | recoup_amount | 否 |  |  |
| 58 | recoup_balance | 否 |  |  |
| 59 | register_date | 否 |  |  |
| 60 | divid_date | 否 |  |  |
| 61 | deal_status | 否 |  |  |
| 62 | date_clear | 否 |  |  |
| 63 | remark | 否 |  |  |
| 64 | position_str | 否 |  |  |
| 65 | client_group | 否 | H |  |
| 66 | room_code | 否 | H |  |
| 67 | asset_prop | 否 | H |  |
| 68 | limit_flag | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | corp_risk_level | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | client_name | 否 | H |  |
| 74 | stock_name | 否 | H |  |
| 75 | client_prop | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_ass_equity_pos | ART | 是 | position_str, position_str |
| idx_crdt_ass_equity | ART | 是 | init_date, position_str, init_date, position_str |
| idx_crdt_ass_equity_acct | ART | 是 | fund_account, fund_account |
| idx_crdt_ass_equity_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtassequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtassequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_crdtassequity_tolast | ART | 是 | date_clear, date_clear |
| idx_crdt_ass_equity_pos | ART | 是 | position_str, position_str |
| idx_crdt_ass_equity | ART | 是 | init_date, position_str, init_date, position_str |
| idx_crdt_ass_equity_acct | ART | 是 | fund_account, fund_account |
| idx_crdt_ass_equity_id | ART | 是 | client_id, client_id |
| uk_rpt_crdtassequity | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtassequity_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_crdtassequity_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_ass_equity_pos | position_str, position_str |
| idx_crdt_ass_equity_pos | position_str, position_str |

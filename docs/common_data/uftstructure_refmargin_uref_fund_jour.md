# uref_fund_jour - 保证金资金流水表

**表对象ID**: 6052
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | report_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | money_type | 否 |  |  |
| 14 | refbusi_code | 否 |  |  |
| 15 | occur_balance | 否 |  |  |
| 16 | post_balance | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | csfc_borrow_accttype | 否 |  |  |
| 20 | client_group | 否 | H |  |
| 21 | room_code | 否 | H |  |
| 22 | asset_prop | 否 | H |  |
| 23 | limit_flag | 否 | H |  |
| 24 | client_prop | 否 | H |  |
| 25 | risk_level | 否 | H |  |
| 26 | corp_client_group | 否 | H |  |
| 27 | asset_level | 否 | H |  |
| 28 | client_name | 否 | H |  |
| 29 | corp_risk_level | 否 | H |  |
| 30 | init_date | 否 |  |  |
| 31 | curr_date | 否 |  |  |
| 32 | curr_time | 否 |  |  |
| 33 | serial_no | 否 |  |  |
| 34 | op_branch_no | 否 |  |  |
| 35 | operator_no | 否 |  |  |
| 36 | op_station | 否 |  |  |
| 37 | company_no | 否 |  |  |
| 38 | report_no | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | money_type | 否 |  |  |
| 43 | refbusi_code | 否 |  |  |
| 44 | occur_balance | 否 |  |  |
| 45 | post_balance | 否 |  |  |
| 46 | remark | 否 |  |  |
| 47 | position_str | 否 |  |  |
| 48 | csfc_borrow_accttype | 否 |  |  |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |
| 51 | asset_prop | 否 | H |  |
| 52 | limit_flag | 否 | H |  |
| 53 | client_prop | 否 | H |  |
| 54 | risk_level | 否 | H |  |
| 55 | corp_client_group | 否 | H |  |
| 56 | asset_level | 否 | H |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_risk_level | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reffundjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reffundjour_id | ART | 是 | client_id, client_id |
| idx_reffundjour_acct | ART | 是 | fund_account, fund_account |
| idx_reffundjour_pos | ART | 是 | position_str, position_str |
| idx_reffundjour | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_reffundjour_id | ART | 是 | client_id, client_id |
| idx_reffundjour_acct | ART | 是 | fund_account, fund_account |
| idx_reffundjour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_reffundjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_ureffundjour | init_date, position_str, init_date, position_str |
| idx_rpt_ureffundjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureffundjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureffundjour_comp | init_date, company_no, position_str, init_date, company_no, position_str |
| idx_reffundjour | serial_no, init_date, serial_no, init_date |
| uk_rpt_ureffundjour | init_date, position_str, init_date, position_str |
| idx_rpt_ureffundjour_id | client_id, position_str, client_id, position_str |
| idx_rpt_ureffundjour_acct | fund_account, position_str, fund_account, position_str |
| idx_rpt_ureffundjour_comp | init_date, company_no, position_str, init_date, company_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 16:02:16 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_fund_jour，添加了表字段(corp_risk_level);
 |
| 2025-10-16 10:34:27 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 16:02:16 | V3.0.2.4 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_fund_jour，添加了表字段(corp_risk_level);
 |
| 2025-10-16 10:34:27 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

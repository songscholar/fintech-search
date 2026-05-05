# usms_qrp_agent_acct_jour - 报价回购代理委托登记流水表(交易管理)

**表对象ID**: 2830
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | open_date | 否 |  |  |
| 15 | qrp_agentacct_status | 否 |  |  |
| 16 | reserve_balance | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | postpone_flag | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | company_no | 否 |  |  |
| 22 | valid_date | 否 |  |  |
| 23 | business_flag | 否 |  |  |
| 24 | qrp_agent_result | 否 |  |  |
| 25 | occur_balance | 否 |  |  |
| 26 | trade_restriction_flag | 否 |  |  |
| 27 | client_name | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | client_prop | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | stock_name | 否 | H |  |
| 37 | stock_type | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | curr_date | 否 |  |  |
| 42 | curr_time | 否 |  |  |
| 43 | op_branch_no | 否 |  |  |
| 44 | operator_no | 否 |  |  |
| 45 | op_station | 否 |  |  |
| 46 | op_entrust_way | 否 |  |  |
| 47 | fund_account | 否 |  |  |
| 48 | client_id | 否 |  |  |
| 49 | branch_no | 否 |  |  |
| 50 | stock_account | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | open_date | 否 |  |  |
| 53 | qrp_agentacct_status | 否 |  |  |
| 54 | reserve_balance | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | postpone_flag | 否 |  |  |
| 57 | position_str | 否 |  |  |
| 58 | exchange_type | 否 |  |  |
| 59 | company_no | 否 |  |  |
| 60 | valid_date | 否 |  |  |
| 61 | business_flag | 否 |  |  |
| 62 | qrp_agent_result | 否 |  |  |
| 63 | occur_balance | 否 |  |  |
| 64 | trade_restriction_flag | 否 |  |  |
| 65 | client_name | 否 | H |  |
| 66 | corp_client_group | 否 | H |  |
| 67 | client_group | 否 | H |  |
| 68 | room_code | 否 | H |  |
| 69 | limit_flag | 否 | H |  |
| 70 | client_prop | 否 | H |  |
| 71 | asset_level | 否 | H |  |
| 72 | risk_level | 否 | H |  |
| 73 | corp_risk_level | 否 | H |  |
| 74 | stock_name | 否 | H |  |
| 75 | stock_type | 否 | H |  |
| 76 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usmsqrpagentacctjour | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usmsqrpagentacctjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usmsqrpagentacctjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_rpt_usmsqrpagentacctjour_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_usmsqrpagentacctjour | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usmsqrpagentacctjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usmsqrpagentacctjour_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_rpt_usmsqrpagentacctjour_id | ART | 是 | client_id, position_str, client_id, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usmsqrpagentacctjour | init_date, serial_no, init_date, serial_no |
| idx_usmsqrpagentacctjour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-07 14:26:00 | 3.0.2.4 | 洪略 | 新增历史表 |
| 2025-04-29 10:39:11 | 3.0.2.2003 | 高志强 | 新增 |
| 2025-11-07 14:26:00 | 3.0.2.4 | 洪略 | 新增历史表 |
| 2025-04-29 10:39:11 | 3.0.2.2003 | 高志强 | 新增 |

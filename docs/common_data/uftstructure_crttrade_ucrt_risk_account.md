# ucrt_risk_account - 风险客户记录表

**表对象ID**: 7570
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | risk_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | begin_assurescale_value | 否 |  |  |
| 7 | assurescale_value | 否 |  |  |
| 8 | risk_deal_type | 否 |  |  |
| 9 | risk_enddate | 否 |  |  |
| 10 | risk_balance | 否 |  |  |
| 11 | asset_balance | 否 |  |  |
| 12 | create_date | 否 |  |  |
| 13 | create_time | 否 |  |  |
| 14 | deal_date | 否 |  |  |
| 15 | deal_time | 否 |  |  |
| 16 | deal_operator_no | 否 |  |  |
| 17 | date_clear | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | position_str | 否 |  | branch_no(5)+fund_account(18)+risk_type(1) |
| 20 | begin_stib_conc_ratio | 否 |  |  |
| 21 | begin_gem_conc_ratio | 否 |  |  |
| 22 | risk_stage | 否 |  |  |
| 23 | assurescale_in | 否 |  |  |
| 24 | assurescale_out | 否 |  |  |
| 25 | risk_change_date | 否 |  |  |
| 26 | append_days | 否 |  |  |
| 27 | payoff_cause | 否 |  |  |
| 28 | risk_begindate | 否 |  |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | risk_type | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | branch_no | 否 |  |  |
| 44 | begin_assurescale_value | 否 |  |  |
| 45 | assurescale_value | 否 |  |  |
| 46 | risk_deal_type | 否 |  |  |
| 47 | risk_enddate | 否 |  |  |
| 48 | risk_balance | 否 |  |  |
| 49 | asset_balance | 否 |  |  |
| 50 | create_date | 否 |  |  |
| 51 | create_time | 否 |  |  |
| 52 | deal_date | 否 |  |  |
| 53 | deal_time | 否 |  |  |
| 54 | deal_operator_no | 否 |  |  |
| 55 | date_clear | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  | branch_no(5)+fund_account(18)+risk_type(1) |
| 58 | begin_stib_conc_ratio | 否 |  |  |
| 59 | begin_gem_conc_ratio | 否 |  |  |
| 60 | risk_stage | 否 |  |  |
| 61 | assurescale_in | 否 |  |  |
| 62 | assurescale_out | 否 |  |  |
| 63 | risk_change_date | 否 |  |  |
| 64 | append_days | 否 |  |  |
| 65 | payoff_cause | 否 |  |  |
| 66 | risk_begindate | 否 |  |  |
| 67 | client_group | 否 | H |  |
| 68 | room_code | 否 | H |  |
| 69 | asset_prop | 否 | H |  |
| 70 | limit_flag | 否 | H |  |
| 71 | risk_level | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | asset_level | 否 | H |  |
| 74 | corp_risk_level | 否 | H |  |
| 75 | client_name | 否 | H |  |
| 76 | client_prop | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_risk_account | 默认 | 否 | fund_account, risk_type, fund_account, risk_type |
| idx_ucrt_risk_account | ART | 是 | fund_account, risk_type, fund_account, risk_type |
| idx_ucrt_risk_account_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_ucrt_risk_account_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_ucrt_risk_account_bra | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| uk_rpt_ucrtriskaccount | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtriskaccount_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_risk_account | 默认 | 否 | fund_account, risk_type, fund_account, risk_type |
| idx_ucrt_risk_account | ART | 是 | fund_account, risk_type, fund_account, risk_type |
| idx_ucrt_risk_account_id | ART | 是 | client_id, position_str, client_id, position_str |
| idx_ucrt_risk_account_acct | ART | 是 | fund_account, position_str, fund_account, position_str |
| idx_ucrt_risk_account_bra | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| uk_rpt_ucrtriskaccount | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtriskaccount_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_risk_account | fund_account, risk_type, fund_account, risk_type |
| idx_ucrt_risk_account | fund_account, risk_type, fund_account, risk_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-26 16:28:32 | 3.0.8.11 | 沈勋 | 当前表ucrt_risk_account，修改了索引idx_ucrt_risk_account,索引字段修改为：(fun... |
| 2025-07-01 10:02:29 | 3.0.2.2007 | 卢杰 | 新增 |
| 2026-01-26 16:28:32 | 3.0.8.11 | 沈勋 | 当前表ucrt_risk_account，修改了索引idx_ucrt_risk_account,索引字段修改为：(fun... |
| 2025-07-01 10:02:29 | 3.0.2.2007 | 卢杰 | 新增 |

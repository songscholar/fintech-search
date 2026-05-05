# settredo_ucrt_risk_account - 清算重做风险客户记录表

**表对象ID**: 7594
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 60 个）

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
| 29 | sett_dml_type | 否 |  |  |
| 30 | sett_batch_no | 否 |  |  |
| 31 | init_date | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | risk_type | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | begin_assurescale_value | 否 |  |  |
| 37 | assurescale_value | 否 |  |  |
| 38 | risk_deal_type | 否 |  |  |
| 39 | risk_enddate | 否 |  |  |
| 40 | risk_balance | 否 |  |  |
| 41 | asset_balance | 否 |  |  |
| 42 | create_date | 否 |  |  |
| 43 | create_time | 否 |  |  |
| 44 | deal_date | 否 |  |  |
| 45 | deal_time | 否 |  |  |
| 46 | deal_operator_no | 否 |  |  |
| 47 | date_clear | 否 |  |  |
| 48 | remark | 否 |  |  |
| 49 | position_str | 否 |  | branch_no(5)+fund_account(18)+risk_type(1) |
| 50 | begin_stib_conc_ratio | 否 |  |  |
| 51 | begin_gem_conc_ratio | 否 |  |  |
| 52 | risk_stage | 否 |  |  |
| 53 | assurescale_in | 否 |  |  |
| 54 | assurescale_out | 否 |  |  |
| 55 | risk_change_date | 否 |  |  |
| 56 | append_days | 否 |  |  |
| 57 | payoff_cause | 否 |  |  |
| 58 | risk_begindate | 否 |  |  |
| 59 | sett_dml_type | 否 |  |  |
| 60 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_ucrt_risk_account | 默认 | 否 | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |
| idx_settredo_ucrt_risk_account | ART | 是 | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |
| idx_settredo_ucrt_risk_account | 默认 | 否 | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |
| idx_settredo_ucrt_risk_account | ART | 是 | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_ucrt_risk_account | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |
| idx_settredo_ucrt_risk_account | sett_batch_no, fund_account, risk_type, sett_batch_no, fund_account, risk_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-26 16:29:59 | 3.0.8.11 | T202601265247 | 当前表settredo_ucrt_risk_account，修改了索引idx_settredo_ucrt_risk_ac... |
| 2025-08-18 16:09:00 | 3.0.2.1 | 曾阳璞 | 新增表 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2026-01-26 16:29:59 | 3.0.8.11 | T202601265247 | 当前表settredo_ucrt_risk_account，修改了索引idx_settredo_ucrt_risk_ac... |
| 2025-08-18 16:09:00 | 3.0.2.1 | 曾阳璞 | 新增表 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

# ucrt_fund_detail_total - 融资融券交易资金明细汇总表

**表对象ID**: 7563
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | business_frozen_balance | 否 |  |  |
| 6 | business_unfrozen_balance | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | branch_no | 否 | H |  |
| 10 | asset_prop | 否 | H |  |
| 11 | limit_flag | 否 | H |  |
| 12 | risk_level | 否 | H |  |
| 13 | corp_client_group | 否 | H |  |
| 14 | corp_risk_level | 否 | H |  |
| 15 | asset_level | 否 | H |  |
| 16 | client_name | 否 | H |  |
| 17 | client_prop | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | init_date | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | money_type | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | business_frozen_balance | 否 |  |  |
| 25 | business_unfrozen_balance | 否 |  |  |
| 26 | fund_enable_level | 否 |  |  |
| 27 | sett_batch_no | 否 |  |  |
| 28 | branch_no | 否 | H |  |
| 29 | asset_prop | 否 | H |  |
| 30 | limit_flag | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | corp_risk_level | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | client_name | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | client_group | 否 | H |  |
| 38 | room_code | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_funddetailtotal | 默认 | 否 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_funddetailtotal | 默认 | 否 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_ucrt_fund_detail_total | 默认 | 否 |  |
| uk_rpt_ucrtfunddetailtotal | 默认 | 否 |  |
| idx_ucrt_fund_detail_total | ART | 是 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| uk_rpt_ucrtfunddetailtotal | ART | 是 | init_date, client_id, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, client_id, fund_account, money_type, fund_enable_level, sett_batch_no |
| idx_funddetailtotal | 默认 | 否 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_funddetailtotal | 默认 | 否 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_ucrt_fund_detail_total | 默认 | 否 |  |
| uk_rpt_ucrtfunddetailtotal | 默认 | 否 |  |
| idx_ucrt_fund_detail_total | ART | 是 | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| uk_rpt_ucrtfunddetailtotal | ART | 是 | init_date, client_id, fund_account, money_type, fund_enable_level, sett_batch_no, init_date, client_id, fund_account, money_type, fund_enable_level, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_funddetailtotal | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |
| idx_funddetailtotal | fund_account, money_type, fund_enable_level, init_date, sett_batch_no, fund_account, money_type, fund_enable_level, init_date, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-10 14:41:38 | 3.0.8.19 | 袁文龙 | 当前表ucrt_fund_detail_total，修改了索引idx_funddetailtotal,索引字段修改为：(... |
| 2025-11-25 09:50:15 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_detail_total，修改了索引idx_funddetailtotal,索引字段修改为：(... |
| 2025-11-25 09:32:44 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_detail_total，修改了索引idx_ucrt_fund_detail_total,索引... |
| 2025-07-27 20:26:28 | V3.0.2.1 | 曾阳璞 | 物理表ucrt_fund_detail_total，添加了表字段(sett_batch_no);
 |
| 2026-02-10 14:41:38 | 3.0.8.19 | 袁文龙 | 当前表ucrt_fund_detail_total，修改了索引idx_funddetailtotal,索引字段修改为：(... |
| 2025-11-25 09:50:15 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_detail_total，修改了索引idx_funddetailtotal,索引字段修改为：(... |
| 2025-11-25 09:32:44 | 3.0.8.11 | 沈勋 | 当前表ucrt_fund_detail_total，修改了索引idx_ucrt_fund_detail_total,索引... |
| 2025-07-27 20:26:28 | V3.0.2.1 | 曾阳璞 | 物理表ucrt_fund_detail_total，添加了表字段(sett_batch_no);
 |

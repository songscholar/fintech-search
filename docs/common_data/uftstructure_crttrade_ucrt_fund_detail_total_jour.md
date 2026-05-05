# ucrt_fund_detail_total_jour - 融资融券交易资金明细汇总流水表

**表对象ID**: 7564
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | business_frozen_balance | 否 |  |  |
| 6 | business_unfrozen_balance | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | serial_no | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | branch_no | 否 | H |  |
| 11 | asset_prop | 否 | H |  |
| 12 | limit_flag | 否 | H |  |
| 13 | risk_level | 否 | H |  |
| 14 | corp_client_group | 否 | H |  |
| 15 | corp_risk_level | 否 | H |  |
| 16 | asset_level | 否 | H |  |
| 17 | client_name | 否 | H |  |
| 18 | client_prop | 否 | H |  |
| 19 | client_group | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | init_date | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | money_type | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | business_frozen_balance | 否 |  |  |
| 26 | business_unfrozen_balance | 否 |  |  |
| 27 | fund_enable_level | 否 |  |  |
| 28 | serial_no | 否 |  |  |
| 29 | sett_batch_no | 否 |  |  |
| 30 | branch_no | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | risk_level | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | asset_level | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | client_prop | 否 | H |  |
| 39 | client_group | 否 | H |  |
| 40 | room_code | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_detail_total_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_ucrtfunddetailtotaljour | ART | 是 | init_date, client_id, fund_account, serial_no, init_date, client_id, fund_account, serial_no |
| idx_ucrt_fund_detail_total_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| uk_rpt_ucrtfunddetailtotaljour | ART | 是 | init_date, client_id, fund_account, serial_no, init_date, client_id, fund_account, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_funddetailtotaljour | init_date, serial_no, init_date, serial_no |
| idx_funddetailtotaljour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-27 20:26:28 | V3.0.2.1 | 曾阳璞 | 物理表ucrt_fund_detail_total_jour，添加了表字段(sett_batch_no);
 |
| 2025-07-27 20:26:28 | V3.0.2.1 | 曾阳璞 | 物理表ucrt_fund_detail_total_jour，添加了表字段(sett_batch_no);
 |

# ucrt_pend_fare - 待扣收表

**表对象ID**: 7520
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 76 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | pendfare_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | compact_id | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | orig_end_date | 否 |  |  |
| 12 | pendfare_type | 否 |  |  |
| 13 | pend_fare | 否 |  |  |
| 14 | total_pend_fare | 否 |  |  |
| 15 | pend_trans_flag | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | cashgroup_no | 否 |  |  |
| 19 | compact_rate | 否 |  |  |
| 20 | satisfied_discount_flag | 否 |  |  |
| 21 | cashcompact_id | 否 |  |  |
| 22 | frozen_balance | 否 |  |  |
| 23 | interest_settle_date | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+partition_no(2)+serial_no(10) |
| 25 | branch_no | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | asset_prop | 否 | H |  |
| 29 | limit_flag | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | client_name | 否 | H |  |
| 35 | tohis_date | 否 | H |  |
| 36 | client_prop | 否 | H |  |
| 37 | sub_stock_type | 否 | H |  |
| 38 | stock_name | 否 | H |  |
| 39 | init_date | 否 |  |  |
| 40 | pendfare_id | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | fund_account | 否 |  |  |
| 43 | exchange_type | 否 |  |  |
| 44 | stock_account | 否 |  |  |
| 45 | stock_type | 否 |  |  |
| 46 | stock_code | 否 |  |  |
| 47 | compact_id | 否 |  |  |
| 48 | money_type | 否 |  |  |
| 49 | orig_end_date | 否 |  |  |
| 50 | pendfare_type | 否 |  |  |
| 51 | pend_fare | 否 |  |  |
| 52 | total_pend_fare | 否 |  |  |
| 53 | pend_trans_flag | 否 |  |  |
| 54 | date_clear | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | cashgroup_no | 否 |  |  |
| 57 | compact_rate | 否 |  |  |
| 58 | satisfied_discount_flag | 否 |  |  |
| 59 | cashcompact_id | 否 |  |  |
| 60 | frozen_balance | 否 |  |  |
| 61 | interest_settle_date | 否 |  |  |
| 62 | position_str | 否 |  | init_date(8)+partition_no(2)+serial_no(10) |
| 63 | branch_no | 否 | H |  |
| 64 | client_group | 否 | H |  |
| 65 | room_code | 否 | H |  |
| 66 | asset_prop | 否 | H |  |
| 67 | limit_flag | 否 | H |  |
| 68 | risk_level | 否 | H |  |
| 69 | corp_client_group | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |
| 71 | asset_level | 否 | H |  |
| 72 | client_name | 否 | H |  |
| 73 | tohis_date | 否 | H |  |
| 74 | client_prop | 否 | H |  |
| 75 | sub_stock_type | 否 | H |  |
| 76 | stock_name | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_pend_fare | ART | 是 | fund_account, pendfare_id, fund_account, pendfare_id |
| idx_ucrt_pend_fare_unique | ART | 是 | pendfare_id, pendfare_id |
| idx_ucrt_pend_fare_orig | ART | 是 | fund_account, orig_end_date, pendfare_id, fund_account, orig_end_date, pendfare_id |
| uk_rpt_ucrtpendfare | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_rpt_ucrtpendfare_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |
| idx_ucrt_pend_fare | ART | 是 | fund_account, pendfare_id, fund_account, pendfare_id |
| idx_ucrt_pend_fare_unique | ART | 是 | pendfare_id, pendfare_id |
| idx_ucrt_pend_fare_orig | ART | 是 | fund_account, orig_end_date, pendfare_id, fund_account, orig_end_date, pendfare_id |
| uk_rpt_ucrtpendfare | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_rpt_ucrtpendfare_cid | ART | 是 | tohis_date, client_id, fund_account, position_str, tohis_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_pend_fare_unique | pendfare_id, pendfare_id |
| idx_ucrt_pend_fare_unique | pendfare_id, pendfare_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-04-02 14:02:36 | 3.0.2.2001 | 卢杰 | 物理表ucrt_pend_fare，添加了表字段(interest_settle_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-11 13:36 | 0.3.3.124 | 董瑞辉 | 新增表字段frozen_balance |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2025-04-02 14:02:36 | 3.0.2.2001 | 卢杰 | 物理表ucrt_pend_fare，添加了表字段(interest_settle_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-11 13:36 | 0.3.3.124 | 董瑞辉 | 新增表字段frozen_balance |

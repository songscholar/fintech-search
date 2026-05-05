# ucrt_uncompact - 未完成合约表

**表对象ID**: 7523
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compact_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | uncompact_type | 否 |  |  |
| 4 | date_clear | 否 |  |  |
| 5 | deal_date | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | compact_type | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | cashgroup_no | 否 |  |  |
| 12 | interest_date | 否 |  |  |
| 13 | compact_integral | 否 |  |  |
| 14 | fine_integral | 否 |  |  |
| 15 | compact_interest | 否 |  |  |
| 16 | repaid_interest | 否 |  |  |
| 17 | year_rate | 否 |  |  |
| 18 | occur_interest | 否 |  |  |
| 19 | occur_frozen_interest | 否 |  |  |
| 20 | ret_end_date | 否 |  |  |
| 21 | compact_postpone_status | 否 |  |  |
| 22 | compact_postpone_times | 否 |  |  |
| 23 | crdt_fare_str | 否 |  |  |
| 24 | compact_status | 否 |  |  |
| 25 | real_status | 否 |  |  |
| 26 | compact_fine_settlement | 否 |  |  |
| 27 | occur_fine_interest | 否 |  |  |
| 28 | fine_rate | 否 |  |  |
| 29 | primerate_flag | 否 |  |  |
| 30 | followdate_flag | 否 |  |  |
| 31 | branch_no | 否 | H |  |
| 32 | client_id | 否 | H |  |
| 33 | client_group | 否 | H |  |
| 34 | room_code | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | risk_level | 否 | H |  |
| 38 | corp_client_group | 否 | H |  |
| 39 | corp_risk_level | 否 | H |  |
| 40 | asset_level | 否 | H |  |
| 41 | client_name | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | compact_id | 否 |  |  |
| 44 | fund_account | 否 |  |  |
| 45 | uncompact_type | 否 |  |  |
| 46 | date_clear | 否 |  |  |
| 47 | deal_date | 否 |  |  |
| 48 | init_date | 否 |  |  |
| 49 | compact_type | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | cashgroup_no | 否 |  |  |
| 54 | interest_date | 否 |  |  |
| 55 | compact_integral | 否 |  |  |
| 56 | fine_integral | 否 |  |  |
| 57 | compact_interest | 否 |  |  |
| 58 | repaid_interest | 否 |  |  |
| 59 | year_rate | 否 |  |  |
| 60 | occur_interest | 否 |  |  |
| 61 | occur_frozen_interest | 否 |  |  |
| 62 | ret_end_date | 否 |  |  |
| 63 | compact_postpone_status | 否 |  |  |
| 64 | compact_postpone_times | 否 |  |  |
| 65 | crdt_fare_str | 否 |  |  |
| 66 | compact_status | 否 |  |  |
| 67 | real_status | 否 |  |  |
| 68 | compact_fine_settlement | 否 |  |  |
| 69 | occur_fine_interest | 否 |  |  |
| 70 | fine_rate | 否 |  |  |
| 71 | primerate_flag | 否 |  |  |
| 72 | followdate_flag | 否 |  |  |
| 73 | branch_no | 否 | H |  |
| 74 | client_id | 否 | H |  |
| 75 | client_group | 否 | H |  |
| 76 | room_code | 否 | H |  |
| 77 | asset_prop | 否 | H |  |
| 78 | limit_flag | 否 | H |  |
| 79 | risk_level | 否 | H |  |
| 80 | corp_client_group | 否 | H |  |
| 81 | corp_risk_level | 否 | H |  |
| 82 | asset_level | 否 | H |  |
| 83 | client_name | 否 | H |  |
| 84 | client_prop | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_uncompact | 默认 | 否 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_ucrt_uncompact | 默认 | 否 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_ucrt_uncompact | 默认 | 否 |  |
| idx_ucrt_uncompact_type | ART | 是 | fund_account, uncompact_type, fund_account, uncompact_type |
| idx_ucrt_uncompact | ART | 是 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| uk_rpt_ucrtuncompact | ART | 是 | date_clear, deal_date, compact_id, uncompact_type, date_clear, deal_date, compact_id, uncompact_type |
| idx_ucrt_uncompact | 默认 | 否 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_ucrt_uncompact | 默认 | 否 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_ucrt_uncompact | 默认 | 否 |  |
| idx_ucrt_uncompact_type | ART | 是 | fund_account, uncompact_type, fund_account, uncompact_type |
| idx_ucrt_uncompact | ART | 是 | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| uk_rpt_ucrtuncompact | ART | 是 | date_clear, deal_date, compact_id, uncompact_type, date_clear, deal_date, compact_id, uncompact_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_uncompact | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |
| idx_ucrt_uncompact | compact_id, uncompact_type, deal_date, compact_id, uncompact_type, deal_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_uncompact，添加了表字段(followdate_flag);
 |
| 2025-08-02 16:01:18 | 3.0.2.2 | 曾阳璞 | 物理表ucrt_uncompact，添加了表字段(init_date);
物理表ucrt_uncompact，添加了表... |
| 2025-08-01 10:12:02 | 3.0.2.1 | 曾阳璞 | 内存表ucrt_uncompact，增加索引(idx_ucrt_uncompact:[compact_id,uncomp... |
| 2024-10-21 10:51:46 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，增加索引(idx_ucrt_uncompact:[compact_id,uncomp... |
| 2024-10-21 10:50:59 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，删除了表索引(idx_ucrt_uncompact);
 |
| 2024-10-21 10:50:19 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，添加了表字段(deal_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_uncompact，添加了表字段(followdate_flag);
 |
| 2025-08-02 16:01:18 | 3.0.2.2 | 曾阳璞 | 物理表ucrt_uncompact，添加了表字段(init_date);
物理表ucrt_uncompact，添加了表... |
| 2025-08-01 10:12:02 | 3.0.2.1 | 曾阳璞 | 内存表ucrt_uncompact，增加索引(idx_ucrt_uncompact:[compact_id,uncomp... |
| 2024-10-21 10:51:46 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，增加索引(idx_ucrt_uncompact:[compact_id,uncomp... |
| 2024-10-21 10:50:59 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，删除了表索引(idx_ucrt_uncompact);
 |
| 2024-10-21 10:50:19 | 3.0.6.9 | 汪杰 | 物理表ucrt_uncompact，添加了表字段(deal_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

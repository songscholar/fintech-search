# settredo_ucrt_uncompact - 日终清算未完成合约表

**表对象ID**: 7585
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compact_id | 否 |  |  |
| 2 | uncompact_type | 否 |  |  |
| 3 | deal_date | 否 |  |  |
| 4 | date_clear | 否 |  |  |
| 5 | interest_date | 否 |  |  |
| 6 | compact_integral | 否 |  |  |
| 7 | fine_integral | 否 |  |  |
| 8 | compact_interest | 否 |  |  |
| 9 | repaid_interest | 否 |  |  |
| 10 | year_rate | 否 |  |  |
| 11 | occur_interest | 否 |  |  |
| 12 | occur_frozen_interest | 否 |  |  |
| 13 | ret_end_date | 否 |  |  |
| 14 | compact_postpone_status | 否 |  |  |
| 15 | compact_postpone_times | 否 |  |  |
| 16 | crdt_fare_str | 否 |  |  |
| 17 | compact_status | 否 |  |  |
| 18 | real_status | 否 |  |  |
| 19 | sett_dml_type | 否 |  |  |
| 20 | sett_batch_no | 否 |  |  |
| 21 | compact_id | 否 |  |  |
| 22 | uncompact_type | 否 |  |  |
| 23 | deal_date | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | interest_date | 否 |  |  |
| 26 | compact_integral | 否 |  |  |
| 27 | fine_integral | 否 |  |  |
| 28 | compact_interest | 否 |  |  |
| 29 | repaid_interest | 否 |  |  |
| 30 | year_rate | 否 |  |  |
| 31 | occur_interest | 否 |  |  |
| 32 | occur_frozen_interest | 否 |  |  |
| 33 | ret_end_date | 否 |  |  |
| 34 | compact_postpone_status | 否 |  |  |
| 35 | compact_postpone_times | 否 |  |  |
| 36 | crdt_fare_str | 否 |  |  |
| 37 | compact_status | 否 |  |  |
| 38 | real_status | 否 |  |  |
| 39 | sett_dml_type | 否 |  |  |
| 40 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_uncompact | ART | 是 | compact_id, uncompact_type, deal_date, sett_batch_no, compact_id, uncompact_type, deal_date, sett_batch_no |
| idx_strd_ucrt_uncompact | ART | 是 | compact_id, uncompact_type, deal_date, sett_batch_no, compact_id, uncompact_type, deal_date, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_uncompact | compact_id, uncompact_type, deal_date, sett_batch_no, compact_id, uncompact_type, deal_date, sett_batch_no |
| idx_strd_ucrt_uncompact | compact_id, uncompact_type, deal_date, sett_batch_no, compact_id, uncompact_type, deal_date, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |

# settredo_ucrt_compact - 日终清算合约表

**表对象ID**: 7584
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 94 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compact_id | 否 |  |  |
| 2 | sett_dml_type | 否 |  |  |
| 3 | sett_batch_no | 否 |  |  |
| 4 | begin_compact_balance | 否 |  |  |
| 5 | begin_compact_amount | 否 |  |  |
| 6 | begin_compact_fare | 否 |  |  |
| 7 | compact_balance | 否 |  |  |
| 8 | compact_amount | 否 |  |  |
| 9 | compact_fare | 否 |  |  |
| 10 | business_balance | 否 |  |  |
| 11 | business_price | 否 |  |  |
| 12 | business_amount | 否 |  |  |
| 13 | business_fare | 否 |  |  |
| 14 | compact_interest | 否 |  |  |
| 15 | repaid_interest | 否 |  |  |
| 16 | frozen_interest | 否 |  |  |
| 17 | repaid_fine_interest | 否 |  |  |
| 18 | compact_integral | 否 |  |  |
| 19 | fine_integral | 否 |  |  |
| 20 | compact_fine_settlement | 否 |  |  |
| 21 | year_rate | 否 |  |  |
| 22 | crdt_ratio | 否 |  |  |
| 23 | interest_date | 否 |  |  |
| 24 | ret_end_date | 否 |  |  |
| 25 | fine_begin_date | 否 |  |  |
| 26 | real_compact_balance | 否 |  |  |
| 27 | real_compact_amount | 否 |  |  |
| 28 | real_compact_interest | 否 |  |  |
| 29 | real_compact_fare | 否 |  |  |
| 30 | real_occuped_balance | 否 |  |  |
| 31 | real_occuped_amount | 否 |  |  |
| 32 | compact_type | 否 |  |  |
| 33 | compact_status | 否 |  |  |
| 34 | date_clear | 否 |  |  |
| 35 | compact_postpone_status | 否 |  |  |
| 36 | compact_postpone_times | 否 |  |  |
| 37 | repaycost_balance | 否 |  |  |
| 38 | primerate_flag | 否 |  |  |
| 39 | real_repaycost_balance | 否 |  |  |
| 40 | orig_end_date | 否 |  |  |
| 41 | slo_compact_end_date | 否 |  |  |
| 42 | interest_settle_date | 否 |  |  |
| 43 | repaid_date | 否 |  |  |
| 44 | prev_end_date | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | back_date | 否 |  |  |
| 47 | crdt_fare_str | 是 |  |  |
| 48 | compact_id | 否 |  |  |
| 49 | sett_dml_type | 否 |  |  |
| 50 | sett_batch_no | 否 |  |  |
| 51 | begin_compact_balance | 否 |  |  |
| 52 | begin_compact_amount | 否 |  |  |
| 53 | begin_compact_fare | 否 |  |  |
| 54 | compact_balance | 否 |  |  |
| 55 | compact_amount | 否 |  |  |
| 56 | compact_fare | 否 |  |  |
| 57 | business_balance | 否 |  |  |
| 58 | business_price | 否 |  |  |
| 59 | business_amount | 否 |  |  |
| 60 | business_fare | 否 |  |  |
| 61 | compact_interest | 否 |  |  |
| 62 | repaid_interest | 否 |  |  |
| 63 | frozen_interest | 否 |  |  |
| 64 | repaid_fine_interest | 否 |  |  |
| 65 | compact_integral | 否 |  |  |
| 66 | fine_integral | 否 |  |  |
| 67 | compact_fine_settlement | 否 |  |  |
| 68 | year_rate | 否 |  |  |
| 69 | crdt_ratio | 否 |  |  |
| 70 | interest_date | 否 |  |  |
| 71 | ret_end_date | 否 |  |  |
| 72 | fine_begin_date | 否 |  |  |
| 73 | real_compact_balance | 否 |  |  |
| 74 | real_compact_amount | 否 |  |  |
| 75 | real_compact_interest | 否 |  |  |
| 76 | real_compact_fare | 否 |  |  |
| 77 | real_occuped_balance | 否 |  |  |
| 78 | real_occuped_amount | 否 |  |  |
| 79 | compact_type | 否 |  |  |
| 80 | compact_status | 否 |  |  |
| 81 | date_clear | 否 |  |  |
| 82 | compact_postpone_status | 否 |  |  |
| 83 | compact_postpone_times | 否 |  |  |
| 84 | repaycost_balance | 否 |  |  |
| 85 | primerate_flag | 否 |  |  |
| 86 | real_repaycost_balance | 否 |  |  |
| 87 | orig_end_date | 否 |  |  |
| 88 | slo_compact_end_date | 否 |  |  |
| 89 | interest_settle_date | 否 |  |  |
| 90 | repaid_date | 否 |  |  |
| 91 | prev_end_date | 否 |  |  |
| 92 | remark | 否 |  |  |
| 93 | back_date | 否 |  |  |
| 94 | crdt_fare_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_compact | ART | 是 | compact_id, sett_batch_no, compact_id, sett_batch_no |
| idx_strd_ucrt_compact | ART | 是 | compact_id, sett_batch_no, compact_id, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_compact | compact_id, sett_batch_no, compact_id, sett_batch_no |
| idx_strd_ucrt_compact | compact_id, sett_batch_no, compact_id, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-23 15:33:38 | 3.0.8.19 | 沈勋 | 所有表settredo_ucrt_compact，添加了表字段(crdt_fare_str);
 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2026-03-23 15:33:38 | 3.0.8.19 | 沈勋 | 所有表settredo_ucrt_compact，添加了表字段(crdt_fare_str);
 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |

# uref_borrower_info - 借入人综合信息表

**表对象ID**: 6057
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | report_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | refbusi_code | 否 |  |  |
| 6 | csfc_borrow_account | 否 |  |  |
| 7 | min_refscale_ratio | 否 |  |  |
| 8 | min_refcash_ratio | 否 |  |  |
| 9 | refdraw_ratio | 否 |  |  |
| 10 | ref_value | 否 |  |  |
| 11 | reffund_value | 否 |  |  |
| 12 | refstock_value | 否 |  |  |
| 13 | refcompact_value | 否 |  |  |
| 14 | refscale_ratio | 否 |  |  |
| 15 | refcash_ratio | 否 |  |  |
| 16 | max_reffetch_bail | 否 |  |  |
| 17 | max_reffetch_balance | 否 |  |  |
| 18 | remind_ref_value | 否 |  |  |
| 19 | remind_reffund_value | 否 |  |  |
| 20 | day_borrow_balance | 否 |  |  |
| 21 | deal_time | 否 |  |  |
| 22 | return_code | 否 |  |  |
| 23 | return_info | 否 |  |  |
| 24 | init_date | 否 |  |  |
| 25 | report_no | 否 |  |  |
| 26 | curr_date | 否 |  |  |
| 27 | curr_time | 否 |  |  |
| 28 | refbusi_code | 否 |  |  |
| 29 | csfc_borrow_account | 否 |  |  |
| 30 | min_refscale_ratio | 否 |  |  |
| 31 | min_refcash_ratio | 否 |  |  |
| 32 | refdraw_ratio | 否 |  |  |
| 33 | ref_value | 否 |  |  |
| 34 | reffund_value | 否 |  |  |
| 35 | refstock_value | 否 |  |  |
| 36 | refcompact_value | 否 |  |  |
| 37 | refscale_ratio | 否 |  |  |
| 38 | refcash_ratio | 否 |  |  |
| 39 | max_reffetch_bail | 否 |  |  |
| 40 | max_reffetch_balance | 否 |  |  |
| 41 | remind_ref_value | 否 |  |  |
| 42 | remind_reffund_value | 否 |  |  |
| 43 | day_borrow_balance | 否 |  |  |
| 44 | deal_time | 否 |  |  |
| 45 | return_code | 否 |  |  |
| 46 | return_info | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refborrowerinfo | ART | 是 | report_no, init_date, report_no, init_date |
| idx_refborrowerinfo | ART | 是 | report_no, init_date, report_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refborrowerinfo | report_no, init_date, report_no, init_date |
| idx_refborrowerinfo | report_no, init_date, report_no, init_date |

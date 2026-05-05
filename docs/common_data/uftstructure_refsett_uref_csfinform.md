# uref_csfinform - 转融通交收通知信息表

**表对象ID**: 6162
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | refacct_type | 否 |  |  |
| 4 | js_date | 否 |  |  |
| 5 | csfc_compact_id | 否 |  |  |
| 6 | refcompact_type | 否 |  |  |
| 7 | ref_type | 否 |  |  |
| 8 | refsett_bs | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | settle_amount | 否 |  |  |
| 14 | clear_balance | 否 |  |  |
| 15 | principal | 否 |  |  |
| 16 | interest | 否 |  |  |
| 17 | pre_fine | 否 |  |  |
| 18 | penalty_balance | 否 |  |  |
| 19 | other_fare | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | csfc_borrow_accttype | 否 |  |  |
| 22 | position_str | 否 |  | refacct_type(1)+company_no(10)+csfc_compact_id(32)+init_date |
| 23 | stock_name | 否 | H |  |
| 24 | stock_type | 否 | H |  |
| 25 | sub_stock_type | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | company_no | 否 |  |  |
| 28 | refacct_type | 否 |  |  |
| 29 | js_date | 否 |  |  |
| 30 | csfc_compact_id | 否 |  |  |
| 31 | refcompact_type | 否 |  |  |
| 32 | ref_type | 否 |  |  |
| 33 | refsett_bs | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_account | 否 |  |  |
| 36 | seat_no | 否 |  |  |
| 37 | stock_code | 否 |  |  |
| 38 | settle_amount | 否 |  |  |
| 39 | clear_balance | 否 |  |  |
| 40 | principal | 否 |  |  |
| 41 | interest | 否 |  |  |
| 42 | pre_fine | 否 |  |  |
| 43 | penalty_balance | 否 |  |  |
| 44 | other_fare | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | csfc_borrow_accttype | 否 |  |  |
| 47 | position_str | 否 |  | refacct_type(1)+company_no(10)+csfc_compact_id(32)+init_date |
| 48 | stock_name | 否 | H |  |
| 49 | stock_type | 否 | H |  |
| 50 | sub_stock_type | 否 | H |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcsfinform | ART | 是 | refacct_type, csfc_compact_id, company_no, init_date, refacct_type, csfc_compact_id, company_no, init_date |
| idx_refcsfinform | ART | 是 | refacct_type, csfc_compact_id, company_no, init_date, refacct_type, csfc_compact_id, company_no, init_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcsfinform | refacct_type, csfc_compact_id, company_no, init_date, refacct_type, csfc_compact_id, company_no, init_date |
| uk_rpt_urefcsfinform | init_date, position_str, init_date, position_str |
| idx_refcsfinform | refacct_type, csfc_compact_id, company_no, init_date, refacct_type, csfc_compact_id, company_no, init_date |
| uk_rpt_urefcsfinform | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:39:09 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:39:09 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

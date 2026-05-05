# uref_refpreend - 转融通提前了结结果通知表

**表对象ID**: 6167
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 64 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | ref_type | 否 |  |  |
| 4 | ref_bs | 否 |  |  |
| 5 | compact_id | 否 |  |  |
| 6 | result_compact_id | 否 |  |  |
| 7 | csfc_compact_id | 否 |  |  |
| 8 | oppcsfc_compact_id | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | report_date | 否 |  |  |
| 14 | report_no | 否 |  |  |
| 15 | compact_balance | 否 |  |  |
| 16 | compact_amount | 否 |  |  |
| 17 | ref_term | 否 |  |  |
| 18 | refbase_rate | 否 |  |  |
| 19 | report_balance | 否 |  |  |
| 20 | report_amount | 否 |  |  |
| 21 | business_balance | 否 |  |  |
| 22 | business_amount | 否 |  |  |
| 23 | valid_date | 否 |  |  |
| 24 | cbpconfer_id | 否 |  |  |
| 25 | preend_status | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | treat_date | 否 |  |  |
| 28 | csfc_borrow_accttype | 否 |  |  |
| 29 | position_str | 否 |  |  |
| 30 | stock_name | 否 | H |  |
| 31 | stock_type | 否 | H |  |
| 32 | sub_stock_type | 否 | H |  |
| 33 | init_date | 否 |  |  |
| 34 | company_no | 否 |  |  |
| 35 | ref_type | 否 |  |  |
| 36 | ref_bs | 否 |  |  |
| 37 | compact_id | 否 |  |  |
| 38 | result_compact_id | 否 |  |  |
| 39 | csfc_compact_id | 否 |  |  |
| 40 | oppcsfc_compact_id | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | seat_no | 否 |  |  |
| 45 | report_date | 否 |  |  |
| 46 | report_no | 否 |  |  |
| 47 | compact_balance | 否 |  |  |
| 48 | compact_amount | 否 |  |  |
| 49 | ref_term | 否 |  |  |
| 50 | refbase_rate | 否 |  |  |
| 51 | report_balance | 否 |  |  |
| 52 | report_amount | 否 |  |  |
| 53 | business_balance | 否 |  |  |
| 54 | business_amount | 否 |  |  |
| 55 | valid_date | 否 |  |  |
| 56 | cbpconfer_id | 否 |  |  |
| 57 | preend_status | 否 |  |  |
| 58 | remark | 否 |  |  |
| 59 | treat_date | 否 |  |  |
| 60 | csfc_borrow_accttype | 否 |  |  |
| 61 | position_str | 否 |  |  |
| 62 | stock_name | 否 | H |  |
| 63 | stock_type | 否 | H |  |
| 64 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refpreend | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpreend_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_refpreend | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpreend_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refpreend | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpreend_code | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_urefpreend | init_date, position_str, init_date, position_str |
| idx_refpreend | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpreend_code | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_urefpreend | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:39:44 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:39:44 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

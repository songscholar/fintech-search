# uref_refpostpone - 转融通展期结果通知表

**表对象ID**: 6163
**所属模块**: refsett
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | ref_type | 否 |  |  |
| 4 | ref_bs | 否 |  |  |
| 5 | compact_id | 否 |  |  |
| 6 | csfc_compact_id | 否 |  |  |
| 7 | oppcsfc_compact_id | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | report_date | 否 |  |  |
| 13 | report_no | 否 |  |  |
| 14 | compact_balance | 否 |  |  |
| 15 | compact_amount | 否 |  |  |
| 16 | ref_term | 否 |  |  |
| 17 | report_balance | 否 |  |  |
| 18 | report_amount | 否 |  |  |
| 19 | business_balance | 否 |  |  |
| 20 | business_amount | 否 |  |  |
| 21 | valid_date | 否 |  |  |
| 22 | cbpconfer_id | 否 |  |  |
| 23 | postpone_status | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | treat_date | 否 |  |  |
| 26 | refconfirm_rate | 否 |  |  |
| 27 | csfc_borrow_accttype | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8) + serial_no(10) |
| 29 | stock_name | 否 | H |  |
| 30 | stock_type | 否 | H |  |
| 31 | sub_stock_type | 否 | H |  |
| 32 | init_date | 否 |  |  |
| 33 | company_no | 否 |  |  |
| 34 | ref_type | 否 |  |  |
| 35 | ref_bs | 否 |  |  |
| 36 | compact_id | 否 |  |  |
| 37 | csfc_compact_id | 否 |  |  |
| 38 | oppcsfc_compact_id | 否 |  |  |
| 39 | exchange_type | 否 |  |  |
| 40 | stock_code | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | seat_no | 否 |  |  |
| 43 | report_date | 否 |  |  |
| 44 | report_no | 否 |  |  |
| 45 | compact_balance | 否 |  |  |
| 46 | compact_amount | 否 |  |  |
| 47 | ref_term | 否 |  |  |
| 48 | report_balance | 否 |  |  |
| 49 | report_amount | 否 |  |  |
| 50 | business_balance | 否 |  |  |
| 51 | business_amount | 否 |  |  |
| 52 | valid_date | 否 |  |  |
| 53 | cbpconfer_id | 否 |  |  |
| 54 | postpone_status | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | treat_date | 否 |  |  |
| 57 | refconfirm_rate | 否 |  |  |
| 58 | csfc_borrow_accttype | 否 |  |  |
| 59 | position_str | 否 |  | init_date(8) + serial_no(10) |
| 60 | stock_name | 否 | H |  |
| 61 | stock_type | 否 | H |  |
| 62 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refpostpone | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpostpone_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_refpostpone | ART | 是 | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpostpone_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_refpostpone | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpostpone_code | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_urefpostpone | init_date, position_str, init_date, position_str |
| idx_refpostpone | csfc_compact_id, company_no, csfc_compact_id, company_no |
| idx_refpostpone_code | stock_code, exchange_type, stock_code, exchange_type |
| uk_rpt_urefpostpone | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:39:26 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:39:26 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

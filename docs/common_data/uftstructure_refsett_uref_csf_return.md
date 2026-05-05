# uref_csf_return - 转融通合约偿还明细

**表对象ID**: 6164
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | company_no | 否 |  |  |
| 4 | refacct_type | 否 |  |  |
| 5 | csfc_compact_id | 否 |  |  |
| 6 | refcompact_type | 否 |  |  |
| 7 | ref_type | 否 |  |  |
| 8 | refsett_bs | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | return_amount | 否 |  |  |
| 14 | return_balance | 否 |  |  |
| 15 | return_principal | 否 |  |  |
| 16 | return_interest | 否 |  |  |
| 17 | return_fine | 否 |  |  |
| 18 | return_penalty | 否 |  |  |
| 19 | return_fare | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | csfc_borrow_accttype | 否 |  |  |
| 22 | init_date | 否 |  |  |
| 23 | serial_no | 否 |  |  |
| 24 | company_no | 否 |  |  |
| 25 | refacct_type | 否 |  |  |
| 26 | csfc_compact_id | 否 |  |  |
| 27 | refcompact_type | 否 |  |  |
| 28 | ref_type | 否 |  |  |
| 29 | refsett_bs | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | seat_no | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | return_amount | 否 |  |  |
| 35 | return_balance | 否 |  |  |
| 36 | return_principal | 否 |  |  |
| 37 | return_interest | 否 |  |  |
| 38 | return_fine | 否 |  |  |
| 39 | return_penalty | 否 |  |  |
| 40 | return_fare | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refcsfreturn | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refcsfreturn | ART | 是 | init_date, serial_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refcsfreturn | init_date, serial_no, init_date, serial_no |
| idx_refcsfreturn | init_date, serial_no, init_date, serial_no |

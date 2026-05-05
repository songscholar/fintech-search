# uref_csf_zrtchhfcc - 转融通合约偿还划付差错

**表对象ID**: 6166
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | orig_entrust_date | 否 |  |  |
| 5 | original_serial_no | 否 |  |  |
| 6 | csfc_compact_id | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stkcode_status | 否 |  |  |
| 10 | datasrc_type | 否 |  |  |
| 11 | occur_balance | 否 |  |  |
| 12 | occur_amount | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | csfc_borrow_accttype | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | company_no | 否 |  |  |
| 17 | serial_no | 否 |  |  |
| 18 | orig_entrust_date | 否 |  |  |
| 19 | original_serial_no | 否 |  |  |
| 20 | csfc_compact_id | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stkcode_status | 否 |  |  |
| 24 | datasrc_type | 否 |  |  |
| 25 | occur_balance | 否 |  |  |
| 26 | occur_amount | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | csfc_borrow_accttype | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_intercsfzrtchhfcc | ART | 是 | company_no, serial_no, company_no, serial_no |
| idx_intercsfzrtchhfcc | ART | 是 | company_no, serial_no, company_no, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_intercsfzrtchhfcc | company_no, serial_no, company_no, serial_no |
| idx_intercsfzrtchhfcc | company_no, serial_no, company_no, serial_no |

# ref_ierisk_info - 风控指标信息表

**表对象ID**: 6216
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | csfc_parti_type | 否 |  |  |
| 3 | csfc_borrow_accttype | 否 |  |  |
| 4 | csfc_organ_code | 否 |  |  |
| 5 | csfc_borrower_code | 否 |  |  |
| 6 | ie_risk_level | 否 |  |  |
| 7 | day_max_bquota | 否 |  |  |
| 8 | surplus_bquota | 否 |  |  |
| 9 | report_no | 否 |  |  |
| 10 | report_status | 否 |  |  |
| 11 | return_code | 否 |  |  |
| 12 | return_info | 否 |  |  |
| 13 | company_no | 否 |  |  |
| 14 | csfc_parti_type | 否 |  |  |
| 15 | csfc_borrow_accttype | 否 |  |  |
| 16 | csfc_organ_code | 否 |  |  |
| 17 | csfc_borrower_code | 否 |  |  |
| 18 | ie_risk_level | 否 |  |  |
| 19 | day_max_bquota | 否 |  |  |
| 20 | surplus_bquota | 否 |  |  |
| 21 | report_no | 否 |  |  |
| 22 | report_status | 否 |  |  |
| 23 | return_code | 否 |  |  |
| 24 | return_info | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_ierisk_info | ART | 是 | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |
| idx_ref_ierisk_info | ART | 是 | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_ierisk_info | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |
| idx_ref_ierisk_info | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |

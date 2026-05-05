# ref_ieblack_info - 黑名单信息表

**表对象ID**: 6218
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | csfc_parti_type | 否 |  |  |
| 3 | csfc_borrow_accttype | 否 |  |  |
| 4 | csfc_organ_code | 否 |  |  |
| 5 | csfc_borrower_code | 否 |  |  |
| 6 | opp_organ_code | 否 |  |  |
| 7 | opp_organ_name | 否 |  |  |
| 8 | opp_borrower_code | 否 |  |  |
| 9 | opp_borrower_name | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | report_no | 否 |  |  |
| 12 | report_status | 否 |  |  |
| 13 | return_code | 否 |  |  |
| 14 | return_info | 否 |  |  |
| 15 | company_no | 否 |  |  |
| 16 | csfc_parti_type | 否 |  |  |
| 17 | csfc_borrow_accttype | 否 |  |  |
| 18 | csfc_organ_code | 否 |  |  |
| 19 | csfc_borrower_code | 否 |  |  |
| 20 | opp_organ_code | 否 |  |  |
| 21 | opp_organ_name | 否 |  |  |
| 22 | opp_borrower_code | 否 |  |  |
| 23 | opp_borrower_name | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | report_no | 否 |  |  |
| 26 | report_status | 否 |  |  |
| 27 | return_code | 否 |  |  |
| 28 | return_info | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_ieblack_info | ART | 是 | csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code, csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code |
| idx_ref_ieblack_info | ART | 是 | csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code, csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_ieblack_info | csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code, csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code |
| idx_ref_ieblack_info | csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code, csfc_organ_code, csfc_borrower_code, opp_organ_code, opp_borrower_code |

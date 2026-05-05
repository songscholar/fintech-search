# ref_ieopp_parti_info - 对手方参与人信息表

**表对象ID**: 6213
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | csfc_parti_type | 否 |  |  |
| 2 | csfc_organ_code | 否 |  |  |
| 3 | ie_organ_name | 否 |  |  |
| 4 | csfc_borrower_code | 否 |  |  |
| 5 | borrower_name | 否 |  |  |
| 6 | ie_sign_status | 否 |  |  |
| 7 | ie_acct_level | 否 |  |  |
| 8 | return_keep_rate | 否 |  |  |
| 9 | intent_keep_rate | 否 |  |  |
| 10 | plat_use_rate | 否 |  |  |
| 11 | balance_mkt_percent | 否 |  |  |
| 12 | lend_prefer | 否 |  |  |
| 13 | borrow_prefer | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | csfc_parti_type | 否 |  |  |
| 16 | csfc_organ_code | 否 |  |  |
| 17 | ie_organ_name | 否 |  |  |
| 18 | csfc_borrower_code | 否 |  |  |
| 19 | borrower_name | 否 |  |  |
| 20 | ie_sign_status | 否 |  |  |
| 21 | ie_acct_level | 否 |  |  |
| 22 | return_keep_rate | 否 |  |  |
| 23 | intent_keep_rate | 否 |  |  |
| 24 | plat_use_rate | 否 |  |  |
| 25 | balance_mkt_percent | 否 |  |  |
| 26 | lend_prefer | 否 |  |  |
| 27 | borrow_prefer | 否 |  |  |
| 28 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_ieopp_parti_info | ART | 是 | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |
| idx_ref_ieopp_parti_info | ART | 是 | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_ieopp_parti_info | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |
| idx_ref_ieopp_parti_info | csfc_organ_code, csfc_borrower_code, csfc_organ_code, csfc_borrower_code |

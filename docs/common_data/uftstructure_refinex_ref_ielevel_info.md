# ref_ielevel_info - 评级信息表

**表对象ID**: 6215
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | csfc_parti_type | 否 |  |  |
| 3 | csfc_borrow_accttype | 否 |  |  |
| 4 | csfc_organ_code | 否 |  |  |
| 5 | csfc_borrower_code | 否 |  |  |
| 6 | effect_flag | 否 |  |  |
| 7 | ie_acct_level | 否 |  |  |
| 8 | return_count | 否 |  |  |
| 9 | returnable_count | 否 |  |  |
| 10 | report_intent_balance | 否 |  |  |
| 11 | intent_balance | 否 |  |  |
| 12 | in_business_balance | 否 |  |  |
| 13 | ref_business_balance | 否 |  |  |
| 14 | parti_intent_scale | 否 |  |  |
| 15 | plat_intent_scale | 否 |  |  |
| 16 | return_keep_rate | 否 |  |  |
| 17 | intent_keep_rate | 否 |  |  |
| 18 | plat_use_rate | 否 |  |  |
| 19 | balance_mkt_percent | 否 |  |  |
| 20 | secu_comp_class | 否 |  |  |
| 21 | company_no | 否 |  |  |
| 22 | csfc_parti_type | 否 |  |  |
| 23 | csfc_borrow_accttype | 否 |  |  |
| 24 | csfc_organ_code | 否 |  |  |
| 25 | csfc_borrower_code | 否 |  |  |
| 26 | effect_flag | 否 |  |  |
| 27 | ie_acct_level | 否 |  |  |
| 28 | return_count | 否 |  |  |
| 29 | returnable_count | 否 |  |  |
| 30 | report_intent_balance | 否 |  |  |
| 31 | intent_balance | 否 |  |  |
| 32 | in_business_balance | 否 |  |  |
| 33 | ref_business_balance | 否 |  |  |
| 34 | parti_intent_scale | 否 |  |  |
| 35 | plat_intent_scale | 否 |  |  |
| 36 | return_keep_rate | 否 |  |  |
| 37 | intent_keep_rate | 否 |  |  |
| 38 | plat_use_rate | 否 |  |  |
| 39 | balance_mkt_percent | 否 |  |  |
| 40 | secu_comp_class | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_ielevel_info | ART | 是 | csfc_organ_code, csfc_borrower_code, effect_flag, csfc_organ_code, csfc_borrower_code, effect_flag |
| idx_ref_ielevel_info | ART | 是 | csfc_organ_code, csfc_borrower_code, effect_flag, csfc_organ_code, csfc_borrower_code, effect_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_ielevel_info | csfc_organ_code, csfc_borrower_code, effect_flag, csfc_organ_code, csfc_borrower_code, effect_flag |
| idx_ref_ielevel_info | csfc_organ_code, csfc_borrower_code, effect_flag, csfc_organ_code, csfc_borrower_code, effect_flag |

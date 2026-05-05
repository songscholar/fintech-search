# uref_iebasket_info - 信息交互平台篮子信息表

**表对象ID**: 6227
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | create_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_milltime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | csfc_organ_code | 否 |  |  |
| 7 | csfc_borrower_code | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | basket_no | 否 |  |  |
| 12 | basket_code | 否 |  |  |
| 13 | basket_name | 否 |  |  |
| 14 | orig_basket_code | 否 |  |  |
| 15 | market_value | 否 |  |  |
| 16 | opp_organ_code | 否 |  |  |
| 17 | opp_organ_name | 否 |  |  |
| 18 | opp_borrower_code | 否 |  |  |
| 19 | opp_borrower_name | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | create_date | 否 |  |  |
| 23 | curr_date | 否 |  |  |
| 24 | curr_milltime | 否 |  |  |
| 25 | serial_no | 否 |  |  |
| 26 | company_no | 否 |  |  |
| 27 | csfc_organ_code | 否 |  |  |
| 28 | csfc_borrower_code | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | client_id | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | basket_no | 否 |  |  |
| 33 | basket_code | 否 |  |  |
| 34 | basket_name | 否 |  |  |
| 35 | orig_basket_code | 否 |  |  |
| 36 | market_value | 否 |  |  |
| 37 | opp_organ_code | 否 |  |  |
| 38 | opp_organ_name | 否 |  |  |
| 39 | opp_borrower_code | 否 |  |  |
| 40 | opp_borrower_name | 否 |  |  |
| 41 | date_clear | 否 |  |  |
| 42 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_iebasketinfo | ART | 是 | position_str, position_str |
| idx_iebasketinfo_acct | ART | 是 | fund_account, basket_code, fund_account, basket_code |
| idx_iebasketinfo | ART | 是 | position_str, position_str |
| idx_iebasketinfo_acct | ART | 是 | fund_account, basket_code, fund_account, basket_code |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_iebasketinfo | position_str, position_str |
| idx_iebasketinfo_acct | fund_account, basket_code, fund_account, basket_code |
| idx_iebasketinfo | position_str, position_str |
| idx_iebasketinfo_acct | fund_account, basket_code, fund_account, basket_code |

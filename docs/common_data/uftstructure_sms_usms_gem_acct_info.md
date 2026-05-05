# usms_gem_acct_info - 创业板适当性信息表(交易管理)

**表对象ID**: 2833
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | organ_flag | 否 |  |  |
| 5 | aml_risk_level | 否 |  |  |
| 6 | first_exchdate | 否 |  |  |
| 7 | two_trade_flag | 否 |  |  |
| 8 | gem_train_flag | 否 |  |  |
| 9 | sub_risk_flag | 否 |  |  |
| 10 | sub_risk_date | 否 |  |  |
| 11 | sub_risk_address | 否 |  |  |
| 12 | eyewitness | 否 |  |  |
| 13 | idiograph | 否 |  |  |
| 14 | hq_censor_flag | 否 |  |  |
| 15 | right_open_flag | 否 |  |  |
| 16 | right_open_date | 否 |  |  |
| 17 | sza_stkaccount | 否 |  |  |
| 18 | id_no | 否 |  |  |
| 19 | risk_sub_type | 否 |  |  |
| 20 | gem_report_status | 否 |  |  |
| 21 | report_date | 否 |  |  |
| 22 | return_date | 否 |  |  |
| 23 | return_result | 否 |  |  |
| 24 | operator_no | 否 |  |  |
| 25 | open_date | 否 |  |  |
| 26 | confirm_status | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | position_str | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | client_id | 否 |  |  |
| 32 | branch_no | 否 |  |  |
| 33 | organ_flag | 否 |  |  |
| 34 | aml_risk_level | 否 |  |  |
| 35 | first_exchdate | 否 |  |  |
| 36 | two_trade_flag | 否 |  |  |
| 37 | gem_train_flag | 否 |  |  |
| 38 | sub_risk_flag | 否 |  |  |
| 39 | sub_risk_date | 否 |  |  |
| 40 | sub_risk_address | 否 |  |  |
| 41 | eyewitness | 否 |  |  |
| 42 | idiograph | 否 |  |  |
| 43 | hq_censor_flag | 否 |  |  |
| 44 | right_open_flag | 否 |  |  |
| 45 | right_open_date | 否 |  |  |
| 46 | sza_stkaccount | 否 |  |  |
| 47 | id_no | 否 |  |  |
| 48 | risk_sub_type | 否 |  |  |
| 49 | gem_report_status | 否 |  |  |
| 50 | report_date | 否 |  |  |
| 51 | return_date | 否 |  |  |
| 52 | return_result | 否 |  |  |
| 53 | operator_no | 否 |  |  |
| 54 | open_date | 否 |  |  |
| 55 | confirm_status | 否 |  |  |
| 56 | remark | 否 |  |  |
| 57 | position_str | 否 |  |  |
| 58 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_gemaccinfo_stk | 默认 | 是 | sza_stkaccount, fund_account, sza_stkaccount, fund_account |
| idx_gemaccinfo_stk | 默认 | 是 | sza_stkaccount, fund_account, sza_stkaccount, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_gemaccinfo_stk | sza_stkaccount, fund_account, sza_stkaccount, fund_account |
| idx_gemaccinfo_stk | sza_stkaccount, fund_account, sza_stkaccount, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 09:38:05 | 3.0.2.3 | 高志强 | 所有表usms_gem_acct_info，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |
| 2025-08-18 09:38:05 | 3.0.2.3 | 高志强 | 所有表usms_gem_acct_info，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |

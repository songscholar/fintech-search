# uopt_company_margin_account - 期权公司保证金账户表

**表对象ID**: 9022
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | optmargin_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | fund_balance | 否 |  |  |
| 6 | enable_bail_balance | 否 |  |  |
| 7 | used_bail_balance | 否 |  |  |
| 8 | in_balance | 否 |  |  |
| 9 | out_balance | 否 |  |  |
| 10 | min_prepare_balance | 否 |  |  |
| 11 | etf_exeuncome_balance | 否 |  |  |
| 12 | exelock_bail_balance | 否 |  |  |
| 13 | etf_exeback_balance | 否 |  |  |
| 14 | exenet_balance | 否 |  |  |
| 15 | exercise_balance | 否 |  |  |
| 16 | opt_cash_balance | 否 |  |  |
| 17 | net_balance | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | external_used_balance | 否 |  |  |
| 20 | partition_no | 否 |  |  |
| 21 | total_in_balance | 否 |  |  |
| 22 | total_out_balance | 否 |  |  |
| 23 | compact_settlement | 否 |  |  |
| 24 | en_clear_no | 否 |  |  |
| 25 | mobile_tel_str | 否 |  |  |
| 26 | e_mail_str | 否 |  |  |
| 27 | company_no | 否 |  |  |
| 28 | optmargin_account | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | seat_no | 否 |  |  |
| 31 | fund_balance | 否 |  |  |
| 32 | enable_bail_balance | 否 |  |  |
| 33 | used_bail_balance | 否 |  |  |
| 34 | in_balance | 否 |  |  |
| 35 | out_balance | 否 |  |  |
| 36 | min_prepare_balance | 否 |  |  |
| 37 | etf_exeuncome_balance | 否 |  |  |
| 38 | exelock_bail_balance | 否 |  |  |
| 39 | etf_exeback_balance | 否 |  |  |
| 40 | exenet_balance | 否 |  |  |
| 41 | exercise_balance | 否 |  |  |
| 42 | opt_cash_balance | 否 |  |  |
| 43 | net_balance | 否 |  |  |
| 44 | branch_no | 否 |  |  |
| 45 | external_used_balance | 否 |  |  |
| 46 | partition_no | 否 |  |  |
| 47 | total_in_balance | 否 |  |  |
| 48 | total_out_balance | 否 |  |  |
| 49 | compact_settlement | 否 |  |  |
| 50 | en_clear_no | 否 |  |  |
| 51 | mobile_tel_str | 否 |  |  |
| 52 | e_mail_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_company_margin_account | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |
| idx_uopt_company_margin_account | 默认 | 是 | company_no, exchange_type, company_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_company_margin_account | company_no, exchange_type, company_no, exchange_type |
| idx_uopt_company_margin_account | company_no, exchange_type, company_no, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-20 11:07:34 | V3.0.2.2 | 韦子晗 | 所有表uopt_company_margin_account，添加了表字段(total_in_balance);
所有... |
| 2025-08-14 17:02:30 | V3.0.2.1 | 韦子晗 | uopt_company_margin_account表新增external_used_balance、partitio... |
| 2025-07-10 11:13:28 | V3.0.3.13 | 张明月 | 去除idx_uopt_company_margin_account_globle索引 |
| 2024-08-21 19:31:31 | V3.0.3.6 | 张明月 | 新增branch_no字段，新增索引idx_uopt_company_margin_account_globle |
| 2025-10-20 11:07:34 | V3.0.2.2 | 韦子晗 | 所有表uopt_company_margin_account，添加了表字段(total_in_balance);
所有... |
| 2025-08-14 17:02:30 | V3.0.2.1 | 韦子晗 | uopt_company_margin_account表新增external_used_balance、partitio... |
| 2025-07-10 11:13:28 | V3.0.3.13 | 张明月 | 去除idx_uopt_company_margin_account_globle索引 |
| 2024-08-21 19:31:31 | V3.0.3.6 | 张明月 | 新增branch_no字段，新增索引idx_uopt_company_margin_account_globle |

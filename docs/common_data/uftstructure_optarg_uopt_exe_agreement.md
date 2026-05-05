# uopt_exe_agreement - 自动行权协议表

**表对象ID**: 9019
**所属模块**: optarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | agreement_id | 否 |  |  |
| 3 | acct_id | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | option_code | 否 |  |  |
| 7 | option_name | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_name | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | optexe_stg_kind | 否 |  |  |
| 13 | optexe_stg_value | 否 |  |  |
| 14 | agree_amount | 否 |  |  |
| 15 | end_date | 否 |  |  |
| 16 | control_flag | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | agreement_id | 否 |  |  |
| 22 | acct_id | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | option_code | 否 |  |  |
| 26 | option_name | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | stock_name | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |
| 31 | optexe_stg_kind | 否 |  |  |
| 32 | optexe_stg_value | 否 |  |  |
| 33 | agree_amount | 否 |  |  |
| 34 | end_date | 否 |  |  |
| 35 | control_flag | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | transaction_no | 否 |  |  |
| 38 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_exe_agreement | 默认 | 是 | agreement_id, agreement_id |
| idx_uopt_exe_agreement | 默认 | 是 | agreement_id, agreement_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_exe_agreement | agreement_id, agreement_id |
| idx_uopt_exe_agreement | agreement_id, agreement_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-08 19:16:51 | V3.0.2.9 | 高志强 | 所有表uopt_exe_agreement，添加了表字段(transaction_no);
 |
| 2025-09-08 19:16:51 | V3.0.2.9 | 高志强 | 所有表uopt_exe_agreement，添加了表字段(transaction_no);
 |

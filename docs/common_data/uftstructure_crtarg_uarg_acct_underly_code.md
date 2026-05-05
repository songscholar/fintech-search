# uarg_acct_underly_code - 个人标的证券信息表2

**表对象ID**: 7114
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | fin_float_ratio | 否 |  |  |
| 7 | fin_status | 否 |  |  |
| 8 | slo_float_ratio | 否 |  |  |
| 9 | slo_status | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | slo_compact_end_date | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | registration_flag | 否 |  |  |
| 14 | active_flag | 否 |  |  |
| 15 | fin_active_flag | 否 |  |  |
| 16 | slo_active_flag | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+stock_code(8 |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | fin_float_ratio | 否 |  |  |
| 28 | fin_status | 否 |  |  |
| 29 | slo_float_ratio | 否 |  |  |
| 30 | slo_status | 否 |  |  |
| 31 | end_date | 否 |  |  |
| 32 | slo_compact_end_date | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | registration_flag | 否 |  |  |
| 35 | active_flag | 否 |  |  |
| 36 | fin_active_flag | 否 |  |  |
| 37 | slo_active_flag | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+stock_code(8 |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_underly_code_uk | ART | 是 | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |
| idx_uarg_acct_underly_code_uk | ART | 是 | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_underly_code_uk | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |
| idx_uarg_acct_underly_code_uk | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 15:02:21 | 3.0.6.102 | 李想 | 新增表 |
| 2025-03-13 15:02:21 | 3.0.6.102 | 李想 | 新增表 |

# uarg_acct_assure_code - 个人担保证券信息表2

**表对象ID**: 7113
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | float_ratio | 否 |  |  |
| 7 | fair_price_flag | 否 |  |  |
| 8 | fair_price | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | assure_status | 否 |  |  |
| 11 | fair_ratio | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | registration_flag | 否 |  |  |
| 14 | active_flag | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | dyna_fair_price_flag | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |
| 21 | client_id | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | float_ratio | 否 |  |  |
| 27 | fair_price_flag | 否 |  |  |
| 28 | fair_price | 否 |  |  |
| 29 | end_date | 否 |  |  |
| 30 | assure_status | 否 |  |  |
| 31 | fair_ratio | 否 |  |  |
| 32 | transaction_no | 否 |  |  |
| 33 | registration_flag | 否 |  |  |
| 34 | active_flag | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | dyna_fair_price_flag | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | update_date | 否 |  |  |
| 39 | update_time | 否 |  |  |
| 40 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_assure_code_uk | ART | 是 | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_uarg_acct_assure_code_uk | ART | 是 | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_assure_code_uk | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_uarg_acct_assure_code_uk | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 14:59:19 | 3.0.6.101 | 李想 | 新增表 |
| 2025-03-13 14:59:19 | 3.0.6.101 | 李想 | 新增表 |

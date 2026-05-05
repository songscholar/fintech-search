# uopt_excharg - 期权交易参数表

**表对象ID**: 9000
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | exchange_name | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | square_type | 否 |  |  |
| 5 | account_len | 否 |  |  |
| 6 | prefix | 否 |  |  |
| 7 | seat_prefix_len | 否 |  |  |
| 8 | intercept_len | 否 |  |  |
| 9 | internal_len | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | exchange_status | 否 |  |  |
| 12 | fback_date | 否 |  |  |
| 13 | bback_date | 否 |  |  |
| 14 | treat_flag | 否 |  |  |
| 15 | hold_resopen_company | 否 |  |  |
| 16 | bail_resopen_company | 否 |  |  |
| 17 | covered_trans_mode | 否 |  |  |
| 18 | init_model | 否 |  | 3.0 |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | exchange_name | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | square_type | 否 |  |  |
| 26 | account_len | 否 |  |  |
| 27 | prefix | 否 |  |  |
| 28 | seat_prefix_len | 否 |  |  |
| 29 | intercept_len | 否 |  |  |
| 30 | internal_len | 否 |  |  |
| 31 | init_date | 否 |  |  |
| 32 | exchange_status | 否 |  |  |
| 33 | fback_date | 否 |  |  |
| 34 | bback_date | 否 |  |  |
| 35 | treat_flag | 否 |  |  |
| 36 | hold_resopen_company | 否 |  |  |
| 37 | bail_resopen_company | 否 |  |  |
| 38 | covered_trans_mode | 否 |  |  |
| 39 | init_model | 否 |  | 3.0 |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_excharg | 默认 | 是 | exchange_type, exchange_type |
| idx_uopt_excharg | 默认 | 是 | exchange_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optexcharg | exchange_type, exchange_type |
| idx_optexcharg | exchange_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-08-23 14:32:57 | V3.0.3.7 | 周君杰 | 调整表位置 |
| 2023-12-16 17:27:15 | 3.0.0.0 | wuxd | 新增 |
| 2024-08-23 14:32:57 | V3.0.3.7 | 周君杰 | 调整表位置 |
| 2023-12-16 17:27:15 | 3.0.0.0 | wuxd | 新增 |

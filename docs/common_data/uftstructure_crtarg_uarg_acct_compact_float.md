# uarg_acct_compact_float - 客户合约浮动利率表2

**表对象ID**: 7116
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | float_ratio | 否 |  |  |
| 4 | float_ratio_type | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+float_ratio_type(1) |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | float_ratio | 否 |  |  |
| 13 | float_ratio_type | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+float_ratio_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_compact_float | ART | 是 | fund_account, float_ratio_type, fund_account, float_ratio_type |
| idx_uarg_acct_compact_float | ART | 是 | fund_account, float_ratio_type, fund_account, float_ratio_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_compact_float | fund_account, float_ratio_type, fund_account, float_ratio_type |
| idx_uarg_acct_compact_float | fund_account, float_ratio_type, fund_account, float_ratio_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 15:07:00 | 3.0.6.104 | 李想 | 新增表 |
| 2025-03-13 15:07:00 | 3.0.6.104 | 李想 | 新增表 |

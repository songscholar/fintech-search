# uarg_acct_ensure_scale - 个人保障比例参数表2

**表对象ID**: 7115
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | ensurescale_value | 否 |  |  |
| 6 | init_ensurescale_value | 否 |  |  |
| 7 | short_ensurescale_value | 否 |  |  |
| 8 | short_init_ensurescale_value | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+stock_code(8)+stock_type(4)+exchange_type(4 |
| 15 | tohis_date | 否 | H |  |
| 16 | fund_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | ensurescale_value | 否 |  |  |
| 21 | init_ensurescale_value | 否 |  |  |
| 22 | short_ensurescale_value | 否 |  |  |
| 23 | short_init_ensurescale_value | 否 |  |  |
| 24 | transaction_no | 否 |  |  |
| 25 | branch_no | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |
| 29 | position_str | 否 |  | fund_account(18)+stock_code(8)+stock_type(4)+exchange_type(4 |
| 30 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_acct_ensure_scale | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| uk_rpt_uargacctensurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_uarg_acct_ensure_scale | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| uk_rpt_uargacctensurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_acct_ensure_scale | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| idx_uarg_acct_ensure_scale | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-13 15:04:37 | 3.0.6.103 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-13 15:04:37 | 3.0.6.103 | 李想 | 新增表 |

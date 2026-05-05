# uarg_crt_bond_exemptricon - 信用可转债交易权限豁免名单信息表

**表对象ID**: 7118
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+stock_account |
| 11 | client_id | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+stock_account |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_crt_bond_exemptricon | ART | 是 | fund_account, client_id, exchange_type, stock_code, fund_account, client_id, exchange_type, stock_code |
| idx_uarg_crt_bond_exemptricon | ART | 是 | fund_account, client_id, exchange_type, stock_code, fund_account, client_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_crt_bond_exemptricon | client_id, fund_account, exchange_type, stock_code, client_id, fund_account, exchange_type, stock_code |
| idx_uarg_crt_bond_exemptricon | client_id, fund_account, exchange_type, stock_code, client_id, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-19 14:34:06 | 3.0.6.106 | 李想 | 新增表 |
| 2025-03-19 14:34:06 | 3.0.6.106 | 李想 | 新增表 |

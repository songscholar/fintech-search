# uref_lender - 转融通出借账户表

**表对象ID**: 6033
**所属模块**: refacct
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | seat_no | 否 |  |  |
| 7 | reflender_status | 否 |  |  |
| 8 | open_date | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | transaction_no | 是 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | seat_no | 否 |  |  |
| 17 | reflender_status | 否 |  |  |
| 18 | open_date | 否 |  |  |
| 19 | position_str | 否 |  |  |
| 20 | transaction_no | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reflender | ART | 是 | position_str, position_str |
| idx_reflender_id | ART | 是 | client_id, client_id |
| idx_reflender_acct | ART | 是 | fund_account, fund_account |
| idx_reflender_acco | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |
| idx_reflender | ART | 是 | position_str, position_str |
| idx_reflender_id | ART | 是 | client_id, client_id |
| idx_reflender_acct | ART | 是 | fund_account, fund_account |
| idx_reflender_acco | ART | 是 | stock_account, branch_no, exchange_type, stock_account, branch_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reflender | position_str, position_str |
| idx_reflender | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-22 19:11:04 | 3.0.2.2 | 童程凯 | 物理表uref_lender，添加了表字段(transaction_no);
 |
| 2025-08-26 17:16:18 | 3.0.2.2 | 高志强 | 数据存储介质改为DB+MDB |
| 2025-09-22 19:11:04 | 3.0.2.2 | 童程凯 | 物理表uref_lender，添加了表字段(transaction_no);
 |
| 2025-08-26 17:16:18 | 3.0.2.2 | 高志强 | 数据存储介质改为DB+MDB |

# ref_holder - 转融通公司账户表

**表对象ID**: 6030
**所属模块**: refacct
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | refholder_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | client_name | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | seat_no | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | refholder_type(1)+exchange_type(4)+fund_account(18)+stock_ac |
| 15 | company_no | 否 |  |  |
| 16 | refholder_type | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | client_name | 否 |  |  |
| 22 | stock_account | 否 |  |  |
| 23 | seat_no | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | refholder_type(1)+exchange_type(4)+fund_account(18)+stock_ac |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_holder | ART | 是 | refholder_type, exchange_type, fund_account, stock_account, company_no, refholder_type, exchange_type, fund_account, stock_account, company_no |
| idx_ref_holder | ART | 是 | refholder_type, exchange_type, fund_account, stock_account, company_no, refholder_type, exchange_type, fund_account, stock_account, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_holder | refholder_type, exchange_type, fund_account, stock_account, company_no, refholder_type, exchange_type, fund_account, stock_account, company_no |
| idx_ref_holder | refholder_type, exchange_type, fund_account, stock_account, company_no, refholder_type, exchange_type, fund_account, stock_account, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:35:54 | 1.0.0.1 | 李想 | 新增表 |
| 2025-02-21 11:35:54 | 1.0.0.1 | 李想 | 新增表 |

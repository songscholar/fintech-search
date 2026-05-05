# self_holder - 自营账户表

**表对象ID**: 2343
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | selfholder_type | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | stock_account(20)+fund_account(18)+exchange_type(4)+selfhold |
| 14 | company_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_account | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | selfholder_type | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | stock_account(20)+fund_account(18)+exchange_type(4)+selfhold |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_self_holder | ART | 是 | stock_account, fund_account, exchange_type, selfholder_type, stock_account, fund_account, exchange_type, selfholder_type |
| idx_self_holder_acct | ART | 是 | fund_account, fund_account |
| idx_self_holder | ART | 是 | stock_account, fund_account, exchange_type, selfholder_type, stock_account, fund_account, exchange_type, selfholder_type |
| idx_self_holder_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_self_holder | stock_account, fund_account, exchange_type, selfholder_type, stock_account, fund_account, exchange_type, selfholder_type |
| idx_self_holder | stock_account, fund_account, exchange_type, selfholder_type, stock_account, fund_account, exchange_type, selfholder_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-27 16:38:07 | 3.0.6.123 | 李想 | 物理表self_holder，添加了表字段(update_date);
物理表self_holder，添加了表字段(u... |
| 2024-11-21 13:56:13 | 3.0.5.1005 | 杨涛 | 自营账户表不回库 |
| 2024-10-15 09:40:21 | 3.0.5.1001 | 董乾坤 | self_holder表从cbptrade移动到sysarg目录。 |
| 2024-09-12 18:04:37 | V3.0.2.14 | 曾剑辉 | 新增表结构 |
| 2025-02-27 16:38:07 | 3.0.6.123 | 李想 | 物理表self_holder，添加了表字段(update_date);
物理表self_holder，添加了表字段(u... |
| 2024-11-21 13:56:13 | 3.0.5.1005 | 杨涛 | 自营账户表不回库 |
| 2024-10-15 09:40:21 | 3.0.5.1001 | 董乾坤 | self_holder表从cbptrade移动到sysarg目录。 |
| 2024-09-12 18:04:37 | V3.0.2.14 | 曾剑辉 | 新增表结构 |

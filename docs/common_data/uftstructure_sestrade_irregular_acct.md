# irregular_acct - 实名制违规账户表

**表对象ID**: 5538
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | clientlist_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | irregular_acct_status | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | clientlist_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | irregular_acct_status | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_irregular_acct | ART | 是 | clientlist_type, stock_account, clientlist_type, stock_account |
| idx_irregular_acct | ART | 是 | clientlist_type, stock_account, clientlist_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_irregular_acct | clientlist_type, stock_account, clientlist_type, stock_account |
| idx_irregular_acct | clientlist_type, stock_account, clientlist_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:52:44 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-06-19 20:55:11 | 3.0.2.21 | 董乾坤 | 物理表irregular_acct，添加了表字段(clientlist_type);
物理表irregular_acc... |
| 2026-03-09 13:52:44 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-06-19 20:55:11 | 3.0.2.21 | 董乾坤 | 物理表irregular_acct，添加了表字段(clientlist_type);
物理表irregular_acc... |

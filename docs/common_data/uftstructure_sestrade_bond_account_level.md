# bond_account_level - 账户债券评级表

**表对象ID**: 5558
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | client_name | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | en_bond_level | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | en_issuemain_level | 否 |  |  |
| 8 | en_imp_bond_level | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | client_name | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | en_bond_level | 否 |  |  |
| 17 | begin_date | 否 |  |  |
| 18 | end_date | 否 |  |  |
| 19 | en_issuemain_level | 否 |  |  |
| 20 | en_imp_bond_level | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_clientbondlevel | ART | 是 | fund_account, fund_account |
| idx_clientbondlevel | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_clientbondlevel | fund_account, fund_account |
| idx_clientbondlevel | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:05:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:38:45 | 3.0.6.15 | 李想 | 物理表bond_account_level，添加了表字段(branch_no);
物理表bond_account_le... |
| 2024-07-18 14:03:34 | 3.0.2.29 | 张云焘 | 物理表bond_account_level，添加了表字段(transaction_no);删除branch_no字段
 |
| 2026-03-09 14:05:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:38:45 | 3.0.6.15 | 李想 | 物理表bond_account_level，添加了表字段(branch_no);
物理表bond_account_le... |
| 2024-07-18 14:03:34 | 3.0.2.29 | 张云焘 | 物理表bond_account_level，添加了表字段(transaction_no);删除branch_no字段
 |

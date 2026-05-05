# client_grade - 客户分级信息表

**表对象ID**: 5560
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | inv_client_grade | 否 |  |  |
| 3 | inv_client_group | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | inv_client_grade | 否 |  |  |
| 10 | inv_client_group | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_client_gradeinfo | ART | 是 | fund_account, fund_account |
| idx_client_gradeinfo | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_gradeinfo | fund_account, fund_account |
| idx_client_gradeinfo | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:10:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:45:25 | 3.0.6.23 | 李想 | 物理表client_grade，添加了表字段(branch_no);
物理表client_grade，添加了表字段(u... |
| 2024-07-18 14:10:12 | 3.0.2.29 | 张云焘 | 物理表client_grade，添加了表字段(transaction_no);
 |
| 2026-03-09 14:10:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:45:25 | 3.0.6.23 | 李想 | 物理表client_grade，添加了表字段(branch_no);
物理表client_grade，添加了表字段(u... |
| 2024-07-18 14:10:12 | 3.0.2.29 | 张云焘 | 物理表client_grade，添加了表字段(transaction_no);
 |

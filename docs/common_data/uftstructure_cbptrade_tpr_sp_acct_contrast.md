# tpr_sp_acct_contrast - 三方回购专户对照关系表

**表对象ID**: 2354
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | spestock_account | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+stock_account(20) |
| 10 | fund_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | spestock_account | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+stock_account(20) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprspacctcontrast | 默认 | 否 |  |
| idx_tprspacctcontrast | ART | 是 | fund_account, stock_account, fund_account, stock_account |
| idx_tprspacctcontrast | 默认 | 否 |  |
| idx_tprspacctcontrast | ART | 是 | fund_account, stock_account, fund_account, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprspacctcontrast | fund_account, stock_account, fund_account, stock_account |
| idx_tprspacctcontrast | fund_account, stock_account, fund_account, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:38:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:36:44 | V3.0.5.1023 | 李想 | 物理表tpr_sp_acct_contrast，添加了表字段(branch_no);
物理表tpr_sp_acct_c... |
| 2024-09-26 19:49:21 | V3.0.2.1008 | 张明月 | 物理表tpr_sp_acct_contrast，添加了表字段(transaction_no);
 |
| 2024-09-23 17:01:32 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:38:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:36:44 | V3.0.5.1023 | 李想 | 物理表tpr_sp_acct_contrast，添加了表字段(branch_no);
物理表tpr_sp_acct_c... |
| 2024-09-26 19:49:21 | V3.0.2.1008 | 张明月 | 物理表tpr_sp_acct_contrast，添加了表字段(transaction_no);
 |
| 2024-09-23 17:01:32 | V3.0.2.1007 | 张明月 | 新增 |

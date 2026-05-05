# tpr_impawn_stock - 三方回购质押券信息表

**表对象ID**: 2528
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | basket_id | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | bond_end_date | 否 |  |  |
| 9 | store_amount | 否 |  |  |
| 10 | reg_impawn_amount | 否 |  |  |
| 11 | pre_out_amount | 否 |  |  |
| 12 | used_amount | 否 |  |  |
| 13 | fruits | 否 |  |  |
| 14 | curr_due_amount | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | basket_id | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | bond_end_date | 否 |  |  |
| 23 | store_amount | 否 |  |  |
| 24 | reg_impawn_amount | 否 |  |  |
| 25 | pre_out_amount | 否 |  |  |
| 26 | used_amount | 否 |  |  |
| 27 | fruits | 否 |  |  |
| 28 | curr_due_amount | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tpr_impawn_stock_acct | 默认 | 否 |  |
| idx_tpr_impawn_stock_acct | 默认 | 否 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_tpr_impawn_stock_acct | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_tpr_impawn_stock_acct | 默认 | 否 |  |
| idx_tpr_impawn_stock_acct | 默认 | 否 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_tpr_impawn_stock_acct | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tpr_impawn_stock_acct | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_tpr_impawn_stock_acct | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:17:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:55:08 | 3.0.2.75 | taocong45644 | 当前表tpr_impawn_stock，修改了索引idx_tpr_impawn_stock_acct,索引字段修改为：(... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |
| 2026-03-04 16:17:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:55:08 | 3.0.2.75 | taocong45644 | 当前表tpr_impawn_stock，修改了索引idx_tpr_impawn_stock_acct,索引字段修改为：(... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |

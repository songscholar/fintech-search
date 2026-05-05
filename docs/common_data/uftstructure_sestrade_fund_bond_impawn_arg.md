# fund_bond_impawn_arg - 客户债券回购参数表

**表对象ID**: 5555
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | old_client_conc_ratio | 否 |  |  |
| 6 | new_client_conc_ratio | 否 |  |  |
| 7 | trustee_amount | 否 |  |  |
| 8 | par_ratio | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | fund_account(18)+stock_code(8)+exchange_type(4) |
| 14 | fund_account | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | stock_type | 否 |  |  |
| 18 | old_client_conc_ratio | 否 |  |  |
| 19 | new_client_conc_ratio | 否 |  |  |
| 20 | trustee_amount | 否 |  |  |
| 21 | par_ratio | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_bond_impawn_arg | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_fund_bond_impawn_arg | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_bond_impawn_arg | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_fund_bond_impawn_arg | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:04:50 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:52:35 | 3.0.6.17 | 李想 | 物理表fund_bond_impawn_arg，添加了表字段(branch_no);
物理表fund_bond_imp... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2026-03-09 14:04:50 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:52:35 | 3.0.6.17 | 李想 | 物理表fund_bond_impawn_arg，添加了表字段(branch_no);
物理表fund_bond_imp... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

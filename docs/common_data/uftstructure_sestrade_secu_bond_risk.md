# secu_bond_risk - 资产账号交易风险控制表

**表对象ID**: 5556
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | bond_risk | 否 |  |  |
| 4 | bond_ratio | 否 |  |  |
| 5 | frozen_ratio | 否 |  |  |
| 6 | bail_ratio | 否 |  |  |
| 7 | trustee_ratio | 否 |  |  |
| 8 | cred_bond_conc_ratio | 否 |  |  |
| 9 | fin_fund_prohibit_flag | 否 |  |  |
| 10 | single_issue_conc_ratio | 否 |  |  |
| 11 | en_stock_type | 否 |  |  |
| 12 | single_issue_enbalance_flag | 否 |  |  |
| 13 | fin_lessthan_over_flag | 否 |  |  |
| 14 | sebd_conc_ratio_no | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | fund_account(18)+exchange_type(4) |
| 20 | fund_account | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | bond_risk | 否 |  |  |
| 23 | bond_ratio | 否 |  |  |
| 24 | frozen_ratio | 否 |  |  |
| 25 | bail_ratio | 否 |  |  |
| 26 | trustee_ratio | 否 |  |  |
| 27 | cred_bond_conc_ratio | 否 |  |  |
| 28 | fin_fund_prohibit_flag | 否 |  |  |
| 29 | single_issue_conc_ratio | 否 |  |  |
| 30 | en_stock_type | 否 |  |  |
| 31 | single_issue_enbalance_flag | 否 |  |  |
| 32 | fin_lessthan_over_flag | 否 |  |  |
| 33 | sebd_conc_ratio_no | 否 |  |  |
| 34 | transaction_no | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secubondrisk | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |
| idx_secubondrisk | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secubondrisk | fund_account, exchange_type, fund_account, exchange_type |
| idx_secubondrisk | fund_account, exchange_type, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:05:15 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:56:48 | 3.0.6.18 | 李想 | 物理表secu_bond_risk，添加了表字段(branch_no);
物理表secu_bond_risk，添加了表... |
| 2026-03-09 14:05:15 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:56:48 | 3.0.6.18 | 李想 | 物理表secu_bond_risk，添加了表字段(branch_no);
物理表secu_bond_risk，添加了表... |

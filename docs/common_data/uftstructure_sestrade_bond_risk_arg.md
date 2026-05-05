# bond_risk_arg - 客户正回购风险参数表

**表对象ID**: 5553
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | inv_client_grade | 否 |  |  |
| 3 | bond_ratio_radix | 否 |  |  |
| 4 | conc_adjust_ratio | 否 |  |  |
| 5 | bond_ratio_pattern | 否 |  |  |
| 6 | en_bond_level | 否 |  |  |
| 7 | min_impawn_rate | 否 |  |  |
| 8 | single_conc_ratio | 否 |  |  |
| 9 | main_conc_ratio | 否 |  |  |
| 10 | submarket_flag | 否 |  |  |
| 11 | conc_ratio_flag | 否 |  |  |
| 12 | fine_balance_rate | 否 |  |  |
| 13 | adv_balance_rate | 否 |  |  |
| 14 | risk_control_status | 否 |  |  |
| 15 | backdate_out_control | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | inv_client_grade | 否 |  |  |
| 22 | bond_ratio_radix | 否 |  |  |
| 23 | conc_adjust_ratio | 否 |  |  |
| 24 | bond_ratio_pattern | 否 |  |  |
| 25 | en_bond_level | 否 |  |  |
| 26 | min_impawn_rate | 否 |  |  |
| 27 | single_conc_ratio | 否 |  |  |
| 28 | main_conc_ratio | 否 |  |  |
| 29 | submarket_flag | 否 |  |  |
| 30 | conc_ratio_flag | 否 |  |  |
| 31 | fine_balance_rate | 否 |  |  |
| 32 | adv_balance_rate | 否 |  |  |
| 33 | risk_control_status | 否 |  |  |
| 34 | backdate_out_control | 否 |  |  |
| 35 | transaction_no | 否 |  |  |
| 36 | branch_no | 否 |  |  |
| 37 | update_date | 否 |  |  |
| 38 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bond_risk_arg | ART | 是 | fund_account, fund_account |
| idx_bond_risk_arg | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bond_risk_arg | fund_account, fund_account |
| idx_bond_risk_arg | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:04:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:36:01 | 3.0.6.20 | 李想 | 物理表bond_risk_arg，添加了表字段(branch_no);
物理表bond_risk_arg，添加了表字段... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2026-03-09 14:04:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:36:01 | 3.0.6.20 | 李想 | 物理表bond_risk_arg，添加了表字段(branch_no);
物理表bond_risk_arg，添加了表字段... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

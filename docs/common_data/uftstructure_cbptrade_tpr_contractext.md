# tpr_contractext - 三方回购合同扩展表

**表对象ID**: 2548
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | contract_id | 否 |  |  |
| 7 | report_id | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | impawn_amount | 否 |  |  |
| 10 | exch_in_amount | 否 |  |  |
| 11 | exch_out_amount | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | contract_id | 否 |  |  |
| 18 | report_id | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | impawn_amount | 否 |  |  |
| 21 | exch_in_amount | 否 |  |  |
| 22 | exch_out_amount | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tpr_contractext_id | 默认 | 否 |  |
| idx_tpr_contractext_id | 默认 | 否 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| idx_tpr_contractext_id | ART | 是 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| idx_tpr_contractext_id | 默认 | 否 |  |
| idx_tpr_contractext_id | 默认 | 否 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| idx_tpr_contractext_id | ART | 是 | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tpr_contractext_id | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |
| idx_tpr_contractext_id | contract_id, exchange_type, stock_code, contract_id, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:28:39 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:54:23 | 3.0.2.75 | taocong45644 | 当前表tpr_contractext，修改了索引idx_tpr_contractext_id,索引字段修改为：(cont... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |
| 2026-03-04 16:28:39 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:54:23 | 3.0.2.75 | taocong45644 | 当前表tpr_contractext，修改了索引idx_tpr_contractext_id,索引字段修改为：(cont... |
| 2023-12-18 10:30:07 | 3.0.1.11 | 全春辉 | 物理表增加索引 |

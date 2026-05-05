# settredo_uqms_cash_stock - 日终清算头寸股份表

**表对象ID**: 1012
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | slo_total_amount | 否 |  |  |
| 6 | slo_used_amount | 否 |  |  |
| 7 | ref_due_amount | 否 |  |  |
| 8 | enable_amount | 否 |  |  |
| 9 | frozen_amount | 否 |  |  |
| 10 | surstock_amount | 否 |  | 上日余券数量 |
| 11 | real_buy_amount | 否 |  |  |
| 12 | sloreturn_business_amount | 否 |  |  |
| 13 | slobuy_surstock_amount | 否 |  | 当日买券还券产生余券数量 |
| 14 | surplus_amount | 否 |  | 实时余券数量 |
| 15 | sloreturn_surstock_amount | 否 |  | 当日现券还券产生余券数量 |
| 16 | real_buy_used_amount | 否 |  |  |
| 17 | sett_dml_type | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |
| 19 | cashgroup_no | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | stock_type | 否 |  |  |
| 23 | slo_total_amount | 否 |  |  |
| 24 | slo_used_amount | 否 |  |  |
| 25 | ref_due_amount | 否 |  |  |
| 26 | enable_amount | 否 |  |  |
| 27 | frozen_amount | 否 |  |  |
| 28 | surstock_amount | 否 |  | 上日余券数量 |
| 29 | real_buy_amount | 否 |  |  |
| 30 | sloreturn_business_amount | 否 |  |  |
| 31 | slobuy_surstock_amount | 否 |  | 当日买券还券产生余券数量 |
| 32 | surplus_amount | 否 |  | 实时余券数量 |
| 33 | sloreturn_surstock_amount | 否 |  | 当日现券还券产生余券数量 |
| 34 | real_buy_used_amount | 否 |  |  |
| 35 | sett_dml_type | 否 |  |  |
| 36 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_uqms_cash_stock | ART | 是 | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |
| idx_strd_uqms_cash_stock | ART | 是 | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_uqms_cash_stock | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |
| idx_strd_uqms_cash_stock | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:55:52 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2026-03-05 16:55:52 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

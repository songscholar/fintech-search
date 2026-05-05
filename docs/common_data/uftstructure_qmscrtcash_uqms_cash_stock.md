# uqms_cash_stock - 头寸股份表

**表对象ID**: 1003
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

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
| 17 | tohis_date | 否 | H |  |
| 18 | stock_name | 否 | H |  |
| 19 | sub_stock_type | 否 | H |  |
| 20 | cashgroup_no | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stock_type | 否 |  |  |
| 24 | slo_total_amount | 否 |  |  |
| 25 | slo_used_amount | 否 |  |  |
| 26 | ref_due_amount | 否 |  |  |
| 27 | enable_amount | 否 |  |  |
| 28 | frozen_amount | 否 |  |  |
| 29 | surstock_amount | 否 |  | 上日余券数量 |
| 30 | real_buy_amount | 否 |  |  |
| 31 | sloreturn_business_amount | 否 |  |  |
| 32 | slobuy_surstock_amount | 否 |  | 当日买券还券产生余券数量 |
| 33 | surplus_amount | 否 |  | 实时余券数量 |
| 34 | sloreturn_surstock_amount | 否 |  | 当日现券还券产生余券数量 |
| 35 | real_buy_used_amount | 否 |  |  |
| 36 | tohis_date | 否 | H |  |
| 37 | stock_name | 否 | H |  |
| 38 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_cash_stock_code | 默认 | 否 | stock_code, stock_code |
| uk_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |
| uk_rpt_uqmscashstock | ART | 是 | tohis_date, cashgroup_no, stock_code, exchange_type, tohis_date, cashgroup_no, stock_code, exchange_type |
| idx_ucrt_cash_stock_code | 默认 | 否 | stock_code, stock_code |
| uk_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |
| uk_rpt_uqmscashstock | ART | 是 | tohis_date, cashgroup_no, stock_code, exchange_type, tohis_date, cashgroup_no, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:52:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-06 11:05:22 | 3.0.6.23 | 黄佳平 | 索引优化 |
| 2025-06-19 09:43:22 | 3.0.6.20 | 牟家乐 | 物理表uqms_cash_stock，添加了表字段(real_buy_used_amount);
 |
| 2024-12-06 16:37:33 | 3.0.6.5 | 刘景锋 | 物理表uqms_cash_stock，添加了表字段(slobuy_surstock_amount);
物理表uqms_... |
| 2024-10-15 19:28:33 | 3.0.6.4 | 牟家乐 | 业务支持 |
| 2024-05-31 16:08:37 | 3.0.2.6 | 牟家乐 | 物理表uqms_cash_stock，增加索引(idx_ucrt_cash_stock_code:[stock_code... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:52:42 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.25 | 周兆军 | 维护历史表 |
| 2025-08-06 11:05:22 | 3.0.6.23 | 黄佳平 | 索引优化 |
| 2025-06-19 09:43:22 | 3.0.6.20 | 牟家乐 | 物理表uqms_cash_stock，添加了表字段(real_buy_used_amount);
 |
| 2024-12-06 16:37:33 | 3.0.6.5 | 刘景锋 | 物理表uqms_cash_stock，添加了表字段(slobuy_surstock_amount);
物理表uqms_... |
| 2024-10-15 19:28:33 | 3.0.6.4 | 牟家乐 | 业务支持 |
| 2024-05-31 16:08:37 | 3.0.2.6 | 牟家乐 | 物理表uqms_cash_stock，增加索引(idx_ucrt_cash_stock_code:[stock_code... |

> 共 16 条修改记录，仅显示最近15条

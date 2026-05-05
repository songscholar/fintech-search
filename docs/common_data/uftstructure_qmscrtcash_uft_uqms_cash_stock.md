# uft_uqms_cash_stock - UFT头寸股份表

**表对象ID**: 1017
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 64 个）

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
| 10 | surstock_amount | 否 |  |  |
| 11 | real_buy_amount | 否 |  |  |
| 12 | sloreturn_business_amount | 否 |  |  |
| 13 | slobuy_surstock_amount | 否 |  |  |
| 14 | surplus_amount | 否 |  |  |
| 15 | sloreturn_surstock_amount | 否 |  |  |
| 16 | real_buy_used_amount | 否 |  |  |
| 17 | cashgroup_no | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | slo_total_amount | 否 |  |  |
| 22 | slo_used_amount | 否 |  |  |
| 23 | ref_due_amount | 否 |  |  |
| 24 | enable_amount | 否 |  |  |
| 25 | frozen_amount | 否 |  |  |
| 26 | surstock_amount | 否 |  |  |
| 27 | real_buy_amount | 否 |  |  |
| 28 | sloreturn_business_amount | 否 |  |  |
| 29 | slobuy_surstock_amount | 否 |  |  |
| 30 | surplus_amount | 否 |  |  |
| 31 | sloreturn_surstock_amount | 否 |  |  |
| 32 | real_buy_used_amount | 否 |  |  |
| 33 | cashgroup_no | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | stock_type | 否 |  |  |
| 37 | slo_total_amount | 否 |  |  |
| 38 | slo_used_amount | 否 |  |  |
| 39 | ref_due_amount | 否 |  |  |
| 40 | enable_amount | 否 |  |  |
| 41 | frozen_amount | 否 |  |  |
| 42 | surstock_amount | 否 |  |  |
| 43 | real_buy_amount | 否 |  |  |
| 44 | sloreturn_business_amount | 否 |  |  |
| 45 | slobuy_surstock_amount | 否 |  |  |
| 46 | surplus_amount | 否 |  |  |
| 47 | sloreturn_surstock_amount | 否 |  |  |
| 48 | real_buy_used_amount | 否 |  |  |
| 49 | cashgroup_no | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_code | 否 |  |  |
| 52 | stock_type | 否 |  |  |
| 53 | slo_total_amount | 否 |  |  |
| 54 | slo_used_amount | 否 |  |  |
| 55 | ref_due_amount | 否 |  |  |
| 56 | enable_amount | 否 |  |  |
| 57 | frozen_amount | 否 |  |  |
| 58 | surstock_amount | 否 |  |  |
| 59 | real_buy_amount | 否 |  |  |
| 60 | sloreturn_business_amount | 否 |  |  |
| 61 | slobuy_surstock_amount | 否 |  |  |
| 62 | surplus_amount | 否 |  |  |
| 63 | sloreturn_surstock_amount | 否 |  |  |
| 64 | real_buy_used_amount | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |
| idx_uft_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |
| idx_uft_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |
| idx_uft_ucrt_cash_stock_unique | ART | 是 | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_code | ART | 是 | cashgroup_no, stock_code, cashgroup_no, stock_code |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |
| idx_uft_ucrt_cash_stock_unique | cashgroup_no, exchange_type, stock_code, cashgroup_no, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:58:00 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 14:15:52 | 3.0.2.1 | 曾阳璞 | 添加表 |
| 2025-09-02 14:15:52 | 3.0.2.1 |  |  |
| 2026-03-05 16:58:00 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 14:15:52 | 3.0.2.1 | 曾阳璞 | 添加表 |
| 2025-09-02 14:15:52 | 3.0.2.1 |  |  |

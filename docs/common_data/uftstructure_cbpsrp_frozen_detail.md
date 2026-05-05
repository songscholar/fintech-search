# frozen_detail - 冻结明细表

**表对象ID**: 2637
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | impawn_id | 否 |  |  |
| 9 | judifrozen_id | 否 |  |  |
| 10 | report_id | 否 |  |  |
| 11 | frozen_type | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | position_str | 否 |  | exchange_type(4)+stock_account(20)+frozen_type(1)+impawn_id( |
| 14 | stock_property | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | sz_frozen_organname | 否 |  |  |
| 18 | principal | 否 |  |  |
| 19 | dividend | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | client_id | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | stock_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | frozen_amount | 否 |  |  |
| 27 | impawn_id | 否 |  |  |
| 28 | judifrozen_id | 否 |  |  |
| 29 | report_id | 否 |  |  |
| 30 | frozen_type | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | position_str | 否 |  | exchange_type(4)+stock_account(20)+frozen_type(1)+impawn_id( |
| 33 | stock_property | 否 |  |  |
| 34 | begin_date | 否 |  |  |
| 35 | end_date | 否 |  |  |
| 36 | sz_frozen_organname | 否 |  |  |
| 37 | principal | 否 |  |  |
| 38 | dividend | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_frozendetail_pos | ART | 是 | position_str, position_str |
| idx_frozendetail_id | ART | 是 | impawn_id, report_id, impawn_id, report_id |
| idx_frozendetail_pos | ART | 是 | position_str, position_str |
| idx_frozendetail_id | ART | 是 | impawn_id, report_id, impawn_id, report_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_frozendetail_pos | position_str, position_str |
| idx_frozendetail_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:59:11 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-24 09:58:19 | 8.26.2.93 | 马天宇 | 所有表frozen_detail，添加了表字段(principal);
所有表frozen_detail，添加了表字段... |
| 2025-09-15 14:28:38 | 3.0.2.2 | yangxz | 修改为回库 |
| 2024-11-29 16:21:14 | 3.0.2.1 | 范文浩 | 物理表frozen_detail，添加了表字段(init_date);
物理表frozen_detail，添加了表字段... |
| 2026-03-06 16:59:11 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-24 09:58:19 | 8.26.2.93 | 马天宇 | 所有表frozen_detail，添加了表字段(principal);
所有表frozen_detail，添加了表字段... |
| 2025-09-15 14:28:38 | 3.0.2.2 | yangxz | 修改为回库 |
| 2024-11-29 16:21:14 | 3.0.2.1 | 范文浩 | 物理表frozen_detail，添加了表字段(init_date);
物理表frozen_detail，添加了表字段... |

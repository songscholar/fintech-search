# srp_mar_ratio - 股票质押履约比表

**表对象ID**: 2617
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | margin_focus_ratio | 否 |  |  |
| 5 | margin_alert_ratio | 否 |  |  |
| 6 | margin_treat_ratio | 否 |  |  |
| 7 | uncir_margin_focus_ratio | 否 |  |  |
| 8 | uncir_margin_alert_ratio | 否 |  |  |
| 9 | uncir_margin_treat_ratio | 否 |  |  |
| 10 | margin_immtreat_ratio | 否 |  |  |
| 11 | uncir_margin_immtreat_ratio | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | stock_type(4)+exchange_type(4)+company_no(10) |
| 15 | transaction_no | 否 |  |  |
| 16 | company_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | margin_focus_ratio | 否 |  |  |
| 20 | margin_alert_ratio | 否 |  |  |
| 21 | margin_treat_ratio | 否 |  |  |
| 22 | uncir_margin_focus_ratio | 否 |  |  |
| 23 | uncir_margin_alert_ratio | 否 |  |  |
| 24 | uncir_margin_treat_ratio | 否 |  |  |
| 25 | margin_immtreat_ratio | 否 |  |  |
| 26 | uncir_margin_immtreat_ratio | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |
| 29 | position_str | 否 |  | stock_type(4)+exchange_type(4)+company_no(10) |
| 30 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpmarratio | ART | 是 | stock_type, exchange_type, company_no, stock_type, exchange_type, company_no |
| idx_srpmarratio | ART | 是 | stock_type, exchange_type, company_no, stock_type, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpmarratio | stock_type, exchange_type, company_no, stock_type, exchange_type, company_no |
| idx_srpmarratio | stock_type, exchange_type, company_no, stock_type, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:51:00 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-04-28 15:43:25 | 3.0.3.11 | 常行 | 物理表srp_mar_ratio，添加了表字段(update_date);
物理表srp_mar_ratio，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:04 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:51:00 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-04-28 15:43:25 | 3.0.3.11 | 常行 | 物理表srp_mar_ratio，添加了表字段(update_date);
物理表srp_mar_ratio，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:04 | 3.0.3.1 | wuxd | 新增 |

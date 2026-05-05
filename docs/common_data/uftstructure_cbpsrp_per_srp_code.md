# per_srp_code - 个人股票质押代码表

**表对象ID**: 2628
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | srp_kind | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | stock_property | 否 |  |  |
| 9 | srp_assure_ratio | 否 |  |  |
| 10 | margin_focus_ratio | 否 |  |  |
| 11 | margin_alert_ratio | 否 |  |  |
| 12 | margin_treat_ratio | 否 |  |  |
| 13 | lift_date | 否 |  |  |
| 14 | max_term | 否 |  |  |
| 15 | fsmp_term | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | srp_kind | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stock_type | 否 |  |  |
| 24 | stock_property | 否 |  |  |
| 25 | srp_assure_ratio | 否 |  |  |
| 26 | margin_focus_ratio | 否 |  |  |
| 27 | margin_alert_ratio | 否 |  |  |
| 28 | margin_treat_ratio | 否 |  |  |
| 29 | lift_date | 否 |  |  |
| 30 | max_term | 否 |  |  |
| 31 | fsmp_term | 否 |  |  |
| 32 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_persrpcode | ART | 是 | fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind, fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind |
| idx_persrpcode | ART | 是 | fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind, fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_persrpcode | fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind, fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind |
| idx_persrpcode | fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind, fund_account, stock_code, exchange_type, stock_type, stock_property, srp_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:55:58 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:22 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:55:58 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:22 | 3.0.3.1 | wuxd | 新增 |

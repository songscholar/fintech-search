# per_srp_kind - 个人股票质押期限产品表

**表对象ID**: 2627
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | srp_kind | 否 |  |  |
| 6 | funder_no | 否 |  |  |
| 7 | stock_property | 否 |  |  |
| 8 | srp_kind_days | 否 |  |  |
| 9 | srp_kind_name | 否 |  |  |
| 10 | srp_interest_ratio | 否 |  |  |
| 11 | srp_float_ratio | 否 |  |  |
| 12 | valid_date | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | srp_kind | 否 |  |  |
| 19 | funder_no | 否 |  |  |
| 20 | stock_property | 否 |  |  |
| 21 | srp_kind_days | 否 |  |  |
| 22 | srp_kind_name | 否 |  |  |
| 23 | srp_interest_ratio | 否 |  |  |
| 24 | srp_float_ratio | 否 |  |  |
| 25 | valid_date | 否 |  |  |
| 26 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_persrpkind | ART | 是 | fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind, fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind |
| idx_persrpkind | ART | 是 | fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind, fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_persrpkind | fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind, fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind |
| idx_persrpkind | fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind, fund_account, srp_kind_days, exchange_type, funder_no, stock_property, srp_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:55:35 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:32 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:55:35 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:22:32 | 3.0.3.1 | wuxd | 新增 |

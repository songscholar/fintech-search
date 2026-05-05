# ucbp_srp_kind - 股票质押回购期限产品表

**表对象ID**: 2601
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | srp_kind_code | 否 |  |  |
| 4 | srp_kind_days | 否 |  |  |
| 5 | srp_kind_name | 否 |  |  |
| 6 | srp_interest_ratio | 否 |  |  |
| 7 | srp_float_ratio | 否 |  |  |
| 8 | funder_no | 否 |  |  |
| 9 | srp_kind | 否 |  |  |
| 10 | recoup_rate | 否 |  |  |
| 11 | max_recoup_days | 否 |  |  |
| 12 | fine_rate | 否 |  |  |
| 13 | client_group | 否 |  |  |
| 14 | pre_back_flag | 否 |  |  |
| 15 | srpkind_ctrlstr | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | srp_kind_days(10)+funder_no(10)+exchange_type(4)+company_no( |
| 20 | company_no | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | srp_kind_code | 否 |  |  |
| 23 | srp_kind_days | 否 |  |  |
| 24 | srp_kind_name | 否 |  |  |
| 25 | srp_interest_ratio | 否 |  |  |
| 26 | srp_float_ratio | 否 |  |  |
| 27 | funder_no | 否 |  |  |
| 28 | srp_kind | 否 |  |  |
| 29 | recoup_rate | 否 |  |  |
| 30 | max_recoup_days | 否 |  |  |
| 31 | fine_rate | 否 |  |  |
| 32 | client_group | 否 |  |  |
| 33 | pre_back_flag | 否 |  |  |
| 34 | srpkind_ctrlstr | 否 |  |  |
| 35 | transaction_no | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | srp_kind_days(10)+funder_no(10)+exchange_type(4)+company_no( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpkind | ART | 是 | srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group, srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group |
| idx_srpkind | ART | 是 | srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group, srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpkind | srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group, srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group |
| idx_srpkind | srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group, srp_kind_days, funder_no, exchange_type, company_no, srp_kind, client_group |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:42:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:14:39 | 3.0.3.4 | 李想 | 物理表ucbp_srp_kind，添加了表字段(update_date);
物理表ucbp_srp_kind，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 17:54:05 | 3.0.3.1 | wuxd |  |
| 2026-03-06 16:42:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:14:39 | 3.0.3.4 | 李想 | 物理表ucbp_srp_kind，添加了表字段(update_date);
物理表ucbp_srp_kind，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 17:54:05 | 3.0.3.1 | wuxd |  |

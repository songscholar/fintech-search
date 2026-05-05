# hstock_quota - H股全流通额度信息表

**表对象ID**: 5723
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | organ_flag | 否 |  |  |
| 5 | id_no | 否 |  |  |
| 6 | holder_name_long | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_code2 | 否 |  |  |
| 10 | stock_name | 否 |  |  |
| 11 | bank_account | 否 |  |  |
| 12 | full_bank_name | 否 |  |  |
| 13 | company_name | 否 |  |  |
| 14 | facility_quota | 否 |  |  |
| 15 | used_quota | 否 |  |  |
| 16 | occur_quota | 否 |  |  |
| 17 | random_code | 否 |  |  |
| 18 | official_document | 否 |  |  |
| 19 | hold_rate_h | 否 |  |  |
| 20 | modify_date | 否 |  |  |
| 21 | op_flag | 否 |  |  |
| 22 | pay_bank_no_long | 否 |  |  |
| 23 | frozen_quota | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | organ_flag | 否 |  |  |
| 28 | id_no | 否 |  |  |
| 29 | holder_name_long | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | stock_code2 | 否 |  |  |
| 33 | stock_name | 否 |  |  |
| 34 | bank_account | 否 |  |  |
| 35 | full_bank_name | 否 |  |  |
| 36 | company_name | 否 |  |  |
| 37 | facility_quota | 否 |  |  |
| 38 | used_quota | 否 |  |  |
| 39 | occur_quota | 否 |  |  |
| 40 | random_code | 否 |  |  |
| 41 | official_document | 否 |  |  |
| 42 | hold_rate_h | 否 |  |  |
| 43 | modify_date | 否 |  |  |
| 44 | op_flag | 否 |  |  |
| 45 | pay_bank_no_long | 否 |  |  |
| 46 | frozen_quota | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hstock_quota | ART | 是 | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |
| idx_hstock_quota | ART | 是 | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hstock_quota | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |
| idx_hstock_quota | fund_account, stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:37:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:37:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

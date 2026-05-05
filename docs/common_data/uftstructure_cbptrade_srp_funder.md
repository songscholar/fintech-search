# srp_funder - 股票质押融出方信息表

**表对象ID**: 2314
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 80 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | funder_no | 否 |  |  |
| 3 | funder_name | 否 |  |  |
| 4 | pledgee_type | 否 |  |  |
| 5 | pledgee_name | 否 |  |  |
| 6 | funder_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | funder_ratio | 否 |  |  |
| 10 | total_quota | 否 |  |  |
| 11 | used_quota | 否 |  |  |
| 12 | status | 否 |  |  |
| 13 | setup_date | 否 |  |  |
| 14 | funder_rate | 否 |  |  |
| 15 | szdc_stock_account | 否 |  |  |
| 16 | szdc_seat_no | 否 |  |  |
| 17 | counter_clear_flag | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | mobile_tel | 否 |  |  |
| 20 | zipcode | 否 |  |  |
| 21 | address | 否 |  |  |
| 22 | register_address | 否 |  |  |
| 23 | instrepr_id_no | 否 |  |  |
| 24 | instrepr_name | 否 |  |  |
| 25 | open_date | 否 |  |  |
| 26 | expire_date | 否 |  |  |
| 27 | instrepr_id_kind | 否 |  |  |
| 28 | funder_id_kind | 否 |  |  |
| 29 | funder_id_no | 否 |  |  |
| 30 | phonecode | 否 |  |  |
| 31 | funder_capital_ratio | 否 |  |  |
| 32 | funder_stock_conc_ratio | 否 |  |  |
| 33 | funder_client_conc_ratio | 否 |  |  |
| 34 | investor_name | 否 |  |  |
| 35 | exch_funder_type | 否 |  |  |
| 36 | transaction_no | 否 |  |  |
| 37 | update_date | 否 |  |  |
| 38 | update_time | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | company_no | 否 |  |  |
| 42 | funder_no | 否 |  |  |
| 43 | funder_name | 否 |  |  |
| 44 | pledgee_type | 否 |  |  |
| 45 | pledgee_name | 否 |  |  |
| 46 | funder_type | 否 |  |  |
| 47 | stock_account | 否 |  |  |
| 48 | seat_no | 否 |  |  |
| 49 | funder_ratio | 否 |  |  |
| 50 | total_quota | 否 |  |  |
| 51 | used_quota | 否 |  |  |
| 52 | status | 否 |  |  |
| 53 | setup_date | 否 |  |  |
| 54 | funder_rate | 否 |  |  |
| 55 | szdc_stock_account | 否 |  |  |
| 56 | szdc_seat_no | 否 |  |  |
| 57 | counter_clear_flag | 否 |  |  |
| 58 | fund_account | 否 |  |  |
| 59 | mobile_tel | 否 |  |  |
| 60 | zipcode | 否 |  |  |
| 61 | address | 否 |  |  |
| 62 | register_address | 否 |  |  |
| 63 | instrepr_id_no | 否 |  |  |
| 64 | instrepr_name | 否 |  |  |
| 65 | open_date | 否 |  |  |
| 66 | expire_date | 否 |  |  |
| 67 | instrepr_id_kind | 否 |  |  |
| 68 | funder_id_kind | 否 |  |  |
| 69 | funder_id_no | 否 |  |  |
| 70 | phonecode | 否 |  |  |
| 71 | funder_capital_ratio | 否 |  |  |
| 72 | funder_stock_conc_ratio | 否 |  |  |
| 73 | funder_client_conc_ratio | 否 |  |  |
| 74 | investor_name | 否 |  |  |
| 75 | exch_funder_type | 否 |  |  |
| 76 | transaction_no | 否 |  |  |
| 77 | update_date | 否 |  |  |
| 78 | update_time | 否 |  |  |
| 79 | branch_no | 否 |  |  |
| 80 | client_id | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_funder | 默认 | 否 |  |
| idx_srp_funder | ART | 是 | funder_no, funder_no |
| idx_srp_funder | 默认 | 否 |  |
| idx_srp_funder | ART | 是 | funder_no, funder_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_funder | funder_no, funder_no |
| idx_srp_funder | funder_no, funder_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:17:26 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:27:03 | V3.0.5.1011 | 李想 | 物理表srp_funder，添加了表字段(update_date);
物理表srp_funder，添加了表字段(upd... |
| 2025-04-07 20:16:58 | 3.0.2.55 | yusz | 物理表srp_funder，添加了表字段(branch_no);
物理表srp_funder，添加了表字段(clien... |
| 2024-09-09 11:18:55 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-27 11:24:44 | V3.0.1.11 | 董乾坤 |  |
| 2026-03-04 15:17:26 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:27:03 | V3.0.5.1011 | 李想 | 物理表srp_funder，添加了表字段(update_date);
物理表srp_funder，添加了表字段(upd... |
| 2025-04-07 20:16:58 | 3.0.2.55 | yusz | 物理表srp_funder，添加了表字段(branch_no);
物理表srp_funder，添加了表字段(clien... |
| 2024-09-09 11:18:55 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-27 11:24:44 | V3.0.1.11 | 董乾坤 |  |

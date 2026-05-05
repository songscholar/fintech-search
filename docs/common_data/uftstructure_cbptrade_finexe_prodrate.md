# finexe_prodrate - 融资行权期限利率表

**表对象ID**: 2330
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | prod_kind_days | 否 |  |  |
| 4 | prod_kind_name | 否 |  |  |
| 5 | year_rate | 否 |  |  |
| 6 | recoup_rate | 否 |  |  |
| 7 | fine_rate | 否 |  |  |
| 8 | executives_flag | 否 |  |  |
| 9 | sopt_code | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | prod_kind_days(10)+exchange_type(4)+company_no(4)+executives |
| 14 | company_no | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | prod_kind_days | 否 |  |  |
| 17 | prod_kind_name | 否 |  |  |
| 18 | year_rate | 否 |  |  |
| 19 | recoup_rate | 否 |  |  |
| 20 | fine_rate | 否 |  |  |
| 21 | executives_flag | 否 |  |  |
| 22 | sopt_code | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | prod_kind_days(10)+exchange_type(4)+company_no(4)+executives |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexeprodrate | 默认 | 否 |  |
| idx_finexeprodrate | ART | 是 | prod_kind_days, exchange_type, company_no, executives_flag, sopt_code, prod_kind_days, exchange_type, company_no, executives_flag, sopt_code |
| idx_finexeprodrate | 默认 | 否 |  |
| idx_finexeprodrate | ART | 是 | prod_kind_days, exchange_type, company_no, executives_flag, sopt_code, prod_kind_days, exchange_type, company_no, executives_flag, sopt_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexeprodrate | prod_kind_days, exchange_type, company_no, executives_flag, sopt_code, prod_kind_days, exchange_type, company_no, executives_flag, sopt_code |
| idx_finexeprodrate | prod_kind_days, exchange_type, company_no, executives_flag, sopt_code, prod_kind_days, exchange_type, company_no, executives_flag, sopt_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:26:54 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:57:35 | V3.0.5.1015 | 李想 | 物理表finexe_prodrate，添加了表字段(update_date);
物理表finexe_prodrate，... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:26:54 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:57:35 | V3.0.5.1015 | 李想 | 物理表finexe_prodrate，添加了表字段(update_date);
物理表finexe_prodrate，... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

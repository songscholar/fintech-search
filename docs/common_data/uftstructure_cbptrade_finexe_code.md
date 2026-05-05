# finexe_code - 融资行权标的证券

**表对象ID**: 2325
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_conc_ratio | 否 |  |  |
| 5 | underly_status | 否 |  |  |
| 6 | margin_focus_ratio | 否 |  |  |
| 7 | margin_alert_ratio | 否 |  |  |
| 8 | margin_treat_ratio | 否 |  |  |
| 9 | execv_margin_focus_ratio | 否 |  |  |
| 10 | execv_margin_alert_ratio | 否 |  |  |
| 11 | execv_margin_treat_ratio | 否 |  |  |
| 12 | execv_fin_ratio | 否 |  |  |
| 13 | margin_draw_ratio | 否 |  |  |
| 14 | execv_margin_draw_ratio | 否 |  |  |
| 15 | spread_ratio | 否 |  |  |
| 16 | fin_ratio_t | 否 |  |  |
| 17 | min_interest_days | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 22 | company_no | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | stock_conc_ratio | 否 |  |  |
| 26 | underly_status | 否 |  |  |
| 27 | margin_focus_ratio | 否 |  |  |
| 28 | margin_alert_ratio | 否 |  |  |
| 29 | margin_treat_ratio | 否 |  |  |
| 30 | execv_margin_focus_ratio | 否 |  |  |
| 31 | execv_margin_alert_ratio | 否 |  |  |
| 32 | execv_margin_treat_ratio | 否 |  |  |
| 33 | execv_fin_ratio | 否 |  |  |
| 34 | margin_draw_ratio | 否 |  |  |
| 35 | execv_margin_draw_ratio | 否 |  |  |
| 36 | spread_ratio | 否 |  |  |
| 37 | fin_ratio_t | 否 |  |  |
| 38 | min_interest_days | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexecode | 默认 | 否 |  |
| idx_finexecode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_finexecode | 默认 | 否 |  |
| idx_finexecode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexecode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_finexecode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:24:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:21:59 | V3.0.5.1018 | 李想 | 物理表finexe_code，添加了表字段(update_date);
物理表finexe_code，添加了表字段(u... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |
| 2026-03-04 15:24:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:21:59 | V3.0.5.1018 | 李想 | 物理表finexe_code，添加了表字段(update_date);
物理表finexe_code，添加了表字段(u... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |

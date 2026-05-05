# arp_mar_ratio - 约定购回履约比表

**表对象ID**: 2539
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | margin_focus_ratio | 否 |  |  |
| 5 | margin_alert_ratio | 否 |  |  |
| 6 | margin_treat_ratio | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | company_no(4)+exchange_type(4)+stock_type(4) |
| 11 | company_no | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | margin_focus_ratio | 否 |  |  |
| 15 | margin_alert_ratio | 否 |  |  |
| 16 | margin_treat_ratio | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | company_no(4)+exchange_type(4)+stock_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpmarratio | ART | 是 | company_no, exchange_type, stock_type, company_no, exchange_type, stock_type |
| idx_arpmarratio | ART | 是 | company_no, exchange_type, stock_type, company_no, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpmarratio | company_no, exchange_type, stock_type, company_no, exchange_type, stock_type |
| idx_arpmarratio | company_no, exchange_type, stock_type, company_no, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:24:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:49:59 | V3.0.5.1014 | 李想 | 物理表arp_mar_ratio，添加了表字段(update_date);
物理表arp_mar_ratio，添加了表... |
| 2026-03-04 16:24:25 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:49:59 | V3.0.5.1014 | 李想 | 物理表arp_mar_ratio，添加了表字段(update_date);
物理表arp_mar_ratio，添加了表... |

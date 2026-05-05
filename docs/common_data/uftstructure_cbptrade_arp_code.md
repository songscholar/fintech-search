# arp_code - 约定购回代码表

**表对象ID**: 2484
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | stock_conc_ratio | 否 |  |  |
| 6 | arp_capital_ratio | 否 |  |  |
| 7 | arp_one_capital_ratio | 否 |  |  |
| 8 | capital_amount | 否 |  |  |
| 9 | circulate_amount | 否 |  |  |
| 10 | arp_assure_ratio | 否 |  |  |
| 11 | fair_price | 否 |  |  |
| 12 | fair_price_flag | 否 |  |  |
| 13 | assure_price | 否 |  |  |
| 14 | assure_status | 否 |  |  |
| 15 | float_ratio_flag | 否 |  |  |
| 16 | stkused_year_rate | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 21 | company_no | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | stock_conc_ratio | 否 |  |  |
| 26 | arp_capital_ratio | 否 |  |  |
| 27 | arp_one_capital_ratio | 否 |  |  |
| 28 | capital_amount | 否 |  |  |
| 29 | circulate_amount | 否 |  |  |
| 30 | arp_assure_ratio | 否 |  |  |
| 31 | fair_price | 否 |  |  |
| 32 | fair_price_flag | 否 |  |  |
| 33 | assure_price | 否 |  |  |
| 34 | assure_status | 否 |  |  |
| 35 | float_ratio_flag | 否 |  |  |
| 36 | stkused_year_rate | 否 |  |  |
| 37 | transaction_no | 否 |  |  |
| 38 | update_date | 否 |  |  |
| 39 | update_time | 否 |  |  |
| 40 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpcode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_arpcode | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpcode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_arpcode | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:47:40 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:42:57 | V3.0.5.1012 | 李想 | 物理表arp_code，添加了表字段(update_date);
物理表arp_code，添加了表字段(update_... |
| 2024-12-06 16:02:20 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 15:47:40 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:42:57 | V3.0.5.1012 | 李想 | 物理表arp_code，添加了表字段(update_date);
物理表arp_code，添加了表字段(update_... |
| 2024-12-06 16:02:20 | V3.0.2.1009 | 黄积冲 | 新增表 |

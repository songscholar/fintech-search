# arp_kind - 约定购回期限表

**表对象ID**: 2531
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | arp_kind_days | 否 |  |  |
| 4 | arp_kind_name | 否 |  |  |
| 5 | arp_interest_ratio | 否 |  |  |
| 6 | arp_assure_ratio | 否 |  |  |
| 7 | begin_date | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+arp_kind_days(10)+begin_date(8)+company_no( |
| 12 | company_no | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | arp_kind_days | 否 |  |  |
| 15 | arp_kind_name | 否 |  |  |
| 16 | arp_interest_ratio | 否 |  |  |
| 17 | arp_assure_ratio | 否 |  |  |
| 18 | begin_date | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+arp_kind_days(10)+begin_date(8)+company_no( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpkind | ART | 是 | exchange_type, arp_kind_days, begin_date, company_no, exchange_type, arp_kind_days, begin_date, company_no |
| idx_arpkind | ART | 是 | exchange_type, arp_kind_days, begin_date, company_no, exchange_type, arp_kind_days, begin_date, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpkind | exchange_type, arp_kind_days, begin_date, company_no, exchange_type, arp_kind_days, begin_date, company_no |
| idx_arpkind | exchange_type, arp_kind_days, begin_date, company_no, exchange_type, arp_kind_days, begin_date, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:20:35 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:46:43 | V3.0.5.1013 | 李想 | 物理表arp_kind，添加了表字段(update_date);
物理表arp_kind，添加了表字段(update_... |
| 2026-03-04 16:20:35 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 19:46:43 | V3.0.5.1013 | 李想 | 物理表arp_kind，添加了表字段(update_date);
物理表arp_kind，添加了表字段(update_... |

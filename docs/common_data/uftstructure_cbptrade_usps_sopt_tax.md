# usps_sopt_tax - 自主行权税率表

**表对象ID**: 2328
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sopttax_kind | 否 |  |  |
| 2 | ordinal | 否 |  |  |
| 3 | down_limited | 否 |  |  |
| 4 | up_limited | 否 |  |  |
| 5 | tax_ratio | 否 |  |  |
| 6 | deduct_base | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | sopttax_kind(10)+ordinal(10) |
| 11 | sopttax_kind | 否 |  |  |
| 12 | ordinal | 否 |  |  |
| 13 | down_limited | 否 |  |  |
| 14 | up_limited | 否 |  |  |
| 15 | tax_ratio | 否 |  |  |
| 16 | deduct_base | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | sopttax_kind(10)+ordinal(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sopttax | 默认 | 否 |  |
| idx_sopttax | ART | 是 | sopttax_kind, ordinal, sopttax_kind, ordinal |
| idx_sopttax | 默认 | 否 |  |
| idx_sopttax | ART | 是 | sopttax_kind, ordinal, sopttax_kind, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sopttax | sopttax_kind, ordinal, sopttax_kind, ordinal |
| idx_sopttax | sopttax_kind, ordinal, sopttax_kind, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:26:13 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:05:38 | V3.0.5.1016 |  | 物理表usps_sopt_tax，添加了表字段(update_date);
物理表usps_sopt_tax，添加了表... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:26:13 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:05:38 | V3.0.5.1016 |  | 物理表usps_sopt_tax，添加了表字段(update_date);
物理表usps_sopt_tax，添加了表... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

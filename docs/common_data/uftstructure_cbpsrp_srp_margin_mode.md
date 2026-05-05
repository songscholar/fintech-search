# srp_margin_mode - 股票质押履约比公式表

**表对象ID**: 2651
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | margin_num | 否 |  |  |
| 2 | margin_mode_name | 否 |  |  |
| 3 | formula_numerator | 否 |  |  |
| 4 | formula_denominator | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | margin_num | 否 |  |  |
| 10 | margin_mode_name | 否 |  |  |
| 11 | formula_numerator | 否 |  |  |
| 12 | formula_denominator | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_margin_mode | 默认 | 否 |  |
| idx_srp_margin_mode | ART | 是 | margin_num, margin_num |
| idx_srp_margin_mode | 默认 | 否 |  |
| idx_srp_margin_mode | ART | 是 | margin_num, margin_num |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_margin_mode | margin_num, margin_num |
| idx_srp_margin_mode | margin_num, margin_num |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:00:27 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:38:53 | 3.0.2.6 | taocong45644 | 当前表srp_margin_mode，修改了索引idx_srp_margin_mode,索引字段修改为：(margin_... |
| 2025-02-19 17:36:15 | 3.0.3.8 | 李想 | 新增表 |
| 2026-03-06 17:00:27 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:38:53 | 3.0.2.6 | taocong45644 | 当前表srp_margin_mode，修改了索引idx_srp_margin_mode,索引字段修改为：(margin_... |
| 2025-02-19 17:36:15 | 3.0.3.8 | 李想 | 新增表 |

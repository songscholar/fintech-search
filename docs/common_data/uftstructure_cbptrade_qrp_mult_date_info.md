# qrp_mult_date_info - 报价在途日期表

**表对象ID**: 2342
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | qrp_date_type | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | settle_start_date | 否 |  |  |
| 5 | settle_due_date | 否 |  |  |
| 6 | nominal_end_date | 否 |  |  |
| 7 | real_end_date | 否 |  |  |
| 8 | qrp_date_type | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | settle_start_date | 否 |  |  |
| 12 | settle_due_date | 否 |  |  |
| 13 | nominal_end_date | 否 |  |  |
| 14 | real_end_date | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_mult_date_info | 默认 | 否 |  |
| idx_qrp_mult_date_info | ART | 是 | qrp_date_type, exchange_type, init_date, qrp_date_type, exchange_type, init_date |
| idx_qrp_mult_date_info | 默认 | 否 |  |
| idx_qrp_mult_date_info | ART | 是 | qrp_date_type, exchange_type, init_date, qrp_date_type, exchange_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_mult_date_info | qrp_date_type, exchange_type, init_date, qrp_date_type, exchange_type, init_date |
| idx_qrp_mult_date_info | qrp_date_type, exchange_type, init_date, qrp_date_type, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:33:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-09-05 10:42:25 | V3.0.2.14 | 曾剑辉 | 新增表结构 |
| 2026-03-04 15:33:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-09-05 10:42:25 | V3.0.2.14 | 曾剑辉 | 新增表结构 |

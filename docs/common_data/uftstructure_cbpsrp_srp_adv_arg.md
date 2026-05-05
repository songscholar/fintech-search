# srp_adv_arg - 股票质押预约参数表

**表对象ID**: 2634
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | srp_kind | 否 |  |  |
| 3 | adv_open_date_str | 否 |  |  |
| 4 | entrust_begin_num | 否 |  |  |
| 5 | entrust_end_num | 否 |  |  |
| 6 | check_end_time | 否 |  |  |
| 7 | begin_time | 否 |  |  |
| 8 | end_time | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | company_no | 否 |  |  |
| 11 | srp_kind | 否 |  |  |
| 12 | adv_open_date_str | 否 |  |  |
| 13 | entrust_begin_num | 否 |  |  |
| 14 | entrust_end_num | 否 |  |  |
| 15 | check_end_time | 否 |  |  |
| 16 | begin_time | 否 |  |  |
| 17 | end_time | 否 |  |  |
| 18 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpadvarg | ART | 是 | company_no, srp_kind, company_no, srp_kind |
| idx_srpadvarg | ART | 是 | company_no, srp_kind, company_no, srp_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpadvarg | company_no, srp_kind, company_no, srp_kind |
| idx_srpadvarg | company_no, srp_kind, company_no, srp_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:57:57 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:07 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:57:57 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:07 | 3.0.3.1 | wuxd | 新增 |

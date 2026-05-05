# fund_busin_settle_jour - 资金业务清算流水表

**表对象ID**: 5579
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | business_settle_no | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | curr_date | 否 |  |  |
| 9 | curr_time | 否 |  |  |
| 10 | business_settle_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_transsettlejour | ART | 是 | init_date, business_settle_no, init_date, business_settle_no |
| idx_transsettlejour | ART | 是 | init_date, business_settle_no, init_date, business_settle_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_transsettlejour | init_date, business_settle_no, init_date, business_settle_no |
| idx_transsettlejour | init_date, business_settle_no, init_date, business_settle_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:30:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 13:00:00 | 3.0.6.1002 | 范文浩 | 新增 |
| 2026-03-09 14:30:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 13:00:00 | 3.0.6.1002 | 范文浩 | 新增 |

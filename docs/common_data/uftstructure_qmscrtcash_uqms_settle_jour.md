# uqms_settle_jour - 头寸清算流水表

**表对象ID**: 1009
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | settle_no | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | curr_date | 否 |  |  |
| 9 | curr_time | 否 |  |  |
| 10 | settle_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_settle_jour | ART | 是 | settle_no, init_date, settle_no, init_date |
| idx_uqms_settle_jour | ART | 是 | settle_no, init_date, settle_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_settle_jour | settle_no, init_date, settle_no, init_date |
| idx_uqms_settle_jour | settle_no, init_date, settle_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:55:04 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-07 09:13:21 | 3.0.2.1 | 沈勋 | 新增表结构 |
| 2026-03-05 16:55:04 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-07 09:13:21 | 3.0.2.1 | 沈勋 | 新增表结构 |

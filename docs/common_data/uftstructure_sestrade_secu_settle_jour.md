# secu_settle_jour - 证券交易清算流水表

**表对象ID**: 5971
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

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
| idx_secusettlejour | ART | 是 | settle_no, init_date, settle_no, init_date |
| idx_secusettlejour | ART | 是 | settle_no, init_date, settle_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secusettlejour | settle_no, init_date, settle_no, init_date |
| idx_secusettlejour | settle_no, init_date, settle_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:48:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-01-10 13:23:07 | 3.0.2.55 | 於达 | 物理表secu_settle_jour，添加了表字段(fund_account);
 |
| 2024-12-21 13:55:21 | 3.0.2.53 | maty | 物理表secu_settle_jour，添加了表字段(init_date);
物理表secu_settle_jour，... |
| 2026-03-09 14:48:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-01-10 13:23:07 | 3.0.2.55 | 於达 | 物理表secu_settle_jour，添加了表字段(fund_account);
 |
| 2024-12-21 13:55:21 | 3.0.2.53 | maty | 物理表secu_settle_jour，添加了表字段(init_date);
物理表secu_settle_jour，... |

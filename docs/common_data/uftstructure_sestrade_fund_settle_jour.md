# fund_settle_jour - 资金交易清算流水表

**表对象ID**: 5576
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | finance_type | 否 |  |  |
| 5 | settle_no | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | curr_date | 否 |  |  |
| 10 | curr_time | 否 |  |  |
| 11 | finance_type | 否 |  |  |
| 12 | settle_no | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_settle_jour | ART | 是 | settle_no, finance_type, init_date, settle_no, finance_type, init_date |
| idx_fund_settle_jour | ART | 是 | settle_no, finance_type, init_date, settle_no, finance_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_settle_jour | settle_no, finance_type, init_date, settle_no, finance_type, init_date |
| idx_fund_settle_jour | settle_no, finance_type, init_date, settle_no, finance_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:26:22 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 16:16:24 | 3.0.6.1001 | 杨森峰 | 物理表fund_settle_jour，添加了表字段(fund_account);
 |
| 2024-12-21 16:12:41 | 3.0.2.53 | 杨森峰 | 重新支持fund_settle_jour表日间回库 |
| 2024-11-07 16:49:28 | 3.0.5.1059 | 雷玄 | 修改fund_settle_jour表日间不回库 |
| 2024-10-23 18:11:47 | 3.0.5.1053 | 洪略 | 新增 |
| 2026-03-09 14:26:22 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-05-19 16:16:24 | 3.0.6.1001 | 杨森峰 | 物理表fund_settle_jour，添加了表字段(fund_account);
 |
| 2024-12-21 16:12:41 | 3.0.2.53 | 杨森峰 | 重新支持fund_settle_jour表日间回库 |
| 2024-11-07 16:49:28 | 3.0.5.1059 | 雷玄 | 修改fund_settle_jour表日间不回库 |
| 2024-10-23 18:11:47 | 3.0.5.1053 | 洪略 | 新增 |

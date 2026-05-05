# uses_fund_interest_total - 证券资金利息入账汇总表

**表对象ID**: 5584
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | interest | 否 |  |  |
| 6 | fine_interest | 否 |  |  |
| 7 | position_str | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | interest | 否 |  |  |
| 13 | fine_interest | 否 |  |  |
| 14 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_fund_interest_total | ART | 是 | init_date, position_str, init_date, position_str |
| idx_uses_fund_interest_total | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_fund_interest_total | init_date, position_str, init_date, position_str |
| idx_uses_fund_interest_total | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:32:45 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-08 10:40:17 | 3.0.2.79 | yusz | 新增 |
| 2026-03-09 14:32:45 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-08 10:40:17 | 3.0.2.79 | yusz | 新增 |

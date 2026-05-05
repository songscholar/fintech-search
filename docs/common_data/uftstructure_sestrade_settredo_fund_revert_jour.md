# settredo_fund_revert_jour - 清算重做资金反向操作流水表

**表对象ID**: 5803
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | treat_status | 否 |  |  |
| 2 | valid_date | 否 |  |  |
| 3 | position_str | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | treat_status | 否 |  |  |
| 6 | valid_date | 否 |  |  |
| 7 | position_str | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_fundrevertjour | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_fundrevertjour | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_fundrevertjour | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_fundrevertjour | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:44:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-13 10:00:54 | 3.0.2.1019 | yangxz | 新增表结构 |
| 2026-03-09 14:44:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-13 10:00:54 | 3.0.2.1019 | yangxz | 新增表结构 |

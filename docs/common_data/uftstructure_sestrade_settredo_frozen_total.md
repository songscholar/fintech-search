# settredo_frozen_total - 清算重做冻结汇总表

**表对象ID**: 5586
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | ordinal | 否 |  |  |
| 2 | sett_dml_type | 否 |  |  |
| 3 | sett_batch_no | 否 |  |  |
| 4 | ordinal | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_frozen_total | 默认 | 否 |  |
| idx_settredo_frozen_total | ART | 是 | ordinal, ordinal |
| idx_settredo_frozen_total | 默认 | 否 |  |
| idx_settredo_frozen_total | ART | 是 | ordinal, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_frozen_total | ordinal, ordinal |
| idx_settredo_frozen_total | ordinal, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:34:25 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:25:02 | 3.0.2.104 | taocong45644 | 当前表settredo_frozen_total，修改了索引idx_settredo_frozen_total,索引字段... |
| 2025-10-27 14:35:32 | V3.0.8.8 | taocong45644 |  |
| 2026-03-09 14:34:25 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:25:02 | 3.0.2.104 | taocong45644 | 当前表settredo_frozen_total，修改了索引idx_settredo_frozen_total,索引字段... |
| 2025-10-27 14:35:32 | V3.0.8.8 | taocong45644 |  |

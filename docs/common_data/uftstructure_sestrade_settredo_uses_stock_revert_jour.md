# settredo_uses_stock_revert_jour - 清算重做证券反向操作流水表

**表对象ID**: 5805
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | treat_status | 否 |  |  |
| 5 | valid_date | 否 |  |  |
| 6 | sett_dml_type | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | serial_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | treat_status | 否 |  |  |
| 12 | valid_date | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_stockrevertjour | 默认 | 否 |  |
| idx_settredo_stockrevertjour | ART | 是 | sett_batch_no, serial_no, init_date, branch_no, sett_batch_no, serial_no, init_date, branch_no |
| idx_settredo_stockrevertjour | 默认 | 否 |  |
| idx_settredo_stockrevertjour | ART | 是 | sett_batch_no, serial_no, init_date, branch_no, sett_batch_no, serial_no, init_date, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_stockrevertjour | serial_no, init_date, branch_no, sett_batch_no, serial_no, init_date, branch_no, sett_batch_no |
| idx_settredo_stockrevertjour | serial_no, init_date, branch_no, sett_batch_no, serial_no, init_date, branch_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:45:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:25:54 | 3.0.2.104 | taocong45644 | 当前表settredo_uses_stock_revert_jour，修改了索引idx_settredo_stockre... |
| 2025-08-13 10:01:24 | 3.0.2.1019 | yangxz | 新增表结构 |
| 2026-03-09 14:45:26 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:25:54 | 3.0.2.104 | taocong45644 | 当前表settredo_uses_stock_revert_jour，修改了索引idx_settredo_stockre... |
| 2025-08-13 10:01:24 | 3.0.2.1019 | yangxz | 新增表结构 |

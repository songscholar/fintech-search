# settredo_uses_ffare_log - 清算重做证券前台费用日志表

**表对象ID**: 5996
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | prev_status | 否 |  |  |
| 2 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 3 | sett_batch_no | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | data_src | 否 |  |  |
| 6 | prev_status | 否 |  |  |
| 7 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 8 | sett_batch_no | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | data_src | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_ffare_log | 默认 | 否 |  |
| idx_settredo_ffare_log | ART | 是 | sett_batch_no, position_str, data_src, sett_batch_no, position_str, data_src |
| idx_settredo_ffare_log | 默认 | 否 |  |
| idx_settredo_ffare_log | ART | 是 | sett_batch_no, position_str, data_src, sett_batch_no, position_str, data_src |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_ffare_log | sett_batch_no, position_str, data_src, sett_batch_no, position_str, data_src |
| idx_settredo_ffare_log | sett_batch_no, position_str, data_src, sett_batch_no, position_str, data_src |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:56:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-01 15:06:30 | 3.0.2.1005 | yangxz | 当前表settredo_uses_ffare_log，修改了索引idx_settredo_ffare_log,索引字段修... |
| 2025-09-01 15:05:15 | 3.0.2.1004 | yangxz | 所有表settredo_uses_ffare_log，添加了表字段(data_src);
所有表settredo_us... |
| 2025-07-24 09:40:31 | 3.0.2.1003 | yangxz |  |
| 2026-03-09 14:56:57 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-01 15:06:30 | 3.0.2.1005 | yangxz | 当前表settredo_uses_ffare_log，修改了索引idx_settredo_ffare_log,索引字段修... |
| 2025-09-01 15:05:15 | 3.0.2.1004 | yangxz | 所有表settredo_uses_ffare_log，添加了表字段(data_src);
所有表settredo_us... |
| 2025-07-24 09:40:31 | 3.0.2.1003 | yangxz |  |

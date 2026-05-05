# settredo_uses_ext_fare_log - 清算重做额外费用日志表

**表对象ID**: 5806
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | status | 否 |  |  |
| 2 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 3 | sett_batch_no | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | status | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | sett_dml_type | 否 |  |  |
| 9 | status | 否 |  |  |
| 10 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 11 | sett_batch_no | 否 |  |  |
| 12 | sett_dml_type | 否 |  |  |
| 13 | status | 否 |  |  |
| 14 | position_str | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | sett_dml_type | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_extfare_log | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_extfare_log | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_extfare_log | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-24 09:40:31 | 3.0.0.1 | yangxz | 添加表 |
| 2025-07-24 09:40:31 | 3.0.0.1 | yangxz |  |
| 2025-07-24 09:40:31 | 3.0.0.1 | yangxz | 添加表 |
| 2025-07-24 09:40:31 | 3.0.0.1 | yangxz |  |

# sett_common_rollback - 清算公共回滚表

**表对象ID**: 504
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | table_name | 否 |  |  |
| 4 | position_str | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | table_name | 否 |  |  |
| 8 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_common_rollback | 默认 | 否 |  |
| idx_sett_common_rollback | ART | 是 | sett_batch_no, table_name, position_str, sett_batch_no, table_name, position_str |
| idx_sett_common_rollback | 默认 | 否 |  |
| idx_sett_common_rollback | ART | 是 | sett_batch_no, table_name, position_str, sett_batch_no, table_name, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_common_rollback | sett_batch_no, table_name, position_str, sett_batch_no, table_name, position_str |
| idx_sett_common_rollback | sett_batch_no, table_name, position_str, sett_batch_no, table_name, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:48:54 | 3.0.2.103 | taocong45644 | 当前表sett_common_rollback，修改了索引idx_sett_common_rollback,索引字段修改... |
| 2025-09-16 14:58:33 | V3.0.2.2 | 李奕轩 | 表空间改成uarg |
| 2025-08-22 15:42:03 | 3.0.2.1 | 曾阳璞 | 调整为DB+MDB模式 |
| 2025-12-01 14:48:54 | 3.0.2.103 | taocong45644 | 当前表sett_common_rollback，修改了索引idx_sett_common_rollback,索引字段修改... |
| 2025-09-16 14:58:33 | V3.0.2.2 | 李奕轩 | 表空间改成uarg |
| 2025-08-22 15:42:03 | 3.0.2.1 | 曾阳璞 | 调整为DB+MDB模式 |

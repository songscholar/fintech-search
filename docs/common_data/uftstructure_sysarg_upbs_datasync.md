# upbs_datasync - 数据同步表

**表对象ID**: 11
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_name | 否 |  |  |
| 2 | dataload_str | 否 |  |  |
| 3 | dataload_type | 否 |  |  |
| 4 | enable_status | 否 |  |  |
| 5 | data_source | 否 |  |  |
| 6 | data_reload_type | 否 |  |  |
| 7 | sql_str | 否 |  |  |
| 8 | table_name | 否 |  |  |
| 9 | dataload_str | 否 |  |  |
| 10 | dataload_type | 否 |  |  |
| 11 | enable_status | 否 |  |  |
| 12 | data_source | 否 |  |  |
| 13 | data_reload_type | 否 |  |  |
| 14 | sql_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_datasync | ART | 是 | table_name, table_name |
| idx_upbs_datasync | ART | 是 | table_name, table_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_datasync | table_name, table_name |
| idx_upbs_datasync | table_name, table_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-15 08:40:30 | 3.0.2.95 | 王云乾 | 所有表upbs_datasync，添加了表字段(sql_str);
 |
| 2025-03-07 15:46:58 | 3.0.2.77 | 谢宗艺 | 新增字段data_reload_type |
| 2024-09-06 15:35:10 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-15 08:40:30 | 3.0.2.95 | 王云乾 | 所有表upbs_datasync，添加了表字段(sql_str);
 |
| 2025-03-07 15:46:58 | 3.0.2.77 | 谢宗艺 | 新增字段data_reload_type |
| 2024-09-06 15:35:10 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

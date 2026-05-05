# upbs_data_persistence - 数据持久化表

**表对象ID**: 91
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_name | 否 |  |  |
| 2 | datapersistence_str | 否 |  |  |
| 3 | datapersistence_type | 否 |  |  |
| 4 | data_scale_level | 否 |  |  |
| 5 | dp_column_str | 否 |  |  |
| 6 | sync_force_flag | 否 |  |  |
| 7 | enable_status | 否 |  |  |
| 8 | table_name | 否 |  |  |
| 9 | datapersistence_str | 否 |  |  |
| 10 | datapersistence_type | 否 |  |  |
| 11 | data_scale_level | 否 |  |  |
| 12 | dp_column_str | 否 |  |  |
| 13 | sync_force_flag | 否 |  |  |
| 14 | enable_status | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_datapersist | ART | 是 | table_name, table_name |
| idx_upbs_datapersist_level | ART | 是 | data_scale_level, data_scale_level |
| idx_upbs_datapersist | ART | 是 | table_name, table_name |
| idx_upbs_datapersist_level | ART | 是 | data_scale_level, data_scale_level |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_datapersist | table_name, table_name |
| idx_upbs_datapersist | table_name, table_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-09 11:04:20 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-23 15:15:51 | V3.0.1.23 | 黄积冲 | 新增表upbs_data_persistence |
| 2024-09-09 11:04:20 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-12-23 15:15:51 | V3.0.1.23 | 黄积冲 | 新增表upbs_data_persistence |

# upbs_datadiff - 回库数据差异表

**表对象ID**: 508
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | table_name | 否 |  |  |
| 4 | where_str | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | partition_no | 否 |  |  |
| 7 | deal_status | 否 |  |  |
| 8 | ordinal | 否 |  |  |
| 9 | init_date | 否 |  |  |
| 10 | serial_no | 否 |  |  |
| 11 | table_name | 否 |  |  |
| 12 | where_str | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | partition_no | 否 |  |  |
| 15 | deal_status | 否 |  |  |
| 16 | ordinal | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_datadiff | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_upbs_datadiff_table | ART | 是 | table_name, ordinal, table_name, ordinal |
| idx_upbs_datadiff | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_upbs_datadiff_table | ART | 是 | table_name, ordinal, table_name, ordinal |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_datadiff | init_date, serial_no, init_date, serial_no |
| idx_upbs_datadiff_table | table_name, ordinal, table_name, ordinal |
| idx_upbs_datadiff | init_date, serial_no, init_date, serial_no |
| idx_upbs_datadiff_table | table_name, ordinal, table_name, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-22 10:58:31 | 3.0.6.1002 | 骆鹏程 | 新增表datadiff |
| 2025-08-22 10:58:31 | 3.0.6.1002 | 骆鹏程 | 新增表datadiff |

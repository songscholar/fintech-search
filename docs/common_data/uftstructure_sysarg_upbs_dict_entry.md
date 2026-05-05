# upbs_dict_entry - 字典条目表

**表对象ID**: 75
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | dict_entry | 否 |  |  |
| 2 | manage_level | 否 |  |  |
| 3 | entry_name | 否 |  |  |
| 4 | access_level | 否 |  |  |
| 5 | dict_type | 否 |  |  |
| 6 | dict_kind | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | dict_entry | 否 |  |  |
| 9 | manage_level | 否 |  |  |
| 10 | entry_name | 否 |  |  |
| 11 | access_level | 否 |  |  |
| 12 | dict_type | 否 |  |  |
| 13 | dict_kind | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_dict_entry | ART | 是 | dict_entry, dict_entry |
| idx_upbs_dict_entry | ART | 是 | dict_entry, dict_entry |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_dict_entry | dict_entry, dict_entry |
| idx_upbs_dict_entry | dict_entry, dict_entry |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 13:59:01 | 8.26.2.99 | 汪杰 | 表空间修改为hs_uft_data |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2026-01-05 13:59:01 | 8.26.2.99 | 汪杰 | 表空间修改为hs_uft_data |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

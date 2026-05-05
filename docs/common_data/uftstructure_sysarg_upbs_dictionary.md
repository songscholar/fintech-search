# upbs_dictionary - 数据字典表

**表对象ID**: 74
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | dict_entry | 否 |  |  |
| 3 | dict_type | 否 |  |  |
| 4 | sub_entry | 否 |  |  |
| 5 | access_level | 否 |  |  |
| 6 | dict_prompt | 否 |  |  |
| 7 | dictionary_flag | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | dict_entry | 否 |  |  |
| 11 | dict_type | 否 |  |  |
| 12 | sub_entry | 否 |  |  |
| 13 | access_level | 否 |  |  |
| 14 | dict_prompt | 否 |  |  |
| 15 | dictionary_flag | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_dictionary_uniq | 默认 | 否 | sub_entry, sub_entry |
| idx_upbs_dictionary_normal | 默认 | 否 | branch_no, branch_no |
| idx_upbs_dictionary_uniq | ART | 是 | dict_entry, sub_entry, dict_entry, sub_entry |
| idx_upbs_dictionary_normal | ART | 是 | branch_no, branch_no |
| idx_upbs_dictionary_uniq | 默认 | 否 | sub_entry, sub_entry |
| idx_upbs_dictionary_normal | 默认 | 否 | branch_no, branch_no |
| idx_upbs_dictionary_uniq | ART | 是 | dict_entry, sub_entry, dict_entry, sub_entry |
| idx_upbs_dictionary_normal | ART | 是 | branch_no, branch_no |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_dictionary | dict_entry, sub_entry, dict_entry, sub_entry |
| idx_upbs_dictionary_uniq | sub_entry, sub_entry |
| idx_upbs_dictionary_normal | branch_no, branch_no |
| idx_upbs_dictionary | dict_entry, sub_entry, dict_entry, sub_entry |
| idx_upbs_dictionary_uniq | sub_entry, sub_entry |
| idx_upbs_dictionary_normal | branch_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 13:58:22 | 8.26.2.98 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-07-17 13:55:47 | 3.0.6.1015 | 常行 | 物理表upbs_dictionary，增加索引(idx_upbs_dictionary_uniq:[sub_entry]... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2026-01-05 13:58:22 | 8.26.2.98 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-07-17 13:55:47 | 3.0.6.1015 | 常行 | 物理表upbs_dictionary，增加索引(idx_upbs_dictionary_uniq:[sub_entry]... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

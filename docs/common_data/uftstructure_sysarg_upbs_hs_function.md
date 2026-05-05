# upbs_hs_function - 证券系统功能表

**表对象ID**: 15
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | en_sys_status | 否 |  |  |
| 2 | func_flag_str | 否 |  |  |
| 3 | function_id | 否 |  |  |
| 4 | password_type | 否 |  |  |
| 5 | restend_time | 否 |  |  |
| 6 | reststart_time | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | func_busi_type | 否 |  |  |
| 9 | right_type | 否 |  |  |
| 10 | transaction_str | 否 |  |  |
| 11 | en_sys_status | 否 |  |  |
| 12 | func_flag_str | 否 |  |  |
| 13 | function_id | 否 |  |  |
| 14 | password_type | 否 |  |  |
| 15 | restend_time | 否 |  |  |
| 16 | reststart_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | func_busi_type | 否 |  |  |
| 19 | right_type | 否 |  |  |
| 20 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_hs_function | ART | 是 | function_id, function_id |
| idx_upbs_hs_function | ART | 是 | function_id, function_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_hs_function | function_id, function_id |
| idx_upbs_hs_function | function_id, function_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 14:00:29 | 8.26.2.101 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:52:17 | 3.0.6.1004 | 汪迎 | 物理表upbs_hs_function，添加了表字段(transaction_str);
 |
| 2025-05-19 19:58:16 | 3.0.6.139 |  | 物理表upbs_hs_function，添加了表字段(right_type);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:02 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2026-01-05 14:00:29 | 8.26.2.101 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:52:17 | 3.0.6.1004 | 汪迎 | 物理表upbs_hs_function，添加了表字段(transaction_str);
 |
| 2025-05-19 19:58:16 | 3.0.6.139 |  | 物理表upbs_hs_function，添加了表字段(right_type);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:02 | 0.0.0.5 | 吴威 | 新增字段transaction_no |

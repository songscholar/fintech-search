# polling_log - 轮询日志表

**表对象ID**: 308
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | curr_microtime | 否 |  |  |
| 3 | entrust_no | 否 |  |  |
| 4 | position_str | 否 |  |  |
| 5 | polling_stage | 否 |  |  |
| 6 | function_no | 否 |  |  |
| 7 | table_category | 否 |  |  |
| 8 | curr_microtime | 否 |  |  |
| 9 | entrust_no | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | polling_stage | 否 |  |  |
| 12 | function_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_polling_log | ART | 是 | table_category, position_str, function_no, table_category, position_str, function_no |
| idx_polling_log | ART | 是 | table_category, position_str, function_no, table_category, position_str, function_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_polling_log | table_category, position_str, function_no, table_category, position_str, function_no |
| idx_polling_log | table_category, position_str, function_no, table_category, position_str, function_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-01-14 10:51:06 | 3.0.2.50 | 李江霖 | 增加function_no为表字段和索引字段 |
| 2024-12-27 13:30:41 | 3.0.2.49 | 钟兆星 | polling_log表不落redo，修复缺陷ZQNCJYIII-2612 |
| 2024-11-12 09:45:13 | 3.0.5.1003 | 杨涛 | polling_log落Redo文件 |
| 2024-06-27 21:00:45 | 3.0.2.15 | 泮新国 | polling_log不回库,不落Redo文件 |
| 2024-05-31 14:04:43 | 3.0.2.13 | 泮新国 | 支持回库和落Redo文件 |
| 2024-05-27 15:53:28 | 3.0.2.9 | 张云焘 | 新增 |
| 2025-01-14 10:51:06 | 3.0.2.50 | 李江霖 | 增加function_no为表字段和索引字段 |
| 2024-12-27 13:30:41 | 3.0.2.49 | 钟兆星 | polling_log表不落redo，修复缺陷ZQNCJYIII-2612 |
| 2024-11-12 09:45:13 | 3.0.5.1003 | 杨涛 | polling_log落Redo文件 |
| 2024-06-27 21:00:45 | 3.0.2.15 | 泮新国 | polling_log不回库,不落Redo文件 |
| 2024-05-31 14:04:43 | 3.0.2.13 | 泮新国 | 支持回库和落Redo文件 |
| 2024-05-27 15:53:28 | 3.0.2.9 | 张云焘 | 新增 |

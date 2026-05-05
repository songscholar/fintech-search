# upbs_syncinfo - 参数账户同步流水表

**表对象ID**: 64
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | app_name | 否 |  |  |
| 6 | reply_status | 否 |  |  |
| 7 | error_no | 否 |  |  |
| 8 | error_info | 否 |  |  |
| 9 | table_category | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | curr_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | app_name | 否 |  |  |
| 14 | reply_status | 否 |  |  |
| 15 | error_no | 否 |  |  |
| 16 | error_info | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_syncinfo_no | ART | 是 | table_category, position_str, transaction_no, app_name, table_category, position_str, transaction_no, app_name |
| idx_upbs_syncinfo_no | ART | 是 | table_category, position_str, transaction_no, app_name, table_category, position_str, transaction_no, app_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_syncinfo_no | table_category, position_str, transaction_no, app_name, table_category, position_str, transaction_no, app_name |
| idx_upbs_syncinfo_no | table_category, position_str, transaction_no, app_name, table_category, position_str, transaction_no, app_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-23 14:36:50 | 3.0.2.1 | 周富安 | 修改分级索引idx_upbs_syncinfo_no |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-15 10:39 | 0.3.3.133 | 吴威 | 删除唯一索引idx_upbs_syncinfo |
| 2023-07-27 16:14 | 0.0.0.15 | 徐志坚 | 修改分级索引idx_upbs_syncinfo_no |
| 2023-06-14 21:17 | 0.0.0.9 | 吴威 | 唯一索引新增字段position_str |
| 2023-06-06 15:54 | 0.0.0.5 | 吴威 | 新增upbs_syncinfo |
| 2025-04-23 14:36:50 | 3.0.2.1 | 周富安 | 修改分级索引idx_upbs_syncinfo_no |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-15 10:39 | 0.3.3.133 | 吴威 | 删除唯一索引idx_upbs_syncinfo |
| 2023-07-27 16:14 | 0.0.0.15 | 徐志坚 | 修改分级索引idx_upbs_syncinfo_no |
| 2023-06-14 21:17 | 0.0.0.9 | 吴威 | 唯一索引新增字段position_str |
| 2023-06-06 15:54 | 0.0.0.5 | 吴威 | 新增upbs_syncinfo |

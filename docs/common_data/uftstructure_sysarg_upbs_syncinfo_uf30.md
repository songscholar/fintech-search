# upbs_syncinfo_uf30 - 参数账户同步流水表_uf30

**表对象ID**: 148
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | transaction_str | 否 |  |  |
| 5 | app_name | 否 |  |  |
| 6 | reply_status | 否 |  |  |
| 7 | error_no | 否 |  |  |
| 8 | error_info | 否 |  |  |
| 9 | table_category | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | curr_time | 否 |  |  |
| 12 | transaction_str | 否 |  |  |
| 13 | app_name | 否 |  |  |
| 14 | reply_status | 否 |  |  |
| 15 | error_no | 否 |  |  |
| 16 | error_info | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_syncinfo_str | 默认 | 否 |  |
| idx_upbs_syncinfo_str | ART | 是 | table_category, position_str, transaction_str, app_name, table_category, position_str, transaction_str, app_name |
| idx_upbs_syncinfo_str | 默认 | 否 |  |
| idx_upbs_syncinfo_str | ART | 是 | table_category, position_str, transaction_str, app_name, table_category, position_str, transaction_str, app_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_syncinfo_str | table_category, position_str, transaction_str, app_name, table_category, position_str, transaction_str, app_name |
| idx_upbs_syncinfo_str | table_category, position_str, transaction_str, app_name, table_category, position_str, transaction_str, app_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:37:33 | 3.0.2.103 | taocong45644 | 当前表upbs_syncinfo_uf30，修改了索引idx_upbs_syncinfo_str,索引字段修改为：(ta... |
| 2024-09-18 13:41:31 | V3.0.3.8 | 韦子晗 | 新增upbs_syninfo_uf30表 |
| 2025-12-01 15:37:33 | 3.0.2.103 | taocong45644 | 当前表upbs_syncinfo_uf30，修改了索引idx_upbs_syncinfo_str,索引字段修改为：(ta... |
| 2024-09-18 13:41:31 | V3.0.3.8 | 韦子晗 | 新增upbs_syninfo_uf30表 |

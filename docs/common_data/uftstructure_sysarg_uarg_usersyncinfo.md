# uarg_usersyncinfo - 用户同步异常信息表

**表对象ID**: 139
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | table_name | 否 |  |  |
| 3 | where_str | 否 |  |  |
| 4 | param_oper_type | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | transaction_status | 否 |  |  |
| 7 | curr_time | 否 |  |  |
| 8 | curr_date | 否 |  |  |
| 9 | error_no | 否 |  |  |
| 10 | error_info | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | partition_no | 否 |  |  |
| 13 | send_count | 否 |  |  |
| 14 | table_category | 否 |  |  |
| 15 | table_name | 否 |  |  |
| 16 | where_str | 否 |  |  |
| 17 | param_oper_type | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | transaction_status | 否 |  |  |
| 20 | curr_time | 否 |  |  |
| 21 | curr_date | 否 |  |  |
| 22 | error_no | 否 |  |  |
| 23 | error_info | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | partition_no | 否 |  |  |
| 26 | send_count | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_usersyncinfo | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| uk_rpt_uargusersyncinfo | ART | 是 | date_clear, table_category, transaction_no, date_clear, table_category, transaction_no |
| idx_uarg_usersyncinfo | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| uk_rpt_uargusersyncinfo | ART | 是 | date_clear, table_category, transaction_no, date_clear, table_category, transaction_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_usersyncinfo | table_category, transaction_no, table_category, transaction_no |
| idx_uarg_usersyncinfo | table_category, transaction_no, table_category, transaction_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-15 15:13:06 | 8.26.2.107 | 袁文龙 | 修改idx_uarg_usersyncinfo为ART唯一索引 |
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-22 14:42:20 | 3.0.6.118 | 李想 | 新增表 |
| 2026-01-15 15:13:06 | 8.26.2.107 | 袁文龙 | 修改idx_uarg_usersyncinfo为ART唯一索引 |
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-22 14:42:20 | 3.0.6.118 | 李想 | 新增表 |

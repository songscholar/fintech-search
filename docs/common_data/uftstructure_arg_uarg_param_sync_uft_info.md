# uarg_param_sync_uft_info - 参数同步极速系统流水表

**表对象ID**: 608
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | transaction_no | 否 |  |  |
| 3 | transaction_status | 否 |  |  |
| 4 | table_name | 否 |  |  |
| 5 | where_str | 否 |  |  |
| 6 | param_oper_type | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_time | 否 |  |  |
| 9 | error_no | 否 |  |  |
| 10 | error_info | 否 |  |  |
| 11 | send_count | 否 |  |  |
| 12 | date_clear | 否 |  |  |
| 13 | current_page | 否 |  |  |
| 14 | system_no | 否 |  |  |
| 15 | table_category | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | transaction_status | 否 |  |  |
| 18 | table_name | 否 |  |  |
| 19 | where_str | 否 |  |  |
| 20 | param_oper_type | 否 |  |  |
| 21 | curr_date | 否 |  |  |
| 22 | curr_time | 否 |  |  |
| 23 | error_no | 否 |  |  |
| 24 | error_info | 否 |  |  |
| 25 | send_count | 否 |  |  |
| 26 | date_clear | 否 |  |  |
| 27 | current_page | 否 |  |  |
| 28 | system_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_param_sync_uft_info | ART | 是 | table_category, transaction_no, system_no, table_category, transaction_no, system_no |
| idx_rpt_uarg_param_sync_uft_info | ART | 是 | table_category, transaction_no, date_clear, system_no, table_category, transaction_no, date_clear, system_no |
| idx_uarg_param_sync_uft_info | ART | 是 | table_category, transaction_no, system_no, table_category, transaction_no, system_no |
| idx_rpt_uarg_param_sync_uft_info | ART | 是 | table_category, transaction_no, date_clear, system_no, table_category, transaction_no, date_clear, system_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_param_sync_uft_info | table_category, transaction_no, table_category, transaction_no |
| idx_uarg_param_sync_uft_info | table_category, transaction_no, table_category, transaction_no |

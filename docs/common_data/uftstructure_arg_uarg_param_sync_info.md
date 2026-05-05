# uarg_param_sync_info - 交易参数参数回导流水表

**表对象ID**: 605
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 54 个）

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
| 13 | fund_account | 否 |  |  |
| 14 | table_category | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | transaction_status | 否 |  |  |
| 17 | table_name | 否 |  |  |
| 18 | where_str | 否 |  |  |
| 19 | param_oper_type | 否 |  |  |
| 20 | curr_date | 否 |  |  |
| 21 | curr_time | 否 |  |  |
| 22 | error_no | 否 |  |  |
| 23 | error_info | 否 |  |  |
| 24 | send_count | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | sync_where_str | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | table_category | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | transaction_status | 否 |  |  |
| 31 | table_name | 否 |  |  |
| 32 | where_str | 否 |  |  |
| 33 | param_oper_type | 否 |  |  |
| 34 | curr_date | 否 |  |  |
| 35 | curr_time | 否 |  |  |
| 36 | error_no | 否 |  |  |
| 37 | error_info | 否 |  |  |
| 38 | send_count | 否 |  |  |
| 39 | date_clear | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | table_category | 否 |  |  |
| 42 | transaction_no | 否 |  |  |
| 43 | transaction_status | 否 |  |  |
| 44 | table_name | 否 |  |  |
| 45 | where_str | 否 |  |  |
| 46 | param_oper_type | 否 |  |  |
| 47 | curr_date | 否 |  |  |
| 48 | curr_time | 否 |  |  |
| 49 | error_no | 否 |  |  |
| 50 | error_info | 否 |  |  |
| 51 | send_count | 否 |  |  |
| 52 | fund_account | 否 |  |  |
| 53 | sync_where_str | 否 |  |  |
| 54 | date_clear | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, date_clear, table_category, transaction_no, date_clear |
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| idx_rpt_uarg_param_sync_info | ART | 是 | table_category, transaction_no, date_clear, table_category, transaction_no, date_clear |
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, date_clear, table_category, transaction_no, date_clear |
| idx_uarg_param_sync_info | ART | 是 | table_category, transaction_no, table_category, transaction_no |
| idx_rpt_uarg_param_sync_info | ART | 是 | table_category, transaction_no, date_clear, table_category, transaction_no, date_clear |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 18:23:18 | 3.0.2.4 | 蒋浩宇 | 所有表uarg_param_sync_info，添加了表字段(sync_where_str);
 |
| 2025-12-08 12:12:42 | 3.0.2.3 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-24 16:06:01 | 3.0.2.3 | 洪略 | 增加历史表 |
| 2025-11-28 10:09:15 | 3.0.2.3 | 刘珊珊 | 添加表 添加历史表 |
| 2025-12-08 18:23:18 | 3.0.2.4 | 蒋浩宇 | 所有表uarg_param_sync_info，添加了表字段(sync_where_str);
 |
| 2025-12-08 12:12:42 | 3.0.2.3 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-24 16:06:01 | 3.0.2.3 | 洪略 | 增加历史表 |
| 2025-11-28 10:09:15 | 3.0.2.3 | 刘珊珊 | 添加表 添加历史表 |

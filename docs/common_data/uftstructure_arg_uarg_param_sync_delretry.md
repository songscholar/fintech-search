# uarg_param_sync_delretry - 交易参数参数回导重发信息表

**表对象ID**: 606
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | transaction_no | 否 |  |  |
| 3 | position_str | 否 |  |  |
| 4 | param_name | 否 |  |  |
| 5 | param_type | 否 |  |  |
| 6 | param_width | 否 |  |  |
| 7 | param_scale | 否 |  |  |
| 8 | param_value | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | table_category | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  |  |
| 13 | param_name | 否 |  |  |
| 14 | param_type | 否 |  |  |
| 15 | param_width | 否 |  |  |
| 16 | param_scale | 否 |  |  |
| 17 | param_value | 否 |  |  |
| 18 | sync_where_str | 否 |  |  |
| 19 | date_clear | 否 |  |  |
| 20 | table_category | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | param_name | 否 |  |  |
| 24 | param_type | 否 |  |  |
| 25 | param_width | 否 |  |  |
| 26 | param_scale | 否 |  |  |
| 27 | param_value | 否 |  |  |
| 28 | date_clear | 否 |  |  |
| 29 | table_category | 否 |  |  |
| 30 | transaction_no | 否 |  |  |
| 31 | position_str | 否 |  |  |
| 32 | param_name | 否 |  |  |
| 33 | param_type | 否 |  |  |
| 34 | param_width | 否 |  |  |
| 35 | param_scale | 否 |  |  |
| 36 | param_value | 否 |  |  |
| 37 | sync_where_str | 否 |  |  |
| 38 | date_clear | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_param_sync_info_bizarg | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |
| idx_uarg_param_sync_delretry | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |
| idx_rpt_uarg_param_sync_delretry | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |
| idx_uarg_param_sync_info_bizarg | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |
| idx_uarg_param_sync_delretry | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |
| idx_rpt_uarg_param_sync_delretry | ART | 是 | table_category, transaction_no, position_str, param_name, table_category, transaction_no, position_str, param_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 18:24:02 | 3.0.2.4 | 蒋浩宇 | 所有表uarg_param_sync_delretry，添加了表字段(sync_where_str);
 |
| 2025-12-08 12:13:24 | 3.0.2.3 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-12-01 15:33:37 | 3.0.2.3 | 蒋浩宇 | 添加表 添加历史表 |
| 2025-12-08 18:24:02 | 3.0.2.4 | 蒋浩宇 | 所有表uarg_param_sync_delretry，添加了表字段(sync_where_str);
 |
| 2025-12-08 12:13:24 | 3.0.2.3 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-12-01 15:33:37 | 3.0.2.3 | 蒋浩宇 | 添加表 添加历史表 |

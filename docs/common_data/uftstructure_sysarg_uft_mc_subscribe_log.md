# uft_mc_subscribe_log - 业务核心消费日志表

**表对象ID**: 388
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | ldp_short_appname | 否 |  |  |
| 5 | param_oper_type | 否 |  |  |
| 6 | table_name | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | table_category | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | ldp_short_appname | 否 |  |  |
| 13 | param_oper_type | 否 |  |  |
| 14 | table_name | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | date_clear | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_mc_subscribe_log | 默认 | 否 |  |
| idx_uft_mc_subscribe_log | ART | 是 | table_category, position_str, transaction_no, ldp_short_appname, table_category, position_str, transaction_no, ldp_short_appname |
| idx_rpt_uft_mc_subscribe_log | ART | 是 | table_category, position_str, transaction_no, ldp_short_appname, init_date, table_category, position_str, transaction_no, ldp_short_appname, init_date |
| idx_uft_mc_subscribe_log | 默认 | 否 |  |
| idx_uft_mc_subscribe_log | ART | 是 | table_category, position_str, transaction_no, ldp_short_appname, table_category, position_str, transaction_no, ldp_short_appname |
| idx_rpt_uft_mc_subscribe_log | ART | 是 | table_category, position_str, transaction_no, ldp_short_appname, init_date, table_category, position_str, transaction_no, ldp_short_appname, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_mc_subscribe_log | table_category, position_str, transaction_no, ldp_short_appname, table_category, position_str, transaction_no, ldp_short_appname |
| idx_uft_mc_subscribe_log | table_category, position_str, transaction_no, ldp_short_appname, table_category, position_str, transaction_no, ldp_short_appname |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-06 13:08:25 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 15:26:48 | 3.0.2.103 | taocong45644 | 当前表uft_mc_subscribe_log，修改了索引idx_uft_mc_subscribe_log,索引字段修改... |
| 2025-07-30 14:19:29 | 3.0.2.89 | 高志强 | 添加表 添加历史表 |
| 2026-01-06 13:08:25 | 3.0.2.105 | 洪略 | 增加历史表 |
| 2025-12-01 15:26:48 | 3.0.2.103 | taocong45644 | 当前表uft_mc_subscribe_log，修改了索引idx_uft_mc_subscribe_log,索引字段修改... |
| 2025-07-30 14:19:29 | 3.0.2.89 | 高志强 | 添加表 添加历史表 |

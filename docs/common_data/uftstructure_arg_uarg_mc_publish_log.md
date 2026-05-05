# uarg_mc_publish_log - 推送消息日志表

**表对象ID**: 602
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | param_oper_type | 否 |  |  |
| 5 | table_name | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | table_category | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | param_oper_type | 否 |  |  |
| 12 | table_name | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | date_clear | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_mc_publish_log | 默认 | 是 | table_category, position_str, transaction_no, table_category, position_str, transaction_no |
| idx_rpt_uarg_mc_publish_log | ART | 是 | init_date, table_category, position_str, transaction_no, init_date, table_category, position_str, transaction_no |
| idx_uarg_mc_publish_log | 默认 | 是 | table_category, position_str, transaction_no, table_category, position_str, transaction_no |
| idx_rpt_uarg_mc_publish_log | ART | 是 | init_date, table_category, position_str, transaction_no, init_date, table_category, position_str, transaction_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-24 19:24:42 | 3.0.2.2 | 洪略 | 增加历史表 |
| 2025-07-30 13:53:19 | 3.0.2.1 | 高志强 | 添加表 添加历史表 |
| 2025-12-24 19:24:42 | 3.0.2.2 | 洪略 | 增加历史表 |
| 2025-07-30 13:53:19 | 3.0.2.1 | 高志强 | 添加表 添加历史表 |

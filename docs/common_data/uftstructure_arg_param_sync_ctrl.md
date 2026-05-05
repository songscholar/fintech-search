# param_sync_ctrl - 内存交易参数回导控制表

**表对象ID**: 604
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | table_name | 否 |  |  |
| 3 | join_table_name | 否 |  | 对应到 UF2.0 的 table_name |
| 4 | sync_flag | 否 |  |  |
| 5 | position_str | 否 |  | table_category |
| 6 | transaction_no | 否 |  |  |
| 7 | table_category | 否 |  |  |
| 8 | table_name | 否 |  |  |
| 9 | join_table_name | 否 |  | 对应到 UF2.0 的 table_name |
| 10 | sync_flag | 否 |  |  |
| 11 | position_str | 否 |  | table_category |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_param_sync_ctrl | ART | 是 | table_category, table_category |
| idx_param_sync_ctrl | ART | 是 | table_category, table_category |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-19 14:13:03 | 3.0.2.2 | 蒋浩宇 | 添加表 |
| 2025-11-19 14:13:03 | 3.0.2.2 | 蒋浩宇 | 添加表 |

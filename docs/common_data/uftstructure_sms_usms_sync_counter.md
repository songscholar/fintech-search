# usms_sync_counter - 交易管理同步事务控制表

**表对象ID**: 2855
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | transaction_str | 否 |  |  |
| 5 | table_category | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | transaction_str | 否 |  |  |
| 9 | table_category | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | transaction_str | 否 |  |  |
| 13 | table_category | 否 |  |  |
| 14 | position_str | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_sync_counter | 默认 | 是 | table_category, position_str, table_category, position_str |
| idx_usms_sync_counter | 默认 | 是 | table_category, position_str, table_category, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-28 14:32:28 | 8.26.2.91 | tongck54118 | 添加表 |
| 2025-08-28 14:32:28 | 8.26.2.91 | tongck54118 | 添加表 |

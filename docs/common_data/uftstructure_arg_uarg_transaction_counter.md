# uarg_transaction_counter - 参数事务号计数表

**表对象ID**: 600
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_category | 否 |  |  |
| 2 | serial_counter_value | 否 |  |  |
| 3 | table_category | 否 |  |  |
| 4 | serial_counter_value | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_transaction_counter | 默认 | 是 | table_category, table_category |
| idx_uarg_transaction_counter | 默认 | 是 | table_category, table_category |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-30 14:23:12 | 3.0.2.1 | 高志强 | 添加表 |
| 2025-07-30 14:23:12 | 3.0.2.1 | 高志强 | 添加表 |

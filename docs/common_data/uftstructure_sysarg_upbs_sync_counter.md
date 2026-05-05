# upbs_sync_counter - 参数账户同步事务控制表

**表对象ID**: 82
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

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

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_sync_counter | ART | 是 | table_category, position_str, table_category, position_str |
| idx_upbs_sync_counter | ART | 是 | table_category, position_str, table_category, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_sync_counter | table_category, position_str, table_category, position_str |
| idx_upbs_sync_counter | table_category, position_str, table_category, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-20 13:20:34 | 3.0.6.139 |  | 物理表upbs_sync_counter，添加了表字段(transaction_str);
 |
| 2023-08-24 19:21:31 | 0.3.3.143 | 徐志坚 | 新增事务控制表用于控制资金帐号、证券帐号等多表合一同步时控制事务用 |
| 2025-05-20 13:20:34 | 3.0.6.139 |  | 物理表upbs_sync_counter，添加了表字段(transaction_str);
 |
| 2023-08-24 19:21:31 | 0.3.3.143 | 徐志坚 | 新增事务控制表用于控制资金帐号、证券帐号等多表合一同步时控制事务用 |

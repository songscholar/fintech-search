# pbs_tradeexport_tables - 清算导出表信息

**表对象ID**: 2513
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | subsys_id | 否 |  |  |
| 2 | table_name | 否 |  |  |
| 3 | table_cname | 否 |  |  |
| 4 | sett_table_name | 否 |  |  |
| 5 | sett_table_cname | 否 |  |  |
| 6 | field_str | 否 |  |  |
| 7 | where_str | 否 |  |  |
| 8 | first_node | 否 |  |  |
| 9 | export_mode | 否 |  |  |
| 10 | order_column | 否 |  |  |
| 11 | enable_status | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | subsys_id | 否 |  |  |
| 14 | table_name | 否 |  |  |
| 15 | table_cname | 否 |  |  |
| 16 | sett_table_name | 否 |  |  |
| 17 | sett_table_cname | 否 |  |  |
| 18 | field_str | 否 |  |  |
| 19 | where_str | 否 |  |  |
| 20 | first_node | 否 |  |  |
| 21 | export_mode | 否 |  |  |
| 22 | order_column | 否 |  |  |
| 23 | enable_status | 否 |  |  |
| 24 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pbs_tradeexport_tables | ART | 是 | subsys_id, table_name, subsys_id, table_name |
| idx_pbs_tradeexport_tables | ART | 是 | subsys_id, table_name, subsys_id, table_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pbs_tradeexport_tables | subsys_id, table_name, subsys_id, table_name |
| idx_pbs_tradeexport_tables | subsys_id, table_name, subsys_id, table_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-28 20:04:30 | 3.0.2.89 | 乐闽庭 | 物理表pbs_tradeexport_tables，添加了表字段(first_node);
物理表pbs_tradee... |
| 2025-06-28 14:02:38 | 3.0.2.88 | zhangyt | 新增支持对接内存清算 |
| 2025-07-28 20:04:30 | 3.0.2.89 | 乐闽庭 | 物理表pbs_tradeexport_tables，添加了表字段(first_node);
物理表pbs_tradee... |
| 2025-06-28 14:02:38 | 3.0.2.88 | zhangyt | 新增支持对接内存清算 |

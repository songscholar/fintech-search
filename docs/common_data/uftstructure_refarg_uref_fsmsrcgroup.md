# uref_fsmsrcgroup - 资券来源组表

**表对象ID**: 6017
**所属模块**: refarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | refsrcgroup_id | 否 |  |  |
| 3 | refsrcgroup_name | 否 |  |  |
| 4 | priority_level | 否 |  |  |
| 5 | refsrc_prop | 否 |  |  |
| 6 | refsrc_ctrlstr | 否 |  |  |
| 7 | auto_publish_flag | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | company_no | 否 |  |  |
| 14 | refsrcgroup_id | 否 |  |  |
| 15 | refsrcgroup_name | 否 |  |  |
| 16 | priority_level | 否 |  |  |
| 17 | refsrc_prop | 否 |  |  |
| 18 | refsrc_ctrlstr | 否 |  |  |
| 19 | auto_publish_flag | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srcgroup | ART | 是 | refsrcgroup_id, refsrcgroup_id |
| idx_srcgroup | ART | 是 | refsrcgroup_id, refsrcgroup_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srcgroup | refsrcgroup_id, refsrcgroup_id |
| idx_srcgroup | refsrcgroup_id, refsrcgroup_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-08 16:44:18 | V3.0.2.3 | 高志强 | 所有表uref_fsmsrcgroup，添加了表字段(transaction_no);
 |
| 2025-07-31 15:55:51 | V3.0.2.1 | 陈征东 | 修改表索引前缀 |
| 2025-09-08 16:44:18 | V3.0.2.3 | 高志强 | 所有表uref_fsmsrcgroup，添加了表字段(transaction_no);
 |
| 2025-07-31 15:55:51 | V3.0.2.1 | 陈征东 | 修改表索引前缀 |

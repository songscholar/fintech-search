# acctdatasync - 客户级数据加载表

**表对象ID**: 7047
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_name | 否 |  |  |
| 2 | dataload_str | 否 |  |  |
| 3 | table_category | 否 |  |  |
| 4 | enable_status | 否 |  |  |
| 5 | dataload_type | 否 |  |  |
| 6 | datasource_type | 否 |  |  |
| 7 | dataload_order | 否 |  |  |
| 8 | table_name | 否 |  |  |
| 9 | dataload_str | 否 |  |  |
| 10 | table_category | 否 |  |  |
| 11 | enable_status | 否 |  |  |
| 12 | dataload_type | 否 |  |  |
| 13 | datasource_type | 否 |  |  |
| 14 | dataload_order | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acctdatasync | ART | 是 | table_category, table_category |
| idx_acctdatasync | ART | 是 | table_category, table_category |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acctdatasync | table_category, table_category |
| idx_acctdatasync | table_category, table_category |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-05 13:38:26 | 3.0.4.3 | 沈勋 | 调整表对象号 |
| 2024-07-30 10:26:58 | 3.0.3.7 | 董瑞辉 | 新增 |
| 2024-09-05 13:38:26 | 3.0.4.3 | 沈勋 | 调整表对象号 |
| 2024-07-30 10:26:58 | 3.0.3.7 | 董瑞辉 | 新增 |

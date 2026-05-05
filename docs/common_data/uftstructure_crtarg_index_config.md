# index_config - 指数信息表

**表对象ID**: 7106
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | index_date | 否 |  |  |
| 2 | index_kind | 否 |  |  |
| 3 | index_value | 否 |  |  |
| 4 | index_date | 否 |  |  |
| 5 | index_kind | 否 |  |  |
| 6 | index_value | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_index_config | ART | 是 | index_date, index_kind, index_date, index_kind |
| idx_index_config | ART | 是 | index_date, index_kind, index_date, index_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_index_config | index_date, index_kind, index_date, index_kind |
| idx_index_config | index_date, index_kind, index_date, index_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-03 12:26:02 | 3.0.6.93 | 李想 | 新增表 |
| 2025-03-03 12:26:02 | 3.0.6.93 | 李想 | 新增表 |

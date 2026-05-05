# index_component - 指数成份股信息表

**表对象ID**: 92
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | index_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | component_code | 否 |  |  |
| 4 | component_name | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | position_str | 否 |  | component_code(20)+exchange_type(4)+index_kind(1) |
| 9 | index_kind | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | component_code | 否 |  |  |
| 12 | component_name | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | component_code(20)+exchange_type(4)+index_kind(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_index_component | ART | 是 | component_code, exchange_type, index_kind, component_code, exchange_type, index_kind |
| idx_index_component | ART | 是 | component_code, exchange_type, index_kind, component_code, exchange_type, index_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_index_component | component_code, exchange_type, index_kind, component_code, exchange_type, index_kind |
| idx_index_component | component_code, exchange_type, index_kind, component_code, exchange_type, index_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 17:23:34 | 3.0.6.72 | 李想 | 物理表index_component，添加了表字段(update_date);
物理表index_component，... |
| 2024-09-09 11:04:56 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2024-03-20 16:10:00 | 3.0.2.6 | 楼欣欣 | 新增index_component |
| 2025-02-18 17:23:34 | 3.0.6.72 | 李想 | 物理表index_component，添加了表字段(update_date);
物理表index_component，... |
| 2024-09-09 11:04:56 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2024-03-20 16:10:00 | 3.0.2.6 | 楼欣欣 | 新增index_component |

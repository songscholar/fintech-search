# usps_entrustway_conv - 委托方式转换关系表

**表对象ID**: 319
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_way_group | 否 |  |  |
| 2 | entrust_way | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | entrust_way_group | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_entrustwayconv | ART | 是 | entrust_way, entrust_way |
| idx_entrustwayconv | ART | 是 | entrust_way, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_entrustwayconv | entrust_way, entrust_way |
| idx_entrustwayconv | entrust_way, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 15:11:14 | 3.0.6.93 | 李想 | 物理表usps_entrustway_conv，添加了表字段(update_date);
物理表usps_entrus... |
| 2024-08-09 13:16:21 | 3.0.2.26 | 骆鹏程 | 修改对象号为319 |
| 2024-05-08 14:16:59 | 3.0.2.8 | 林统 | 新增 |
| 2025-02-19 15:11:14 | 3.0.6.93 | 李想 | 物理表usps_entrustway_conv，添加了表字段(update_date);
物理表usps_entrus... |
| 2024-08-09 13:16:21 | 3.0.2.26 | 骆鹏程 | 修改对象号为319 |
| 2024-05-08 14:16:59 | 3.0.2.8 | 林统 | 新增 |

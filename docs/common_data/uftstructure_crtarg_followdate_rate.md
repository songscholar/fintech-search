# followdate_rate - 随日融利率参数表

**表对象ID**: 7080
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | followdate_kind | 否 |  |  |
| 2 | crdt_type | 否 |  |  |
| 3 | cashgroup_prop | 否 |  |  |
| 4 | followdate_year_rate | 否 |  |  |
| 5 | followdate_fine_rate | 否 |  |  |
| 6 | followdate_postpone_rate | 否 |  |  |
| 7 | int_begin_days | 否 |  |  |
| 8 | int_end_days | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | index_field | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | position_str | 否 |  | followdate_kind(10)+crdt_type(1)+cashgroup_prop(1) |
| 15 | followdate_kind | 否 |  |  |
| 16 | crdt_type | 否 |  |  |
| 17 | cashgroup_prop | 否 |  |  |
| 18 | followdate_year_rate | 否 |  |  |
| 19 | followdate_fine_rate | 否 |  |  |
| 20 | followdate_postpone_rate | 否 |  |  |
| 21 | int_begin_days | 否 |  |  |
| 22 | int_end_days | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | index_field | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | position_str | 否 |  | followdate_kind(10)+crdt_type(1)+cashgroup_prop(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_followdate_rate | ART | 是 | followdate_kind, crdt_type, cashgroup_prop, followdate_kind, crdt_type, cashgroup_prop |
| idx_followdate_rate | ART | 是 | followdate_kind, crdt_type, cashgroup_prop, followdate_kind, crdt_type, cashgroup_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_followdate_rate | followdate_kind, crdt_type, cashgroup_prop, followdate_kind, crdt_type, cashgroup_prop |
| idx_followdate_rate | followdate_kind, crdt_type, cashgroup_prop, followdate_kind, crdt_type, cashgroup_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 18:07:44 | 3.0.6.37 | 李想 | 新增表 |
| 2025-02-13 18:07:44 | 3.0.6.37 | 李想 | 新增表 |

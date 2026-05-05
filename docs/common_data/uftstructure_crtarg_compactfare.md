# compactfare - 合约费用表

**表对象ID**: 7081
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compactfare_kind | 否 |  |  |
| 2 | compactfare_type | 否 |  |  |
| 3 | compactfare_ratio | 否 |  |  |
| 4 | max_fare | 否 |  |  |
| 5 | min_fare | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | compactfare_kind(10)+compactfare_type(1) |
| 10 | compactfare_kind | 否 |  |  |
| 11 | compactfare_type | 否 |  |  |
| 12 | compactfare_ratio | 否 |  |  |
| 13 | max_fare | 否 |  |  |
| 14 | min_fare | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | compactfare_kind(10)+compactfare_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_compactfare | ART | 是 | compactfare_kind, compactfare_type, compactfare_kind, compactfare_type |
| idx_compactfare | ART | 是 | compactfare_kind, compactfare_type, compactfare_kind, compactfare_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_compactfare | compactfare_kind, compactfare_type, compactfare_kind, compactfare_type |
| idx_compactfare | compactfare_kind, compactfare_type, compactfare_kind, compactfare_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 19:08:30 | 3.0.6.38 | 李想 | 新增表 |
| 2025-02-13 19:08:30 | 3.0.6.38 | 李想 | 新增表 |

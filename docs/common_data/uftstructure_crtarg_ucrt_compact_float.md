# ucrt_compact_float - 合约浮动利率表

**表对象ID**: 7042
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | index_field | 否 |  |  |
| 2 | float_ratio_type | 否 |  |  |
| 3 | compactfloat_days | 否 |  |  |
| 4 | float_ratio | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | position_str | 否 |  | index_field(32)+float_ratio_type(1)+compactfloat_days(10) |
| 9 | index_field | 否 |  |  |
| 10 | float_ratio_type | 否 |  |  |
| 11 | compactfloat_days | 否 |  |  |
| 12 | float_ratio | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | index_field(32)+float_ratio_type(1)+compactfloat_days(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_float | ART | 是 | index_field, float_ratio_type, compactfloat_days, index_field, float_ratio_type, compactfloat_days |
| idx_ucrt_compact_float | ART | 是 | index_field, float_ratio_type, compactfloat_days, index_field, float_ratio_type, compactfloat_days |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_float | index_field, float_ratio_type, compactfloat_days, index_field, float_ratio_type, compactfloat_days |
| idx_ucrt_compact_float | index_field, float_ratio_type, compactfloat_days, index_field, float_ratio_type, compactfloat_days |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 19:31:11 | 3.0.6.40 |  | 物理表ucrt_compact_float，添加了表字段(update_date);
物理表ucrt_compact_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-05-25 18:08 | 0.0.0.2 | 徐世晗 | 新增 |
| 2025-02-13 19:31:11 | 3.0.6.40 |  | 物理表ucrt_compact_float，添加了表字段(update_date);
物理表ucrt_compact_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-05-25 18:08 | 0.0.0.2 | 徐世晗 | 新增 |

# ucrt_compact_rate - 融资融券合约利率表

**表对象ID**: 7009
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compactrate_kind | 否 |  |  |
| 2 | compact_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | year_rate | 否 |  |  |
| 6 | fine_rate | 否 |  |  |
| 7 | int_begin_days | 否 |  |  |
| 8 | index_field | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | int_end_days | 否 |  |  |
| 11 | param_flag | 否 |  |  |
| 12 | en_branch_no | 否 |  |  |
| 13 | primerate_kind | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | compact_type(1)+stock_code(8)+exchange_type(4)+compactrate_k |
| 17 | compactrate_kind | 否 |  |  |
| 18 | compact_type | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | year_rate | 否 |  |  |
| 22 | fine_rate | 否 |  |  |
| 23 | int_begin_days | 否 |  |  |
| 24 | index_field | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | int_end_days | 否 |  |  |
| 27 | param_flag | 否 |  |  |
| 28 | en_branch_no | 否 |  |  |
| 29 | primerate_kind | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | position_str | 否 |  | compact_type(1)+stock_code(8)+exchange_type(4)+compactrate_k |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_rate | 默认 | 否 | param_flag, param_flag |
| idx_ucrt_compact_rate | ART | 是 | compact_type, stock_code, exchange_type, compactrate_kind, param_flag, compact_type, stock_code, exchange_type, compactrate_kind, param_flag |
| idx_ucrt_compact_rate | 默认 | 否 | param_flag, param_flag |
| idx_ucrt_compact_rate | ART | 是 | compact_type, stock_code, exchange_type, compactrate_kind, param_flag, compact_type, stock_code, exchange_type, compactrate_kind, param_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_rate | compact_type, stock_code, exchange_type, compactrate_kind, param_flag, compact_type, stock_code, exchange_type, compactrate_kind, param_flag |
| idx_ucrt_compact_rate | compact_type, stock_code, exchange_type, compactrate_kind, param_flag, compact_type, stock_code, exchange_type, compactrate_kind, param_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 19:43:56 | 3.0.6.41 |  | 物理表ucrt_compact_rate，添加了表字段(en_branch_no);
物理表ucrt_compact_... |
| 2025-01-04 17:17:32 | 3.0.6.25 | 袁文龙 | 物理表ucrt_compact_rate，添加了表字段(int_end_days);
 |
| 2024-12-24 10:58:16 | 3.0.6.23 | 沈勋 | 物理表ucrt_compact_rate，增加索引字段(索引idx_ucrt_compact_rate:增加了索引字段：... |
| 2024-12-24 10:58:02 | 3.0.6.23 | 沈勋 | 物理表ucrt_compact_rate，添加了表字段(param_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-02-13 19:43:56 | 3.0.6.41 |  | 物理表ucrt_compact_rate，添加了表字段(en_branch_no);
物理表ucrt_compact_... |
| 2025-01-04 17:17:32 | 3.0.6.25 | 袁文龙 | 物理表ucrt_compact_rate，添加了表字段(int_end_days);
 |
| 2024-12-24 10:58:16 | 3.0.6.23 | 沈勋 | 物理表ucrt_compact_rate，增加索引字段(索引idx_ucrt_compact_rate:增加了索引字段：... |
| 2024-12-24 10:58:02 | 3.0.6.23 | 沈勋 | 物理表ucrt_compact_rate，添加了表字段(param_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

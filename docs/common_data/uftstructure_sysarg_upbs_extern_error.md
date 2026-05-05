# upbs_extern_error - 外部错误表

**表对象ID**: 16
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | error_info | 否 |  |  |
| 2 | error_no_dest | 否 |  | 对应UF20的error_no |
| 3 | error_sort | 否 |  |  |
| 4 | error_source | 否 |  |  |
| 5 | error_no_original | 否 |  | 对应UF20的extern_code |
| 6 | transaction_no | 否 |  |  |
| 7 | transaction_str | 否 |  |  |
| 8 | error_info | 否 |  |  |
| 9 | error_no_dest | 否 |  | 对应UF20的error_no |
| 10 | error_sort | 否 |  |  |
| 11 | error_source | 否 |  |  |
| 12 | error_no_original | 否 |  | 对应UF20的extern_code |
| 13 | transaction_no | 否 |  |  |
| 14 | transaction_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_extern_error | 默认 | 否 | error_no_dest, error_no_dest |
| idx_upbs_extern_error | ART | 是 | error_sort, error_source, error_no_original, error_no_dest, error_sort, error_source, error_no_original, error_no_dest |
| idx_upbs_extern_error | 默认 | 否 | error_no_dest, error_no_dest |
| idx_upbs_extern_error | ART | 是 | error_sort, error_source, error_no_original, error_no_dest, error_sort, error_source, error_no_original, error_no_dest |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_extern_error | error_sort, error_source, error_no_original, error_no_dest, error_sort, error_source, error_no_original, error_no_dest |
| idx_upbs_extern_error | error_sort, error_source, error_no_original, error_no_dest, error_sort, error_source, error_no_original, error_no_dest |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-13 14:53:01 | 3.0.6.1005 | 汪迎 | 物理表upbs_extern_error，添加了表字段(transaction_str);
 |
| 2025-03-12 14:13:07 | 3.0.2.6 | 祝丁恺 | 调整分级索引idx_upbs_extern_error，将error_no_original变为二级索引，error_n... |
| 2024-04-01 15:42:47 | 3.0.2.5 | 叶慧军 | 索引idx_upbs_extern_error类型改为分级索引 |
| 2023-10-14 10:38:35 | V3.0.1.14 | 余世泽 | 物理表upbs_extern_error，增加索引字段(索引idx_upbs_extern_error:增加了索引字段：... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:01 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2025-06-13 14:53:01 | 3.0.6.1005 | 汪迎 | 物理表upbs_extern_error，添加了表字段(transaction_str);
 |
| 2025-03-12 14:13:07 | 3.0.2.6 | 祝丁恺 | 调整分级索引idx_upbs_extern_error，将error_no_original变为二级索引，error_n... |
| 2024-04-01 15:42:47 | 3.0.2.5 | 叶慧军 | 索引idx_upbs_extern_error类型改为分级索引 |
| 2023-10-14 10:38:35 | V3.0.1.14 | 余世泽 | 物理表upbs_extern_error，增加索引字段(索引idx_upbs_extern_error:增加了索引字段：... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:01 | 0.0.0.5 | 吴威 | 新增字段transaction_no |

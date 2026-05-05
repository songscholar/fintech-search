# ucrt_compact_audit_stk - 合约展期证券控制表

**表对象ID**: 7012
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | en_compact_type | 否 |  |  |
| 4 | max_term | 否 |  |  |
| 5 | control_flag | 否 |  |  |
| 6 | postpone_restrict_type | 否 |  |  |
| 7 | compact_source | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | stock_code(8)+exchange_type(4)+postpone_restrict_type(32)+co |
| 13 | stock_code | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | en_compact_type | 否 |  |  |
| 16 | max_term | 否 |  |  |
| 17 | control_flag | 否 |  |  |
| 18 | postpone_restrict_type | 否 |  |  |
| 19 | compact_source | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | stock_code(8)+exchange_type(4)+postpone_restrict_type(32)+co |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_audit_stk | ART | 是 | stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type, stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type |
| idx_ucrt_compact_audit_stk | ART | 是 | stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type, stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_audit_stk | stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type, stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type |
| idx_ucrt_compact_audit_stk | stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type, stock_code, exchange_type, postpone_restrict_type, compact_source, en_compact_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 12:03:53 | 3.0.6.78 | 李想 | 物理表ucrt_compact_audit_stk，添加了表字段(remark);
物理表ucrt_compact_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；调整索引 |
| 2025-02-18 12:03:53 | 3.0.6.78 | 李想 | 物理表ucrt_compact_audit_stk，添加了表字段(remark);
物理表ucrt_compact_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；调整索引 |

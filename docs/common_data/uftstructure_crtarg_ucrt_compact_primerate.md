# ucrt_compact_primerate - 合约优惠利率配置表

**表对象ID**: 7010
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | primerate_id | 否 |  |  |
| 2 | primerate_name | 否 |  |  |
| 3 | compact_type | 否 |  |  |
| 4 | prime_rate | 否 |  |  |
| 5 | primerate_type | 否 |  |  |
| 6 | valid_days | 否 |  |  |
| 7 | valid_months | 否 |  |  |
| 8 | primerate_begin_date | 否 |  |  |
| 9 | primerate_end_date | 否 |  |  |
| 10 | primerate_audit_status | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | en_branch_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | primerate_id(10)+compact_type(1)+stock_code(8)+exchange_type |
| 19 | primerate_id | 否 |  |  |
| 20 | primerate_name | 否 |  |  |
| 21 | compact_type | 否 |  |  |
| 22 | prime_rate | 否 |  |  |
| 23 | primerate_type | 否 |  |  |
| 24 | valid_days | 否 |  |  |
| 25 | valid_months | 否 |  |  |
| 26 | primerate_begin_date | 否 |  |  |
| 27 | primerate_end_date | 否 |  |  |
| 28 | primerate_audit_status | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | stock_type | 否 |  |  |
| 33 | en_branch_no | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | position_str | 否 |  | primerate_id(10)+compact_type(1)+stock_code(8)+exchange_type |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_primerate | 默认 | 否 | stock_type, stock_type |
| idx_ucrt_compact_primerate | ART | 是 | primerate_id, compact_type, stock_code, exchange_type, stock_type, primerate_id, compact_type, stock_code, exchange_type, stock_type |
| idx_ucrt_compact_primerate | 默认 | 否 | stock_type, stock_type |
| idx_ucrt_compact_primerate | ART | 是 | primerate_id, compact_type, stock_code, exchange_type, stock_type, primerate_id, compact_type, stock_code, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_primerate | primerate_id, compact_type, stock_code, exchange_type, stock_type, primerate_id, compact_type, stock_code, exchange_type, stock_type |
| idx_ucrt_compact_primerate | primerate_id, compact_type, stock_code, exchange_type, stock_type, primerate_id, compact_type, stock_code, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 19:21:57 | 3.0.6.39 | 李想 | 物理表ucrt_compact_primerate，添加了表字段(en_branch_no);
物理表ucrt_com... |
| 2024-10-23 09:28:14 | 3.0.6.7 | 沈勋 | 物理表ucrt_compact_primerate，增加索引字段(索引idx_ucrt_compact_primerat... |
| 2024-10-23 09:20:59 | 3.0.6.7 | 沈勋 | 物理表ucrt_compact_primerate，添加了表字段(stock_type);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:24 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2025-02-13 19:21:57 | 3.0.6.39 | 李想 | 物理表ucrt_compact_primerate，添加了表字段(en_branch_no);
物理表ucrt_com... |
| 2024-10-23 09:28:14 | 3.0.6.7 | 沈勋 | 物理表ucrt_compact_primerate，增加索引字段(索引idx_ucrt_compact_primerat... |
| 2024-10-23 09:20:59 | 3.0.6.7 | 沈勋 | 物理表ucrt_compact_primerate，添加了表字段(stock_type);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:24 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |

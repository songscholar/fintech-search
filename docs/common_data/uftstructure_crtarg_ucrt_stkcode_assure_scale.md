# ucrt_stkcode_assure_scale - 代码维持担保比例控制表

**表对象ID**: 7004
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | assurescale_value | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | enable_status | 否 |  |  |
| 7 | priority_assure_back | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 12 | stock_code | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | assurescale_value | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | enable_status | 否 |  |  |
| 18 | priority_assure_back | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stkcode_assure_scale | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_ucrt_stkcode_assure_scale | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stkcode_assure_scale | stock_code, exchange_type, stock_code, exchange_type |
| idx_ucrt_stkcode_assure_scale | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 13:56:50 | V3.0.6.1070 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-02-18 10:23:55 | 3.0.6.70 | 李想 | 物理表ucrt_stkcode_assure_scale，添加了表字段(update_date);
物理表ucrt_s... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-01-05 13:56:50 | V3.0.6.1070 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-02-18 10:23:55 | 3.0.6.70 | 李想 | 物理表ucrt_stkcode_assure_scale，添加了表字段(update_date);
物理表ucrt_s... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

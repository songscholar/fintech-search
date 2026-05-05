# grade_impawn_rate - 分级质押比率表

**表对象ID**: 314
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | impawn_rate_1 | 否 |  |  |
| 4 | impawn_rate_2 | 否 |  |  |
| 5 | impawn_rate_3 | 否 |  |  |
| 6 | impawn_rate_4 | 否 |  |  |
| 7 | impawn_rate_5 | 否 |  |  |
| 8 | impawn_rate_6 | 否 |  |  |
| 9 | impawn_rate_7 | 否 |  |  |
| 10 | impawn_rate_8 | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | impawn_rate_1 | 否 |  |  |
| 18 | impawn_rate_2 | 否 |  |  |
| 19 | impawn_rate_3 | 否 |  |  |
| 20 | impawn_rate_4 | 否 |  |  |
| 21 | impawn_rate_5 | 否 |  |  |
| 22 | impawn_rate_6 | 否 |  |  |
| 23 | impawn_rate_7 | 否 |  |  |
| 24 | impawn_rate_8 | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_grade_impawn_rate | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_grade_impawn_rate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_grade_impawn_rate | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_grade_impawn_rate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_grade_impawn_rate | exchange_type, stock_code, exchange_type, stock_code |
| idx_grade_impawn_rate | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 13:22:15 | 3.0.6.113 | 李想 | 物理表grade_impawn_rate，添加了表字段(update_date);
物理表grade_impawn_r... |
| 2024-07-18 11:15:25 | 3.0.2.23 | 张云焘 | 物理表grade_impawn_rate，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.0.198 | 全春辉 | 物理表增加索引 |
| 2025-02-20 13:22:15 | 3.0.6.113 | 李想 | 物理表grade_impawn_rate，添加了表字段(update_date);
物理表grade_impawn_r... |
| 2024-07-18 11:15:25 | 3.0.2.23 | 张云焘 | 物理表grade_impawn_rate，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.0.198 | 全春辉 | 物理表增加索引 |

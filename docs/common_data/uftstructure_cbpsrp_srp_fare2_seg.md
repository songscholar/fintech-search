# srp_fare2_seg - 股票质押费用分段表

**表对象ID**: 2621
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | aim_value | 否 |  |  |
| 4 | balance_ratio | 否 |  |  |
| 5 | par_ratio | 否 |  |  |
| 6 | min_fare | 否 |  |  |
| 7 | max_fare | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | fare_type(1)+stock_type(4)+aim_value(20) |
| 12 | fare_type | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | aim_value | 否 |  |  |
| 15 | balance_ratio | 否 |  |  |
| 16 | par_ratio | 否 |  |  |
| 17 | min_fare | 否 |  |  |
| 18 | max_fare | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | fare_type(1)+stock_type(4)+aim_value(20) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpfareseg | ART | 是 | fare_type, stock_type, aim_value, fare_type, stock_type, aim_value |
| idx_srpfareseg | ART | 是 | fare_type, stock_type, aim_value, fare_type, stock_type, aim_value |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpfareseg | fare_type, stock_type, aim_value, fare_type, stock_type, aim_value |
| idx_srpfareseg | fare_type, stock_type, aim_value, fare_type, stock_type, aim_value |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:52:55 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 11:36:20 | 3.0.3.3 |  | 物理表srp_fare2_seg，添加了表字段(update_date);
物理表srp_fare2_seg，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:57 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:52:55 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 11:36:20 | 3.0.3.3 |  | 物理表srp_fare2_seg，添加了表字段(update_date);
物理表srp_fare2_seg，添加了表... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:24:57 | 3.0.3.1 | wuxd | 新增 |

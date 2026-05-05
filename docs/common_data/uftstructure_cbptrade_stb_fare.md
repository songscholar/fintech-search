# stb_fare - 三板业务费用表

**表对象ID**: 2319
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | trans_type | 否 |  |  |
| 4 | fare_type | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | balance_ratio | 否 |  |  |
| 8 | par_ratio | 否 |  |  |
| 9 | fare | 否 |  |  |
| 10 | sub_stock_type | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | branch_no(6)+exchange_type(4)+trans_type(2)+stock_type(4)+fa |
| 15 | branch_no | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | trans_type | 否 |  |  |
| 18 | fare_type | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | balance_ratio | 否 |  |  |
| 22 | par_ratio | 否 |  |  |
| 23 | fare | 否 |  |  |
| 24 | sub_stock_type | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | branch_no(6)+exchange_type(4)+trans_type(2)+stock_type(4)+fa |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stbfare | 默认 | 否 |  |
| idx_stbfare | ART | 是 | branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type, branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type |
| idx_stbfare | 默认 | 否 |  |
| idx_stbfare | ART | 是 | branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type, branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stbfare | branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type, branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type |
| idx_stbfare | branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type, branch_no, exchange_type, trans_type, stock_type, fare_type, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:20:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 16:52:30 | V3.0.5.1006 | 李想 | 物理表stb_fare，添加了表字段(update_date);
物理表stb_fare，添加了表字段(update_... |
| 2024-09-09 11:21:41 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-02 14:53:43 | V3.0.1.16 | 全春辉 | 新增 |
| 2026-03-04 15:20:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-14 16:52:30 | V3.0.5.1006 | 李想 | 物理表stb_fare，添加了表字段(update_date);
物理表stb_fare，添加了表字段(update_... |
| 2024-09-09 11:21:41 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-02 14:53:43 | V3.0.1.16 | 全春辉 | 新增 |

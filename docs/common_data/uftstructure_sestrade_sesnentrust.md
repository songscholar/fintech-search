# sesnentrust - 证券内存夜市委托表

**表对象ID**: 5574
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_prop | 否 |  |  |
| 2 | order_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | partition_no | 否 |  |  |
| 7 | entrust_prop | 否 |  |  |
| 8 | order_id | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sesnentrust | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_sesnentrust | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sesnentrust | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_sesnentrust | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:23:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-23 19:19:53 | 3.0.2.48 | 余世泽 | 新增 |
| 2026-03-09 14:23:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-23 19:19:53 | 3.0.2.48 | 余世泽 | 新增 |

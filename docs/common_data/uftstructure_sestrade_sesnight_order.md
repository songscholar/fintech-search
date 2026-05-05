# sesnight_order - 证券内存夜市订单表

**表对象ID**: 5578
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
| idx_sesnight_order | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_sesnight_order | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sesnight_order | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_sesnight_order | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:28:21 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-12-17 19:45:32 | 3.0.6.6 | 卢杰 |  |
| 2024-11-05 15:34:26 | 3.0.5.1058 | 杨森峰 | 新增 |
| 2026-03-09 14:28:21 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-12-17 19:45:32 | 3.0.6.6 | 卢杰 |  |
| 2024-11-05 15:34:26 | 3.0.5.1058 | 杨森峰 | 新增 |

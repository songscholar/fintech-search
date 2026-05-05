# crtnentrust - 内存客户夜市委托表

**表对象ID**: 7554
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_prop | 否 |  |  |
| 2 | order_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | partition_no | 是 |  |  |
| 7 | entrust_prop | 否 |  |  |
| 8 | order_id | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | partition_no | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crtnentrust | 默认 | 否 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_crtnentrust | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_crtnentrust | 默认 | 否 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_crtnentrust | ART | 是 | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crtnentrust | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |
| idx_crtnentrust | order_id, entrust_prop, branch_no, exchange_type, seat_no, order_id, entrust_prop, branch_no, exchange_type, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-11 16:24:55 | 3.0.6.1067 | 汪杰 | 所有表crtnentrust，添加了表字段(partition_no);
 |
| 2024-01-31 19:03:44 | V3.0.2.2 | 汪杰 | 物理表crtnentrust，增加索引(idx_crtnentrust:[order_id,entrust_prop,b... |
| 2024-01-31 18:57:39 | V3.0.2.2 | 汪杰 | 物理表crtnentrust，添加了表字段(entrust_prop);
物理表crtnentrust，添加了表字段(... |
| 2025-09-11 16:24:55 | 3.0.6.1067 | 汪杰 | 所有表crtnentrust，添加了表字段(partition_no);
 |
| 2024-01-31 19:03:44 | V3.0.2.2 | 汪杰 | 物理表crtnentrust，增加索引(idx_crtnentrust:[order_id,entrust_prop,b... |
| 2024-01-31 18:57:39 | V3.0.2.2 | 汪杰 | 物理表crtnentrust，添加了表字段(entrust_prop);
物理表crtnentrust，添加了表字段(... |

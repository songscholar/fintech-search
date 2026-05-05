# crdtstkadfare - 融资融券证券类别冻结调整表

**表对象ID**: 338
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | frozen_adjustfare | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | position_str | 否 |  | stock_type(4)+exchange_type(4) |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_type | 否 |  |  |
| 10 | frozen_adjustfare | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | position_str | 否 |  | stock_type(4)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtstkadfare | ART | 是 | stock_type, exchange_type, stock_type, exchange_type |
| idx_crdtstkadfare | ART | 是 | stock_type, exchange_type, stock_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtstkadfare | stock_type, exchange_type, stock_type, exchange_type |
| idx_crdtstkadfare | stock_type, exchange_type, stock_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 20:10:22 | 3.0.6.12 | 李想 | 物理表crdtstkadfare，添加了表字段(update_date);
物理表crdtstkadfare，添加了表... |
| 2024-09-27 15:22:49 | 3.0.3.14 | 张明月 | 物理表crdtstkadfare，添加了表字段(transaction_no);
 |
| 2024-09-23 15:54:10 | 3.0.3.7 | 张明月 | 新增 |
| 2025-02-13 20:10:22 | 3.0.6.12 | 李想 | 物理表crdtstkadfare，添加了表字段(update_date);
物理表crdtstkadfare，添加了表... |
| 2024-09-27 15:22:49 | 3.0.3.14 | 张明月 | 物理表crdtstkadfare，添加了表字段(transaction_no);
 |
| 2024-09-23 15:54:10 | 3.0.3.7 | 张明月 | 新增 |

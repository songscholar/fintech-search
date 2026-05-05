# pre_stock_info - 原持仓信息表

**表对象ID**: 324
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_prestockinfo | ART | 是 | client_id, exchange_type, stock_code, client_id, exchange_type, stock_code |
| idx_prestockinfo | ART | 是 | client_id, exchange_type, stock_code, client_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_prestockinfo | client_id, exchange_type, stock_code, client_id, exchange_type, stock_code |
| idx_prestockinfo | client_id, exchange_type, stock_code, client_id, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-14 10:04:28 | 3.0.2.91 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-09-24 13:39:58 | 3.0.2.29 | 范文浩 | 物理表pre_stock_info，添加了表字段(init_date);
物理表pre_stock_info，添加了表... |
| 2025-08-14 10:04:28 | 3.0.2.91 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-09-24 13:39:58 | 3.0.2.29 | 范文浩 | 物理表pre_stock_info，添加了表字段(init_date);
物理表pre_stock_info，添加了表... |

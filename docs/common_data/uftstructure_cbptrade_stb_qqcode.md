# stb_qqcode - 特别股份确权股份信息

**表对象ID**: 2344
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | current_amount | 否 |  |  |
| 5 | confirm_amount | 否 |  |  |
| 6 | face_value | 否 |  |  |
| 7 | fare0 | 否 |  |  |
| 8 | fare1 | 否 |  |  |
| 9 | farex | 否 |  |  |
| 10 | id_no | 否 |  |  |
| 11 | secu_type | 否 |  |  |
| 12 | fare0_ratio | 否 |  |  |
| 13 | fare1_ratio | 否 |  |  |
| 14 | min_fare0 | 否 |  |  |
| 15 | max_fare0 | 否 |  |  |
| 16 | one_farex | 否 |  |  |
| 17 | org_farex | 否 |  |  |
| 18 | secu_id | 否 |  |  |
| 19 | secu_name | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | stbqq_status | 否 |  |  |
| 22 | src_exchange_type | 否 |  |  |
| 23 | src_stock_code | 否 |  |  |
| 24 | src_stock_name | 否 |  |  |
| 25 | stbqq_flag | 否 |  |  |
| 26 | crdt_stbqq_flag | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |
| 31 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 32 | exchange_type | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | stock_name | 否 |  |  |
| 35 | current_amount | 否 |  |  |
| 36 | confirm_amount | 否 |  |  |
| 37 | face_value | 否 |  |  |
| 38 | fare0 | 否 |  |  |
| 39 | fare1 | 否 |  |  |
| 40 | farex | 否 |  |  |
| 41 | id_no | 否 |  |  |
| 42 | secu_type | 否 |  |  |
| 43 | fare0_ratio | 否 |  |  |
| 44 | fare1_ratio | 否 |  |  |
| 45 | min_fare0 | 否 |  |  |
| 46 | max_fare0 | 否 |  |  |
| 47 | one_farex | 否 |  |  |
| 48 | org_farex | 否 |  |  |
| 49 | secu_id | 否 |  |  |
| 50 | secu_name | 否 |  |  |
| 51 | remark | 否 |  |  |
| 52 | stbqq_status | 否 |  |  |
| 53 | src_exchange_type | 否 |  |  |
| 54 | src_stock_code | 否 |  |  |
| 55 | src_stock_name | 否 |  |  |
| 56 | stbqq_flag | 否 |  |  |
| 57 | crdt_stbqq_flag | 否 |  |  |
| 58 | money_type | 否 |  |  |
| 59 | transaction_no | 否 |  |  |
| 60 | update_date | 否 |  |  |
| 61 | update_time | 否 |  |  |
| 62 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stbqqcode | 默认 | 否 |  |
| idx_stbqqcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_stbqqcode | 默认 | 否 |  |
| idx_stbqqcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stbqqcode | stock_code, exchange_type, stock_code, exchange_type |
| idx_stbqqcode | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:33:54 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:45:42 | V3.0.5.1007 | 李想 | 物理表stb_qqcode，添加了表字段(update_date);
物理表stb_qqcode，添加了表字段(upd... |
| 2024-09-14 19:00:17 | 3.0.2.47 | 杨森峰 | 新增 |
| 2026-03-04 15:33:54 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-18 16:45:42 | V3.0.5.1007 | 李想 | 物理表stb_qqcode，添加了表字段(update_date);
物理表stb_qqcode，添加了表字段(upd... |
| 2024-09-14 19:00:17 | 3.0.2.47 | 杨森峰 | 新增 |

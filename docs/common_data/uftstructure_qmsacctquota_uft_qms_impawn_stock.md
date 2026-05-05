# uft_qms_impawn_stock - UFT存管质押国债表

**表对象ID**: 1652
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | store_amount | 否 |  |  |
| 5 | pre_in_amount | 否 |  |  |
| 6 | pre_out_amount | 否 |  |  |
| 7 | order_no | 否 |  |  |
| 8 | acode_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | store_amount | 否 |  |  |
| 12 | pre_in_amount | 否 |  |  |
| 13 | pre_out_amount | 否 |  |  |
| 14 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_uqms_impawn_stock | 默认 | 否 |  |
| idx_uft_uqms_impawn_stock | ART | 是 | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |
| idx_uft_uqms_impawn_stock | 默认 | 否 |  |
| idx_uft_uqms_impawn_stock | ART | 是 | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_uqms_impawn_stock | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |
| idx_uft_uqms_impawn_stock | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:49:37 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:48:40 | 3.0.2.14 | taocong45644 | 当前表uft_qms_impawn_stock，修改了索引idx_uft_uqms_impawn_stock,索引字段修... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:10:03 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-05 16:49:37 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:48:40 | 3.0.2.14 | taocong45644 | 当前表uft_qms_impawn_stock，修改了索引idx_uft_uqms_impawn_stock,索引字段修... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:10:03 | 3.0.2.2001 | 杨新照 | 新增表结构 |

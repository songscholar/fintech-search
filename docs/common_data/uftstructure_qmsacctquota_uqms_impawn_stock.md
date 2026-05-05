# uqms_impawn_stock - 存管质押国债表

**表对象ID**: 1613
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | store_amount | 否 |  |  |
| 5 | pre_in_amount | 否 |  |  |
| 6 | pre_out_amount | 否 |  |  |
| 7 | acode_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | store_amount | 否 |  |  |
| 11 | pre_in_amount | 否 |  |  |
| 12 | pre_out_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_impawn_stock | ART | 是 | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |
| idx_uqms_impawn_stock | ART | 是 | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_impawn_stock | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |
| idx_uqms_impawn_stock | acode_account, stock_code, exchange_type, acode_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:43:34 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2026-03-05 16:43:34 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |

# uft_impawn_stock - UFT质押国债表

**表对象ID**: 5978
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | pre_out_amount | 否 |  |  |
| 7 | pre_in_amount | 否 |  |  |
| 8 | store_amount | 否 |  |  |
| 9 | order_no | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | pre_out_amount | 否 |  |  |
| 16 | pre_in_amount | 否 |  |  |
| 17 | store_amount | 否 |  |  |
| 18 | order_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_impawn_stock | 默认 | 否 |  |
| idx_uft_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_uft_impawn_stock | 默认 | 否 |  |
| idx_uft_impawn_stock | ART | 是 | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_impawn_stock | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |
| idx_uft_impawn_stock | fund_account, exchange_type, stock_account, stock_code, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:51:58 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:27:53 | 3.0.2.104 | taocong45644 | 当前表uft_impawn_stock，修改了索引idx_uft_impawn_stock,索引字段修改为：(fund_... |
| 2025-03-11 11:07:05 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-09 14:51:58 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:27:53 | 3.0.2.104 | taocong45644 | 当前表uft_impawn_stock，修改了索引idx_uft_impawn_stock,索引字段修改为：(fund_... |
| 2025-03-11 11:07:05 | 3.0.2.2001 | 杨新照 | 新增表结构 |

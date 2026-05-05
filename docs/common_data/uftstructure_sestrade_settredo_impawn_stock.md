# settredo_impawn_stock - 清算重做质押国债表

**表对象ID**: 5801
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | pre_out_amount | 否 |  |  |
| 6 | pre_in_amount | 否 |  |  |
| 7 | store_amount | 否 |  |  |
| 8 | sett_dml_type | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | pre_out_amount | 否 |  |  |
| 15 | pre_in_amount | 否 |  |  |
| 16 | store_amount | 否 |  |  |
| 17 | sett_dml_type | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_impawn_stock | ART | 是 | sett_batch_no, fund_account, exchange_type, stock_account, stock_code, sett_batch_no, fund_account, exchange_type, stock_account, stock_code |
| idx_settredo_impawn_stock | ART | 是 | sett_batch_no, fund_account, exchange_type, stock_account, stock_code, sett_batch_no, fund_account, exchange_type, stock_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_impawn_stock | sett_batch_no, fund_account, exchange_type, stock_account, stock_code, sett_batch_no, fund_account, exchange_type, stock_account, stock_code |
| idx_settredo_impawn_stock | sett_batch_no, fund_account, exchange_type, stock_account, stock_code, sett_batch_no, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:43:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:48:32 | 3.0.6.1011 | yangxz |  |
| 2026-03-09 14:43:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:48:32 | 3.0.6.1011 | yangxz |  |

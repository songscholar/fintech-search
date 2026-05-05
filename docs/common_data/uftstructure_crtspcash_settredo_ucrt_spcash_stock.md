# settredo_ucrt_spcash_stock - 日终清算客户专项头寸股份表

**表对象ID**: 8006
**所属模块**: crtspcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | slo_total_amount | 否 |  |  |
| 6 | slo_used_amount | 否 |  |  |
| 7 | ref_due_amount | 否 |  |  |
| 8 | sett_dml_type | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | enable_amount | 是 |  |  |
| 11 | surstock_amount | 是 |  |  |
| 12 | cashgroup_no | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | slo_total_amount | 否 |  |  |
| 17 | slo_used_amount | 否 |  |  |
| 18 | ref_due_amount | 否 |  |  |
| 19 | sett_dml_type | 否 |  |  |
| 20 | sett_batch_no | 否 |  |  |
| 21 | enable_amount | 是 |  |  |
| 22 | surstock_amount | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucrt_spcash_stock | ART | 是 | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucrt_spcash_stock | ART | 是 | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucrt_spcash_stock | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucrt_spcash_stock | cashgroup_no, exchange_type, stock_code, sett_batch_no, cashgroup_no, exchange_type, stock_code, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-20 11:20:38 | 3.0.6.6 | 沈勋 | 所有表settredo_ucrt_spcash_stock，添加了表字段(enable_amount);
所有表set... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2025-10-20 11:20:38 | 3.0.6.6 | 沈勋 | 所有表settredo_ucrt_spcash_stock，添加了表字段(enable_amount);
所有表set... |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

# ref_ieriskext_info - 风控指标扩展信息表

**表对象ID**: 6217
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | csfc_organ_code | 否 |  |  |
| 2 | csfc_borrower_code | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | upper_lend_amount | 否 |  |  |
| 6 | enable_lend_amount | 否 |  |  |
| 7 | csfc_organ_code | 否 |  |  |
| 8 | csfc_borrower_code | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | upper_lend_amount | 否 |  |  |
| 12 | enable_lend_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_ieriskext_info | ART | 是 | csfc_organ_code, csfc_borrower_code, stock_code, exchange_type, csfc_organ_code, csfc_borrower_code, stock_code, exchange_type |
| idx_ref_ieriskext_info | ART | 是 | csfc_organ_code, csfc_borrower_code, stock_code, exchange_type, csfc_organ_code, csfc_borrower_code, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_ieriskext_info | csfc_organ_code, csfc_borrower_code, stock_code, exchange_type, csfc_organ_code, csfc_borrower_code, stock_code, exchange_type |
| idx_ref_ieriskext_info | csfc_organ_code, csfc_borrower_code, stock_code, exchange_type, csfc_organ_code, csfc_borrower_code, stock_code, exchange_type |

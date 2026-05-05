# settredo_ucbp_ipoinfo - 日终清算新股申购信息表

**表对象ID**: 2649
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | ipo_short_balance | 否 |  |  |
| 7 | ipo_pacancel_amount | 否 |  |  |
| 8 | ipo_info_status | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | sett_dml_type | 否 |  |  |
| 13 | sett_batch_no | 否 |  |  |
| 14 | ipo_short_balance | 否 |  |  |
| 15 | ipo_pacancel_amount | 否 |  |  |
| 16 | ipo_info_status | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_ucbp_ipoinfo | ART | 是 | fund_account, exchange_type, stock_code, sett_batch_no, fund_account, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucbp_ipoinfo | ART | 是 | fund_account, exchange_type, stock_code, sett_batch_no, fund_account, exchange_type, stock_code, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_ucbp_ipoinfo | fund_account, exchange_type, stock_code, sett_batch_no, fund_account, exchange_type, stock_code, sett_batch_no |
| idx_strd_ucbp_ipoinfo | fund_account, exchange_type, stock_code, sett_batch_no, fund_account, exchange_type, stock_code, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:32:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-10-30 16:18:05 | 3.0.2.1 | 沈勋 | 新增表 |
| 2026-03-04 16:32:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-10-30 16:18:05 | 3.0.2.1 | 沈勋 | 新增表 |
